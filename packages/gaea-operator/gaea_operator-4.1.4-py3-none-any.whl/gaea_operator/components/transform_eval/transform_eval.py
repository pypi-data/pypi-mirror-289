#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/22
# @Author  : yanxiaodong
# @File    : transform_eval.py
"""
import os
import shutil
from argparse import ArgumentParser
from typing import Dict
import json
import base64

from gaea_tracker import ExperimentTracker
from bcelogger.base_logger import setup_logger
import bcelogger
from windmilltrainingv1.client.training_api_dataset import parse_dataset_name
from windmillmodelv1.client.model_api_model import parse_model_name
from windmillartifactv1.client.artifact_api_artifact import get_name
from windmillclient.client.windmill_client import WindmillClient
from tritonv2.evaluator import evaluate

from gaea_operator.config import Config
from gaea_operator.metric import EvalMetricAnalysis, Metric
from gaea_operator.utils import find_dir, \
    read_file, \
    is_base64, \
    get_accelerator, \
    ModelTemplate, \
    DEFAULT_TRITON_CONFIG_FILE_NAME


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
    parser.add_argument("--public-model-store",
                        type=str,
                        default=os.environ.get("PUBLIC_MODEL_STORE", "workspaces/public/modelstores/public"))
    parser.add_argument("--tracking-uri", type=str, default=os.environ.get("TRACKING_URI"))
    parser.add_argument("--experiment-name", type=str, default=os.environ.get("EXPERIMENT_NAME"))
    parser.add_argument("--experiment-kind", type=str, default=os.environ.get("EXPERIMENT_KIND"))
    parser.add_argument("--accelerator", type=str, default=os.environ.get("ACCELERATOR", "t4"))
    parser.add_argument("--algorithm", type=str, default=os.environ.get("ALGORITHM", ""))
    parser.add_argument("--advanced-parameters",
                        type=str,
                        default=os.environ.get("ADVANCED_PARAMETERS", "{}"))

    parser.add_argument("--input-model-uri", type=str, default=os.environ.get("INPUT_MODEL_URI"))
    parser.add_argument("--input-dataset-uri", type=str, default=os.environ.get("INPUT_DATASET_URI"))
    parser.add_argument("--output-uri", type=str, default=os.environ.get("OUTPUT_URI"))

    parser.add_argument("--icafe-id", type=str, default=os.environ.get("ICAFE_ID"))
    parser.add_argument("--icafe-operator", type=str, default=os.environ.get("ICAFE_OPERATOR"))

    args, _ = parser.parse_known_args()

    return args


def package_model_by_template(windmill_client: WindmillClient,
                              tracker_client: ExperimentTracker,
                              metadata: Dict,
                              input_model_uri: str,
                              output_model_uri: str,
                              ensemble_name: str,
                              pre_name: str,
                              post_name: str,
                              model_name: str,
                              accelerator: str):
    """
    Package model by template.
    """
    pre = pre_name
    post = post_name
    model = model_name
    ensemble = parse_model_name(ensemble_name).local_name
    modify_model_names = {
        'preprocess': [pre],
        'postprocess': [post],
        'ensemble': [ensemble]
    }

    config = Config(windmill_client=windmill_client, tracker_client=tracker_client, metadata=metadata)
    config.write_triton_package_config(transform_model_uri=input_model_uri,
                                       ensemble_model_uri=output_model_uri,
                                       modify_model_names=modify_model_names,
                                       ensemble_local_name=ensemble,
                                       accelerator=accelerator)

    pre_uri = os.path.join(output_model_uri, pre)
    shutil.copyfile(src=os.path.join(find_dir(pre_uri), DEFAULT_TRITON_CONFIG_FILE_NAME),
                    dst=os.path.join(pre_uri, DEFAULT_TRITON_CONFIG_FILE_NAME))

    post_uri = os.path.join(output_model_uri, post)
    shutil.copyfile(src=os.path.join(find_dir(post_uri), DEFAULT_TRITON_CONFIG_FILE_NAME),
                    dst=os.path.join(post_uri, DEFAULT_TRITON_CONFIG_FILE_NAME))
    shutil.copyfile(src=os.path.join(find_dir(post_uri), "parse.yaml"),
                    dst=os.path.join(post_uri, "parse.yaml"))

    model_uri = os.path.join(output_model_uri, model)
    shutil.rmtree(find_dir(model_uri))
    shutil.copytree(src=input_model_uri, dst=os.path.join(model_uri, str(1)))
    shutil.copyfile(src=os.path.join(find_dir(model_uri), DEFAULT_TRITON_CONFIG_FILE_NAME),
                    dst=os.path.join(model_uri, DEFAULT_TRITON_CONFIG_FILE_NAME))


def transform_eval(args):
    """
    Package component for ppyoloe_plus model.
    """
    try:
        if args.icafe_id:
            from gaea_operator.components.icafe import icafe
            icafe.sync_icafe_transform_eval_start(args)
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
    metadata = response["artifact"]["metadata"]

    output_model_uri = "/home/windmill/tmp/model"
    # 1. 下载ensemble template 模型
    model_template = ModelTemplate(windmill_client=windmill_client,
                                   scene=args.scene,
                                   accelerator=args.accelerator,
                                   model_store_name=args.public_model_store,
                                   algorithm=args.algorithm)
    ensemble = model_template.suggest_template_ensemble()
    ensemble_artifact_name = get_name(object_name=ensemble, version="latest")
    bcelogger.info(f"Dumping model {ensemble_artifact_name} to {output_model_uri}")
    windmill_client.dump_models(artifact_name=ensemble_artifact_name,
                                location_style="Triton",
                                rename="ensemble",
                                output_uri=output_model_uri)

    # 2. 基于模板文件组装转换后模型包
    pre = parse_model_name(model_template.suggest_template_preprocess()).local_name
    post = parse_model_name(model_template.suggest_template_postprocess()).local_name
    model = parse_model_name(model_template.suggest_template_model()).local_name
    package_model_by_template(windmill_client=windmill_client,
                              tracker_client=tracker_client,
                              metadata=metadata,
                              input_model_uri=args.input_model_uri,
                              output_model_uri=output_model_uri,
                              ensemble_name=ensemble,
                              pre_name=pre,
                              post_name=post,
                              model_name=model,
                              accelerator=args.accelerator)

    # 3.评估数据集
    response = read_file(input_dir=args.input_dataset_uri)
    triton_server_extra_args = get_accelerator(name=args.accelerator).suggest_args()
    dataset_instance = parse_dataset_name(name=response["objectName"])
    response = windmill_client.get_dataset(workspace_id=dataset_instance.workspace_id,
                                           project_name=dataset_instance.project_name,
                                           local_name=dataset_instance.local_name)

    if is_base64(args.advanced_parameters):
        advanced_parameters = json.loads(base64.b64decode(args.advanced_parameters))
    else:
        advanced_parameters = json.loads(args.advanced_parameters)
    conf_threshold = advanced_parameters["conf_threshold"]
    iou_threshold = advanced_parameters["iou_threshold"]
    eval_metric_analysis = EvalMetricAnalysis(category=response.category["category"],
                                              conf_threshold=conf_threshold,
                                              iou_threshold=iou_threshold)
    metric = Metric([eval_metric_analysis], dataset_name=response.artifact["name"])
    evaluate(model_path=output_model_uri,
             dataset_path=args.input_dataset_uri,
             annotation_format=response.annotationFormat,
             output_uri=tracker_client.job_work_dir,
             metric=metric,
             triton_server_extra_args=triton_server_extra_args)

    try:
        if args.icafe_id:
            from gaea_operator.components.icafe import icafe
            icafe.sync_icafe_transform_eval_end(args)
    except Exception as e:
        bcelogger.error(f"Sync icafe failed args:{args} exception: {e}")


if __name__ == "__main__":
    args = parse_args()
    transform_eval(args=args)
