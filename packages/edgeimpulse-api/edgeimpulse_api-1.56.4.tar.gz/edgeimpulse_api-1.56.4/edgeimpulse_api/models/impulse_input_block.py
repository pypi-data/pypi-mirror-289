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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint, validator

class ImpulseInputBlock(BaseModel):
    id: conint(strict=True, ge=1) = Field(..., description="Identifier for this block. Make sure to up this number when creating a new block, and don't re-use identifiers. If the block hasn't changed, keep the ID as-is. ID must be unique across the project and greather than zero (>0).")
    type: StrictStr = Field(..., description="Block type (either time-series or image)")
    name: StrictStr = Field(..., description="Block name, will be used in menus")
    title: StrictStr = Field(..., description="Block title, used in the impulse UI")
    window_size_ms: Optional[StrictInt] = Field(None, alias="windowSizeMs", description="Size of the sliding window in milliseconds")
    window_increase_ms: Optional[StrictInt] = Field(None, alias="windowIncreaseMs", description="We use a sliding window to go over the raw data. How many milliseconds to increase the sliding window with for each step.")
    frequency_hz: Optional[float] = Field(None, alias="frequencyHz", description="(Input only) Frequency of the input data in Hz")
    classification_window_increase_ms: Optional[StrictInt] = Field(None, alias="classificationWindowIncreaseMs", description="We use a sliding window to go over the raw data. How many milliseconds to increase the sliding window with for each step in classification mode.")
    pad_zeros: Optional[StrictBool] = Field(None, alias="padZeros", description="Whether to zero pad data when a data item is too short")
    image_width: Optional[StrictInt] = Field(None, alias="imageWidth", description="Width all images are resized to before training")
    image_height: Optional[StrictInt] = Field(None, alias="imageHeight", description="Width all images are resized to before training")
    resize_mode: Optional[StrictStr] = Field(None, alias="resizeMode", description="How to resize images before training")
    resize_method: Optional[StrictStr] = Field(None, alias="resizeMethod", description="Resize method to use when resizing images")
    crop_anchor: Optional[StrictStr] = Field(None, alias="cropAnchor", description="If images are resized using a crop, choose where to anchor the crop")
    description: Optional[StrictStr] = Field(None, description="A short description of the block version, displayed in the block versioning UI")
    created_by: Optional[StrictStr] = Field(None, alias="createdBy", description="The system component that created the block version (createImpulse | clone | tuner). Cannot be set via API.")
    created_at: Optional[datetime] = Field(None, alias="createdAt", description="The datetime that the block version was created. Cannot be set via API.")
    __properties = ["id", "type", "name", "title", "windowSizeMs", "windowIncreaseMs", "frequencyHz", "classificationWindowIncreaseMs", "padZeros", "imageWidth", "imageHeight", "resizeMode", "resizeMethod", "cropAnchor", "description", "createdBy", "createdAt"]

    @validator('type')
    def type_validate_enum(cls, v):
        if v not in ('time-series', 'image'):
            raise ValueError("must validate the enum values ('time-series', 'image')")
        return v

    @validator('resize_mode')
    def resize_mode_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('squash', 'fit-short', 'fit-long', 'crop'):
            raise ValueError("must validate the enum values ('squash', 'fit-short', 'fit-long', 'crop')")
        return v

    @validator('resize_method')
    def resize_method_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('lanczos3', 'nearest'):
            raise ValueError("must validate the enum values ('lanczos3', 'nearest')")
        return v

    @validator('crop_anchor')
    def crop_anchor_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('top-left', 'top-center', 'top-right', 'middle-left', 'middle-center', 'middle-right', 'bottom-left', 'bottom-center', 'bottom-right'):
            raise ValueError("must validate the enum values ('top-left', 'top-center', 'top-right', 'middle-left', 'middle-center', 'middle-right', 'bottom-left', 'bottom-center', 'bottom-right')")
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
    def from_json(cls, json_str: str) -> ImpulseInputBlock:
        """Create an instance of ImpulseInputBlock from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ImpulseInputBlock:
        """Create an instance of ImpulseInputBlock from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ImpulseInputBlock.construct(**obj)

        _obj = ImpulseInputBlock.construct(**{
            "id": obj.get("id"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "title": obj.get("title"),
            "window_size_ms": obj.get("windowSizeMs"),
            "window_increase_ms": obj.get("windowIncreaseMs"),
            "frequency_hz": obj.get("frequencyHz"),
            "classification_window_increase_ms": obj.get("classificationWindowIncreaseMs"),
            "pad_zeros": obj.get("padZeros"),
            "image_width": obj.get("imageWidth"),
            "image_height": obj.get("imageHeight"),
            "resize_mode": obj.get("resizeMode"),
            "resize_method": obj.get("resizeMethod"),
            "crop_anchor": obj.get("cropAnchor"),
            "description": obj.get("description"),
            "created_by": obj.get("createdBy"),
            "created_at": obj.get("createdAt")
        })
        return _obj

