#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/3/8
# @Author  : yanxiaodong
# @File    : consts.py
"""
DEFAULT_TRAIN_CONFIG_FILE_NAME = "train_config.yaml"
DEFAULT_TRANSFORM_CONFIG_FILE_NAME = "transform_config.yaml"
DEFAULT_DEPLOY_CONFIG_FILE_NAME = "deploy_config.yaml"
DEFAULT_META_FILE_NAME = "meta.yaml"
DEFAULT_METRIC_FILE_NAME = "metric.json"
DEFAULT_PADDLEPADDLE_MODEL_FILE_NAME = "best_model.pdparams"
DEFAULT_TRITON_CONFIG_FILE_NAME = "config.pbtxt"
DEFAULT_PYTORCH_MODEL_FILE_NAME = "best_model.pth"

# 数据存放文件夹的目录为对应filesystem的endpoint目录下（例如：cvfs的endpoint为/wsmp/store）
# 数据挖掘文件夹名称
DEFAULT_DATA_MINING_FOLDER_NAME = "data_mining"
# 数据标注（人工）文件夹名称
DEFAULT_DATA_LABEL_FOLDER_NAME = "data_label"
# 互联网搜图文件夹名称
DEFAULT_NET_SEARCH_FOLDER_NAME = "data_net_search"
# AIGC文件夹名称
DEFAULT_AIGC_FOLDER_NAME = "data_aigc"
# 数据存储（上传）文件夹名称
DEFAULT_DATA_UPLOAD_FOLDER_NAME = "data_upload"
# 数据筛选文件夹名称
DEFAULT_DATA_SELECT_FOLDER_NAME = "data_select"
# 交通资产管理平台的bucket
DEFAULT_TRAFFIC_BUCKET = "air-ai-forge-data"