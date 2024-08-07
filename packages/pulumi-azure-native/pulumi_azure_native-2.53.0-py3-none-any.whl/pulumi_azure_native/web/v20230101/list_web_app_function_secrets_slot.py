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
    'ListWebAppFunctionSecretsSlotResult',
    'AwaitableListWebAppFunctionSecretsSlotResult',
    'list_web_app_function_secrets_slot',
    'list_web_app_function_secrets_slot_output',
]

@pulumi.output_type
class ListWebAppFunctionSecretsSlotResult:
    """
    Function secrets.
    """
    def __init__(__self__, key=None, trigger_url=None):
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if trigger_url and not isinstance(trigger_url, str):
            raise TypeError("Expected argument 'trigger_url' to be a str")
        pulumi.set(__self__, "trigger_url", trigger_url)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        """
        Secret key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="triggerUrl")
    def trigger_url(self) -> Optional[str]:
        """
        Trigger URL.
        """
        return pulumi.get(self, "trigger_url")


class AwaitableListWebAppFunctionSecretsSlotResult(ListWebAppFunctionSecretsSlotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWebAppFunctionSecretsSlotResult(
            key=self.key,
            trigger_url=self.trigger_url)


def list_web_app_function_secrets_slot(function_name: Optional[str] = None,
                                       name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       slot: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWebAppFunctionSecretsSlotResult:
    """
    Description for Get function secrets for a function in a web site, or a deployment slot.


    :param str function_name: Function name.
    :param str name: Site name.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    :param str slot: Name of the deployment slot.
    """
    __args__ = dict()
    __args__['functionName'] = function_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __args__['slot'] = slot
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20230101:listWebAppFunctionSecretsSlot', __args__, opts=opts, typ=ListWebAppFunctionSecretsSlotResult).value

    return AwaitableListWebAppFunctionSecretsSlotResult(
        key=pulumi.get(__ret__, 'key'),
        trigger_url=pulumi.get(__ret__, 'trigger_url'))


@_utilities.lift_output_func(list_web_app_function_secrets_slot)
def list_web_app_function_secrets_slot_output(function_name: Optional[pulumi.Input[str]] = None,
                                              name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              slot: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListWebAppFunctionSecretsSlotResult]:
    """
    Description for Get function secrets for a function in a web site, or a deployment slot.


    :param str function_name: Function name.
    :param str name: Site name.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    :param str slot: Name of the deployment slot.
    """
    ...
