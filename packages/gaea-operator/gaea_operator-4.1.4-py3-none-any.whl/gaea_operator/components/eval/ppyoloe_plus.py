#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/2/23
# @Author  : yanxiaodong
# @File    : eval_component.py
"""
import os
from argparse import ArgumentParser

from gaea_tracker import ExperimentTracker
from bcelogger.base_logger import setup_logger
from windmilltrainingv1.client.training_api_job import parse_job_name
from windmillclient.client.windmill_client import WindmillClient

from gaea_operator.dataset import CocoDataset
from gaea_operator.trainer import Trainer
from gaea_operator.metric import update_metric_file
from gaea_operator.utils import read_file
from gaea_operator.config import PPYOLOEPLUSMConfig
import bcelogger


def parse_args():
    """
    Parse arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("--windmill-ak", type=str, default=os.environ.get("WINDMILL_AK"))
    parser.add_argument("--windmill-sk", type=str, default=os.environ.get("WINDMILL_SK"))
    parser.add_argument("--windmill-endpoint", type=str, default=os.environ.get("WINDMILL_ENDPOINT"))
    parser.add_argument("--project-name", type=str, default=os.environ.get("PROJECT_NAME"))
    parser.add_argument("--scene", type=str, default=os.environ.get("SCENE"))
    parser.add_argument("--tracking-uri", type=str, default=os.environ.get("TRACKING_URI"))
    parser.add_argument("--experiment-name", type=str, default=os.environ.get("EXPERIMENT_NAME"))
    parser.add_argument("--experiment-kind", type=str, default=os.environ.get("EXPERIMENT_KIND"))
    parser.add_argument("--dataset-name", type=str, default=os.environ.get("DATASET_NAME"))
    parser.add_argument("--advanced-parameters",
                        type=str,
                        default=os.environ.get("ADVANCED_PARAMETERS", "{}"))

    parser.add_argument("--input-model-uri", type=str, default=os.environ.get("INPUT_MODEL_URI"))
    parser.add_argument("--output-dataset-uri", type=str, default=os.environ.get("OUTPUT_DATASET_URI"))
    parser.add_argument("--output-uri", type=str, default=os.environ.get("OUTPUT_URI"))

    parser.add_argument("--icafe-id", type=str, default=os.environ.get("ICAFE_ID"))
    parser.add_argument("--icafe-operator", type=str, default=os.environ.get("ICAFE_OPERATOR"))

    args, _ = parser.parse_known_args()

    return args


def ppyoloe_plus_eval(args):
    """
    Eval component for ppyoloe_plus_m model.
    """
    try:
        if args.icafe_id:
            from gaea_operator.components.icafe import icafe
            icafe.sync_icafe_eval_start(args)
    except Exception as e:
        bcelogger.error(f"Sync icafe failed args:{args} exception: {e}")

    windmill_client = WindmillClient(ak=args.windmill_ak,
                                     sk=args.windmill_sk,
                                     endpoint=args.windmill_endpoint)
    tracker_client = ExperimentTracker(windmill_client=windmill_client,
                                       tracking_uri=args.tracking_uri,
                                       experiment_name=args.experiment_name,
                                       experiment_kind=args.experiment_kind,
                                       project_name=args.project_name)
    setup_logger(config=dict(file_name=os.path.join(args.output_uri, "worker.log")))

    response = read_file(input_dir=args.input_model_uri)

    coco_dataset = CocoDataset(windmill_client=windmill_client, work_dir=tracker_client.work_dir)
    # 1. 合并分片数据集
    coco_dataset.concat_dataset(dataset_name=args.dataset_name,
                                output_dir=args.output_dataset_uri,
                                usage=CocoDataset.usages[1])

    # 2. 生成评估配置文件
    PPYOLOEPLUSMConfig(windmill_client=windmill_client, tracker_client=tracker_client).write_eval_config(
        dataset_uri=args.output_dataset_uri,
        model_uri=args.input_model_uri)

    # 3. 评估
    trainer = Trainer(framework="PaddlePaddle", tracker_client=tracker_client)
    trainer.track_train_log(output_uri=args.output_uri)
    trainer.launch()

    # 4. 更新指标文件
    update_metric_file(windmill_client=windmill_client,
                       tracker_client=tracker_client,
                       dataset_name=args.dataset_name,
                       model_object_name=response["artifact"]["objectName"],
                       model_artifact_name=response["artifact"]["name"])

    # 5. 更新job tags
    tags = {"artifactName": response["artifact"]["name"], "datasetName": args.dataset_name}
    job_name = parse_job_name(tracker_client.job_name)
    workspace_id, project_name, local_name = job_name.workspace_id, job_name.project_name, job_name.local_name
    windmill_client.update_job(workspace_id=workspace_id, project_name=project_name, local_name=local_name, tags=tags)

    try:
        if args.icafe_id:
            from gaea_operator.components.icafe import icafe
            icafe.sync_icafe_eval_end(args)
    except Exception as e:
        bcelogger.error(f"Sync icafe failed args:{args} exception: {e}")


if __name__ == "__main__":
    args = parse_args()
    ppyoloe_plus_eval(args=args)
