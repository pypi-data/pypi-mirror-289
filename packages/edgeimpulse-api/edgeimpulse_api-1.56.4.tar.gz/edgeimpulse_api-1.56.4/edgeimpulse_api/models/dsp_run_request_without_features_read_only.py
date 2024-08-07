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


from typing import Dict
from pydantic import BaseModel, Field, StrictStr

class DspRunRequestWithoutFeaturesReadOnly(BaseModel):
    params: Dict[str, StrictStr] = Field(..., description="DSP parameters with values")
    __properties = ["params"]

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
    def from_json(cls, json_str: str) -> DspRunRequestWithoutFeaturesReadOnly:
        """Create an instance of DspRunRequestWithoutFeaturesReadOnly from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DspRunRequestWithoutFeaturesReadOnly:
        """Create an instance of DspRunRequestWithoutFeaturesReadOnly from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DspRunRequestWithoutFeaturesReadOnly.construct(**obj)

        _obj = DspRunRequestWithoutFeaturesReadOnly.construct(**{
            "params": obj.get("params")
        })
        return _obj

