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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt
from edgeimpulse_api.models.anomaly_config import AnomalyConfig
from edgeimpulse_api.models.anomaly_gmm_metadata import AnomalyGmmMetadata
from edgeimpulse_api.models.anomaly_model_metadata import AnomalyModelMetadata

class DetailedImpulseLearnBlockAnomalyConfigsInner(BaseModel):
    block_id: StrictInt = Field(..., alias="blockId")
    config: AnomalyConfig = ...
    metadata: Optional[AnomalyModelMetadata] = None
    gmm_metadata: Optional[AnomalyGmmMetadata] = Field(None, alias="gmmMetadata")
    __properties = ["blockId", "config", "metadata", "gmmMetadata"]

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
    def from_json(cls, json_str: str) -> DetailedImpulseLearnBlockAnomalyConfigsInner:
        """Create an instance of DetailedImpulseLearnBlockAnomalyConfigsInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gmm_metadata
        if self.gmm_metadata:
            _dict['gmmMetadata'] = self.gmm_metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DetailedImpulseLearnBlockAnomalyConfigsInner:
        """Create an instance of DetailedImpulseLearnBlockAnomalyConfigsInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DetailedImpulseLearnBlockAnomalyConfigsInner.construct(**obj)

        _obj = DetailedImpulseLearnBlockAnomalyConfigsInner.construct(**{
            "block_id": obj.get("blockId"),
            "config": AnomalyConfig.from_dict(obj.get("config")) if obj.get("config") is not None else None,
            "metadata": AnomalyModelMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None,
            "gmm_metadata": AnomalyGmmMetadata.from_dict(obj.get("gmmMetadata")) if obj.get("gmmMetadata") is not None else None
        })
        return _obj

