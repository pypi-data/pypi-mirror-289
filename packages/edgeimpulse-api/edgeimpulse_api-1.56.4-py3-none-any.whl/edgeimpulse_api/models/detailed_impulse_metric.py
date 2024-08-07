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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator
from edgeimpulse_api.models.detailed_impulse_metric_category import DetailedImpulseMetricCategory
from edgeimpulse_api.models.detailed_impulse_metric_value import DetailedImpulseMetricValue

class DetailedImpulseMetric(BaseModel):
    name: StrictStr = ...
    type: StrictStr = ...
    category: DetailedImpulseMetricCategory = ...
    description: StrictStr = ...
    value: DetailedImpulseMetricValue = ...
    title: Optional[StrictStr] = None
    value_for_sorting: Optional[StrictInt] = Field(None, alias="valueForSorting")
    __properties = ["name", "type", "category", "description", "value", "title", "valueForSorting"]

    @validator('type')
    def type_validate_enum(cls, v):
        if v not in ('core', 'additional'):
            raise ValueError("must validate the enum values ('core', 'additional')")
        return v

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
    def from_json(cls, json_str: str) -> DetailedImpulseMetric:
        """Create an instance of DetailedImpulseMetric from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DetailedImpulseMetric:
        """Create an instance of DetailedImpulseMetric from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DetailedImpulseMetric.construct(**obj)

        _obj = DetailedImpulseMetric.construct(**{
            "name": obj.get("name"),
            "type": obj.get("type"),
            "category": obj.get("category"),
            "description": obj.get("description"),
            "value": DetailedImpulseMetricValue.from_dict(obj.get("value")) if obj.get("value") is not None else None,
            "title": obj.get("title"),
            "value_for_sorting": obj.get("valueForSorting")
        })
        return _obj

