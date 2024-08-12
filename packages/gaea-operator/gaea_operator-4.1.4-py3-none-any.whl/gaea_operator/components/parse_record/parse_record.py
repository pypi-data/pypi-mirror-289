#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, random, re, string, sys
from argparse import ArgumentParser
import bcelogger
from windmillcomputev1.client.compute_api_filesystem import parse_filesystem_name
from windmilltrainingv1.client.training_api_dataset import parse_dataset_name
from windmillclient.client.windmill_client import WindmillClient
from bcelogger.base_logger import setup_logger

sys.path.append(os.environ.get("RECORD_UTILS_PATH"))
from extract_image import extract_image


PARSE_RECORD_DIR = "parse_record"


def parse_args():
    """
    Parse arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("--windmill-ak", type=str, default=os.environ.get("WINDMILL_AK"))
    parser.add_argument("--windmill-sk", type=str, default=os.environ.get("WINDMILL_SK"))
    parser.add_argument("--windmill-endpoint", type=str, default=os.environ.get("WINDMILL_ENDPOINT"))
    parser.add_argument("--project-name", type=str, default=os.environ.get("PROJECT_NAME"))
    parser.add_argument("--workspace-id", type=str, default=os.environ.get("WORKSPACE_ID"))

    parser.add_argument("--output-uri", type=str, default=os.environ.get("PF_OUTPUT_ARTIFACT_OUTPUT_URI"))

    parser.add_argument("--work-dir", type=str, default=os.environ.get("PF_WORK_DIR"))
    parser.add_argument("--extra-work-dir", type=str, default=os.environ.get("PF_EXTRA_WORK_DIR"))

    parser.add_argument("--input-dataset-name", type=str, default=os.environ.get("INPUT_DATASET_NAME"))

    args, _ = parser.parse_known_args()

    return args


def parse_record(args):
    windmill_client = WindmillClient(ak=args.windmill_ak,
                                     sk=args.windmill_sk,
                                     endpoint=args.windmill_endpoint)
    setup_logger(config=dict(file_name=os.path.join(args.output_uri, "worker.log")))

    # get input dataset
    work_dirs = [args.extra_work_dir, args.work_dir]
    trimmed_str = args.input_dataset_name.strip('[]')
    dataset_list = trimmed_str.split()

    # get dataset filesystem
    input_artifact_response = windmill_client.get_artifact(name=dataset_list[0])
    filesystem = windmill_client.suggest_first_filesystem(workspace_id=input_artifact_response.workspaceID,
                                                          guest_name=input_artifact_response.objectName)

    # find dataset mining files
    dataset_mining_files_dict = _get_dataset_files(windmill_client, dataset_list, work_dirs, filesystem)

    # get output dataset storage path
    job_name = _get_job_name(args.output_uri)
    output_dataset_artifact_uri_path = os.path.join(args.work_dir, PARSE_RECORD_DIR, job_name)

    # trans the input dataset list
    for dataset_name, path in dataset_mining_files_dict.items():
        dataset_name_instance = parse_dataset_name(dataset_name)
        storage_path = os.path.join(output_dataset_artifact_uri_path, dataset_name_instance.local_name)
        bcelogger.info("extract_image path: {} storage_path: {}".format(path, storage_path))
        extract_image(path, storage_path)

    # create new dataset based on exist dataset
    input_artifact_response = windmill_client.get_artifact(name=dataset_list[0])
    _dataset_instance = parse_dataset_name(input_artifact_response.objectName)
    get_output_dataset_response = windmill_client.get_dataset(workspace_id=_dataset_instance.workspace_id,
                                                              project_name=_dataset_instance.project_name,
                                                              local_name=_dataset_instance.local_name)
    dataset_category = get_output_dataset_response.category['category']

    s3_uri_path = output_dataset_artifact_uri_path.replace(args.work_dir, "s3://" + filesystem["endpoint"]) + "/"
    output_dataset_name = f"parse_record-{job_name}"
    bcelogger.info("create new dataset: {}".format(output_dataset_name))
    create_new_dataset_response = windmill_client.create_dataset(
        workspace_id=_dataset_instance.workspace_id,
        project_name=_dataset_instance.project_name,
        category=dataset_category,
        local_name=output_dataset_name,
        display_name=output_dataset_name,
        artifact_uri=s3_uri_path,
    )
    output_dataset_full_name = create_new_dataset_response.name
    bcelogger.info("output_dataset_full_name: {}/versions/1".format(output_dataset_full_name))
    bcelogger.info("create_dataset response: {}".format(create_new_dataset_response))


def find_fs_work_dir(filesystem_local_name, work_dirs):
    """
    查找指定文件系统名称在工作目录列表中的路径，如果没有找到则返回空字符串。
    
    Args:
        filesystem_local_name (str): 文件系统本地名称，例如"nfs://192.168.0.1/data"。
        work_dirs (list[str]): 工作目录列表，每个元素为一个字符串，例如["/home", "/mnt"]。
    
    Returns:
        str: 返回查找结果，如果找到则是包含文件系统本地名称的工作目录路径，否则是空字符串。
    """
    for s in work_dirs:
        if filesystem_local_name in s:
            return s

    return ""


def _get_dataset_files(client, input_datasets, work_dirs, filesystem):
    """
    获取数据集文件，返回一个字典，键为输入的数据集名称，值为该数据集在本地工作目录下的路径。
    
    Args:
        client (Client): Client对象，用于调用API接口。
        input_datasets (List[str]): 需要处理的输入数据集列表，每个元素是一个字符串，代表数据集名称。
        work_dirs (List[str]): 本地工作目录列表，每个元素是一个字符串，代表工作目录的路径。
        filesystem (Dict[str, str]): 包含文件系统名称和终结点的字典，其中 "name" 是文件系统名称，"endpoint" 是终结点。
    
    Returns:
        Dict[str, str]: 返回一个字典，键为输入的数据集名称，值为该数据集在本地工作目录下的路径。如果找不到相应的数据集或工作目录，则返回空字典。
    """
    dataset_mining_files_path = dict()
    filesystem_instance = parse_filesystem_name(filesystem["name"])

    for input_dataset in input_datasets:
        # find dataset artifact path
        input_artifact_response = client.get_artifact(name=input_dataset)
        input_artifact_metadata = input_artifact_response.metadata
        dataset_name = input_artifact_response.objectName
        uri_s3 = input_artifact_metadata["paths"][0]

        # get dataset local path
        _dataset_work_dir = find_fs_work_dir(filesystem_instance.local_name, work_dirs)
        uri_without_s3 = uri_s3.replace("s3://" + filesystem['endpoint'], _dataset_work_dir)
        bcelogger.info("uri without s3: {}".format(uri_without_s3))

        dataset_mining_files_path[input_dataset] = uri_without_s3
        bcelogger.info("dataset_mining_files_path: {}".format(dataset_mining_files_path))
    return dataset_mining_files_path


def _get_job_name(path):
    """
    获取路径中的作业名称，如果没有找到则返回空字符串。
    
    Args:
        path (str): 需要解析的路径字符串。
    
    Returns:
        str: 返回路径中包含的作业名称，如果没有找到则返回空字符串。
    """
    match = re.search(r"job\w+", path)
    if match:
        return match.group()
    else:
        return ""


def _generate_dataset_name(prefix='ds-', length=8):
    """
    生成一个带有前缀和指定长度的随机字符串，默认前缀为'ds-'，长度为8。
    
    Args:
        prefix (str, optional): 字符串前缀，默认为'ds-'（数据集名称前缀）. Defaults to 'ds-'.
        length (int, optional): 字符串长度，默认为8. Defaults to 8.
    
    Returns:
        str: 返回一个带有前缀和指定长度的随机字符串。
    """
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return prefix + random_string


if __name__ == "__main__":
    args = parse_args()
    bcelogger.info("args parameters {}".format(args))
    parse_record(args=args)
