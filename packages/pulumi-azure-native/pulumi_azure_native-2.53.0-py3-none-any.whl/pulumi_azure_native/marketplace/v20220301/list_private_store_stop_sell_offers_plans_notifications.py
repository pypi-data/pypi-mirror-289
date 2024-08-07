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
    'ListPrivateStoreStopSellOffersPlansNotificationsResult',
    'AwaitableListPrivateStoreStopSellOffersPlansNotificationsResult',
    'list_private_store_stop_sell_offers_plans_notifications',
    'list_private_store_stop_sell_offers_plans_notifications_output',
]

@pulumi.output_type
class ListPrivateStoreStopSellOffersPlansNotificationsResult:
    """
    List of stop sell offers and plans notifications.
    """
    def __init__(__self__, stop_sell_notifications=None):
        if stop_sell_notifications and not isinstance(stop_sell_notifications, list):
            raise TypeError("Expected argument 'stop_sell_notifications' to be a list")
        pulumi.set(__self__, "stop_sell_notifications", stop_sell_notifications)

    @property
    @pulumi.getter(name="stopSellNotifications")
    def stop_sell_notifications(self) -> Optional[Sequence['outputs.StopSellOffersPlansNotificationsListPropertiesResponse']]:
        return pulumi.get(self, "stop_sell_notifications")


class AwaitableListPrivateStoreStopSellOffersPlansNotificationsResult(ListPrivateStoreStopSellOffersPlansNotificationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListPrivateStoreStopSellOffersPlansNotificationsResult(
            stop_sell_notifications=self.stop_sell_notifications)


def list_private_store_stop_sell_offers_plans_notifications(private_store_id: Optional[str] = None,
                                                            subscriptions: Optional[Sequence[str]] = None,
                                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListPrivateStoreStopSellOffersPlansNotificationsResult:
    """
    List stop sell notifications for both stop sell offers and stop sell plans


    :param str private_store_id: The store ID - must use the tenant ID
    """
    __args__ = dict()
    __args__['privateStoreId'] = private_store_id
    __args__['subscriptions'] = subscriptions
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:marketplace/v20220301:listPrivateStoreStopSellOffersPlansNotifications', __args__, opts=opts, typ=ListPrivateStoreStopSellOffersPlansNotificationsResult).value

    return AwaitableListPrivateStoreStopSellOffersPlansNotificationsResult(
        stop_sell_notifications=pulumi.get(__ret__, 'stop_sell_notifications'))


@_utilities.lift_output_func(list_private_store_stop_sell_offers_plans_notifications)
def list_private_store_stop_sell_offers_plans_notifications_output(private_store_id: Optional[pulumi.Input[str]] = None,
                                                                   subscriptions: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListPrivateStoreStopSellOffersPlansNotificationsResult]:
    """
    List stop sell notifications for both stop sell offers and stop sell plans


    :param str private_store_id: The store ID - must use the tenant ID
    """
    ...
