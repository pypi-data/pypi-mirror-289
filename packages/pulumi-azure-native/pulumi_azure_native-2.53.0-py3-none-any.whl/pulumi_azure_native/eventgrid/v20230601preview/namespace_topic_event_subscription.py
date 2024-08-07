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
from ._enums import *
from ._inputs import *

__all__ = ['NamespaceTopicEventSubscriptionArgs', 'NamespaceTopicEventSubscription']

@pulumi.input_type
class NamespaceTopicEventSubscriptionArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 topic_name: pulumi.Input[str],
                 delivery_configuration: Optional[pulumi.Input['DeliveryConfigurationArgs']] = None,
                 event_delivery_schema: Optional[pulumi.Input[Union[str, 'DeliverySchema']]] = None,
                 event_subscription_name: Optional[pulumi.Input[str]] = None,
                 filters_configuration: Optional[pulumi.Input['FiltersConfigurationArgs']] = None):
        """
        The set of arguments for constructing a NamespaceTopicEventSubscription resource.
        :param pulumi.Input[str] namespace_name: Name of the namespace.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[str] topic_name: Name of the namespace topic.
        :param pulumi.Input['DeliveryConfigurationArgs'] delivery_configuration: Information about the delivery configuration of the event subscription.
        :param pulumi.Input[Union[str, 'DeliverySchema']] event_delivery_schema: The event delivery schema for the event subscription.
        :param pulumi.Input[str] event_subscription_name: Name of the event subscription to be created. Event subscription names must be between 3 and 100 characters in length and use alphanumeric letters only.
        :param pulumi.Input['FiltersConfigurationArgs'] filters_configuration: Information about the filter for the event subscription.
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "topic_name", topic_name)
        if delivery_configuration is not None:
            pulumi.set(__self__, "delivery_configuration", delivery_configuration)
        if event_delivery_schema is not None:
            pulumi.set(__self__, "event_delivery_schema", event_delivery_schema)
        if event_subscription_name is not None:
            pulumi.set(__self__, "event_subscription_name", event_subscription_name)
        if filters_configuration is not None:
            pulumi.set(__self__, "filters_configuration", filters_configuration)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        Name of the namespace.
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> pulumi.Input[str]:
        """
        Name of the namespace topic.
        """
        return pulumi.get(self, "topic_name")

    @topic_name.setter
    def topic_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "topic_name", value)

    @property
    @pulumi.getter(name="deliveryConfiguration")
    def delivery_configuration(self) -> Optional[pulumi.Input['DeliveryConfigurationArgs']]:
        """
        Information about the delivery configuration of the event subscription.
        """
        return pulumi.get(self, "delivery_configuration")

    @delivery_configuration.setter
    def delivery_configuration(self, value: Optional[pulumi.Input['DeliveryConfigurationArgs']]):
        pulumi.set(self, "delivery_configuration", value)

    @property
    @pulumi.getter(name="eventDeliverySchema")
    def event_delivery_schema(self) -> Optional[pulumi.Input[Union[str, 'DeliverySchema']]]:
        """
        The event delivery schema for the event subscription.
        """
        return pulumi.get(self, "event_delivery_schema")

    @event_delivery_schema.setter
    def event_delivery_schema(self, value: Optional[pulumi.Input[Union[str, 'DeliverySchema']]]):
        pulumi.set(self, "event_delivery_schema", value)

    @property
    @pulumi.getter(name="eventSubscriptionName")
    def event_subscription_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the event subscription to be created. Event subscription names must be between 3 and 100 characters in length and use alphanumeric letters only.
        """
        return pulumi.get(self, "event_subscription_name")

    @event_subscription_name.setter
    def event_subscription_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "event_subscription_name", value)

    @property
    @pulumi.getter(name="filtersConfiguration")
    def filters_configuration(self) -> Optional[pulumi.Input['FiltersConfigurationArgs']]:
        """
        Information about the filter for the event subscription.
        """
        return pulumi.get(self, "filters_configuration")

    @filters_configuration.setter
    def filters_configuration(self, value: Optional[pulumi.Input['FiltersConfigurationArgs']]):
        pulumi.set(self, "filters_configuration", value)


class NamespaceTopicEventSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_configuration: Optional[pulumi.Input[Union['DeliveryConfigurationArgs', 'DeliveryConfigurationArgsDict']]] = None,
                 event_delivery_schema: Optional[pulumi.Input[Union[str, 'DeliverySchema']]] = None,
                 event_subscription_name: Optional[pulumi.Input[str]] = None,
                 filters_configuration: Optional[pulumi.Input[Union['FiltersConfigurationArgs', 'FiltersConfigurationArgsDict']]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Event Subscription.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['DeliveryConfigurationArgs', 'DeliveryConfigurationArgsDict']] delivery_configuration: Information about the delivery configuration of the event subscription.
        :param pulumi.Input[Union[str, 'DeliverySchema']] event_delivery_schema: The event delivery schema for the event subscription.
        :param pulumi.Input[str] event_subscription_name: Name of the event subscription to be created. Event subscription names must be between 3 and 100 characters in length and use alphanumeric letters only.
        :param pulumi.Input[Union['FiltersConfigurationArgs', 'FiltersConfigurationArgsDict']] filters_configuration: Information about the filter for the event subscription.
        :param pulumi.Input[str] namespace_name: Name of the namespace.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[str] topic_name: Name of the namespace topic.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceTopicEventSubscriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Event Subscription.

        :param str resource_name: The name of the resource.
        :param NamespaceTopicEventSubscriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceTopicEventSubscriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_configuration: Optional[pulumi.Input[Union['DeliveryConfigurationArgs', 'DeliveryConfigurationArgsDict']]] = None,
                 event_delivery_schema: Optional[pulumi.Input[Union[str, 'DeliverySchema']]] = None,
                 event_subscription_name: Optional[pulumi.Input[str]] = None,
                 filters_configuration: Optional[pulumi.Input[Union['FiltersConfigurationArgs', 'FiltersConfigurationArgsDict']]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamespaceTopicEventSubscriptionArgs.__new__(NamespaceTopicEventSubscriptionArgs)

            __props__.__dict__["delivery_configuration"] = delivery_configuration
            __props__.__dict__["event_delivery_schema"] = event_delivery_schema
            __props__.__dict__["event_subscription_name"] = event_subscription_name
            __props__.__dict__["filters_configuration"] = filters_configuration
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if topic_name is None and not opts.urn:
                raise TypeError("Missing required property 'topic_name'")
            __props__.__dict__["topic_name"] = topic_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventgrid:NamespaceTopicEventSubscription"), pulumi.Alias(type_="azure-native:eventgrid/v20231215preview:NamespaceTopicEventSubscription"), pulumi.Alias(type_="azure-native:eventgrid/v20240601preview:NamespaceTopicEventSubscription")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NamespaceTopicEventSubscription, __self__).__init__(
            'azure-native:eventgrid/v20230601preview:NamespaceTopicEventSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NamespaceTopicEventSubscription':
        """
        Get an existing NamespaceTopicEventSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NamespaceTopicEventSubscriptionArgs.__new__(NamespaceTopicEventSubscriptionArgs)

        __props__.__dict__["delivery_configuration"] = None
        __props__.__dict__["event_delivery_schema"] = None
        __props__.__dict__["filters_configuration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return NamespaceTopicEventSubscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deliveryConfiguration")
    def delivery_configuration(self) -> pulumi.Output[Optional['outputs.DeliveryConfigurationResponse']]:
        """
        Information about the delivery configuration of the event subscription.
        """
        return pulumi.get(self, "delivery_configuration")

    @property
    @pulumi.getter(name="eventDeliverySchema")
    def event_delivery_schema(self) -> pulumi.Output[Optional[str]]:
        """
        The event delivery schema for the event subscription.
        """
        return pulumi.get(self, "event_delivery_schema")

    @property
    @pulumi.getter(name="filtersConfiguration")
    def filters_configuration(self) -> pulumi.Output[Optional['outputs.FiltersConfigurationResponse']]:
        """
        Information about the filter for the event subscription.
        """
        return pulumi.get(self, "filters_configuration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the event subscription.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to Event Subscription resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

