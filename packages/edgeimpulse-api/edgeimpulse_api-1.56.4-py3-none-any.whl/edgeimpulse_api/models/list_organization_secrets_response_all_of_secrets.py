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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from edgeimpulse_api.models.created_updated_by_user import CreatedUpdatedByUser

class ListOrganizationSecretsResponseAllOfSecrets(BaseModel):
    id: StrictInt = ...
    name: StrictStr = ...
    description: StrictStr = ...
    created: datetime = ...
    created_by_user: Optional[CreatedUpdatedByUser] = Field(None, alias="createdByUser")
    __properties = ["id", "name", "description", "created", "createdByUser"]

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
    def from_json(cls, json_str: str) -> ListOrganizationSecretsResponseAllOfSecrets:
        """Create an instance of ListOrganizationSecretsResponseAllOfSecrets from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of created_by_user
        if self.created_by_user:
            _dict['createdByUser'] = self.created_by_user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListOrganizationSecretsResponseAllOfSecrets:
        """Create an instance of ListOrganizationSecretsResponseAllOfSecrets from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ListOrganizationSecretsResponseAllOfSecrets.construct(**obj)

        _obj = ListOrganizationSecretsResponseAllOfSecrets.construct(**{
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "created": obj.get("created"),
            "created_by_user": CreatedUpdatedByUser.from_dict(obj.get("createdByUser")) if obj.get("createdByUser") is not None else None
        })
        return _obj

