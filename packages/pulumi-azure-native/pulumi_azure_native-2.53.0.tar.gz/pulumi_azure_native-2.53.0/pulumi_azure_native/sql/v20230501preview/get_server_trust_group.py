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
    'GetServerTrustGroupResult',
    'AwaitableGetServerTrustGroupResult',
    'get_server_trust_group',
    'get_server_trust_group_output',
]

@pulumi.output_type
class GetServerTrustGroupResult:
    """
    A server trust group.
    """
    def __init__(__self__, group_members=None, id=None, name=None, trust_scopes=None, type=None):
        if group_members and not isinstance(group_members, list):
            raise TypeError("Expected argument 'group_members' to be a list")
        pulumi.set(__self__, "group_members", group_members)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if trust_scopes and not isinstance(trust_scopes, list):
            raise TypeError("Expected argument 'trust_scopes' to be a list")
        pulumi.set(__self__, "trust_scopes", trust_scopes)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="groupMembers")
    def group_members(self) -> Sequence['outputs.ServerInfoResponse']:
        """
        Group members information for the server trust group.
        """
        return pulumi.get(self, "group_members")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="trustScopes")
    def trust_scopes(self) -> Sequence[str]:
        """
        Trust scope of the server trust group.
        """
        return pulumi.get(self, "trust_scopes")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetServerTrustGroupResult(GetServerTrustGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerTrustGroupResult(
            group_members=self.group_members,
            id=self.id,
            name=self.name,
            trust_scopes=self.trust_scopes,
            type=self.type)


def get_server_trust_group(location_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           server_trust_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerTrustGroupResult:
    """
    Gets a server trust group.


    :param str location_name: The name of the region where the resource is located.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_trust_group_name: The name of the server trust group.
    """
    __args__ = dict()
    __args__['locationName'] = location_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverTrustGroupName'] = server_trust_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20230501preview:getServerTrustGroup', __args__, opts=opts, typ=GetServerTrustGroupResult).value

    return AwaitableGetServerTrustGroupResult(
        group_members=pulumi.get(__ret__, 'group_members'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        trust_scopes=pulumi.get(__ret__, 'trust_scopes'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_server_trust_group)
def get_server_trust_group_output(location_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  server_trust_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerTrustGroupResult]:
    """
    Gets a server trust group.


    :param str location_name: The name of the region where the resource is located.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_trust_group_name: The name of the server trust group.
    """
    ...
