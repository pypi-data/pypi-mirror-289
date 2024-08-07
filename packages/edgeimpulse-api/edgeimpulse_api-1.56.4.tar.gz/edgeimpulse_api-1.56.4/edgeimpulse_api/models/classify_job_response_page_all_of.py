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
from edgeimpulse_api.models.model_prediction import ModelPrediction
from edgeimpulse_api.models.model_result import ModelResult

class ClassifyJobResponsePageAllOf(BaseModel):
    result: List[ModelResult] = ...
    predictions: List[ModelPrediction] = ...
    __properties = ["result", "predictions"]

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
    def from_json(cls, json_str: str) -> ClassifyJobResponsePageAllOf:
        """Create an instance of ClassifyJobResponsePageAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in result (list)
        _items = []
        if self.result:
            for _item in self.result:
                if _item:
                    _items.append(_item.to_dict())
            _dict['result'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in predictions (list)
        _items = []
        if self.predictions:
            for _item in self.predictions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['predictions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClassifyJobResponsePageAllOf:
        """Create an instance of ClassifyJobResponsePageAllOf from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ClassifyJobResponsePageAllOf.construct(**obj)

        _obj = ClassifyJobResponsePageAllOf.construct(**{
            "result": [ModelResult.from_dict(_item) for _item in obj.get("result")] if obj.get("result") is not None else None,
            "predictions": [ModelPrediction.from_dict(_item) for _item in obj.get("predictions")] if obj.get("predictions") is not None else None
        })
        return _obj

