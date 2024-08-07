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

__all__ = [
    'ListApmSecretKeysResult',
    'AwaitableListApmSecretKeysResult',
    'list_apm_secret_keys',
    'list_apm_secret_keys_output',
]

@pulumi.output_type
class ListApmSecretKeysResult:
    """
    Keys of APM sensitive properties
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence[str]]:
        """
        Collection of the keys for the APM sensitive properties
        """
        return pulumi.get(self, "value")


class AwaitableListApmSecretKeysResult(ListApmSecretKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListApmSecretKeysResult(
            value=self.value)


def list_apm_secret_keys(apm_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         service_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListApmSecretKeysResult:
    """
    List keys of APM sensitive properties.


    :param str apm_name: The name of the APM
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str service_name: The name of the Service resource.
    """
    __args__ = dict()
    __args__['apmName'] = apm_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appplatform/v20240501preview:listApmSecretKeys', __args__, opts=opts, typ=ListApmSecretKeysResult).value

    return AwaitableListApmSecretKeysResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_apm_secret_keys)
def list_apm_secret_keys_output(apm_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                service_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListApmSecretKeysResult]:
    """
    List keys of APM sensitive properties.


    :param str apm_name: The name of the APM
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str service_name: The name of the Service resource.
    """
    ...
