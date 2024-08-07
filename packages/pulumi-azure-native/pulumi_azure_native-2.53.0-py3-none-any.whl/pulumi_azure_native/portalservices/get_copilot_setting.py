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
    'GetCopilotSettingResult',
    'AwaitableGetCopilotSettingResult',
    'get_copilot_setting',
    'get_copilot_setting_output',
]

@pulumi.output_type
class GetCopilotSettingResult:
    """
    The copilot settings tenant resource definition.
    """
    def __init__(__self__, access_control_enabled=None, id=None, name=None, provisioning_state=None, system_data=None, type=None):
        if access_control_enabled and not isinstance(access_control_enabled, bool):
            raise TypeError("Expected argument 'access_control_enabled' to be a bool")
        pulumi.set(__self__, "access_control_enabled", access_control_enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accessControlEnabled")
    def access_control_enabled(self) -> bool:
        """
        Boolean indicating if role-based access control is enabled for copilot in this tenant.
        """
        return pulumi.get(self, "access_control_enabled")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the last provisioning operation performed on the resource.
        """
        return pulumi.get(self, "provisioning_state")

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


class AwaitableGetCopilotSettingResult(GetCopilotSettingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCopilotSettingResult(
            access_control_enabled=self.access_control_enabled,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_copilot_setting(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCopilotSettingResult:
    """
    Get a CopilotSettingsResource
    Azure REST API version: 2024-04-01-preview.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:portalservices:getCopilotSetting', __args__, opts=opts, typ=GetCopilotSettingResult).value

    return AwaitableGetCopilotSettingResult(
        access_control_enabled=pulumi.get(__ret__, 'access_control_enabled'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_copilot_setting)
def get_copilot_setting_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCopilotSettingResult]:
    """
    Get a CopilotSettingsResource
    Azure REST API version: 2024-04-01-preview.
    """
    ...
