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
    'GetPlanMemberResult',
    'AwaitableGetPlanMemberResult',
    'get_plan_member',
    'get_plan_member_output',
]

@pulumi.output_type
class GetPlanMemberResult:
    """
    Represents a devcenter plan member resource.
    """
    def __init__(__self__, id=None, member_id=None, member_type=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if member_id and not isinstance(member_id, str):
            raise TypeError("Expected argument 'member_id' to be a str")
        pulumi.set(__self__, "member_id", member_id)
        if member_type and not isinstance(member_type, str):
            raise TypeError("Expected argument 'member_type' to be a str")
        pulumi.set(__self__, "member_type", member_type)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> Optional[str]:
        """
        The unique id of the member.
        """
        return pulumi.get(self, "member_id")

    @property
    @pulumi.getter(name="memberType")
    def member_type(self) -> Optional[str]:
        """
        The type of the member (user, group)
        """
        return pulumi.get(self, "member_type")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetPlanMemberResult(GetPlanMemberResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPlanMemberResult(
            id=self.id,
            member_id=self.member_id,
            member_type=self.member_type,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_plan_member(member_name: Optional[str] = None,
                    plan_name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPlanMemberResult:
    """
    Gets a devcenter plan member.


    :param str member_name: The name of a devcenter plan member.
    :param str plan_name: The name of the devcenter plan.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['memberName'] = member_name
    __args__['planName'] = plan_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devcenter/v20240501preview:getPlanMember', __args__, opts=opts, typ=GetPlanMemberResult).value

    return AwaitableGetPlanMemberResult(
        id=pulumi.get(__ret__, 'id'),
        member_id=pulumi.get(__ret__, 'member_id'),
        member_type=pulumi.get(__ret__, 'member_type'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_plan_member)
def get_plan_member_output(member_name: Optional[pulumi.Input[str]] = None,
                           plan_name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPlanMemberResult]:
    """
    Gets a devcenter plan member.


    :param str member_name: The name of a devcenter plan member.
    :param str plan_name: The name of the devcenter plan.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
