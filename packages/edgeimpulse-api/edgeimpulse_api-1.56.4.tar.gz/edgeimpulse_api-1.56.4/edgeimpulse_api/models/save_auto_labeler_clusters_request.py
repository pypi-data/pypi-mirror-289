# coding: utf-8

"""
    Edge Impulse API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel
from edgeimpulse_api.models.save_auto_labeler_clusters_request_clusters_inner import SaveAutoLabelerClustersRequestClustersInner

class SaveAutoLabelerClustersRequest(BaseModel):
    clusters: List[SaveAutoLabelerClustersRequestClustersInner] = ...
    __properties = ["clusters"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = False

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SaveAutoLabelerClustersRequest:
        """Create an instance of SaveAutoLabelerClustersRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in clusters (list)
        _items = []
        if self.clusters:
            for _item in self.clusters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['clusters'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SaveAutoLabelerClustersRequest:
        """Create an instance of SaveAutoLabelerClustersRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SaveAutoLabelerClustersRequest.construct(**obj)

        _obj = SaveAutoLabelerClustersRequest.construct(**{
            "clusters": [SaveAutoLabelerClustersRequestClustersInner.from_dict(_item) for _item in obj.get("clusters")] if obj.get("clusters") is not None else None
        })
        return _obj

