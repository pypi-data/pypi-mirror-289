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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from edgeimpulse_api.models.development_keys import DevelopmentKeys
from edgeimpulse_api.models.device import Device
from edgeimpulse_api.models.latency_device import LatencyDevice
from edgeimpulse_api.models.project import Project
from edgeimpulse_api.models.project_data_summary import ProjectDataSummary
from edgeimpulse_api.models.project_info_response_all_of_acquisition_settings import ProjectInfoResponseAllOfAcquisitionSettings
from edgeimpulse_api.models.project_info_response_all_of_compute_time import ProjectInfoResponseAllOfComputeTime
from edgeimpulse_api.models.project_info_response_all_of_data_summary_per_category import ProjectInfoResponseAllOfDataSummaryPerCategory
from edgeimpulse_api.models.project_info_response_all_of_deploy_settings import ProjectInfoResponseAllOfDeploySettings
from edgeimpulse_api.models.project_info_response_all_of_experiments import ProjectInfoResponseAllOfExperiments
from edgeimpulse_api.models.project_info_response_all_of_impulse import ProjectInfoResponseAllOfImpulse
from edgeimpulse_api.models.project_info_response_all_of_performance import ProjectInfoResponseAllOfPerformance
from edgeimpulse_api.models.project_info_response_all_of_readme import ProjectInfoResponseAllOfReadme
from edgeimpulse_api.models.project_info_response_all_of_show_getting_started_wizard import ProjectInfoResponseAllOfShowGettingStartedWizard
from edgeimpulse_api.models.project_info_response_all_of_urls import ProjectInfoResponseAllOfUrls
from edgeimpulse_api.models.target_constraints import TargetConstraints
from edgeimpulse_api.models.user import User

class ProjectInfoResponse(BaseModel):
    success: StrictBool = Field(..., description="Whether the operation succeeded")
    error: Optional[StrictStr] = Field(None, description="Optional error description (set if 'success' was false)")
    project: Project = ...
    development_keys: DevelopmentKeys = Field(..., alias="developmentKeys")
    impulse: ProjectInfoResponseAllOfImpulse = ...
    devices: List[Device] = ...
    data_summary: ProjectDataSummary = Field(..., alias="dataSummary")
    data_summary_per_category: ProjectInfoResponseAllOfDataSummaryPerCategory = Field(..., alias="dataSummaryPerCategory")
    compute_time: ProjectInfoResponseAllOfComputeTime = Field(..., alias="computeTime")
    acquisition_settings: ProjectInfoResponseAllOfAcquisitionSettings = Field(..., alias="acquisitionSettings")
    collaborators: List[User] = ...
    deploy_settings: ProjectInfoResponseAllOfDeploySettings = Field(..., alias="deploySettings")
    experiments: List[ProjectInfoResponseAllOfExperiments] = Field(..., description="Experiments that the project has access to. Enabling experiments can only be done through a JWT token.")
    latency_devices: List[LatencyDevice] = Field(..., alias="latencyDevices")
    urls: ProjectInfoResponseAllOfUrls = ...
    show_create_first_impulse: StrictBool = Field(..., alias="showCreateFirstImpulse")
    show_getting_started_wizard: ProjectInfoResponseAllOfShowGettingStartedWizard = Field(..., alias="showGettingStartedWizard")
    performance: ProjectInfoResponseAllOfPerformance = ...
    readme: Optional[ProjectInfoResponseAllOfReadme] = None
    train_job_notification_uids: List[StrictInt] = Field(..., alias="trainJobNotificationUids", description="The IDs of users who should be notified when a Keras or retrain job is finished.")
    dsp_job_notification_uids: List[StrictInt] = Field(..., alias="dspJobNotificationUids", description="The IDs of users who should be notified when a DSP job is finished.")
    model_testing_job_notification_uids: List[StrictInt] = Field(..., alias="modelTestingJobNotificationUids", description="The IDs of users who should be notified when a model testing job is finished.")
    auto_segmenter_job_notification_uids: List[StrictInt] = Field(..., alias="autoSegmenterJobNotificationUids", description="The IDs of users who should be notified when an auto segmentation job is finished.")
    export_job_notification_uids: List[StrictInt] = Field(..., alias="exportJobNotificationUids", description="The IDs of users who should be notified when an export job is finished.")
    has_new_training_data: StrictBool = Field(..., alias="hasNewTrainingData")
    csv_import_config: Optional[Dict[str, Any]] = Field(None, alias="csvImportConfig", description="Config file specifying how to process CSV files.")
    studio_url: StrictStr = Field(..., alias="studioUrl")
    in_pretrained_model_flow: StrictBool = Field(..., alias="inPretrainedModelFlow")
    dsp_page_size: Optional[StrictInt] = Field(None, alias="dspPageSize")
    show_sensor_data_in_acquisition_graph: StrictBool = Field(..., alias="showSensorDataInAcquisitionGraph", description="Whether to show the actual sensor data in acquisition charts (only applies when you have structured labels)")
    target_constraints: Optional[TargetConstraints] = Field(None, alias="targetConstraints")
    notifications: List[StrictStr] = Field(..., description="List of notifications to show within the project")
    default_impulse_id: Optional[StrictInt] = Field(None, alias="defaultImpulseId", description="Default selected impulse (by ID).")
    __properties = ["success", "error", "project", "developmentKeys", "impulse", "devices", "dataSummary", "dataSummaryPerCategory", "computeTime", "acquisitionSettings", "collaborators", "deploySettings", "experiments", "latencyDevices", "urls", "showCreateFirstImpulse", "showGettingStartedWizard", "performance", "readme", "trainJobNotificationUids", "dspJobNotificationUids", "modelTestingJobNotificationUids", "autoSegmenterJobNotificationUids", "exportJobNotificationUids", "hasNewTrainingData", "csvImportConfig", "studioUrl", "inPretrainedModelFlow", "dspPageSize", "showSensorDataInAcquisitionGraph", "targetConstraints", "notifications", "defaultImpulseId"]

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
    def from_json(cls, json_str: str) -> ProjectInfoResponse:
        """Create an instance of ProjectInfoResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of development_keys
        if self.development_keys:
            _dict['developmentKeys'] = self.development_keys.to_dict()
        # override the default output from pydantic by calling `to_dict()` of impulse
        if self.impulse:
            _dict['impulse'] = self.impulse.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in devices (list)
        _items = []
        if self.devices:
            for _item in self.devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['devices'] = _items
        # override the default output from pydantic by calling `to_dict()` of data_summary
        if self.data_summary:
            _dict['dataSummary'] = self.data_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of data_summary_per_category
        if self.data_summary_per_category:
            _dict['dataSummaryPerCategory'] = self.data_summary_per_category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of compute_time
        if self.compute_time:
            _dict['computeTime'] = self.compute_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of acquisition_settings
        if self.acquisition_settings:
            _dict['acquisitionSettings'] = self.acquisition_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in collaborators (list)
        _items = []
        if self.collaborators:
            for _item in self.collaborators:
                if _item:
                    _items.append(_item.to_dict())
            _dict['collaborators'] = _items
        # override the default output from pydantic by calling `to_dict()` of deploy_settings
        if self.deploy_settings:
            _dict['deploySettings'] = self.deploy_settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in experiments (list)
        _items = []
        if self.experiments:
            for _item in self.experiments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['experiments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in latency_devices (list)
        _items = []
        if self.latency_devices:
            for _item in self.latency_devices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['latencyDevices'] = _items
        # override the default output from pydantic by calling `to_dict()` of urls
        if self.urls:
            _dict['urls'] = self.urls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of show_getting_started_wizard
        if self.show_getting_started_wizard:
            _dict['showGettingStartedWizard'] = self.show_getting_started_wizard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of performance
        if self.performance:
            _dict['performance'] = self.performance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of readme
        if self.readme:
            _dict['readme'] = self.readme.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_constraints
        if self.target_constraints:
            _dict['targetConstraints'] = self.target_constraints.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProjectInfoResponse:
        """Create an instance of ProjectInfoResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ProjectInfoResponse.construct(**obj)

        _obj = ProjectInfoResponse.construct(**{
            "success": obj.get("success"),
            "error": obj.get("error"),
            "project": Project.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "development_keys": DevelopmentKeys.from_dict(obj.get("developmentKeys")) if obj.get("developmentKeys") is not None else None,
            "impulse": ProjectInfoResponseAllOfImpulse.from_dict(obj.get("impulse")) if obj.get("impulse") is not None else None,
            "devices": [Device.from_dict(_item) for _item in obj.get("devices")] if obj.get("devices") is not None else None,
            "data_summary": ProjectDataSummary.from_dict(obj.get("dataSummary")) if obj.get("dataSummary") is not None else None,
            "data_summary_per_category": ProjectInfoResponseAllOfDataSummaryPerCategory.from_dict(obj.get("dataSummaryPerCategory")) if obj.get("dataSummaryPerCategory") is not None else None,
            "compute_time": ProjectInfoResponseAllOfComputeTime.from_dict(obj.get("computeTime")) if obj.get("computeTime") is not None else None,
            "acquisition_settings": ProjectInfoResponseAllOfAcquisitionSettings.from_dict(obj.get("acquisitionSettings")) if obj.get("acquisitionSettings") is not None else None,
            "collaborators": [User.from_dict(_item) for _item in obj.get("collaborators")] if obj.get("collaborators") is not None else None,
            "deploy_settings": ProjectInfoResponseAllOfDeploySettings.from_dict(obj.get("deploySettings")) if obj.get("deploySettings") is not None else None,
            "experiments": [ProjectInfoResponseAllOfExperiments.from_dict(_item) for _item in obj.get("experiments")] if obj.get("experiments") is not None else None,
            "latency_devices": [LatencyDevice.from_dict(_item) for _item in obj.get("latencyDevices")] if obj.get("latencyDevices") is not None else None,
            "urls": ProjectInfoResponseAllOfUrls.from_dict(obj.get("urls")) if obj.get("urls") is not None else None,
            "show_create_first_impulse": obj.get("showCreateFirstImpulse"),
            "show_getting_started_wizard": ProjectInfoResponseAllOfShowGettingStartedWizard.from_dict(obj.get("showGettingStartedWizard")) if obj.get("showGettingStartedWizard") is not None else None,
            "performance": ProjectInfoResponseAllOfPerformance.from_dict(obj.get("performance")) if obj.get("performance") is not None else None,
            "readme": ProjectInfoResponseAllOfReadme.from_dict(obj.get("readme")) if obj.get("readme") is not None else None,
            "train_job_notification_uids": obj.get("trainJobNotificationUids"),
            "dsp_job_notification_uids": obj.get("dspJobNotificationUids"),
            "model_testing_job_notification_uids": obj.get("modelTestingJobNotificationUids"),
            "auto_segmenter_job_notification_uids": obj.get("autoSegmenterJobNotificationUids"),
            "export_job_notification_uids": obj.get("exportJobNotificationUids"),
            "has_new_training_data": obj.get("hasNewTrainingData"),
            "csv_import_config": obj.get("csvImportConfig"),
            "studio_url": obj.get("studioUrl"),
            "in_pretrained_model_flow": obj.get("inPretrainedModelFlow"),
            "dsp_page_size": obj.get("dspPageSize"),
            "show_sensor_data_in_acquisition_graph": obj.get("showSensorDataInAcquisitionGraph"),
            "target_constraints": TargetConstraints.from_dict(obj.get("targetConstraints")) if obj.get("targetConstraints") is not None else None,
            "notifications": obj.get("notifications"),
            "default_impulse_id": obj.get("defaultImpulseId")
        })
        return _obj

