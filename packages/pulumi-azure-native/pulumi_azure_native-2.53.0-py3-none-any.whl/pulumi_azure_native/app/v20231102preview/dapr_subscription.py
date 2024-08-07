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
from ._inputs import *

__all__ = ['DaprSubscriptionArgs', 'DaprSubscription']

@pulumi.input_type
class DaprSubscriptionArgs:
    def __init__(__self__, *,
                 environment_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 bulk_subscribe: Optional[pulumi.Input['DaprSubscriptionBulkSubscribeOptionsArgs']] = None,
                 dead_letter_topic: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pubsub_name: Optional[pulumi.Input[str]] = None,
                 routes: Optional[pulumi.Input['DaprSubscriptionRoutesArgs']] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 topic: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DaprSubscription resource.
        :param pulumi.Input[str] environment_name: Name of the Managed Environment.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['DaprSubscriptionBulkSubscribeOptionsArgs'] bulk_subscribe: Bulk subscription options
        :param pulumi.Input[str] dead_letter_topic: Deadletter topic name
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Subscription metadata
        :param pulumi.Input[str] name: Name of the Dapr subscription.
        :param pulumi.Input[str] pubsub_name: Dapr PubSub component name
        :param pulumi.Input['DaprSubscriptionRoutesArgs'] routes: Subscription routes
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Application scopes to restrict the subscription to specific apps.
        :param pulumi.Input[str] topic: Topic name
        """
        pulumi.set(__self__, "environment_name", environment_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if bulk_subscribe is not None:
            pulumi.set(__self__, "bulk_subscribe", bulk_subscribe)
        if dead_letter_topic is not None:
            pulumi.set(__self__, "dead_letter_topic", dead_letter_topic)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if pubsub_name is not None:
            pulumi.set(__self__, "pubsub_name", pubsub_name)
        if routes is not None:
            pulumi.set(__self__, "routes", routes)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[str]:
        """
        Name of the Managed Environment.
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="bulkSubscribe")
    def bulk_subscribe(self) -> Optional[pulumi.Input['DaprSubscriptionBulkSubscribeOptionsArgs']]:
        """
        Bulk subscription options
        """
        return pulumi.get(self, "bulk_subscribe")

    @bulk_subscribe.setter
    def bulk_subscribe(self, value: Optional[pulumi.Input['DaprSubscriptionBulkSubscribeOptionsArgs']]):
        pulumi.set(self, "bulk_subscribe", value)

    @property
    @pulumi.getter(name="deadLetterTopic")
    def dead_letter_topic(self) -> Optional[pulumi.Input[str]]:
        """
        Deadletter topic name
        """
        return pulumi.get(self, "dead_letter_topic")

    @dead_letter_topic.setter
    def dead_letter_topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dead_letter_topic", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Subscription metadata
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Dapr subscription.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="pubsubName")
    def pubsub_name(self) -> Optional[pulumi.Input[str]]:
        """
        Dapr PubSub component name
        """
        return pulumi.get(self, "pubsub_name")

    @pubsub_name.setter
    def pubsub_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pubsub_name", value)

    @property
    @pulumi.getter
    def routes(self) -> Optional[pulumi.Input['DaprSubscriptionRoutesArgs']]:
        """
        Subscription routes
        """
        return pulumi.get(self, "routes")

    @routes.setter
    def routes(self, value: Optional[pulumi.Input['DaprSubscriptionRoutesArgs']]):
        pulumi.set(self, "routes", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Application scopes to restrict the subscription to specific apps.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        Topic name
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)


class DaprSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bulk_subscribe: Optional[pulumi.Input[Union['DaprSubscriptionBulkSubscribeOptionsArgs', 'DaprSubscriptionBulkSubscribeOptionsArgsDict']]] = None,
                 dead_letter_topic: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pubsub_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routes: Optional[pulumi.Input[Union['DaprSubscriptionRoutesArgs', 'DaprSubscriptionRoutesArgsDict']]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Dapr PubSub Event Subscription.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['DaprSubscriptionBulkSubscribeOptionsArgs', 'DaprSubscriptionBulkSubscribeOptionsArgsDict']] bulk_subscribe: Bulk subscription options
        :param pulumi.Input[str] dead_letter_topic: Deadletter topic name
        :param pulumi.Input[str] environment_name: Name of the Managed Environment.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Subscription metadata
        :param pulumi.Input[str] name: Name of the Dapr subscription.
        :param pulumi.Input[str] pubsub_name: Dapr PubSub component name
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union['DaprSubscriptionRoutesArgs', 'DaprSubscriptionRoutesArgsDict']] routes: Subscription routes
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Application scopes to restrict the subscription to specific apps.
        :param pulumi.Input[str] topic: Topic name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DaprSubscriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Dapr PubSub Event Subscription.

        :param str resource_name: The name of the resource.
        :param DaprSubscriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DaprSubscriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bulk_subscribe: Optional[pulumi.Input[Union['DaprSubscriptionBulkSubscribeOptionsArgs', 'DaprSubscriptionBulkSubscribeOptionsArgsDict']]] = None,
                 dead_letter_topic: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 pubsub_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routes: Optional[pulumi.Input[Union['DaprSubscriptionRoutesArgs', 'DaprSubscriptionRoutesArgsDict']]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DaprSubscriptionArgs.__new__(DaprSubscriptionArgs)

            __props__.__dict__["bulk_subscribe"] = bulk_subscribe
            __props__.__dict__["dead_letter_topic"] = dead_letter_topic
            if environment_name is None and not opts.urn:
                raise TypeError("Missing required property 'environment_name'")
            __props__.__dict__["environment_name"] = environment_name
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["name"] = name
            __props__.__dict__["pubsub_name"] = pubsub_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["routes"] = routes
            __props__.__dict__["scopes"] = scopes
            __props__.__dict__["topic"] = topic
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:app:DaprSubscription"), pulumi.Alias(type_="azure-native:app/v20230801preview:DaprSubscription"), pulumi.Alias(type_="azure-native:app/v20240202preview:DaprSubscription")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DaprSubscription, __self__).__init__(
            'azure-native:app/v20231102preview:DaprSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DaprSubscription':
        """
        Get an existing DaprSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DaprSubscriptionArgs.__new__(DaprSubscriptionArgs)

        __props__.__dict__["bulk_subscribe"] = None
        __props__.__dict__["dead_letter_topic"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["pubsub_name"] = None
        __props__.__dict__["routes"] = None
        __props__.__dict__["scopes"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["topic"] = None
        __props__.__dict__["type"] = None
        return DaprSubscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bulkSubscribe")
    def bulk_subscribe(self) -> pulumi.Output[Optional['outputs.DaprSubscriptionBulkSubscribeOptionsResponse']]:
        """
        Bulk subscription options
        """
        return pulumi.get(self, "bulk_subscribe")

    @property
    @pulumi.getter(name="deadLetterTopic")
    def dead_letter_topic(self) -> pulumi.Output[Optional[str]]:
        """
        Deadletter topic name
        """
        return pulumi.get(self, "dead_letter_topic")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Subscription metadata
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pubsubName")
    def pubsub_name(self) -> pulumi.Output[Optional[str]]:
        """
        Dapr PubSub component name
        """
        return pulumi.get(self, "pubsub_name")

    @property
    @pulumi.getter
    def routes(self) -> pulumi.Output[Optional['outputs.DaprSubscriptionRoutesResponse']]:
        """
        Subscription routes
        """
        return pulumi.get(self, "routes")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Application scopes to restrict the subscription to specific apps.
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Output[Optional[str]]:
        """
        Topic name
        """
        return pulumi.get(self, "topic")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

