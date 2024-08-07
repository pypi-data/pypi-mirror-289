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
from . import outputs

__all__ = [
    'ListProviderActionInUseStorageAccountsResult',
    'AwaitableListProviderActionInUseStorageAccountsResult',
    'list_provider_action_in_use_storage_accounts',
    'list_provider_action_in_use_storage_accounts_output',
]

@pulumi.output_type
class ListProviderActionInUseStorageAccountsResult:
    """
    Parameters for listing in use storage accounts operation. If subscription list is null, it will check the user's all subscriptions.
    """
    def __init__(__self__, storage_account_list=None):
        if storage_account_list and not isinstance(storage_account_list, list):
            raise TypeError("Expected argument 'storage_account_list' to be a list")
        pulumi.set(__self__, "storage_account_list", storage_account_list)

    @property
    @pulumi.getter(name="storageAccountList")
    def storage_account_list(self) -> Optional[Sequence['outputs.StorageInfoResponse']]:
        """
        The storage account list which in use in related reports.
        """
        return pulumi.get(self, "storage_account_list")


class AwaitableListProviderActionInUseStorageAccountsResult(ListProviderActionInUseStorageAccountsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListProviderActionInUseStorageAccountsResult(
            storage_account_list=self.storage_account_list)


def list_provider_action_in_use_storage_accounts(subscription_ids: Optional[Sequence[str]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListProviderActionInUseStorageAccountsResult:
    """
    List the storage accounts which are in use by related reports
    Azure REST API version: 2024-06-27.


    :param Sequence[str] subscription_ids: List of subscription ids to be query. If the list is null or empty, the API will query all the subscriptions of the user.
    """
    __args__ = dict()
    __args__['subscriptionIds'] = subscription_ids
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appcomplianceautomation:listProviderActionInUseStorageAccounts', __args__, opts=opts, typ=ListProviderActionInUseStorageAccountsResult).value

    return AwaitableListProviderActionInUseStorageAccountsResult(
        storage_account_list=pulumi.get(__ret__, 'storage_account_list'))


@_utilities.lift_output_func(list_provider_action_in_use_storage_accounts)
def list_provider_action_in_use_storage_accounts_output(subscription_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListProviderActionInUseStorageAccountsResult]:
    """
    List the storage accounts which are in use by related reports
    Azure REST API version: 2024-06-27.


    :param Sequence[str] subscription_ids: List of subscription ids to be query. If the list is null or empty, the API will query all the subscriptions of the user.
    """
    ...
