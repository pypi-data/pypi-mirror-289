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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from edgeimpulse_api.models.permission import Permission
from edgeimpulse_api.models.staff_info import StaffInfo
from edgeimpulse_api.models.user_tier_enum import UserTierEnum

class ProjectCollaborator(BaseModel):
    id: StrictInt = ...
    username: StrictStr = ...
    name: StrictStr = ...
    email: StrictStr = ...
    photo: Optional[StrictStr] = None
    created: datetime = ...
    last_seen: Optional[datetime] = Field(None, alias="lastSeen")
    staff_info: StaffInfo = Field(..., alias="staffInfo")
    pending: StrictBool = ...
    last_tos_acceptance_date: Optional[datetime] = Field(None, alias="lastTosAcceptanceDate")
    job_title: Optional[StrictStr] = Field(None, alias="jobTitle")
    permissions: Optional[List[Permission]] = Field(None, description="List of permissions the user has")
    company_name: Optional[StrictStr] = Field(None, alias="companyName")
    activated: StrictBool = Field(..., description="Whether the user has activated their account or not.")
    mfa_configured: StrictBool = Field(..., alias="mfaConfigured", description="Whether the user has configured multi-factor authentication")
    stripe_customer_id: Optional[StrictStr] = Field(None, alias="stripeCustomerId", description="Stripe customer ID, if any.")
    has_pending_payments: Optional[StrictBool] = Field(None, alias="hasPendingPayments", description="Whether the user has pending payments.")
    tier: Optional[UserTierEnum] = None
    is_owner: StrictBool = Field(..., alias="isOwner")
    __properties = ["id", "username", "name", "email", "photo", "created", "lastSeen", "staffInfo", "pending", "lastTosAcceptanceDate", "jobTitle", "permissions", "companyName", "activated", "mfaConfigured", "stripeCustomerId", "hasPendingPayments", "tier", "isOwner"]

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
    def from_json(cls, json_str: str) -> ProjectCollaborator:
        """Create an instance of ProjectCollaborator from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of staff_info
        if self.staff_info:
            _dict['staffInfo'] = self.staff_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProjectCollaborator:
        """Create an instance of ProjectCollaborator from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ProjectCollaborator.construct(**obj)

        _obj = ProjectCollaborator.construct(**{
            "id": obj.get("id"),
            "username": obj.get("username"),
            "name": obj.get("name"),
            "email": obj.get("email"),
            "photo": obj.get("photo"),
            "created": obj.get("created"),
            "last_seen": obj.get("lastSeen"),
            "staff_info": StaffInfo.from_dict(obj.get("staffInfo")) if obj.get("staffInfo") is not None else None,
            "pending": obj.get("pending"),
            "last_tos_acceptance_date": obj.get("lastTosAcceptanceDate"),
            "job_title": obj.get("jobTitle"),
            "permissions": obj.get("permissions"),
            "company_name": obj.get("companyName"),
            "activated": obj.get("activated"),
            "mfa_configured": obj.get("mfaConfigured"),
            "stripe_customer_id": obj.get("stripeCustomerId"),
            "has_pending_payments": obj.get("hasPendingPayments"),
            "tier": obj.get("tier"),
            "is_owner": obj.get("isOwner")
        })
        return _obj

