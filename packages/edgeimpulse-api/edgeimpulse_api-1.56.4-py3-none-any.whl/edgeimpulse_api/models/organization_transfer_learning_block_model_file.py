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



from pydantic import BaseModel, Field, StrictStr, validator

class OrganizationTransferLearningBlockModelFile(BaseModel):
    id: StrictStr = Field(..., description="Output artifact unique file ID, in kebab case")
    name: StrictStr = Field(..., description="Output artifact file name")
    type: StrictStr = Field(..., description="Output artifact file type")
    description: StrictStr = Field(..., description="Output artifact file description")
    __properties = ["id", "name", "type", "description"]

    @validator('type')
    def type_validate_enum(cls, v):
        if v not in ('binary', 'json', 'text'):
            raise ValueError("must validate the enum values ('binary', 'json', 'text')")
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
    def from_json(cls, json_str: str) -> OrganizationTransferLearningBlockModelFile:
        """Create an instance of OrganizationTransferLearningBlockModelFile from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationTransferLearningBlockModelFile:
        """Create an instance of OrganizationTransferLearningBlockModelFile from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OrganizationTransferLearningBlockModelFile.construct(**obj)

        _obj = OrganizationTransferLearningBlockModelFile.construct(**{
            "id": obj.get("id"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "description": obj.get("description")
        })
        return _obj

