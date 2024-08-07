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
    'ListMediaServiceKeysResult',
    'AwaitableListMediaServiceKeysResult',
    'list_media_service_keys',
    'list_media_service_keys_output',
]

@pulumi.output_type
class ListMediaServiceKeysResult:
    """
    The response body for a ListKeys API.
    """
    def __init__(__self__, primary_auth_endpoint=None, primary_key=None, scope=None, secondary_auth_endpoint=None, secondary_key=None):
        if primary_auth_endpoint and not isinstance(primary_auth_endpoint, str):
            raise TypeError("Expected argument 'primary_auth_endpoint' to be a str")
        pulumi.set(__self__, "primary_auth_endpoint", primary_auth_endpoint)
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if secondary_auth_endpoint and not isinstance(secondary_auth_endpoint, str):
            raise TypeError("Expected argument 'secondary_auth_endpoint' to be a str")
        pulumi.set(__self__, "secondary_auth_endpoint", secondary_auth_endpoint)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="primaryAuthEndpoint")
    def primary_auth_endpoint(self) -> Optional[str]:
        """
        The primary authorization endpoint.
        """
        return pulumi.get(self, "primary_auth_endpoint")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[str]:
        """
        The primary key for the Media Service resource.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter
    def scope(self) -> Optional[str]:
        """
        The authorization scope.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="secondaryAuthEndpoint")
    def secondary_auth_endpoint(self) -> Optional[str]:
        """
        The secondary authorization endpoint.
        """
        return pulumi.get(self, "secondary_auth_endpoint")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[str]:
        """
        The secondary key for the Media Service resource.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListMediaServiceKeysResult(ListMediaServiceKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListMediaServiceKeysResult(
            primary_auth_endpoint=self.primary_auth_endpoint,
            primary_key=self.primary_key,
            scope=self.scope,
            secondary_auth_endpoint=self.secondary_auth_endpoint,
            secondary_key=self.secondary_key)


def list_media_service_keys(media_service_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListMediaServiceKeysResult:
    """
    Lists the keys for a Media Service.
    Azure REST API version: 2015-10-01.


    :param str media_service_name: Name of the Media Service.
    :param str resource_group_name: Name of the resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['mediaServiceName'] = media_service_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:media:listMediaServiceKeys', __args__, opts=opts, typ=ListMediaServiceKeysResult).value

    return AwaitableListMediaServiceKeysResult(
        primary_auth_endpoint=pulumi.get(__ret__, 'primary_auth_endpoint'),
        primary_key=pulumi.get(__ret__, 'primary_key'),
        scope=pulumi.get(__ret__, 'scope'),
        secondary_auth_endpoint=pulumi.get(__ret__, 'secondary_auth_endpoint'),
        secondary_key=pulumi.get(__ret__, 'secondary_key'))


@_utilities.lift_output_func(list_media_service_keys)
def list_media_service_keys_output(media_service_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListMediaServiceKeysResult]:
    """
    Lists the keys for a Media Service.
    Azure REST API version: 2015-10-01.


    :param str media_service_name: Name of the Media Service.
    :param str resource_group_name: Name of the resource group within the Azure subscription.
    """
    ...
