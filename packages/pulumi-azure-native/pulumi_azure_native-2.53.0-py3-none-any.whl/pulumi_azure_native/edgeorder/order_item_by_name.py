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
from ._enums import *
from ._inputs import *

__all__ = ['OrderItemByNameArgs', 'OrderItemByName']

@pulumi.input_type
class OrderItemByNameArgs:
    def __init__(__self__, *,
                 address_details: pulumi.Input['AddressDetailsArgs'],
                 order_id: pulumi.Input[str],
                 order_item_details: pulumi.Input['OrderItemDetailsArgs'],
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 order_item_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a OrderItemByName resource.
        :param pulumi.Input['AddressDetailsArgs'] address_details: Represents shipping and return address for order item
        :param pulumi.Input[str] order_id: Id of the order to which order item belongs to
        :param pulumi.Input['OrderItemDetailsArgs'] order_item_details: Represents order item details.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] order_item_name: The name of the order item
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "address_details", address_details)
        pulumi.set(__self__, "order_id", order_id)
        pulumi.set(__self__, "order_item_details", order_item_details)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if order_item_name is not None:
            pulumi.set(__self__, "order_item_name", order_item_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="addressDetails")
    def address_details(self) -> pulumi.Input['AddressDetailsArgs']:
        """
        Represents shipping and return address for order item
        """
        return pulumi.get(self, "address_details")

    @address_details.setter
    def address_details(self, value: pulumi.Input['AddressDetailsArgs']):
        pulumi.set(self, "address_details", value)

    @property
    @pulumi.getter(name="orderId")
    def order_id(self) -> pulumi.Input[str]:
        """
        Id of the order to which order item belongs to
        """
        return pulumi.get(self, "order_id")

    @order_id.setter
    def order_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "order_id", value)

    @property
    @pulumi.getter(name="orderItemDetails")
    def order_item_details(self) -> pulumi.Input['OrderItemDetailsArgs']:
        """
        Represents order item details.
        """
        return pulumi.get(self, "order_item_details")

    @order_item_details.setter
    def order_item_details(self, value: pulumi.Input['OrderItemDetailsArgs']):
        pulumi.set(self, "order_item_details", value)

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
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="orderItemName")
    def order_item_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the order item
        """
        return pulumi.get(self, "order_item_name")

    @order_item_name.setter
    def order_item_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "order_item_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class OrderItemByName(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_details: Optional[pulumi.Input[Union['AddressDetailsArgs', 'AddressDetailsArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 order_id: Optional[pulumi.Input[str]] = None,
                 order_item_details: Optional[pulumi.Input[Union['OrderItemDetailsArgs', 'OrderItemDetailsArgsDict']]] = None,
                 order_item_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Represents order item contract
        Azure REST API version: 2021-12-01. Prior API version in Azure Native 1.x: 2021-12-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['AddressDetailsArgs', 'AddressDetailsArgsDict']] address_details: Represents shipping and return address for order item
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] order_id: Id of the order to which order item belongs to
        :param pulumi.Input[Union['OrderItemDetailsArgs', 'OrderItemDetailsArgsDict']] order_item_details: Represents order item details.
        :param pulumi.Input[str] order_item_name: The name of the order item
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrderItemByNameArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents order item contract
        Azure REST API version: 2021-12-01. Prior API version in Azure Native 1.x: 2021-12-01.

        :param str resource_name: The name of the resource.
        :param OrderItemByNameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrderItemByNameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_details: Optional[pulumi.Input[Union['AddressDetailsArgs', 'AddressDetailsArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 order_id: Optional[pulumi.Input[str]] = None,
                 order_item_details: Optional[pulumi.Input[Union['OrderItemDetailsArgs', 'OrderItemDetailsArgsDict']]] = None,
                 order_item_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OrderItemByNameArgs.__new__(OrderItemByNameArgs)

            if address_details is None and not opts.urn:
                raise TypeError("Missing required property 'address_details'")
            __props__.__dict__["address_details"] = address_details
            __props__.__dict__["location"] = location
            if order_id is None and not opts.urn:
                raise TypeError("Missing required property 'order_id'")
            __props__.__dict__["order_id"] = order_id
            if order_item_details is None and not opts.urn:
                raise TypeError("Missing required property 'order_item_details'")
            __props__.__dict__["order_item_details"] = order_item_details
            __props__.__dict__["order_item_name"] = order_item_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["start_time"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:edgeorder/v20201201preview:OrderItemByName"), pulumi.Alias(type_="azure-native:edgeorder/v20211201:OrderItemByName"), pulumi.Alias(type_="azure-native:edgeorder/v20220501preview:OrderItemByName"), pulumi.Alias(type_="azure-native:edgeorder/v20240201:OrderItemByName")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(OrderItemByName, __self__).__init__(
            'azure-native:edgeorder:OrderItemByName',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'OrderItemByName':
        """
        Get an existing OrderItemByName resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrderItemByNameArgs.__new__(OrderItemByNameArgs)

        __props__.__dict__["address_details"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["order_id"] = None
        __props__.__dict__["order_item_details"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return OrderItemByName(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressDetails")
    def address_details(self) -> pulumi.Output['outputs.AddressDetailsResponse']:
        """
        Represents shipping and return address for order item
        """
        return pulumi.get(self, "address_details")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orderId")
    def order_id(self) -> pulumi.Output[str]:
        """
        Id of the order to which order item belongs to
        """
        return pulumi.get(self, "order_id")

    @property
    @pulumi.getter(name="orderItemDetails")
    def order_item_details(self) -> pulumi.Output['outputs.OrderItemDetailsResponse']:
        """
        Represents order item details.
        """
        return pulumi.get(self, "order_item_details")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[str]:
        """
        Start time of order item
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Represents resource creation and update time
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

