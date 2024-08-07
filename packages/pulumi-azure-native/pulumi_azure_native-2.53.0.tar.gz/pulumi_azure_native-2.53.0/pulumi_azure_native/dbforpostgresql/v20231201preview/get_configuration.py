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
from ... import _utilities
from . import outputs

__all__ = [
    'GetConfigurationResult',
    'AwaitableGetConfigurationResult',
    'get_configuration',
    'get_configuration_output',
]

@pulumi.output_type
class GetConfigurationResult:
    """
    Represents a Configuration.
    """
    def __init__(__self__, allowed_values=None, data_type=None, default_value=None, description=None, documentation_link=None, id=None, is_config_pending_restart=None, is_dynamic_config=None, is_read_only=None, name=None, source=None, system_data=None, type=None, unit=None, value=None):
        if allowed_values and not isinstance(allowed_values, str):
            raise TypeError("Expected argument 'allowed_values' to be a str")
        pulumi.set(__self__, "allowed_values", allowed_values)
        if data_type and not isinstance(data_type, str):
            raise TypeError("Expected argument 'data_type' to be a str")
        pulumi.set(__self__, "data_type", data_type)
        if default_value and not isinstance(default_value, str):
            raise TypeError("Expected argument 'default_value' to be a str")
        pulumi.set(__self__, "default_value", default_value)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if documentation_link and not isinstance(documentation_link, str):
            raise TypeError("Expected argument 'documentation_link' to be a str")
        pulumi.set(__self__, "documentation_link", documentation_link)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_config_pending_restart and not isinstance(is_config_pending_restart, bool):
            raise TypeError("Expected argument 'is_config_pending_restart' to be a bool")
        pulumi.set(__self__, "is_config_pending_restart", is_config_pending_restart)
        if is_dynamic_config and not isinstance(is_dynamic_config, bool):
            raise TypeError("Expected argument 'is_dynamic_config' to be a bool")
        pulumi.set(__self__, "is_dynamic_config", is_dynamic_config)
        if is_read_only and not isinstance(is_read_only, bool):
            raise TypeError("Expected argument 'is_read_only' to be a bool")
        pulumi.set(__self__, "is_read_only", is_read_only)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if source and not isinstance(source, str):
            raise TypeError("Expected argument 'source' to be a str")
        pulumi.set(__self__, "source", source)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unit and not isinstance(unit, str):
            raise TypeError("Expected argument 'unit' to be a str")
        pulumi.set(__self__, "unit", unit)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> str:
        """
        Allowed values of the configuration.
        """
        return pulumi.get(self, "allowed_values")

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> str:
        """
        Data type of the configuration.
        """
        return pulumi.get(self, "data_type")

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> str:
        """
        Default value of the configuration.
        """
        return pulumi.get(self, "default_value")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the configuration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="documentationLink")
    def documentation_link(self) -> str:
        """
        Configuration documentation link.
        """
        return pulumi.get(self, "documentation_link")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isConfigPendingRestart")
    def is_config_pending_restart(self) -> bool:
        """
        Configuration is pending restart or not.
        """
        return pulumi.get(self, "is_config_pending_restart")

    @property
    @pulumi.getter(name="isDynamicConfig")
    def is_dynamic_config(self) -> bool:
        """
        Configuration dynamic or static.
        """
        return pulumi.get(self, "is_dynamic_config")

    @property
    @pulumi.getter(name="isReadOnly")
    def is_read_only(self) -> bool:
        """
        Configuration read-only or not.
        """
        return pulumi.get(self, "is_read_only")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def source(self) -> Optional[str]:
        """
        Source of the configuration.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def unit(self) -> str:
        """
        Configuration unit.
        """
        return pulumi.get(self, "unit")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Value of the configuration.
        """
        return pulumi.get(self, "value")


class AwaitableGetConfigurationResult(GetConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationResult(
            allowed_values=self.allowed_values,
            data_type=self.data_type,
            default_value=self.default_value,
            description=self.description,
            documentation_link=self.documentation_link,
            id=self.id,
            is_config_pending_restart=self.is_config_pending_restart,
            is_dynamic_config=self.is_dynamic_config,
            is_read_only=self.is_read_only,
            name=self.name,
            source=self.source,
            system_data=self.system_data,
            type=self.type,
            unit=self.unit,
            value=self.value)


def get_configuration(configuration_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      server_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationResult:
    """
    Gets information about a configuration of server.


    :param str configuration_name: The name of the server configuration.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['configurationName'] = configuration_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:dbforpostgresql/v20231201preview:getConfiguration', __args__, opts=opts, typ=GetConfigurationResult).value

    return AwaitableGetConfigurationResult(
        allowed_values=pulumi.get(__ret__, 'allowed_values'),
        data_type=pulumi.get(__ret__, 'data_type'),
        default_value=pulumi.get(__ret__, 'default_value'),
        description=pulumi.get(__ret__, 'description'),
        documentation_link=pulumi.get(__ret__, 'documentation_link'),
        id=pulumi.get(__ret__, 'id'),
        is_config_pending_restart=pulumi.get(__ret__, 'is_config_pending_restart'),
        is_dynamic_config=pulumi.get(__ret__, 'is_dynamic_config'),
        is_read_only=pulumi.get(__ret__, 'is_read_only'),
        name=pulumi.get(__ret__, 'name'),
        source=pulumi.get(__ret__, 'source'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        unit=pulumi.get(__ret__, 'unit'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_configuration)
def get_configuration_output(configuration_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             server_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigurationResult]:
    """
    Gets information about a configuration of server.


    :param str configuration_name: The name of the server configuration.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str server_name: The name of the server.
    """
    ...
