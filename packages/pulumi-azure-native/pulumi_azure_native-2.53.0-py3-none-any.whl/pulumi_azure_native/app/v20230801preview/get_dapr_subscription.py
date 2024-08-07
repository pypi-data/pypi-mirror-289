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
    'GetDaprSubscriptionResult',
    'AwaitableGetDaprSubscriptionResult',
    'get_dapr_subscription',
    'get_dapr_subscription_output',
]

@pulumi.output_type
class GetDaprSubscriptionResult:
    """
    Dapr PubSub Event Subscription.
    """
    def __init__(__self__, bulk_subscribe=None, dead_letter_topic=None, id=None, metadata=None, name=None, pubsub_name=None, routes=None, scopes=None, system_data=None, topic=None, type=None):
        if bulk_subscribe and not isinstance(bulk_subscribe, dict):
            raise TypeError("Expected argument 'bulk_subscribe' to be a dict")
        pulumi.set(__self__, "bulk_subscribe", bulk_subscribe)
        if dead_letter_topic and not isinstance(dead_letter_topic, str):
            raise TypeError("Expected argument 'dead_letter_topic' to be a str")
        pulumi.set(__self__, "dead_letter_topic", dead_letter_topic)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pubsub_name and not isinstance(pubsub_name, str):
            raise TypeError("Expected argument 'pubsub_name' to be a str")
        pulumi.set(__self__, "pubsub_name", pubsub_name)
        if routes and not isinstance(routes, dict):
            raise TypeError("Expected argument 'routes' to be a dict")
        pulumi.set(__self__, "routes", routes)
        if scopes and not isinstance(scopes, list):
            raise TypeError("Expected argument 'scopes' to be a list")
        pulumi.set(__self__, "scopes", scopes)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if topic and not isinstance(topic, str):
            raise TypeError("Expected argument 'topic' to be a str")
        pulumi.set(__self__, "topic", topic)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="bulkSubscribe")
    def bulk_subscribe(self) -> Optional['outputs.DaprSubscriptionBulkSubscribeOptionsResponse']:
        """
        Bulk subscription options
        """
        return pulumi.get(self, "bulk_subscribe")

    @property
    @pulumi.getter(name="deadLetterTopic")
    def dead_letter_topic(self) -> Optional[str]:
        """
        Deadletter topic name
        """
        return pulumi.get(self, "dead_letter_topic")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, str]]:
        """
        Subscription metadata
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pubsubName")
    def pubsub_name(self) -> Optional[str]:
        """
        Dapr PubSub component name
        """
        return pulumi.get(self, "pubsub_name")

    @property
    @pulumi.getter
    def routes(self) -> Optional['outputs.DaprSubscriptionRoutesResponse']:
        """
        Subscription routes
        """
        return pulumi.get(self, "routes")

    @property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[str]]:
        """
        Application scopes to restrict the subscription to specific apps.
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def topic(self) -> Optional[str]:
        """
        Topic name
        """
        return pulumi.get(self, "topic")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetDaprSubscriptionResult(GetDaprSubscriptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDaprSubscriptionResult(
            bulk_subscribe=self.bulk_subscribe,
            dead_letter_topic=self.dead_letter_topic,
            id=self.id,
            metadata=self.metadata,
            name=self.name,
            pubsub_name=self.pubsub_name,
            routes=self.routes,
            scopes=self.scopes,
            system_data=self.system_data,
            topic=self.topic,
            type=self.type)


def get_dapr_subscription(environment_name: Optional[str] = None,
                          name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDaprSubscriptionResult:
    """
    Dapr PubSub Event Subscription.


    :param str environment_name: Name of the Managed Environment.
    :param str name: Name of the Dapr subscription.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:app/v20230801preview:getDaprSubscription', __args__, opts=opts, typ=GetDaprSubscriptionResult).value

    return AwaitableGetDaprSubscriptionResult(
        bulk_subscribe=pulumi.get(__ret__, 'bulk_subscribe'),
        dead_letter_topic=pulumi.get(__ret__, 'dead_letter_topic'),
        id=pulumi.get(__ret__, 'id'),
        metadata=pulumi.get(__ret__, 'metadata'),
        name=pulumi.get(__ret__, 'name'),
        pubsub_name=pulumi.get(__ret__, 'pubsub_name'),
        routes=pulumi.get(__ret__, 'routes'),
        scopes=pulumi.get(__ret__, 'scopes'),
        system_data=pulumi.get(__ret__, 'system_data'),
        topic=pulumi.get(__ret__, 'topic'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_dapr_subscription)
def get_dapr_subscription_output(environment_name: Optional[pulumi.Input[str]] = None,
                                 name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDaprSubscriptionResult]:
    """
    Dapr PubSub Event Subscription.


    :param str environment_name: Name of the Managed Environment.
    :param str name: Name of the Dapr subscription.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
