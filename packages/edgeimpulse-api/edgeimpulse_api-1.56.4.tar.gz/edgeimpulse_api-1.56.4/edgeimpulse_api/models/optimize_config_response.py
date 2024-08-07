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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator
from edgeimpulse_api.models.optimize_config_target_device import OptimizeConfigTargetDevice
from edgeimpulse_api.models.tuner_space_impulse import TunerSpaceImpulse

class OptimizeConfigResponse(BaseModel):
    success: StrictBool = Field(..., description="Whether the operation succeeded")
    error: Optional[StrictStr] = Field(None, description="Optional error description (set if 'success' was false)")
    name: Optional[StrictStr] = None
    dataset_category: StrictStr = Field(..., alias="datasetCategory", description="Dataset category")
    classification_type: StrictStr = Field(..., alias="classificationType", description="Classification type")
    target_latency: StrictInt = Field(..., alias="targetLatency", description="Target latency in MS")
    target_device: OptimizeConfigTargetDevice = Field(..., alias="targetDevice")
    compiler: Optional[List[StrictStr]] = None
    precision: Optional[List[StrictStr]] = None
    training_cycles: Optional[StrictInt] = Field(None, alias="trainingCycles", description="Maximum number of training cycles")
    tuning_max_trials: Optional[StrictInt] = Field(None, alias="tuningMaxTrials", description="Maximum number of trials")
    tuning_workers: Optional[StrictInt] = Field(None, alias="tuningWorkers", description="Maximum number of parallel workers/jobs")
    min_maccs: Optional[float] = Field(None, alias="minMACCS")
    max_maccs: Optional[float] = Field(None, alias="maxMACCS")
    tuning_algorithm: Optional[StrictStr] = Field(None, alias="tuningAlgorithm", description="Tuning algorithm to use to search hyperparameter space")
    notification_on_completion: Optional[StrictBool] = Field(None, alias="notificationOnCompletion")
    tuner_space_options: Optional[Dict[str, List[StrictStr]]] = Field(None, alias="tunerSpaceOptions")
    space: Optional[List[TunerSpaceImpulse]] = Field(None, description="List of impulses specifying the EON Tuner search space")
    device: Optional[Dict[str, Any]] = None
    __properties = ["success", "error", "name", "datasetCategory", "classificationType", "targetLatency", "targetDevice", "compiler", "precision", "trainingCycles", "tuningMaxTrials", "tuningWorkers", "minMACCS", "maxMACCS", "tuningAlgorithm", "notificationOnCompletion", "tunerSpaceOptions", "space", "device"]

    @validator('dataset_category')
    def dataset_category_validate_enum(cls, v):
        if v not in ('speech_keyword', 'speech_continuous', 'audio_event', 'audio_continuous', 'transfer_learning', 'motion_event', 'motion_continuous', 'audio_syntiant', 'object_detection_bounding_boxes', 'object_detection_centroids', 'visual_ad'):
            raise ValueError("must validate the enum values ('speech_keyword', 'speech_continuous', 'audio_event', 'audio_continuous', 'transfer_learning', 'motion_event', 'motion_continuous', 'audio_syntiant', 'object_detection_bounding_boxes', 'object_detection_centroids', 'visual_ad')")
        return v

    @validator('classification_type')
    def classification_type_validate_enum(cls, v):
        if v not in ('classification', 'regression', 'anomaly', 'object_detection'):
            raise ValueError("must validate the enum values ('classification', 'regression', 'anomaly', 'object_detection')")
        return v

    @validator('tuning_algorithm')
    def tuning_algorithm_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('random', 'hyperband', 'bayesian', 'custom'):
            raise ValueError("must validate the enum values ('random', 'hyperband', 'bayesian', 'custom')")
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
    def from_json(cls, json_str: str) -> OptimizeConfigResponse:
        """Create an instance of OptimizeConfigResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of target_device
        if self.target_device:
            _dict['targetDevice'] = self.target_device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in space (list)
        _items = []
        if self.space:
            for _item in self.space:
                if _item:
                    _items.append(_item.to_dict())
            _dict['space'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OptimizeConfigResponse:
        """Create an instance of OptimizeConfigResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OptimizeConfigResponse.construct(**obj)

        _obj = OptimizeConfigResponse.construct(**{
            "success": obj.get("success"),
            "error": obj.get("error"),
            "name": obj.get("name"),
            "dataset_category": obj.get("datasetCategory"),
            "classification_type": obj.get("classificationType"),
            "target_latency": obj.get("targetLatency"),
            "target_device": OptimizeConfigTargetDevice.from_dict(obj.get("targetDevice")) if obj.get("targetDevice") is not None else None,
            "compiler": obj.get("compiler"),
            "precision": obj.get("precision"),
            "training_cycles": obj.get("trainingCycles"),
            "tuning_max_trials": obj.get("tuningMaxTrials"),
            "tuning_workers": obj.get("tuningWorkers"),
            "min_maccs": obj.get("minMACCS"),
            "max_maccs": obj.get("maxMACCS"),
            "tuning_algorithm": obj.get("tuningAlgorithm"),
            "notification_on_completion": obj.get("notificationOnCompletion"),
            "tuner_space_options": obj.get("tunerSpaceOptions"),
            "space": [TunerSpaceImpulse.from_dict(_item) for _item in obj.get("space")] if obj.get("space") is not None else None,
            "device": obj.get("device")
        })
        return _obj

