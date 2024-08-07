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
from ._inputs import *

__all__ = ['VirtualNetworkArgs', 'VirtualNetwork']

@pulumi.input_type
class VirtualNetworkArgs:
    def __init__(__self__, *,
                 extended_location: pulumi.Input['ExtendedLocationArgs'],
                 resource_group_name: pulumi.Input[str],
                 inventory_item_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 uuid: Optional[pulumi.Input[str]] = None,
                 virtual_network_name: Optional[pulumi.Input[str]] = None,
                 vmm_server_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualNetwork resource.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] inventory_item_id: Gets or sets the inventory Item ID for the resource.
        :param pulumi.Input[str] location: Gets or sets the location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] uuid: Unique ID of the virtual network.
        :param pulumi.Input[str] virtual_network_name: Name of the VirtualNetwork.
        :param pulumi.Input[str] vmm_server_id: ARM Id of the vmmServer resource in which this resource resides.
        """
        pulumi.set(__self__, "extended_location", extended_location)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if inventory_item_id is not None:
            pulumi.set(__self__, "inventory_item_id", inventory_item_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)
        if virtual_network_name is not None:
            pulumi.set(__self__, "virtual_network_name", virtual_network_name)
        if vmm_server_id is not None:
            pulumi.set(__self__, "vmm_server_id", vmm_server_id)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input['ExtendedLocationArgs']:
        """
        The extended location.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: pulumi.Input['ExtendedLocationArgs']):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the inventory Item ID for the resource.
        """
        return pulumi.get(self, "inventory_item_id")

    @inventory_item_id.setter
    def inventory_item_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "inventory_item_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[str]]:
        """
        Unique ID of the virtual network.
        """
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uuid", value)

    @property
    @pulumi.getter(name="virtualNetworkName")
    def virtual_network_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the VirtualNetwork.
        """
        return pulumi.get(self, "virtual_network_name")

    @virtual_network_name.setter
    def virtual_network_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_network_name", value)

    @property
    @pulumi.getter(name="vmmServerId")
    def vmm_server_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM Id of the vmmServer resource in which this resource resides.
        """
        return pulumi.get(self, "vmm_server_id")

    @vmm_server_id.setter
    def vmm_server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vmm_server_id", value)


class VirtualNetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 inventory_item_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 uuid: Optional[pulumi.Input[str]] = None,
                 virtual_network_name: Optional[pulumi.Input[str]] = None,
                 vmm_server_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The VirtualNetworks resource definition.
        Azure REST API version: 2022-05-21-preview. Prior API version in Azure Native 1.x: 2020-06-05-preview.

        Other available API versions: 2023-04-01-preview, 2023-10-07, 2024-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']] extended_location: The extended location.
        :param pulumi.Input[str] inventory_item_id: Gets or sets the inventory Item ID for the resource.
        :param pulumi.Input[str] location: Gets or sets the location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] uuid: Unique ID of the virtual network.
        :param pulumi.Input[str] virtual_network_name: Name of the VirtualNetwork.
        :param pulumi.Input[str] vmm_server_id: ARM Id of the vmmServer resource in which this resource resides.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualNetworkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The VirtualNetworks resource definition.
        Azure REST API version: 2022-05-21-preview. Prior API version in Azure Native 1.x: 2020-06-05-preview.

        Other available API versions: 2023-04-01-preview, 2023-10-07, 2024-06-01.

        :param str resource_name: The name of the resource.
        :param VirtualNetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualNetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 inventory_item_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 uuid: Optional[pulumi.Input[str]] = None,
                 virtual_network_name: Optional[pulumi.Input[str]] = None,
                 vmm_server_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualNetworkArgs.__new__(VirtualNetworkArgs)

            if extended_location is None and not opts.urn:
                raise TypeError("Missing required property 'extended_location'")
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["inventory_item_id"] = inventory_item_id
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["uuid"] = uuid
            __props__.__dict__["virtual_network_name"] = virtual_network_name
            __props__.__dict__["vmm_server_id"] = vmm_server_id
            __props__.__dict__["name"] = None
            __props__.__dict__["network_name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:scvmm/v20200605preview:VirtualNetwork"), pulumi.Alias(type_="azure-native:scvmm/v20220521preview:VirtualNetwork"), pulumi.Alias(type_="azure-native:scvmm/v20230401preview:VirtualNetwork"), pulumi.Alias(type_="azure-native:scvmm/v20231007:VirtualNetwork"), pulumi.Alias(type_="azure-native:scvmm/v20240601:VirtualNetwork")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualNetwork, __self__).__init__(
            'azure-native:scvmm:VirtualNetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualNetwork':
        """
        Get an existing VirtualNetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualNetworkArgs.__new__(VirtualNetworkArgs)

        __props__.__dict__["extended_location"] = None
        __props__.__dict__["inventory_item_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["uuid"] = None
        __props__.__dict__["vmm_server_id"] = None
        return VirtualNetwork(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output['outputs.ExtendedLocationResponse']:
        """
        The extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="inventoryItemId")
    def inventory_item_id(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the inventory Item ID for the resource.
        """
        return pulumi.get(self, "inventory_item_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Gets or sets the location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkName")
    def network_name(self) -> pulumi.Output[str]:
        """
        Name of the virtual network in vmmServer.
        """
        return pulumi.get(self, "network_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets or sets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource Type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[Optional[str]]:
        """
        Unique ID of the virtual network.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter(name="vmmServerId")
    def vmm_server_id(self) -> pulumi.Output[Optional[str]]:
        """
        ARM Id of the vmmServer resource in which this resource resides.
        """
        return pulumi.get(self, "vmm_server_id")

