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
    'ListIotDpsResourceKeysResult',
    'AwaitableListIotDpsResourceKeysResult',
    'list_iot_dps_resource_keys',
    'list_iot_dps_resource_keys_output',
]

@pulumi.output_type
class ListIotDpsResourceKeysResult:
    """
    List of shared access keys.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> str:
        """
        The next link.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.SharedAccessSignatureAuthorizationRuleAccessRightsDescriptionResponse']]:
        """
        The list of shared access policies.
        """
        return pulumi.get(self, "value")


class AwaitableListIotDpsResourceKeysResult(ListIotDpsResourceKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListIotDpsResourceKeysResult(
            next_link=self.next_link,
            value=self.value)


def list_iot_dps_resource_keys(provisioning_service_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListIotDpsResourceKeysResult:
    """
    List the primary and secondary keys for a provisioning service.


    :param str provisioning_service_name: The provisioning service name to get the shared access keys for.
    :param str resource_group_name: resource group name
    """
    __args__ = dict()
    __args__['provisioningServiceName'] = provisioning_service_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devices/v20221212:listIotDpsResourceKeys', __args__, opts=opts, typ=ListIotDpsResourceKeysResult).value

    return AwaitableListIotDpsResourceKeysResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_iot_dps_resource_keys)
def list_iot_dps_resource_keys_output(provisioning_service_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListIotDpsResourceKeysResult]:
    """
    List the primary and secondary keys for a provisioning service.


    :param str provisioning_service_name: The provisioning service name to get the shared access keys for.
    :param str resource_group_name: resource group name
    """
    ...
