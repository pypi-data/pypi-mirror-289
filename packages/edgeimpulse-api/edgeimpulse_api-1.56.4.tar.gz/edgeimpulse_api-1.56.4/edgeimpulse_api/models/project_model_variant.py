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



from pydantic import BaseModel, Field, StrictBool
from edgeimpulse_api.models.keras_model_variant_enum import KerasModelVariantEnum

class ProjectModelVariant(BaseModel):
    variant: KerasModelVariantEnum = ...
    is_reference_variant: StrictBool = Field(..., alias="isReferenceVariant", description="True if this model variant is the default or \"reference variant\" for this project")
    is_enabled: StrictBool = Field(..., alias="isEnabled", description="True if profiling for this model variant is enabled for the current project")
    is_selected: StrictBool = Field(..., alias="isSelected", description="True if this is the selected model variant for this project, used to keep the same view after refreshing. Update this via defaultProfilingVariant in UpdateProjectRequest.")
    __properties = ["variant", "isReferenceVariant", "isEnabled", "isSelected"]

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
    def from_json(cls, json_str: str) -> ProjectModelVariant:
        """Create an instance of ProjectModelVariant from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProjectModelVariant:
        """Create an instance of ProjectModelVariant from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ProjectModelVariant.construct(**obj)

        _obj = ProjectModelVariant.construct(**{
            "variant": obj.get("variant"),
            "is_reference_variant": obj.get("isReferenceVariant"),
            "is_enabled": obj.get("isEnabled"),
            "is_selected": obj.get("isSelected")
        })
        return _obj

