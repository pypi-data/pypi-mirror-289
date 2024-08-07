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

__all__ = [
    'GetProviderActionCollectionCountResult',
    'AwaitableGetProviderActionCollectionCountResult',
    'get_provider_action_collection_count',
    'get_provider_action_collection_count_output',
]

@pulumi.output_type
class GetProviderActionCollectionCountResult:
    """
    The get collection count response.
    """
    def __init__(__self__, count=None):
        if count and not isinstance(count, int):
            raise TypeError("Expected argument 'count' to be a int")
        pulumi.set(__self__, "count", count)

    @property
    @pulumi.getter
    def count(self) -> Optional[int]:
        """
        The count of the specified resource.
        """
        return pulumi.get(self, "count")


class AwaitableGetProviderActionCollectionCountResult(GetProviderActionCollectionCountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProviderActionCollectionCountResult(
            count=self.count)


def get_provider_action_collection_count(type: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProviderActionCollectionCountResult:
    """
    Get the count of reports.
    Azure REST API version: 2024-06-27.


    :param str type: The resource type.
    """
    __args__ = dict()
    __args__['type'] = type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appcomplianceautomation:getProviderActionCollectionCount', __args__, opts=opts, typ=GetProviderActionCollectionCountResult).value

    return AwaitableGetProviderActionCollectionCountResult(
        count=pulumi.get(__ret__, 'count'))


@_utilities.lift_output_func(get_provider_action_collection_count)
def get_provider_action_collection_count_output(type: Optional[pulumi.Input[Optional[str]]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProviderActionCollectionCountResult]:
    """
    Get the count of reports.
    Azure REST API version: 2024-06-27.


    :param str type: The resource type.
    """
    ...
