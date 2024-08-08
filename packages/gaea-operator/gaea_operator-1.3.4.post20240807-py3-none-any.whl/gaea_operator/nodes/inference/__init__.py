#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/21
# @Author  : yanxiaodong
# @File    : __init__.py.py
"""
from typing import Dict, List
from paddleflow.pipeline import ContainerStep
from paddleflow.pipeline import Artifact

from ..base_node import BaseNode, set_node_parameters
from ..types import Properties
from gaea_operator.artifacts import Variable
from gaea_operator.utils import Accelerator, get_accelerator


class Inference(BaseNode):
    """
    Transform
    """
    NAME = "inference"
    DISPLAY_NAME = "模型包评估"

    def __init__(self,
                 inference_skip: int = -1,
                 accelerator: str = Accelerator.T4,
                 pre_nodes: Dict[str, ContainerStep] = None):
        self.accelerator = accelerator
        accelerator = get_accelerator(kind=Accelerator.NVIDIA)
        compute_tips = {Accelerator.NVIDIA: ["training"] + accelerator.suggest_resource_tips()}
        flavour_tips = {Accelerator.NVIDIA: accelerator.suggest_flavour_tips()}

        accelerator = get_accelerator(kind=Accelerator.KUNLUN)
        compute_tips[Accelerator.KUNLUN] = ["training"] + accelerator.suggest_resource_tips()
        flavour_tips[Accelerator.KUNLUN] = accelerator.suggest_flavour_tips()
        properties = Properties(accelerator=self.accelerator,
                                computeTips=compute_tips,
                                flavourTips=flavour_tips,
                                modelFormats=["TensorRT", "PaddleLite"])

        inputs: List[Variable] = \
            [
                Variable(type="model", name="input_model_uri", value="package.output_model_uri"),
                Variable(type="dataset", name="input_dataset_uri", value="eval.output_dataset_uri")
            ]

        super().__init__(inputs=inputs, properties=properties)

        self.inference_skip = inference_skip
        self.pre_nodes = pre_nodes

    def __call__(self,
                 base_params: dict = None,
                 base_env: dict = None,
                 ensemble_model_name: str = "",
                 dataset_name: str = ""):
        inference_params = {"skip": self.inference_skip,
                            "accelerator": self.accelerator,
                            "model_name": ensemble_model_name,
                            "dataset_name": dataset_name,
                            "advanced_parameters": '{"conf_threshold":"0.5"}'}
        inference_env = {"ACCELERATOR": "{{accelerator}}",
                         "MODEL_NAME": "{{model_name}}",
                         "DATASET_NAME": "{{dataset_name}}",
                         "ADVANCED_PARAMETERS": "{{advanced_parameters}}"}
        inference_params.update(base_params)
        inference_env.update(base_env)
        accelerator = get_accelerator(name=self.accelerator)
        inference_env.update(accelerator.suggest_env())

        inference = ContainerStep(name=Inference.name(),
                                  docker_env=self.suggest_image(),
                                  env=inference_env,
                                  parameters=inference_params,
                                  outputs={"output_uri": Artifact()},
                                  command=f'cd /root && '
                                          f'python3 -m gaea_operator.nodes.inference.inference '
                                          f'--input-model-uri={{{{input_model_uri}}}} '
                                          f'--input-dataset-uri={{{{input_dataset_uri}}}} '
                                          f'--output-uri={{{{output_uri}}}}')
        set_node_parameters(skip=self.inference_skip, step=inference, inputs=self.inputs, pre_nodes=self.pre_nodes)

        return inference
