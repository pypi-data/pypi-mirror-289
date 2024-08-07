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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from edgeimpulse_api.models.entitlement_limits import EntitlementLimits

class AdminUpdateOrganizationRequest(BaseModel):
    logo: Optional[StrictStr] = Field(None, description="New logo URL, or set to `null` to remove the logo.")
    header_img: Optional[StrictStr] = Field(None, alias="headerImg", description="New leader image URL, or set to `null` to remove the leader.")
    name: Optional[StrictStr] = Field(None, description="New organization name.")
    experiments: Optional[List[StrictStr]] = None
    readme: Optional[StrictStr] = Field(None, description="Readme for the organization (in Markdown)")
    billable: Optional[StrictBool] = None
    entitlement_limits: Optional[EntitlementLimits] = Field(None, alias="entitlementLimits")
    contract_start_date: Optional[datetime] = Field(None, alias="contractStartDate", description="The date in which the organization contract started. Compute time will be calculated from this date.")
    domain: Optional[StrictStr] = Field(None, description="The domain of the organization. The organization domain is used to add new users to an organization. For example, new @edgeimpulse.com would be added to the Edge Impulse organization if this organization has edgeimpulse.com as the domain.")
    __properties = ["logo", "headerImg", "name", "experiments", "readme", "billable", "entitlementLimits", "contractStartDate", "domain"]

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
    def from_json(cls, json_str: str) -> AdminUpdateOrganizationRequest:
        """Create an instance of AdminUpdateOrganizationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of entitlement_limits
        if self.entitlement_limits:
            _dict['entitlementLimits'] = self.entitlement_limits.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AdminUpdateOrganizationRequest:
        """Create an instance of AdminUpdateOrganizationRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AdminUpdateOrganizationRequest.construct(**obj)

        _obj = AdminUpdateOrganizationRequest.construct(**{
            "logo": obj.get("logo"),
            "header_img": obj.get("headerImg"),
            "name": obj.get("name"),
            "experiments": obj.get("experiments"),
            "readme": obj.get("readme"),
            "billable": obj.get("billable"),
            "entitlement_limits": EntitlementLimits.from_dict(obj.get("entitlementLimits")) if obj.get("entitlementLimits") is not None else None,
            "contract_start_date": obj.get("contractStartDate"),
            "domain": obj.get("domain")
        })
        return _obj

