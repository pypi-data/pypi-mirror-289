#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/27
# @Author  : yanxiaodong
# @File    : algorithm.py
"""
import bcelogger
from windmillmodelv1.client.model_api_modelstore import parse_modelstore_name
from windmillclient.client.windmill_client import WindmillClient

from .accelerator import get_accelerator


class ModelTemplate(object):
    """
    Algorithm class
    """
    PPYOLOE_PLUS_NAME = "PPYOLOEPLUS/Model"
    CHANGE_PPYOLOE_PLUS_NAME = "ChangePPYOLOEPLUS/Model"
    RESNET_NAME = "ResNet/Model"
    OCRNET_NAME = "OCRNet/Model"
    CHANGE_OCRNET_NAME = "ChangeOCRNet/Model"
    CODETR_NAME = "CODETR/Model"
    REPVIT_NAME = "RepVit/Model"
    CONVNEXT_NAME = "ConvNext/Model"
    VITBASE_NAME = "VitBase/Model"

    DEFAULT_SCENE = ""

    def __init__(self, windmill_client: WindmillClient,
                 model_store_name: str,
                 scene: str = None,
                 accelerator: str = "T4",
                 algorithm: str = "PPYOLOEPLUS/Model"):
        self.windmill_client = windmill_client
        self.scene = scene
        self.accelerator = get_accelerator(name=accelerator)
        self.algorithm = algorithm

        model_store = parse_modelstore_name(model_store_name)
        self.workspace_id = model_store.workspace_id
        self.model_store_name = model_store.local_name

        bcelogger.info(f"Model scene is {self.scene}")

    def suggest_template_model(self):
        """
        Get template name for model
        """
        tags = [{"algorithm": self.algorithm}]
        if self.scene is not None and len(self.scene) > 0:
            tags.append({"scene": self.scene})
        else:
            tags.append({"scene": self.DEFAULT_SCENE})

        bcelogger.info(f"List model for workspace_id {self.workspace_id} "
                       f"model_store_name {self.model_store_name} "
                       f"and tags {tags}")
        response = self.windmill_client.list_model(workspace_id=self.workspace_id,
                                                   model_store_name=self.model_store_name,
                                                   tags=tags)
        assert len(response.result) > 0, f"No model found for tags {tags}"
        for model in response.result:
            model_accelerator = model["preferModelServerParameters"]["resource"]["accelerator"]
            if get_accelerator(name=model_accelerator).get_kind == self.accelerator.get_kind:
                bcelogger.info(f"Model {model['name']} found")
                return model["name"]
        raise ValueError(f"The model {response.result} not found for kind {self.accelerator.get_kind}")

    def suggest_template_ensemble(self):
        """
        Get template name for ensemble
        """
        if self.scene is not None and len(self.scene) > 0:
            scene_list = self.scene.rsplit("/", maxsplit=1)
            assert len(scene_list) >= 1, f"Scene {self.scene} is not valid."

            ensemble_scene = scene_list[0] + "/" + "Ensemble"
            tags = [{"scene": ensemble_scene}]
        else:
            algorithm_list = self.algorithm.rsplit("/", maxsplit=1)
            assert len(algorithm_list) >= 1, f"Algorithm {self.algorithm} is not valid."
            ensemble_algorithm = algorithm_list[0] + "/" + "Ensemble"
            tags = [{"algorithm": ensemble_algorithm}]

        bcelogger.info(f"List model for workspace_id {self.workspace_id} "
                       f"model_store_name {self.model_store_name} "
                       f"and tags {tags}")
        response = self.windmill_client.list_model(workspace_id=self.workspace_id,
                                                   model_store_name=self.model_store_name,
                                                   tags=tags)
        assert len(response.result) > 0, f"No model found for tags {tags}"
        for model in response.result:
            model_accelerator = model["preferModelServerParameters"]["resource"]["accelerator"]
            if get_accelerator(name=model_accelerator).get_kind == self.accelerator.get_kind:
                bcelogger.info(f"Model {model['name']} found")
                return model["name"]
        raise ValueError(f"The model {response.result} not found for kind {self.accelerator.get_kind}")

    def suggest_template_preprocess(self):
        """
        Get template name for preprocess
        """
        if self.scene is not None and len(self.scene) > 0:
            scene_list = self.scene.split("/", maxsplit=1)
            assert len(scene_list) >= 1, f"Scene {self.scene} is not valid."

            ensemble_scene = scene_list[0] + "/" + "Preprocess"
            tags = [{"scene": ensemble_scene}]
        else:
            algorithm_list = self.algorithm.split("/", maxsplit=1)
            assert len(algorithm_list) >= 1, f"Algorithm {self.algorithm} is not valid."
            ensemble_algorithm = algorithm_list[0] + "/" + "Preprocess"
            tags = [{"algorithm": ensemble_algorithm}]

        bcelogger.info(f"List model for workspace_id {self.workspace_id} "
                       f"model_store_name {self.model_store_name} "
                       f"and tags {tags}")
        response = self.windmill_client.list_model(workspace_id=self.workspace_id,
                                                   model_store_name=self.model_store_name,
                                                   tags=tags)
        assert len(response.result) > 0, f"No model found for tags {tags}"
        for model in response.result:
            model_accelerator = model["preferModelServerParameters"]["resource"]["accelerator"]
            if get_accelerator(name=model_accelerator).get_kind == self.accelerator.get_kind:
                bcelogger.info(f"Model {model['name']} found")
                return model["name"]
        raise ValueError(f"The model {response.result} not found for kind {self.accelerator.get_kind}")

    def suggest_template_postprocess(self):
        """
        Get template name for postprocess
        """
        if self.scene is not None and len(self.scene) > 0:
            scene_list = self.scene.split("/", maxsplit=1)
            assert len(scene_list) >= 1, f"Scene {self.scene} is not valid."

            ensemble_scene = scene_list[0] + "/" + "Postprocess"
            tags = [{"scene": ensemble_scene}]
        else:
            algorithm_list = self.algorithm.split("/", maxsplit=1)
            assert len(algorithm_list) >= 1, f"Algorithm {self.algorithm} is not valid."
            ensemble_algorithm = algorithm_list[0] + "/" + "Postprocess"
            tags = [{"algorithm": ensemble_algorithm}]

        bcelogger.info(f"List model for workspace_id {self.workspace_id} "
                       f"model_store_name {self.model_store_name} "
                       f"and tags {tags}")
        response = self.windmill_client.list_model(workspace_id=self.workspace_id,
                                                   model_store_name=self.model_store_name,
                                                   tags=tags)
        assert len(response.result) > 0, f"No model found for tags {tags}"
        for model in response.result:
            model_accelerator = model["preferModelServerParameters"]["resource"]["accelerator"]
            if get_accelerator(name=model_accelerator).get_kind == self.accelerator.get_kind:
                bcelogger.info(f"Model {model['name']} found")
                return model["name"]
        raise ValueError(f"The model {response.result} not found for kind {self.accelerator.get_kind}")

