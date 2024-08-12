#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/6/05
# @Author  : 李岱
# @File    : __init__.py.py
"""

import os
from argparse import ArgumentParser
import json
import base64

from gaea_tracker import ExperimentTracker
from bcelogger.base_logger import setup_logger
import bcelogger
from windmilltrainingv1.client.training_api_dataset import parse_dataset_name
from windmillclient.client.windmill_client import WindmillClient
from tritonv2.evaluator import evaluate

from gaea_operator.metric import InferenceMetricAnalysis, Metric
from gaea_operator.utils import get_accelerator, read_file, is_base64


def parse_args():
    """
    Parse arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("--windmill-ak", type=str, default=os.environ.get("WINDMILL_AK"))
    parser.add_argument("--windmill-sk", type=str, default=os.environ.get("WINDMILL_SK"))
    parser.add_argument("--windmill-endpoint", type=str, default=os.environ.get("WINDMILL_ENDPOINT"))
    parser.add_argument("--project-name", type=str, default=os.environ.get("PROJECT_NAME"))
    parser.add_argument("--tracking-uri", type=str, default=os.environ.get("TRACKING_URI"))
    parser.add_argument("--experiment-name", type=str, default=os.environ.get("EXPERIMENT_NAME"))
    parser.add_argument("--experiment-kind", type=str, default=os.environ.get("EXPERIMENT_KIND"))
    parser.add_argument("--accelerator", type=str, default=os.environ.get("ACCELERATOR", "t4"))
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


def inference(args):
    """
    Package component for ppyoloe_plus model.
    """
    try:
        if args.icafe_id:
            from gaea_operator.components.icafe import icafe
            icafe.sync_icafe_inference_start(args)
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

    ensemble_artifact_name = response["artifact"]["name"]
    output_model_uri = "/home/windmill/tmp/model"
    # 1. 下载ensemble template 模型
    bcelogger.info(f"Downloading ensemble from {ensemble_artifact_name}")
    windmill_client.dump_models(artifact_name=ensemble_artifact_name,
                                location_style="Triton",
                                rename="ensemble",
                                output_uri=output_model_uri)

    # 2.评估数据集
    response = read_file(input_dir=args.input_dataset_uri)
    dataset_instance = parse_dataset_name(name=response["objectName"])
    response = windmill_client.get_dataset(workspace_id=dataset_instance.workspace_id,
                                           project_name=dataset_instance.project_name,
                                           local_name=dataset_instance.local_name)

    triton_server_extra_args = get_accelerator(name=args.accelerator).suggest_args()
    if is_base64(args.advanced_parameters):
        advanced_parameters = json.loads(base64.b64decode(args.advanced_parameters))
    else:
        advanced_parameters = json.loads(args.advanced_parameters)

    conf_threshold = advanced_parameters["conf_threshold"]
    eval_metric_analysis = InferenceMetricAnalysis(conf_threshold=conf_threshold)
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
            icafe.sync_icafe_inference_end(args)
    except Exception as e:
        bcelogger.error(f"Sync icafe failed args:{args} exception: {e}")


if __name__ == "__main__":
    args = parse_args()
    inference(args=args)
