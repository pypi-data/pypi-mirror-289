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
    'GetObjectReplicationPolicyResult',
    'AwaitableGetObjectReplicationPolicyResult',
    'get_object_replication_policy',
    'get_object_replication_policy_output',
]

@pulumi.output_type
class GetObjectReplicationPolicyResult:
    """
    The replication policy between two storage accounts. Multiple rules can be defined in one policy.
    """
    def __init__(__self__, destination_account=None, enabled_time=None, id=None, name=None, policy_id=None, rules=None, source_account=None, type=None):
        if destination_account and not isinstance(destination_account, str):
            raise TypeError("Expected argument 'destination_account' to be a str")
        pulumi.set(__self__, "destination_account", destination_account)
        if enabled_time and not isinstance(enabled_time, str):
            raise TypeError("Expected argument 'enabled_time' to be a str")
        pulumi.set(__self__, "enabled_time", enabled_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if policy_id and not isinstance(policy_id, str):
            raise TypeError("Expected argument 'policy_id' to be a str")
        pulumi.set(__self__, "policy_id", policy_id)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if source_account and not isinstance(source_account, str):
            raise TypeError("Expected argument 'source_account' to be a str")
        pulumi.set(__self__, "source_account", source_account)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="destinationAccount")
    def destination_account(self) -> str:
        """
        Required. Destination account name. It should be full resource id if allowCrossTenantReplication set to false.
        """
        return pulumi.get(self, "destination_account")

    @property
    @pulumi.getter(name="enabledTime")
    def enabled_time(self) -> str:
        """
        Indicates when the policy is enabled on the source account.
        """
        return pulumi.get(self, "enabled_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> str:
        """
        A unique id for object replication policy.
        """
        return pulumi.get(self, "policy_id")

    @property
    @pulumi.getter
    def rules(self) -> Optional[Sequence['outputs.ObjectReplicationPolicyRuleResponse']]:
        """
        The storage account object replication rules.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="sourceAccount")
    def source_account(self) -> str:
        """
        Required. Source account name. It should be full resource id if allowCrossTenantReplication set to false.
        """
        return pulumi.get(self, "source_account")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetObjectReplicationPolicyResult(GetObjectReplicationPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetObjectReplicationPolicyResult(
            destination_account=self.destination_account,
            enabled_time=self.enabled_time,
            id=self.id,
            name=self.name,
            policy_id=self.policy_id,
            rules=self.rules,
            source_account=self.source_account,
            type=self.type)


def get_object_replication_policy(account_name: Optional[str] = None,
                                  object_replication_policy_id: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetObjectReplicationPolicyResult:
    """
    Get the object replication policy of the storage account by policy ID.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str object_replication_policy_id: For the destination account, provide the value 'default'. Configure the policy on the destination account first. For the source account, provide the value of the policy ID that is returned when you download the policy that was defined on the destination account. The policy is downloaded as a JSON file.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['objectReplicationPolicyId'] = object_replication_policy_id
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storage/v20230101:getObjectReplicationPolicy', __args__, opts=opts, typ=GetObjectReplicationPolicyResult).value

    return AwaitableGetObjectReplicationPolicyResult(
        destination_account=pulumi.get(__ret__, 'destination_account'),
        enabled_time=pulumi.get(__ret__, 'enabled_time'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        policy_id=pulumi.get(__ret__, 'policy_id'),
        rules=pulumi.get(__ret__, 'rules'),
        source_account=pulumi.get(__ret__, 'source_account'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_object_replication_policy)
def get_object_replication_policy_output(account_name: Optional[pulumi.Input[str]] = None,
                                         object_replication_policy_id: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetObjectReplicationPolicyResult]:
    """
    Get the object replication policy of the storage account by policy ID.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str object_replication_policy_id: For the destination account, provide the value 'default'. Configure the policy on the destination account first. For the source account, provide the value of the policy ID that is returned when you download the policy that was defined on the destination account. The policy is downloaded as a JSON file.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    ...
