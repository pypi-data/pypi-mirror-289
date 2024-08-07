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
    'GetWorkloadInstanceResult',
    'AwaitableGetWorkloadInstanceResult',
    'get_workload_instance',
    'get_workload_instance_output',
]

@pulumi.output_type
class GetWorkloadInstanceResult:
    """
    Workload instance model.
    """
    def __init__(__self__, id=None, name=None, properties=None, system_data=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Gets or sets the Id of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets or sets the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.WorkloadInstanceModelPropertiesResponse':
        """
        Workload instance model properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.WorkloadInstanceModelResponseSystemData':
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Gets or sets the resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets or sets the type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkloadInstanceResult(GetWorkloadInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkloadInstanceResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_workload_instance(modernize_project_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          subscription_id: Optional[str] = None,
                          workload_instance_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkloadInstanceResult:
    """
    Gets the details of the workload instance.
    Azure REST API version: 2022-05-01-preview.


    :param str modernize_project_name: ModernizeProject name.
    :param str resource_group_name: Name of the Azure Resource Group that project is part of.
    :param str subscription_id: Azure Subscription Id in which project was created.
    :param str workload_instance_name: Workload instance name.
    """
    __args__ = dict()
    __args__['modernizeProjectName'] = modernize_project_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['subscriptionId'] = subscription_id
    __args__['workloadInstanceName'] = workload_instance_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:migrate:getWorkloadInstance', __args__, opts=opts, typ=GetWorkloadInstanceResult).value

    return AwaitableGetWorkloadInstanceResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_workload_instance)
def get_workload_instance_output(modernize_project_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 subscription_id: Optional[pulumi.Input[Optional[str]]] = None,
                                 workload_instance_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkloadInstanceResult]:
    """
    Gets the details of the workload instance.
    Azure REST API version: 2022-05-01-preview.


    :param str modernize_project_name: ModernizeProject name.
    :param str resource_group_name: Name of the Azure Resource Group that project is part of.
    :param str subscription_id: Azure Subscription Id in which project was created.
    :param str workload_instance_name: Workload instance name.
    """
    ...
