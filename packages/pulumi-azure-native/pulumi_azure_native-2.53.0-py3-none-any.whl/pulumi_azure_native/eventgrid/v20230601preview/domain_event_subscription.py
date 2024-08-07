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

__all__ = ['DomainEventSubscriptionArgs', 'DomainEventSubscription']

@pulumi.input_type
class DomainEventSubscriptionArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 dead_letter_destination: Optional[pulumi.Input['StorageBlobDeadLetterDestinationArgs']] = None,
                 dead_letter_with_resource_identity: Optional[pulumi.Input['DeadLetterWithResourceIdentityArgs']] = None,
                 delivery_with_resource_identity: Optional[pulumi.Input['DeliveryWithResourceIdentityArgs']] = None,
                 destination: Optional[pulumi.Input[Union['AzureFunctionEventSubscriptionDestinationArgs', 'EventHubEventSubscriptionDestinationArgs', 'HybridConnectionEventSubscriptionDestinationArgs', 'PartnerEventSubscriptionDestinationArgs', 'ServiceBusQueueEventSubscriptionDestinationArgs', 'ServiceBusTopicEventSubscriptionDestinationArgs', 'StorageQueueEventSubscriptionDestinationArgs', 'WebHookEventSubscriptionDestinationArgs']]] = None,
                 event_delivery_schema: Optional[pulumi.Input[Union[str, 'EventDeliverySchema']]] = None,
                 event_subscription_name: Optional[pulumi.Input[str]] = None,
                 expiration_time_utc: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input['EventSubscriptionFilterArgs']] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 retry_policy: Optional[pulumi.Input['RetryPolicyArgs']] = None):
        """
        The set of arguments for constructing a DomainEventSubscription resource.
        :param pulumi.Input[str] domain_name: Name of the domain topic.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input['StorageBlobDeadLetterDestinationArgs'] dead_letter_destination: The dead letter destination of the event subscription. Any event that cannot be delivered to its' destination is sent to the dead letter destination.
               Uses Azure Event Grid's identity to acquire the authentication tokens being used during delivery / dead-lettering.
        :param pulumi.Input['DeadLetterWithResourceIdentityArgs'] dead_letter_with_resource_identity: The dead letter destination of the event subscription. Any event that cannot be delivered to its' destination is sent to the dead letter destination.
               Uses the managed identity setup on the parent resource (namely, topic or domain) to acquire the authentication tokens being used during delivery / dead-lettering.
        :param pulumi.Input['DeliveryWithResourceIdentityArgs'] delivery_with_resource_identity: Information about the destination where events have to be delivered for the event subscription.
               Uses the managed identity setup on the parent resource (namely, topic or domain) to acquire the authentication tokens being used during delivery / dead-lettering.
        :param pulumi.Input[Union['AzureFunctionEventSubscriptionDestinationArgs', 'EventHubEventSubscriptionDestinationArgs', 'HybridConnectionEventSubscriptionDestinationArgs', 'PartnerEventSubscriptionDestinationArgs', 'ServiceBusQueueEventSubscriptionDestinationArgs', 'ServiceBusTopicEventSubscriptionDestinationArgs', 'StorageQueueEventSubscriptionDestinationArgs', 'WebHookEventSubscriptionDestinationArgs']] destination: Information about the destination where events have to be delivered for the event subscription.
               Uses Azure Event Grid's identity to acquire the authentication tokens being used during delivery / dead-lettering.
        :param pulumi.Input[Union[str, 'EventDeliverySchema']] event_delivery_schema: The event delivery schema for the event subscription.
        :param pulumi.Input[str] event_subscription_name: Name of the event subscription to be created. Event subscription names must be between 3 and 100 characters in length and use alphanumeric letters only.
        :param pulumi.Input[str] expiration_time_utc: Expiration time of the event subscription.
        :param pulumi.Input['EventSubscriptionFilterArgs'] filter: Information about the filter for the event subscription.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of user defined labels.
        :param pulumi.Input['RetryPolicyArgs'] retry_policy: The retry policy for events. This can be used to configure maximum number of delivery attempts and time to live for events.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if dead_letter_destination is not None:
            pulumi.set(__self__, "dead_letter_destination", dead_letter_destination)
        if dead_letter_with_resource_identity is not None:
            pulumi.set(__self__, "dead_letter_with_resource_identity", dead_letter_with_resource_identity)
        if delivery_with_resource_identity is not None:
            pulumi.set(__self__, "delivery_with_resource_identity", delivery_with_resource_identity)
        if destination is not None:
            pulumi.set(__self__, "destination", destination)
        if event_delivery_schema is None:
            event_delivery_schema = 'EventGridSchema'
        if event_delivery_schema is not None:
            pulumi.set(__self__, "event_delivery_schema", event_delivery_schema)
        if event_subscription_name is not None:
            pulumi.set(__self__, "event_subscription_name", event_subscription_name)
        if expiration_time_utc is not None:
            pulumi.set(__self__, "expiration_time_utc", expiration_time_utc)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if retry_policy is not None:
            pulumi.set(__self__, "retry_policy", retry_policy)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        Name of the domain topic.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

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
    @pulumi.getter(name="deadLetterDestination")
    def dead_letter_destination(self) -> Optional[pulumi.Input['StorageBlobDeadLetterDestinationArgs']]:
        """
        The dead letter destination of the event subscription. Any event that cannot be delivered to its' destination is sent to the dead letter destination.
        Uses Azure Event Grid's identity to acquire the authentication tokens being used during delivery / dead-lettering.
        """
        return pulumi.get(self, "dead_letter_destination")

    @dead_letter_destination.setter
    def dead_letter_destination(self, value: Optional[pulumi.Input['StorageBlobDeadLetterDestinationArgs']]):
        pulumi.set(self, "dead_letter_destination", value)

    @property
    @pulumi.getter(name="deadLetterWithResourceIdentity")
    def dead_letter_with_resource_identity(self) -> Optional[pulumi.Input['DeadLetterWithResourceIdentityArgs']]:
        """
        The dead letter destination of the event subscription. Any event that cannot be delivered to its' destination is sent to the dead letter destination.
        Uses the managed identity setup on the parent resource (namely, topic or domain) to acquire the authentication tokens being used during delivery / dead-lettering.
        """
        return pulumi.get(self, "dead_letter_with_resource_identity")

    @dead_letter_with_resource_identity.setter
    def dead_letter_with_resource_identity(self, value: Optional[pulumi.Input['DeadLetterWithResourceIdentityArgs']]):
        pulumi.set(self, "dead_letter_with_resource_identity", value)

    @property
    @pulumi.getter(name="deliveryWithResourceIdentity")
    def delivery_with_resource_identity(self) -> Optional[pulumi.Input['DeliveryWithResourceIdentityArgs']]:
        """
        Information about the destination where events have to be delivered for the event subscription.
        Uses the managed identity setup on the parent resource (namely, topic or domain) to acquire the authentication tokens being used during delivery / dead-lettering.
        """
        return pulumi.get(self, "delivery_with_resource_identity")

    @delivery_with_resource_identity.setter
    def delivery_with_resource_identity(self, value: Optional[pulumi.Input['DeliveryWithResourceIdentityArgs']]):
        pulumi.set(self, "delivery_with_resource_identity", value)

    @property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[Union['AzureFunctionEventSubscriptionDestinationArgs', 'EventHubEventSubscriptionDestinationArgs', 'HybridConnectionEventSubscriptionDestinationArgs', 'PartnerEventSubscriptionDestinationArgs', 'ServiceBusQueueEventSubscriptionDestinationArgs', 'ServiceBusTopicEventSubscriptionDestinationArgs', 'StorageQueueEventSubscriptionDestinationArgs', 'WebHookEventSubscriptionDestinationArgs']]]:
        """
        Information about the destination where events have to be delivered for the event subscription.
        Uses Azure Event Grid's identity to acquire the authentication tokens being used during delivery / dead-lettering.
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: Optional[pulumi.Input[Union['AzureFunctionEventSubscriptionDestinationArgs', 'EventHubEventSubscriptionDestinationArgs', 'HybridConnectionEventSubscriptionDestinationArgs', 'PartnerEventSubscriptionDestinationArgs', 'ServiceBusQueueEventSubscriptionDestinationArgs', 'ServiceBusTopicEventSubscriptionDestinationArgs', 'StorageQueueEventSubscriptionDestinationArgs', 'WebHookEventSubscriptionDestinationArgs']]]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter(name="eventDeliverySchema")
    def event_delivery_schema(self) -> Optional[pulumi.Input[Union[str, 'EventDeliverySchema']]]:
        """
        The event delivery schema for the event subscription.
        """
        return pulumi.get(self, "event_delivery_schema")

    @event_delivery_schema.setter
    def event_delivery_schema(self, value: Optional[pulumi.Input[Union[str, 'EventDeliverySchema']]]):
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
    @pulumi.getter(name="expirationTimeUtc")
    def expiration_time_utc(self) -> Optional[pulumi.Input[str]]:
        """
        Expiration time of the event subscription.
        """
        return pulumi.get(self, "expiration_time_utc")

    @expiration_time_utc.setter
    def expiration_time_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_time_utc", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input['EventSubscriptionFilterArgs']]:
        """
        Information about the filter for the event subscription.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input['EventSubscriptionFilterArgs']]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of user defined labels.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> Optional[pulumi.Input['RetryPolicyArgs']]:
        """
        The retry policy for events. This can be used to configure maximum number of delivery attempts and time to live for events.
        """
        return pulumi.get(self, "retry_policy")

    @retry_policy.setter
    def retry_policy(self, value: Optional[pulumi.Input['RetryPolicyArgs']]):
        pulumi.set(self, "retry_policy", value)


class DomainEventSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dead_letter_destination: Optional[pulumi.Input[Union['StorageBlobDeadLetterDestinationArgs', 'StorageBlobDeadLetterDestinationArgsDict']]] = None,
                 dead_letter_with_resource_identity: Optional[pulumi.Input[Union['DeadLetterWithResourceIdentityArgs', 'DeadLetterWithResourceIdentityArgsDict']]] = None,
                 delivery_with_resource_identity: Optional[pulumi.Input[Union['DeliveryWithResourceIdentityArgs', 'DeliveryWithResourceIdentityArgsDict']]] = None,
                 destination: Optional[pulumi.Input[Union[Union['AzureFunctionEventSubscriptionDestinationArgs', 'AzureFunctionEventSubscriptionDestinationArgsDict'], Union['EventHubEventSubscriptionDestinationArgs', 'EventHubEventSubscriptionDestinationArgsDict'], Union['HybridConnectionEventSubscriptionDestinationArgs', 'HybridConnectionEventSubscriptionDestinationArgsDict'], Union['PartnerEventSubscriptionDestinationArgs', 'PartnerEventSubscriptionDestinationArgsDict'], Union['ServiceBusQueueEventSubscriptionDestinationArgs', 'ServiceBusQueueEventSubscriptionDestinationArgsDict'], Union['ServiceBusTopicEventSubscriptionDestinationArgs', 'ServiceBusTopicEventSubscriptionDestinationArgsDict'], Union['StorageQueueEventSubscriptionDestinationArgs', 'StorageQueueEventSubscriptionDestinationArgsDict'], Union['WebHookEventSubscriptionDestinationArgs', 'WebHookEventSubscriptionDestinationArgsDict']]]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 event_delivery_schema: Optional[pulumi.Input[Union[str, 'EventDeliverySchema']]] = None,
                 event_subscription_name: Optional[pulumi.Input[str]] = None,
                 expiration_time_utc: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[Union['EventSubscriptionFilterArgs', 'EventSubscriptionFilterArgsDict']]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retry_policy: Optional[pulumi.Input[Union['RetryPolicyArgs', 'RetryPolicyArgsDict']]] = None,
                 __props__=None):
        """
        Event Subscription.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['StorageBlobDeadLetterDestinationArgs', 'StorageBlobDeadLetterDestinationArgsDict']] dead_letter_destination: The dead letter destination of the event subscription. Any event that cannot be delivered to its' destination is sent to the dead letter destination.
               Uses Azure Event Grid's identity to acquire the authentication tokens being used during delivery / dead-lettering.
        :param pulumi.Input[Union['DeadLetterWithResourceIdentityArgs', 'DeadLetterWithResourceIdentityArgsDict']] dead_letter_with_resource_identity: The dead letter destination of the event subscription. Any event that cannot be delivered to its' destination is sent to the dead letter destination.
               Uses the managed identity setup on the parent resource (namely, topic or domain) to acquire the authentication tokens being used during delivery / dead-lettering.
        :param pulumi.Input[Union['DeliveryWithResourceIdentityArgs', 'DeliveryWithResourceIdentityArgsDict']] delivery_with_resource_identity: Information about the destination where events have to be delivered for the event subscription.
               Uses the managed identity setup on the parent resource (namely, topic or domain) to acquire the authentication tokens being used during delivery / dead-lettering.
        :param pulumi.Input[Union[Union['AzureFunctionEventSubscriptionDestinationArgs', 'AzureFunctionEventSubscriptionDestinationArgsDict'], Union['EventHubEventSubscriptionDestinationArgs', 'EventHubEventSubscriptionDestinationArgsDict'], Union['HybridConnectionEventSubscriptionDestinationArgs', 'HybridConnectionEventSubscriptionDestinationArgsDict'], Union['PartnerEventSubscriptionDestinationArgs', 'PartnerEventSubscriptionDestinationArgsDict'], Union['ServiceBusQueueEventSubscriptionDestinationArgs', 'ServiceBusQueueEventSubscriptionDestinationArgsDict'], Union['ServiceBusTopicEventSubscriptionDestinationArgs', 'ServiceBusTopicEventSubscriptionDestinationArgsDict'], Union['StorageQueueEventSubscriptionDestinationArgs', 'StorageQueueEventSubscriptionDestinationArgsDict'], Union['WebHookEventSubscriptionDestinationArgs', 'WebHookEventSubscriptionDestinationArgsDict']]] destination: Information about the destination where events have to be delivered for the event subscription.
               Uses Azure Event Grid's identity to acquire the authentication tokens being used during delivery / dead-lettering.
        :param pulumi.Input[str] domain_name: Name of the domain topic.
        :param pulumi.Input[Union[str, 'EventDeliverySchema']] event_delivery_schema: The event delivery schema for the event subscription.
        :param pulumi.Input[str] event_subscription_name: Name of the event subscription to be created. Event subscription names must be between 3 and 100 characters in length and use alphanumeric letters only.
        :param pulumi.Input[str] expiration_time_utc: Expiration time of the event subscription.
        :param pulumi.Input[Union['EventSubscriptionFilterArgs', 'EventSubscriptionFilterArgsDict']] filter: Information about the filter for the event subscription.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of user defined labels.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[Union['RetryPolicyArgs', 'RetryPolicyArgsDict']] retry_policy: The retry policy for events. This can be used to configure maximum number of delivery attempts and time to live for events.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainEventSubscriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Event Subscription.

        :param str resource_name: The name of the resource.
        :param DomainEventSubscriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainEventSubscriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dead_letter_destination: Optional[pulumi.Input[Union['StorageBlobDeadLetterDestinationArgs', 'StorageBlobDeadLetterDestinationArgsDict']]] = None,
                 dead_letter_with_resource_identity: Optional[pulumi.Input[Union['DeadLetterWithResourceIdentityArgs', 'DeadLetterWithResourceIdentityArgsDict']]] = None,
                 delivery_with_resource_identity: Optional[pulumi.Input[Union['DeliveryWithResourceIdentityArgs', 'DeliveryWithResourceIdentityArgsDict']]] = None,
                 destination: Optional[pulumi.Input[Union[Union['AzureFunctionEventSubscriptionDestinationArgs', 'AzureFunctionEventSubscriptionDestinationArgsDict'], Union['EventHubEventSubscriptionDestinationArgs', 'EventHubEventSubscriptionDestinationArgsDict'], Union['HybridConnectionEventSubscriptionDestinationArgs', 'HybridConnectionEventSubscriptionDestinationArgsDict'], Union['PartnerEventSubscriptionDestinationArgs', 'PartnerEventSubscriptionDestinationArgsDict'], Union['ServiceBusQueueEventSubscriptionDestinationArgs', 'ServiceBusQueueEventSubscriptionDestinationArgsDict'], Union['ServiceBusTopicEventSubscriptionDestinationArgs', 'ServiceBusTopicEventSubscriptionDestinationArgsDict'], Union['StorageQueueEventSubscriptionDestinationArgs', 'StorageQueueEventSubscriptionDestinationArgsDict'], Union['WebHookEventSubscriptionDestinationArgs', 'WebHookEventSubscriptionDestinationArgsDict']]]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 event_delivery_schema: Optional[pulumi.Input[Union[str, 'EventDeliverySchema']]] = None,
                 event_subscription_name: Optional[pulumi.Input[str]] = None,
                 expiration_time_utc: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[Union['EventSubscriptionFilterArgs', 'EventSubscriptionFilterArgsDict']]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retry_policy: Optional[pulumi.Input[Union['RetryPolicyArgs', 'RetryPolicyArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainEventSubscriptionArgs.__new__(DomainEventSubscriptionArgs)

            __props__.__dict__["dead_letter_destination"] = dead_letter_destination
            __props__.__dict__["dead_letter_with_resource_identity"] = dead_letter_with_resource_identity
            __props__.__dict__["delivery_with_resource_identity"] = delivery_with_resource_identity
            __props__.__dict__["destination"] = destination
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            if event_delivery_schema is None:
                event_delivery_schema = 'EventGridSchema'
            __props__.__dict__["event_delivery_schema"] = event_delivery_schema
            __props__.__dict__["event_subscription_name"] = event_subscription_name
            __props__.__dict__["expiration_time_utc"] = expiration_time_utc
            __props__.__dict__["filter"] = filter
            __props__.__dict__["labels"] = labels
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["retry_policy"] = retry_policy
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["topic"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventgrid:DomainEventSubscription"), pulumi.Alias(type_="azure-native:eventgrid/v20211015preview:DomainEventSubscription"), pulumi.Alias(type_="azure-native:eventgrid/v20220615:DomainEventSubscription"), pulumi.Alias(type_="azure-native:eventgrid/v20231215preview:DomainEventSubscription"), pulumi.Alias(type_="azure-native:eventgrid/v20240601preview:DomainEventSubscription")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DomainEventSubscription, __self__).__init__(
            'azure-native:eventgrid/v20230601preview:DomainEventSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DomainEventSubscription':
        """
        Get an existing DomainEventSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DomainEventSubscriptionArgs.__new__(DomainEventSubscriptionArgs)

        __props__.__dict__["dead_letter_destination"] = None
        __props__.__dict__["dead_letter_with_resource_identity"] = None
        __props__.__dict__["delivery_with_resource_identity"] = None
        __props__.__dict__["destination"] = None
        __props__.__dict__["event_delivery_schema"] = None
        __props__.__dict__["expiration_time_utc"] = None
        __props__.__dict__["filter"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["retry_policy"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["topic"] = None
        __props__.__dict__["type"] = None
        return DomainEventSubscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deadLetterDestination")
    def dead_letter_destination(self) -> pulumi.Output[Optional['outputs.StorageBlobDeadLetterDestinationResponse']]:
        """
        The dead letter destination of the event subscription. Any event that cannot be delivered to its' destination is sent to the dead letter destination.
        Uses Azure Event Grid's identity to acquire the authentication tokens being used during delivery / dead-lettering.
        """
        return pulumi.get(self, "dead_letter_destination")

    @property
    @pulumi.getter(name="deadLetterWithResourceIdentity")
    def dead_letter_with_resource_identity(self) -> pulumi.Output[Optional['outputs.DeadLetterWithResourceIdentityResponse']]:
        """
        The dead letter destination of the event subscription. Any event that cannot be delivered to its' destination is sent to the dead letter destination.
        Uses the managed identity setup on the parent resource (namely, topic or domain) to acquire the authentication tokens being used during delivery / dead-lettering.
        """
        return pulumi.get(self, "dead_letter_with_resource_identity")

    @property
    @pulumi.getter(name="deliveryWithResourceIdentity")
    def delivery_with_resource_identity(self) -> pulumi.Output[Optional['outputs.DeliveryWithResourceIdentityResponse']]:
        """
        Information about the destination where events have to be delivered for the event subscription.
        Uses the managed identity setup on the parent resource (namely, topic or domain) to acquire the authentication tokens being used during delivery / dead-lettering.
        """
        return pulumi.get(self, "delivery_with_resource_identity")

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Output[Optional[Any]]:
        """
        Information about the destination where events have to be delivered for the event subscription.
        Uses Azure Event Grid's identity to acquire the authentication tokens being used during delivery / dead-lettering.
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="eventDeliverySchema")
    def event_delivery_schema(self) -> pulumi.Output[Optional[str]]:
        """
        The event delivery schema for the event subscription.
        """
        return pulumi.get(self, "event_delivery_schema")

    @property
    @pulumi.getter(name="expirationTimeUtc")
    def expiration_time_utc(self) -> pulumi.Output[Optional[str]]:
        """
        Expiration time of the event subscription.
        """
        return pulumi.get(self, "expiration_time_utc")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional['outputs.EventSubscriptionFilterResponse']]:
        """
        Information about the filter for the event subscription.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of user defined labels.
        """
        return pulumi.get(self, "labels")

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
    @pulumi.getter(name="retryPolicy")
    def retry_policy(self) -> pulumi.Output[Optional['outputs.RetryPolicyResponse']]:
        """
        The retry policy for events. This can be used to configure maximum number of delivery attempts and time to live for events.
        """
        return pulumi.get(self, "retry_policy")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to Event Subscription resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Output[str]:
        """
        Name of the topic of the event subscription.
        """
        return pulumi.get(self, "topic")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

