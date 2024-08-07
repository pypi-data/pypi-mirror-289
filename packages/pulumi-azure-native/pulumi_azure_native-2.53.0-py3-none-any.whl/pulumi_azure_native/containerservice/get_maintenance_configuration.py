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
    'GetMaintenanceConfigurationResult',
    'AwaitableGetMaintenanceConfigurationResult',
    'get_maintenance_configuration',
    'get_maintenance_configuration_output',
]

@pulumi.output_type
class GetMaintenanceConfigurationResult:
    """
    See [planned maintenance](https://docs.microsoft.com/azure/aks/planned-maintenance) for more information about planned maintenance.
    """
    def __init__(__self__, id=None, name=None, not_allowed_time=None, system_data=None, time_in_week=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if not_allowed_time and not isinstance(not_allowed_time, list):
            raise TypeError("Expected argument 'not_allowed_time' to be a list")
        pulumi.set(__self__, "not_allowed_time", not_allowed_time)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if time_in_week and not isinstance(time_in_week, list):
            raise TypeError("Expected argument 'time_in_week' to be a list")
        pulumi.set(__self__, "time_in_week", time_in_week)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notAllowedTime")
    def not_allowed_time(self) -> Optional[Sequence['outputs.TimeSpanResponse']]:
        """
        Time slots on which upgrade is not allowed.
        """
        return pulumi.get(self, "not_allowed_time")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="timeInWeek")
    def time_in_week(self) -> Optional[Sequence['outputs.TimeInWeekResponse']]:
        """
        If two array entries specify the same day of the week, the applied configuration is the union of times in both entries.
        """
        return pulumi.get(self, "time_in_week")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetMaintenanceConfigurationResult(GetMaintenanceConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMaintenanceConfigurationResult(
            id=self.id,
            name=self.name,
            not_allowed_time=self.not_allowed_time,
            system_data=self.system_data,
            time_in_week=self.time_in_week,
            type=self.type)


def get_maintenance_configuration(config_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  resource_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMaintenanceConfigurationResult:
    """
    See [planned maintenance](https://docs.microsoft.com/azure/aks/planned-maintenance) for more information about planned maintenance.
    Azure REST API version: 2023-04-01.

    Other available API versions: 2023-05-02-preview, 2023-06-01, 2023-06-02-preview, 2023-07-01, 2023-07-02-preview, 2023-08-01, 2023-08-02-preview, 2023-09-01, 2023-09-02-preview, 2023-10-01, 2023-10-02-preview, 2023-11-01, 2023-11-02-preview, 2024-01-01, 2024-01-02-preview, 2024-02-01, 2024-02-02-preview, 2024-03-02-preview, 2024-04-02-preview, 2024-05-01, 2024-05-02-preview.


    :param str config_name: The name of the maintenance configuration.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the managed cluster resource.
    """
    __args__ = dict()
    __args__['configName'] = config_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerservice:getMaintenanceConfiguration', __args__, opts=opts, typ=GetMaintenanceConfigurationResult).value

    return AwaitableGetMaintenanceConfigurationResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        not_allowed_time=pulumi.get(__ret__, 'not_allowed_time'),
        system_data=pulumi.get(__ret__, 'system_data'),
        time_in_week=pulumi.get(__ret__, 'time_in_week'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_maintenance_configuration)
def get_maintenance_configuration_output(config_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         resource_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMaintenanceConfigurationResult]:
    """
    See [planned maintenance](https://docs.microsoft.com/azure/aks/planned-maintenance) for more information about planned maintenance.
    Azure REST API version: 2023-04-01.

    Other available API versions: 2023-05-02-preview, 2023-06-01, 2023-06-02-preview, 2023-07-01, 2023-07-02-preview, 2023-08-01, 2023-08-02-preview, 2023-09-01, 2023-09-02-preview, 2023-10-01, 2023-10-02-preview, 2023-11-01, 2023-11-02-preview, 2024-01-01, 2024-01-02-preview, 2024-02-01, 2024-02-02-preview, 2024-03-02-preview, 2024-04-02-preview, 2024-05-01, 2024-05-02-preview.


    :param str config_name: The name of the maintenance configuration.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the managed cluster resource.
    """
    ...
