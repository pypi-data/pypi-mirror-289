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
    'GetVolumeGroupIdForLdapUserResult',
    'AwaitableGetVolumeGroupIdForLdapUserResult',
    'get_volume_group_id_for_ldap_user',
    'get_volume_group_id_for_ldap_user_output',
]

@pulumi.output_type
class GetVolumeGroupIdForLdapUserResult:
    """
    Group Id list for Ldap user
    """
    def __init__(__self__, group_ids_for_ldap_user=None):
        if group_ids_for_ldap_user and not isinstance(group_ids_for_ldap_user, list):
            raise TypeError("Expected argument 'group_ids_for_ldap_user' to be a list")
        pulumi.set(__self__, "group_ids_for_ldap_user", group_ids_for_ldap_user)

    @property
    @pulumi.getter(name="groupIdsForLdapUser")
    def group_ids_for_ldap_user(self) -> Optional[Sequence[str]]:
        """
        Group Id list
        """
        return pulumi.get(self, "group_ids_for_ldap_user")


class AwaitableGetVolumeGroupIdForLdapUserResult(GetVolumeGroupIdForLdapUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVolumeGroupIdForLdapUserResult(
            group_ids_for_ldap_user=self.group_ids_for_ldap_user)


def get_volume_group_id_for_ldap_user(account_name: Optional[str] = None,
                                      pool_name: Optional[str] = None,
                                      resource_group_name: Optional[str] = None,
                                      username: Optional[str] = None,
                                      volume_name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVolumeGroupIdForLdapUserResult:
    """
    Returns the list of group Ids for a specific LDAP User


    :param str account_name: The name of the NetApp account
    :param str pool_name: The name of the capacity pool
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str username: username is required to fetch the group to which user is part of
    :param str volume_name: The name of the volume
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['poolName'] = pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['username'] = username
    __args__['volumeName'] = volume_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:netapp/v20231101preview:getVolumeGroupIdForLdapUser', __args__, opts=opts, typ=GetVolumeGroupIdForLdapUserResult).value

    return AwaitableGetVolumeGroupIdForLdapUserResult(
        group_ids_for_ldap_user=pulumi.get(__ret__, 'group_ids_for_ldap_user'))


@_utilities.lift_output_func(get_volume_group_id_for_ldap_user)
def get_volume_group_id_for_ldap_user_output(account_name: Optional[pulumi.Input[str]] = None,
                                             pool_name: Optional[pulumi.Input[str]] = None,
                                             resource_group_name: Optional[pulumi.Input[str]] = None,
                                             username: Optional[pulumi.Input[str]] = None,
                                             volume_name: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVolumeGroupIdForLdapUserResult]:
    """
    Returns the list of group Ids for a specific LDAP User


    :param str account_name: The name of the NetApp account
    :param str pool_name: The name of the capacity pool
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str username: username is required to fetch the group to which user is part of
    :param str volume_name: The name of the volume
    """
    ...
