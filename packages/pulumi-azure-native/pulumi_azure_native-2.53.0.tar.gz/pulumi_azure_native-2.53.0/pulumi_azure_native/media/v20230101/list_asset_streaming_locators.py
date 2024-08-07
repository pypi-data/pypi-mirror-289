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
    'ListAssetStreamingLocatorsResult',
    'AwaitableListAssetStreamingLocatorsResult',
    'list_asset_streaming_locators',
    'list_asset_streaming_locators_output',
]

@pulumi.output_type
class ListAssetStreamingLocatorsResult:
    """
    The Streaming Locators associated with this Asset.
    """
    def __init__(__self__, streaming_locators=None):
        if streaming_locators and not isinstance(streaming_locators, list):
            raise TypeError("Expected argument 'streaming_locators' to be a list")
        pulumi.set(__self__, "streaming_locators", streaming_locators)

    @property
    @pulumi.getter(name="streamingLocators")
    def streaming_locators(self) -> Sequence['outputs.AssetStreamingLocatorResponse']:
        """
        The list of Streaming Locators.
        """
        return pulumi.get(self, "streaming_locators")


class AwaitableListAssetStreamingLocatorsResult(ListAssetStreamingLocatorsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListAssetStreamingLocatorsResult(
            streaming_locators=self.streaming_locators)


def list_asset_streaming_locators(account_name: Optional[str] = None,
                                  asset_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListAssetStreamingLocatorsResult:
    """
    Lists Streaming Locators which are associated with this asset.


    :param str account_name: The Media Services account name.
    :param str asset_name: The Asset name.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['assetName'] = asset_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:media/v20230101:listAssetStreamingLocators', __args__, opts=opts, typ=ListAssetStreamingLocatorsResult).value

    return AwaitableListAssetStreamingLocatorsResult(
        streaming_locators=pulumi.get(__ret__, 'streaming_locators'))


@_utilities.lift_output_func(list_asset_streaming_locators)
def list_asset_streaming_locators_output(account_name: Optional[pulumi.Input[str]] = None,
                                         asset_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListAssetStreamingLocatorsResult]:
    """
    Lists Streaming Locators which are associated with this asset.


    :param str account_name: The Media Services account name.
    :param str asset_name: The Asset name.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    ...
