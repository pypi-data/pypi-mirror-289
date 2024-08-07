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
from pydantic import BaseModel, Field, StrictInt
from edgeimpulse_api.models.organization_pipeline_item_count import OrganizationPipelineItemCount
from edgeimpulse_api.models.organization_pipeline_run_step import OrganizationPipelineRunStep

class OrganizationPipelineRun(BaseModel):
    id: StrictInt = ...
    steps: List[OrganizationPipelineRunStep] = ...
    created: datetime = ...
    finished: Optional[datetime] = None
    item_count_before: Optional[OrganizationPipelineItemCount] = Field(None, alias="itemCountBefore")
    item_count_after: Optional[OrganizationPipelineItemCount] = Field(None, alias="itemCountAfter")
    item_count_import_into_project_failed: Optional[StrictInt] = Field(None, alias="itemCountImportIntoProjectFailed", description="Number of data items that failed to import into a project (through the s3-to-project, portal-to-project or dataset-to-project) transform blocks")
    __properties = ["id", "steps", "created", "finished", "itemCountBefore", "itemCountAfter", "itemCountImportIntoProjectFailed"]

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
    def from_json(cls, json_str: str) -> OrganizationPipelineRun:
        """Create an instance of OrganizationPipelineRun from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item in self.steps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['steps'] = _items
        # override the default output from pydantic by calling `to_dict()` of item_count_before
        if self.item_count_before:
            _dict['itemCountBefore'] = self.item_count_before.to_dict()
        # override the default output from pydantic by calling `to_dict()` of item_count_after
        if self.item_count_after:
            _dict['itemCountAfter'] = self.item_count_after.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationPipelineRun:
        """Create an instance of OrganizationPipelineRun from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OrganizationPipelineRun.construct(**obj)

        _obj = OrganizationPipelineRun.construct(**{
            "id": obj.get("id"),
            "steps": [OrganizationPipelineRunStep.from_dict(_item) for _item in obj.get("steps")] if obj.get("steps") is not None else None,
            "created": obj.get("created"),
            "finished": obj.get("finished"),
            "item_count_before": OrganizationPipelineItemCount.from_dict(obj.get("itemCountBefore")) if obj.get("itemCountBefore") is not None else None,
            "item_count_after": OrganizationPipelineItemCount.from_dict(obj.get("itemCountAfter")) if obj.get("itemCountAfter") is not None else None,
            "item_count_import_into_project_failed": obj.get("itemCountImportIntoProjectFailed")
        })
        return _obj

