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
from pydantic import BaseModel, Field

class OrganizationComputeTimeUsage(BaseModel):
    cpu_compute_time: Optional[float] = Field(None, alias="cpuComputeTime", description="CPU compute time in seconds of all jobs in the organization (including organizational project jobs).")
    gpu_compute_time: Optional[float] = Field(None, alias="gpuComputeTime", description="GPU compute time in seconds of all jobs in the organization (including organizational project jobs).")
    total_compute_time: Optional[float] = Field(None, alias="totalComputeTime", description="Total compute time is the amount of computation time spent in jobs, in minutes used by an organization over the given period, calculated as CPU + GPU minutes.")
    __properties = ["cpuComputeTime", "gpuComputeTime", "totalComputeTime"]

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
    def from_json(cls, json_str: str) -> OrganizationComputeTimeUsage:
        """Create an instance of OrganizationComputeTimeUsage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationComputeTimeUsage:
        """Create an instance of OrganizationComputeTimeUsage from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OrganizationComputeTimeUsage.construct(**obj)

        _obj = OrganizationComputeTimeUsage.construct(**{
            "cpu_compute_time": obj.get("cpuComputeTime"),
            "gpu_compute_time": obj.get("gpuComputeTime"),
            "total_compute_time": obj.get("totalComputeTime")
        })
        return _obj

