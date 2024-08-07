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
    'ListRedisKeysResult',
    'AwaitableListRedisKeysResult',
    'list_redis_keys',
    'list_redis_keys_output',
]

@pulumi.output_type
class ListRedisKeysResult:
    """
    Redis cache access keys.
    """
    def __init__(__self__, primary_key=None, secondary_key=None):
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> str:
        """
        The current primary key that clients can use to authenticate with Redis cache.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> str:
        """
        The current secondary key that clients can use to authenticate with Redis cache.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListRedisKeysResult(ListRedisKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListRedisKeysResult(
            primary_key=self.primary_key,
            secondary_key=self.secondary_key)


def list_redis_keys(name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListRedisKeysResult:
    """
    Retrieve a Redis cache's access keys. This operation requires write permission to the cache resource.


    :param str name: The name of the Redis cache.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cache/v20200601:listRedisKeys', __args__, opts=opts, typ=ListRedisKeysResult).value

    return AwaitableListRedisKeysResult(
        primary_key=pulumi.get(__ret__, 'primary_key'),
        secondary_key=pulumi.get(__ret__, 'secondary_key'))


@_utilities.lift_output_func(list_redis_keys)
def list_redis_keys_output(name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListRedisKeysResult]:
    """
    Retrieve a Redis cache's access keys. This operation requires write permission to the cache resource.


    :param str name: The name of the Redis cache.
    :param str resource_group_name: The name of the resource group.
    """
    ...
