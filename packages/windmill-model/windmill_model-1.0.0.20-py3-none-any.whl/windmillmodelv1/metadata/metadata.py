#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/8/2
# @Author  : yanxiaodong
# @File    : model_metadata_update.py
"""
import os
from typing import Dict
import yaml

import bcelogger
from pygraphv1.client.graph_api_graph import GraphContent
from windmillmodelv1.client.model_api_model import Category, Label


def metadata(graph: GraphContent, model_metadata: Dict, input_uri: str = "/home/windmill/tmp/model"):
    """
    Update the model metadata.
    """
    # 1. 获取后处理节点
    model_name = None
    category = None
    for node in graph.nodes:
        for property_ in node.properties:
            if property_.name == "localName":
                model_name = property_.value
            if property_.name == "category" and property_.value == Category.CategoryImagePostprocess.value:
                category = property_.value
        if model_name is not None and category is not None:
            break
    assert category is not None, "No postprocess model found"
    bcelogger.info(f"Postprocess model name: {model_name}, category: {category}")

    # 2. 解析后处理节点
    labels = []
    label_set = set()
    index = 0
    filepath = os.path.join(input_uri, model_name, "parse.yaml")
    data = yaml.load(open(filepath, "r"), Loader=yaml.FullLoader)
    assert len(data["outputs"]) > 0, f"No output found in {data}"
    assert "fields_map" in data["outputs"][0], f'Field fields_map not in {data["outputs"][0]}'
    for item in data["outputs"][0]["fields_map"]:
        for label in item["categories"]:
            if label["id"] in label_set:
                continue
            bcelogger.info(f'Model {item["model_name"]} label: {label}')
            if "display_name" in label:
                idx = label["id"]
                name = label["name"]
                display_name = label["display_name"]
                label_set.add(label["name"])
            else:
                idx = index
                name = label["id"]
                display_name = label["name"]
                index += 1
                label_set.add(label["id"])
            labels.append(Label(id=idx, name=name, displayName=display_name).dict())
            index += 1

    model_metadata["labels"] = labels
    metadata["graphContent"] = graph.dict(by_alias=True)