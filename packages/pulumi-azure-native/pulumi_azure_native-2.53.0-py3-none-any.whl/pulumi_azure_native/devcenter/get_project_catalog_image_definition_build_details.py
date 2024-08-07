# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from . import outputs

__all__ = [
    'GetProjectCatalogImageDefinitionBuildDetailsResult',
    'AwaitableGetProjectCatalogImageDefinitionBuildDetailsResult',
    'get_project_catalog_image_definition_build_details',
    'get_project_catalog_image_definition_build_details_output',
]

@pulumi.output_type
class GetProjectCatalogImageDefinitionBuildDetailsResult:
    """
    Represents a specific build of an Image Definition.
    """
    def __init__(__self__, end_time=None, error_details=None, id=None, image_reference=None, name=None, start_time=None, status=None, system_data=None, task_groups=None, type=None):
        if end_time and not isinstance(end_time, str):
            raise TypeError("Expected argument 'end_time' to be a str")
        pulumi.set(__self__, "end_time", end_time)
        if error_details and not isinstance(error_details, dict):
            raise TypeError("Expected argument 'error_details' to be a dict")
        pulumi.set(__self__, "error_details", error_details)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_reference and not isinstance(image_reference, dict):
            raise TypeError("Expected argument 'image_reference' to be a dict")
        pulumi.set(__self__, "image_reference", image_reference)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if task_groups and not isinstance(task_groups, list):
            raise TypeError("Expected argument 'task_groups' to be a list")
        pulumi.set(__self__, "task_groups", task_groups)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        End time of the task group.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter(name="errorDetails")
    def error_details(self) -> 'outputs.ImageCreationErrorDetailsResponse':
        """
        Details for image creation error. Populated when the image creation is not successful.
        """
        return pulumi.get(self, "error_details")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageReference")
    def image_reference(self) -> 'outputs.ImageReferenceResponse':
        """
        The specific image version used by the build.
        """
        return pulumi.get(self, "image_reference")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        Start time of the task group.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the build.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="taskGroups")
    def task_groups(self) -> Sequence['outputs.ImageDefinitionBuildTaskGroupResponse']:
        """
        The list of task groups executed during the image definition build.
        """
        return pulumi.get(self, "task_groups")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetProjectCatalogImageDefinitionBuildDetailsResult(GetProjectCatalogImageDefinitionBuildDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectCatalogImageDefinitionBuildDetailsResult(
            end_time=self.end_time,
            error_details=self.error_details,
            id=self.id,
            image_reference=self.image_reference,
            name=self.name,
            start_time=self.start_time,
            status=self.status,
            system_data=self.system_data,
            task_groups=self.task_groups,
            type=self.type)


def get_project_catalog_image_definition_build_details(build_name: Optional[str] = None,
                                                       catalog_name: Optional[str] = None,
                                                       image_definition_name: Optional[str] = None,
                                                       project_name: Optional[str] = None,
                                                       resource_group_name: Optional[str] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProjectCatalogImageDefinitionBuildDetailsResult:
    """
    Gets Build details
    Azure REST API version: 2024-07-01-preview.


    :param str build_name: The ID of the Image Definition Build.
    :param str catalog_name: The name of the Catalog.
    :param str image_definition_name: The name of the Image Definition.
    :param str project_name: The name of the project.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['buildName'] = build_name
    __args__['catalogName'] = catalog_name
    __args__['imageDefinitionName'] = image_definition_name
    __args__['projectName'] = project_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devcenter:getProjectCatalogImageDefinitionBuildDetails', __args__, opts=opts, typ=GetProjectCatalogImageDefinitionBuildDetailsResult).value

    return AwaitableGetProjectCatalogImageDefinitionBuildDetailsResult(
        end_time=pulumi.get(__ret__, 'end_time'),
        error_details=pulumi.get(__ret__, 'error_details'),
        id=pulumi.get(__ret__, 'id'),
        image_reference=pulumi.get(__ret__, 'image_reference'),
        name=pulumi.get(__ret__, 'name'),
        start_time=pulumi.get(__ret__, 'start_time'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        task_groups=pulumi.get(__ret__, 'task_groups'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_project_catalog_image_definition_build_details)
def get_project_catalog_image_definition_build_details_output(build_name: Optional[pulumi.Input[str]] = None,
                                                              catalog_name: Optional[pulumi.Input[str]] = None,
                                                              image_definition_name: Optional[pulumi.Input[str]] = None,
                                                              project_name: Optional[pulumi.Input[str]] = None,
                                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProjectCatalogImageDefinitionBuildDetailsResult]:
    """
    Gets Build details
    Azure REST API version: 2024-07-01-preview.


    :param str build_name: The ID of the Image Definition Build.
    :param str catalog_name: The name of the Catalog.
    :param str image_definition_name: The name of the Image Definition.
    :param str project_name: The name of the project.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
