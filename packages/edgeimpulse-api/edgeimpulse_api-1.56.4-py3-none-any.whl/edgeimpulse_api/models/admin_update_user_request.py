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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class AdminUpdateUserRequest(BaseModel):
    email: Optional[StrictStr] = Field(None, description="New email. This will also update the forum's email address but the user may need to logout/login back")
    name: Optional[StrictStr] = Field(None, description="New user full name")
    activated: Optional[StrictBool] = Field(None, description="Whether the user is active or not. Can only go from inactive to active.")
    suspended: Optional[StrictBool] = Field(None, description="Whether the user is suspended or not.")
    job_title: Optional[StrictStr] = Field(None, alias="jobTitle", description="New user job title")
    experiments: Optional[List[StrictStr]] = Field(None, description="List of user experiments")
    __properties = ["email", "name", "activated", "suspended", "jobTitle", "experiments"]

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
    def from_json(cls, json_str: str) -> AdminUpdateUserRequest:
        """Create an instance of AdminUpdateUserRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdminUpdateUserRequest:
        """Create an instance of AdminUpdateUserRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AdminUpdateUserRequest.construct(**obj)

        _obj = AdminUpdateUserRequest.construct(**{
            "email": obj.get("email"),
            "name": obj.get("name"),
            "activated": obj.get("activated"),
            "suspended": obj.get("suspended"),
            "job_title": obj.get("jobTitle"),
            "experiments": obj.get("experiments")
        })
        return _obj

