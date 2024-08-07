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
    'ListHybridConnectionKeysResult',
    'AwaitableListHybridConnectionKeysResult',
    'list_hybrid_connection_keys',
    'list_hybrid_connection_keys_output',
]

@pulumi.output_type
class ListHybridConnectionKeysResult:
    """
    Namespace/Relay Connection String
    """
    def __init__(__self__, key_name=None, primary_connection_string=None, primary_key=None, secondary_connection_string=None, secondary_key=None):
        if key_name and not isinstance(key_name, str):
            raise TypeError("Expected argument 'key_name' to be a str")
        pulumi.set(__self__, "key_name", key_name)
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
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[str]:
        """
        A string that describes the authorization rule.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter(name="primaryConnectionString")
    def primary_connection_string(self) -> Optional[str]:
        """
        Primary connection string of the created namespace authorization rule.
        """
        return pulumi.get(self, "primary_connection_string")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[str]:
        """
        A base64-encoded 256-bit primary key for signing and validating the SAS token.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryConnectionString")
    def secondary_connection_string(self) -> Optional[str]:
        """
        Secondary connection string of the created namespace authorization rule.
        """
        return pulumi.get(self, "secondary_connection_string")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[str]:
        """
        A base64-encoded 256-bit secondary key for signing and validating the SAS token.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListHybridConnectionKeysResult(ListHybridConnectionKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListHybridConnectionKeysResult(
            key_name=self.key_name,
            primary_connection_string=self.primary_connection_string,
            primary_key=self.primary_key,
            secondary_connection_string=self.secondary_connection_string,
            secondary_key=self.secondary_key)


def list_hybrid_connection_keys(authorization_rule_name: Optional[str] = None,
                                hybrid_connection_name: Optional[str] = None,
                                namespace_name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListHybridConnectionKeysResult:
    """
    Primary and secondary connection strings to the hybrid connection.


    :param str authorization_rule_name: The authorization rule name.
    :param str hybrid_connection_name: The hybrid connection name.
    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['authorizationRuleName'] = authorization_rule_name
    __args__['hybridConnectionName'] = hybrid_connection_name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:relay/v20211101:listHybridConnectionKeys', __args__, opts=opts, typ=ListHybridConnectionKeysResult).value

    return AwaitableListHybridConnectionKeysResult(
        key_name=pulumi.get(__ret__, 'key_name'),
        primary_connection_string=pulumi.get(__ret__, 'primary_connection_string'),
        primary_key=pulumi.get(__ret__, 'primary_key'),
        secondary_connection_string=pulumi.get(__ret__, 'secondary_connection_string'),
        secondary_key=pulumi.get(__ret__, 'secondary_key'))


@_utilities.lift_output_func(list_hybrid_connection_keys)
def list_hybrid_connection_keys_output(authorization_rule_name: Optional[pulumi.Input[str]] = None,
                                       hybrid_connection_name: Optional[pulumi.Input[str]] = None,
                                       namespace_name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListHybridConnectionKeysResult]:
    """
    Primary and secondary connection strings to the hybrid connection.


    :param str authorization_rule_name: The authorization rule name.
    :param str hybrid_connection_name: The hybrid connection name.
    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    ...
