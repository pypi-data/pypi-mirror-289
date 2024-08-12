#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/4/01
# @Author  : liyinggang
# @File    : transform_component.py
"""
import os
import json
from argparse import ArgumentParser

import bcelogger
from gaea_tracker import ExperimentTracker
from bcelogger.base_logger import setup_logger
from windmilltrainingv1.client.training_api_dataset import parse_dataset_name
from windmillmodelv1.client.model_api_model import parse_model_name
from windmillclient.client.windmill_client import WindmillClient
from gaea_operator.transform import Transform

from gaea_operator.config import Config
from gaea_operator.utils import write_file, read_file, ModelTemplate, get_accelerator
from gaea_operator.config.generate_transform_config import KEY_ACCELERATOR
from gaea_operator.config import OCRNetConfig


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
    parser.add_argument("--transform-model-name",
                        type=str,
                        default=os.environ.get("TRANSFORM_MODEL_NAME"))
    parser.add_argument("--transform-model-display-name",
                        type=str,
                        default=os.environ.get("TRANSFORM_MODEL_DISPLAY_NAME"))
    parser.add_argument("--accelerator", type=str, default=os.environ.get("ACCELERATOR", "T4"))
    parser.add_argument("--advanced-parameters",
                        type=str,
                        default=os.environ.get("ADVANCED_PARAMETERS", "{}"))

    parser.add_argument("--input-model-uri", type=str, default=os.environ.get("INPUT_MODEL_URI"))
    parser.add_argument("--input-dataset-uri", type=str, default=os.environ.get("INPUT_DATASET_URI"))
    parser.add_argument("--output-model-uri", type=str, default=os.environ.get("OUTPUT_MODEL_URI"))
    parser.add_argument("--output-uri", type=str, default=os.environ.get("OUTPUT_URI"))

    args, _ = parser.parse_known_args()

    return args


def change_ocrnet_transform(args):
    """
    Transform component for model.
    """
    try:
        if args.icafe_id:
            from gaea_operator.components.icafe import icafe
            icafe.sync_icafe_transform_start(args)
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

    input_model_response = read_file(input_dir=args.input_model_uri)
    response = windmill_client.get_artifact(object_name=input_model_response['artifact']["objectName"],
                                            version=str(input_model_response['artifact']["version"]))
    metadata = response.metadata

    # 1. 生成转换配置文件，固定名称 transform_config.yaml 保存在 output_model_uri
    transform_advanced_parameters = json.loads(args.advanced_parameters)
    transform_advanced_parameters.update({KEY_ACCELERATOR: args.accelerator})
    config = OCRNetConfig(windmill_client=windmill_client, tracker_client=tracker_client, metadata=metadata)

    config.write_transform_config(model_uri=args.output_model_uri, advanced_parameters=transform_advanced_parameters)

    # 2. 下载模板模型
    model_template = ModelTemplate(windmill_client=windmill_client,
                                   scene=args.scene,
                                   accelerator=args.accelerator,
                                   model_store_name=args.public_model_store,
                                   algorithm=ModelTemplate.CHANGE_OCRNET_NAME)
    model = model_template.suggest_template_model()
    windmill_client.download_artifact(object_name=model, version="latest", output_uri=args.output_model_uri)

    if args.input_dataset_uri is not None and len(args.input_dataset_uri) > 0:
        bcelogger.info("input_dataset_uri: {args.input_dataset_uri}")
        response = read_file(input_dir=args.input_dataset_uri)
        dataset_instance = parse_dataset_name(name=response["objectName"])
        response = windmill_client.get_dataset(workspace_id=dataset_instance.workspace_id,
                                            project_name=dataset_instance.project_name,
                                            local_name=dataset_instance.local_name)
    # 3. 生成配置文件
    modify_model_names = {'model': [model]}
    config.write_sub_model_config(transform_model_uri=args.output_model_uri,
                                  modify_model_names=modify_model_names)

    # 4. 转换
    Transform(windmill_client=windmill_client).transform(transform_config_dir=args.output_model_uri,
                                                         src_model_uri=args.input_model_uri,
                                                         dst_model_uri=args.output_model_uri,
                                                         src_dataset_uri=args.input_dataset_uri)

    # 5. 上传转换后的模型
    accelerator = get_accelerator(name=args.accelerator)
    model_name = parse_model_name(name=args.transform_model_name)
    workspace_id = model_name.workspace_id
    model_store_name = model_name.model_store_name
    local_name = model_name.local_name
    response = windmill_client.create_model(
        artifact_uri=args.output_model_uri,
        workspace_id=workspace_id,
        model_store_name=model_store_name,
        local_name=local_name,
        display_name=args.transform_model_display_name,
        prefer_model_server_parameters=accelerator.suggest_model_server_parameters(),
        category="Image/ChangeDetection/SemanticSegmentation",
        artifact_metadata=config.metadata,
        model_formats=[
            Config.accelerator2model_format[args.accelerator]])
    bcelogger.info(f"Model {args.transform_model_name} created response: {response}")

    # 6. 输出文件
    write_file(obj=json.loads(response.raw_data), output_dir=args.output_model_uri)

    try:
        if args.icafe_id:
            from gaea_operator.components.icafe import icafe
            icafe.sync_icafe_transform_end(args)
    except Exception as e:
        bcelogger.error(f"Sync icafe failed args:{args} exception: {e}")


if __name__ == "__main__":
    args = parse_args()
    change_ocrnet_transform(args=args)
