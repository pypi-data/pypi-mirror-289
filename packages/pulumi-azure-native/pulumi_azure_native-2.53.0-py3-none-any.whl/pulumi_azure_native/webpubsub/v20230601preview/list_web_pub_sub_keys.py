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
    'ListWebPubSubKeysResult',
    'AwaitableListWebPubSubKeysResult',
    'list_web_pub_sub_keys',
    'list_web_pub_sub_keys_output',
]

@pulumi.output_type
class ListWebPubSubKeysResult:
    """
    A class represents the access keys of the resource.
    """
    def __init__(__self__, primary_connection_string=None, primary_key=None, secondary_connection_string=None, secondary_key=None):
        if primary_connection_string and not isinstance(primary_connection_string, str):
            raise TypeError("Expected argument 'primary_connection_string' to be a str")
        pulumi.set(__self__, "primary_connection_string", primary_connection_string)
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if secondary_connection_string and not isinstance(secondary_connection_string, str):
            raise TypeError("Expected argument 'secondary_connection_string' to be a str")
        pulumi.set(__self__, "secondary_connection_string", secondary_connection_string)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="primaryConnectionString")
    def primary_connection_string(self) -> Optional[str]:
        """
        Connection string constructed via the primaryKey
        """
        return pulumi.get(self, "primary_connection_string")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[str]:
        """
        The primary access key.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryConnectionString")
    def secondary_connection_string(self) -> Optional[str]:
        """
        Connection string constructed via the secondaryKey
        """
        return pulumi.get(self, "secondary_connection_string")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[str]:
        """
        The secondary access key.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListWebPubSubKeysResult(ListWebPubSubKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListWebPubSubKeysResult(
            primary_connection_string=self.primary_connection_string,
            primary_key=self.primary_key,
            secondary_connection_string=self.secondary_connection_string,
            secondary_key=self.secondary_key)


def list_web_pub_sub_keys(resource_group_name: Optional[str] = None,
                          resource_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListWebPubSubKeysResult:
    """
    Get the access keys of the resource.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:webpubsub/v20230601preview:listWebPubSubKeys', __args__, opts=opts, typ=ListWebPubSubKeysResult).value

    return AwaitableListWebPubSubKeysResult(
        primary_connection_string=pulumi.get(__ret__, 'primary_connection_string'),
        primary_key=pulumi.get(__ret__, 'primary_key'),
        secondary_connection_string=pulumi.get(__ret__, 'secondary_connection_string'),
        secondary_key=pulumi.get(__ret__, 'secondary_key'))


@_utilities.lift_output_func(list_web_pub_sub_keys)
def list_web_pub_sub_keys_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                 resource_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListWebPubSubKeysResult]:
    """
    Get the access keys of the resource.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the resource.
    """
    ...
