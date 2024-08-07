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
from ._enums import *

__all__ = [
    'NetworkRuleSetArgs',
    'NetworkRuleSetArgsDict',
    'PrivateLinkServiceConnectionStateArgs',
    'PrivateLinkServiceConnectionStateArgsDict',
    'SkuArgs',
    'SkuArgsDict',
    'SourceCreationDataArgs',
    'SourceCreationDataArgsDict',
    'VirtualNetworkRuleArgs',
    'VirtualNetworkRuleArgsDict',
]

MYPY = False

if not MYPY:
    class NetworkRuleSetArgsDict(TypedDict):
        """
        A set of rules governing the network accessibility.
        """
        virtual_network_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgsDict']]]]
        """
        The list of virtual network rules.
        """
elif False:
    NetworkRuleSetArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class NetworkRuleSetArgs:
    def __init__(__self__, *,
                 virtual_network_rules: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgs']]]] = None):
        """
        A set of rules governing the network accessibility.
        :param pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgs']]] virtual_network_rules: The list of virtual network rules.
        """
        if virtual_network_rules is not None:
            pulumi.set(__self__, "virtual_network_rules", virtual_network_rules)

    @property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgs']]]]:
        """
        The list of virtual network rules.
        """
        return pulumi.get(self, "virtual_network_rules")

    @virtual_network_rules.setter
    def virtual_network_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgs']]]]):
        pulumi.set(self, "virtual_network_rules", value)


if not MYPY:
    class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
        """
        Response for Private Link Service Connection state
        """
        actions_required: NotRequired[pulumi.Input[str]]
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        description: NotRequired[pulumi.Input[str]]
        """
        The reason for approval/rejection of the connection.
        """
        status: NotRequired[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
elif False:
    PrivateLinkServiceConnectionStateArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 actions_required: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]] = None):
        """
        Response for Private Link Service Connection state
        :param pulumi.Input[str] actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param pulumi.Input[str] description: The reason for approval/rejection of the connection.
        :param pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']] status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[str]]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "actions_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]):
        pulumi.set(self, "status", value)


if not MYPY:
    class SkuArgsDict(TypedDict):
        """
        The SKU name. Required for account creation; optional for update.
        """
        name: pulumi.Input[Union[str, 'SkuName']]
        """
        The sku name.
        """
        tier: NotRequired[pulumi.Input[Union[str, 'SkuTier']]]
        """
        The sku tier.
        """
elif False:
    SkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[Union[str, 'SkuName']],
                 tier: Optional[pulumi.Input[Union[str, 'SkuTier']]] = None):
        """
        The SKU name. Required for account creation; optional for update.
        :param pulumi.Input[Union[str, 'SkuName']] name: The sku name.
        :param pulumi.Input[Union[str, 'SkuTier']] tier: The sku tier.
        """
        pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[str, 'SkuName']]:
        """
        The sku name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[str, 'SkuName']]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[str, 'SkuTier']]]:
        """
        The sku tier.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[str, 'SkuTier']]]):
        pulumi.set(self, "tier", value)


if not MYPY:
    class SourceCreationDataArgsDict(TypedDict):
        """
        Data source used when creating the volume.
        """
        create_source: NotRequired[pulumi.Input['VolumeCreateOption']]
        """
        This enumerates the possible sources of a volume creation.
        """
        source_uri: NotRequired[pulumi.Input[str]]
        """
        If createOption is Copy, this is the ARM id of the source snapshot or disk. If createOption is Restore, this is the ARM-like id of the source disk restore point.
        """
elif False:
    SourceCreationDataArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SourceCreationDataArgs:
    def __init__(__self__, *,
                 create_source: Optional[pulumi.Input['VolumeCreateOption']] = None,
                 source_uri: Optional[pulumi.Input[str]] = None):
        """
        Data source used when creating the volume.
        :param pulumi.Input['VolumeCreateOption'] create_source: This enumerates the possible sources of a volume creation.
        :param pulumi.Input[str] source_uri: If createOption is Copy, this is the ARM id of the source snapshot or disk. If createOption is Restore, this is the ARM-like id of the source disk restore point.
        """
        if create_source is not None:
            pulumi.set(__self__, "create_source", create_source)
        if source_uri is not None:
            pulumi.set(__self__, "source_uri", source_uri)

    @property
    @pulumi.getter(name="createSource")
    def create_source(self) -> Optional[pulumi.Input['VolumeCreateOption']]:
        """
        This enumerates the possible sources of a volume creation.
        """
        return pulumi.get(self, "create_source")

    @create_source.setter
    def create_source(self, value: Optional[pulumi.Input['VolumeCreateOption']]):
        pulumi.set(self, "create_source", value)

    @property
    @pulumi.getter(name="sourceUri")
    def source_uri(self) -> Optional[pulumi.Input[str]]:
        """
        If createOption is Copy, this is the ARM id of the source snapshot or disk. If createOption is Restore, this is the ARM-like id of the source disk restore point.
        """
        return pulumi.get(self, "source_uri")

    @source_uri.setter
    def source_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_uri", value)


if not MYPY:
    class VirtualNetworkRuleArgsDict(TypedDict):
        """
        Virtual Network rule.
        """
        virtual_network_resource_id: pulumi.Input[str]
        """
        Resource ID of a subnet, for example: /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}.
        """
        action: NotRequired[pulumi.Input['Action']]
        """
        The action of virtual network rule.
        """
elif False:
    VirtualNetworkRuleArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class VirtualNetworkRuleArgs:
    def __init__(__self__, *,
                 virtual_network_resource_id: pulumi.Input[str],
                 action: Optional[pulumi.Input['Action']] = None):
        """
        Virtual Network rule.
        :param pulumi.Input[str] virtual_network_resource_id: Resource ID of a subnet, for example: /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}.
        :param pulumi.Input['Action'] action: The action of virtual network rule.
        """
        pulumi.set(__self__, "virtual_network_resource_id", virtual_network_resource_id)
        if action is None:
            action = 'Allow'
        if action is not None:
            pulumi.set(__self__, "action", action)

    @property
    @pulumi.getter(name="virtualNetworkResourceId")
    def virtual_network_resource_id(self) -> pulumi.Input[str]:
        """
        Resource ID of a subnet, for example: /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}.
        """
        return pulumi.get(self, "virtual_network_resource_id")

    @virtual_network_resource_id.setter
    def virtual_network_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_network_resource_id", value)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input['Action']]:
        """
        The action of virtual network rule.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input['Action']]):
        pulumi.set(self, "action", value)


