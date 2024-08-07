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
    'ListShareSubscriptionSynchronizationDetailsResult',
    'AwaitableListShareSubscriptionSynchronizationDetailsResult',
    'list_share_subscription_synchronization_details',
    'list_share_subscription_synchronization_details_output',
]

@pulumi.output_type
class ListShareSubscriptionSynchronizationDetailsResult:
    """
    details of synchronization
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        The Url of next result page.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.SynchronizationDetailsResponse']:
        """
        Collection of items of type DataTransferObjects.
        """
        return pulumi.get(self, "value")


class AwaitableListShareSubscriptionSynchronizationDetailsResult(ListShareSubscriptionSynchronizationDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListShareSubscriptionSynchronizationDetailsResult(
            next_link=self.next_link,
            value=self.value)


def list_share_subscription_synchronization_details(account_name: Optional[str] = None,
                                                    filter: Optional[str] = None,
                                                    orderby: Optional[str] = None,
                                                    resource_group_name: Optional[str] = None,
                                                    share_subscription_name: Optional[str] = None,
                                                    skip_token: Optional[str] = None,
                                                    synchronization_id: Optional[str] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListShareSubscriptionSynchronizationDetailsResult:
    """
    List synchronization details


    :param str account_name: The name of the share account.
    :param str filter: Filters the results using OData syntax.
    :param str orderby: Sorts the results using OData syntax.
    :param str resource_group_name: The resource group name.
    :param str share_subscription_name: The name of the share subscription.
    :param str skip_token: Continuation token
    :param str synchronization_id: Synchronization id
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['filter'] = filter
    __args__['orderby'] = orderby
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareSubscriptionName'] = share_subscription_name
    __args__['skipToken'] = skip_token
    __args__['synchronizationId'] = synchronization_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datashare/v20210801:listShareSubscriptionSynchronizationDetails', __args__, opts=opts, typ=ListShareSubscriptionSynchronizationDetailsResult).value

    return AwaitableListShareSubscriptionSynchronizationDetailsResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_share_subscription_synchronization_details)
def list_share_subscription_synchronization_details_output(account_name: Optional[pulumi.Input[str]] = None,
                                                           filter: Optional[pulumi.Input[Optional[str]]] = None,
                                                           orderby: Optional[pulumi.Input[Optional[str]]] = None,
                                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                                           share_subscription_name: Optional[pulumi.Input[str]] = None,
                                                           skip_token: Optional[pulumi.Input[Optional[str]]] = None,
                                                           synchronization_id: Optional[pulumi.Input[str]] = None,
                                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListShareSubscriptionSynchronizationDetailsResult]:
    """
    List synchronization details


    :param str account_name: The name of the share account.
    :param str filter: Filters the results using OData syntax.
    :param str orderby: Sorts the results using OData syntax.
    :param str resource_group_name: The resource group name.
    :param str share_subscription_name: The name of the share subscription.
    :param str skip_token: Continuation token
    :param str synchronization_id: Synchronization id
    """
    ...
