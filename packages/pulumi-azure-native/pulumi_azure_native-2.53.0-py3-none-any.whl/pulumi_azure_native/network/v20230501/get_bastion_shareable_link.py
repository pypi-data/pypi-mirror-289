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
from ._inputs import *

__all__ = [
    'GetBastionShareableLinkResult',
    'AwaitableGetBastionShareableLinkResult',
    'get_bastion_shareable_link',
    'get_bastion_shareable_link_output',
]

@pulumi.output_type
class GetBastionShareableLinkResult:
    """
    Response for all the Bastion Shareable Link endpoints.
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
    def next_link(self) -> Optional[str]:
        """
        The URL to get the next set of results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.BastionShareableLinkResponse']]:
        """
        List of Bastion Shareable Links for the request.
        """
        return pulumi.get(self, "value")


class AwaitableGetBastionShareableLinkResult(GetBastionShareableLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBastionShareableLinkResult(
            next_link=self.next_link,
            value=self.value)


def get_bastion_shareable_link(bastion_host_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               vms: Optional[Sequence[Union['BastionShareableLink', 'BastionShareableLinkDict']]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBastionShareableLinkResult:
    """
    Return the Bastion Shareable Links for all the VMs specified in the request.


    :param str bastion_host_name: The name of the Bastion Host.
    :param str resource_group_name: The name of the resource group.
    :param Sequence[Union['BastionShareableLink', 'BastionShareableLinkDict']] vms: List of VM references.
    """
    __args__ = dict()
    __args__['bastionHostName'] = bastion_host_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['vms'] = vms
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230501:getBastionShareableLink', __args__, opts=opts, typ=GetBastionShareableLinkResult).value

    return AwaitableGetBastionShareableLinkResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_bastion_shareable_link)
def get_bastion_shareable_link_output(bastion_host_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      vms: Optional[pulumi.Input[Optional[Sequence[Union['BastionShareableLink', 'BastionShareableLinkDict']]]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBastionShareableLinkResult]:
    """
    Return the Bastion Shareable Links for all the VMs specified in the request.


    :param str bastion_host_name: The name of the Bastion Host.
    :param str resource_group_name: The name of the resource group.
    :param Sequence[Union['BastionShareableLink', 'BastionShareableLinkDict']] vms: List of VM references.
    """
    ...
