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
    'GetComponentLinkedStorageAccountResult',
    'AwaitableGetComponentLinkedStorageAccountResult',
    'get_component_linked_storage_account',
    'get_component_linked_storage_account_output',
]

@pulumi.output_type
class GetComponentLinkedStorageAccountResult:
    """
    An Application Insights component linked storage accounts
    """
    def __init__(__self__, id=None, linked_storage_account=None, name=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if linked_storage_account and not isinstance(linked_storage_account, str):
            raise TypeError("Expected argument 'linked_storage_account' to be a str")
        pulumi.set(__self__, "linked_storage_account", linked_storage_account)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="linkedStorageAccount")
    def linked_storage_account(self) -> Optional[str]:
        """
        Linked storage account resource ID
        """
        return pulumi.get(self, "linked_storage_account")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetComponentLinkedStorageAccountResult(GetComponentLinkedStorageAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetComponentLinkedStorageAccountResult(
            id=self.id,
            linked_storage_account=self.linked_storage_account,
            name=self.name,
            type=self.type)


def get_component_linked_storage_account(resource_group_name: Optional[str] = None,
                                         resource_name: Optional[str] = None,
                                         storage_type: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetComponentLinkedStorageAccountResult:
    """
    Returns the current linked storage settings for an Application Insights component.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the Application Insights component resource.
    :param str storage_type: The type of the Application Insights component data source for the linked storage account.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    __args__['storageType'] = storage_type
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:insights/v20200301preview:getComponentLinkedStorageAccount', __args__, opts=opts, typ=GetComponentLinkedStorageAccountResult).value

    return AwaitableGetComponentLinkedStorageAccountResult(
        id=pulumi.get(__ret__, 'id'),
        linked_storage_account=pulumi.get(__ret__, 'linked_storage_account'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_component_linked_storage_account)
def get_component_linked_storage_account_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                resource_name: Optional[pulumi.Input[str]] = None,
                                                storage_type: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetComponentLinkedStorageAccountResult]:
    """
    Returns the current linked storage settings for an Application Insights component.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the Application Insights component resource.
    :param str storage_type: The type of the Application Insights component data source for the linked storage account.
    """
    ...
