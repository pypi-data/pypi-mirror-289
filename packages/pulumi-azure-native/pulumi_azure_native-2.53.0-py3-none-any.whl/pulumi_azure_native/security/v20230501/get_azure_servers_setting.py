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
    'GetAzureServersSettingResult',
    'AwaitableGetAzureServersSettingResult',
    'get_azure_servers_setting',
    'get_azure_servers_setting_output',
]

@pulumi.output_type
class GetAzureServersSettingResult:
    """
    A vulnerability assessments setting on Azure servers in the defined scope.
    """
    def __init__(__self__, id=None, kind=None, name=None, selected_provider=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if selected_provider and not isinstance(selected_provider, str):
            raise TypeError("Expected argument 'selected_provider' to be a str")
        pulumi.set(__self__, "selected_provider", selected_provider)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of the server vulnerability assessments setting
        Expected value is 'AzureServersSetting'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="selectedProvider")
    def selected_provider(self) -> str:
        """
        The selected vulnerability assessments provider on Azure servers in the defined scope.
        """
        return pulumi.get(self, "selected_provider")

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


class AwaitableGetAzureServersSettingResult(GetAzureServersSettingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAzureServersSettingResult(
            id=self.id,
            kind=self.kind,
            name=self.name,
            selected_provider=self.selected_provider,
            system_data=self.system_data,
            type=self.type)


def get_azure_servers_setting(setting_kind: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAzureServersSettingResult:
    """
    Get a server vulnerability assessments setting of the requested kind, that is set on the subscription


    :param str setting_kind: The kind of the server vulnerability assessments setting
    """
    __args__ = dict()
    __args__['settingKind'] = setting_kind
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:security/v20230501:getAzureServersSetting', __args__, opts=opts, typ=GetAzureServersSettingResult).value

    return AwaitableGetAzureServersSettingResult(
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        selected_provider=pulumi.get(__ret__, 'selected_provider'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_azure_servers_setting)
def get_azure_servers_setting_output(setting_kind: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAzureServersSettingResult]:
    """
    Get a server vulnerability assessments setting of the requested kind, that is set on the subscription


    :param str setting_kind: The kind of the server vulnerability assessments setting
    """
    ...
