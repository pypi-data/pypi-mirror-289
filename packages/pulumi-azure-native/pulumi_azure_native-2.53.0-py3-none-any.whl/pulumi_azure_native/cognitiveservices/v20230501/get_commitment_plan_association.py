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
    'GetCommitmentPlanAssociationResult',
    'AwaitableGetCommitmentPlanAssociationResult',
    'get_commitment_plan_association',
    'get_commitment_plan_association_output',
]

@pulumi.output_type
class GetCommitmentPlanAssociationResult:
    """
    The commitment plan association.
    """
    def __init__(__self__, account_id=None, etag=None, id=None, name=None, system_data=None, type=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[str]:
        """
        The Azure resource id of the account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Resource Etag.
        """
        return pulumi.get(self, "etag")

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
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetCommitmentPlanAssociationResult(GetCommitmentPlanAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCommitmentPlanAssociationResult(
            account_id=self.account_id,
            etag=self.etag,
            id=self.id,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_commitment_plan_association(commitment_plan_association_name: Optional[str] = None,
                                    commitment_plan_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCommitmentPlanAssociationResult:
    """
    Gets the association of the Cognitive Services commitment plan.


    :param str commitment_plan_association_name: The name of the commitment plan association with the Cognitive Services Account
    :param str commitment_plan_name: The name of the commitmentPlan associated with the Cognitive Services Account
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['commitmentPlanAssociationName'] = commitment_plan_association_name
    __args__['commitmentPlanName'] = commitment_plan_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cognitiveservices/v20230501:getCommitmentPlanAssociation', __args__, opts=opts, typ=GetCommitmentPlanAssociationResult).value

    return AwaitableGetCommitmentPlanAssociationResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_commitment_plan_association)
def get_commitment_plan_association_output(commitment_plan_association_name: Optional[pulumi.Input[str]] = None,
                                           commitment_plan_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCommitmentPlanAssociationResult]:
    """
    Gets the association of the Cognitive Services commitment plan.


    :param str commitment_plan_association_name: The name of the commitment plan association with the Cognitive Services Account
    :param str commitment_plan_name: The name of the commitmentPlan associated with the Cognitive Services Account
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
