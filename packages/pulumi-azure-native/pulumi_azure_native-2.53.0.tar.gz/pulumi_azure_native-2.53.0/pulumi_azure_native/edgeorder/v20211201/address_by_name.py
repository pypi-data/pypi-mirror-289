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

__all__ = ['AddressByNameArgs', 'AddressByName']

@pulumi.input_type
class AddressByNameArgs:
    def __init__(__self__, *,
                 contact_details: pulumi.Input['ContactDetailsArgs'],
                 resource_group_name: pulumi.Input[str],
                 address_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 shipping_address: Optional[pulumi.Input['ShippingAddressArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AddressByName resource.
        :param pulumi.Input['ContactDetailsArgs'] contact_details: Contact details for the address
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] address_name: The name of the address Resource within the specified resource group. address names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['ShippingAddressArgs'] shipping_address: Shipping details for the address
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "contact_details", contact_details)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if address_name is not None:
            pulumi.set(__self__, "address_name", address_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if shipping_address is not None:
            pulumi.set(__self__, "shipping_address", shipping_address)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> pulumi.Input['ContactDetailsArgs']:
        """
        Contact details for the address
        """
        return pulumi.get(self, "contact_details")

    @contact_details.setter
    def contact_details(self, value: pulumi.Input['ContactDetailsArgs']):
        pulumi.set(self, "contact_details", value)

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
    @pulumi.getter(name="addressName")
    def address_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the address Resource within the specified resource group. address names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
        """
        return pulumi.get(self, "address_name")

    @address_name.setter
    def address_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_name", value)

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
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[pulumi.Input['ShippingAddressArgs']]:
        """
        Shipping details for the address
        """
        return pulumi.get(self, "shipping_address")

    @shipping_address.setter
    def shipping_address(self, value: Optional[pulumi.Input['ShippingAddressArgs']]):
        pulumi.set(self, "shipping_address", value)

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


class AddressByName(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_name: Optional[pulumi.Input[str]] = None,
                 contact_details: Optional[pulumi.Input[Union['ContactDetailsArgs', 'ContactDetailsArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 shipping_address: Optional[pulumi.Input[Union['ShippingAddressArgs', 'ShippingAddressArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Address Resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_name: The name of the address Resource within the specified resource group. address names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
        :param pulumi.Input[Union['ContactDetailsArgs', 'ContactDetailsArgsDict']] contact_details: Contact details for the address
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union['ShippingAddressArgs', 'ShippingAddressArgsDict']] shipping_address: Shipping details for the address
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AddressByNameArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Address Resource.

        :param str resource_name: The name of the resource.
        :param AddressByNameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AddressByNameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_name: Optional[pulumi.Input[str]] = None,
                 contact_details: Optional[pulumi.Input[Union['ContactDetailsArgs', 'ContactDetailsArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 shipping_address: Optional[pulumi.Input[Union['ShippingAddressArgs', 'ShippingAddressArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AddressByNameArgs.__new__(AddressByNameArgs)

            __props__.__dict__["address_name"] = address_name
            if contact_details is None and not opts.urn:
                raise TypeError("Missing required property 'contact_details'")
            __props__.__dict__["contact_details"] = contact_details
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["shipping_address"] = shipping_address
            __props__.__dict__["tags"] = tags
            __props__.__dict__["address_validation_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:edgeorder:AddressByName"), pulumi.Alias(type_="azure-native:edgeorder/v20201201preview:AddressByName"), pulumi.Alias(type_="azure-native:edgeorder/v20220501preview:AddressByName"), pulumi.Alias(type_="azure-native:edgeorder/v20240201:AddressByName")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AddressByName, __self__).__init__(
            'azure-native:edgeorder/v20211201:AddressByName',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AddressByName':
        """
        Get an existing AddressByName resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AddressByNameArgs.__new__(AddressByNameArgs)

        __props__.__dict__["address_validation_status"] = None
        __props__.__dict__["contact_details"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["shipping_address"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return AddressByName(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressValidationStatus")
    def address_validation_status(self) -> pulumi.Output[str]:
        """
        Status of address validation
        """
        return pulumi.get(self, "address_validation_status")

    @property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> pulumi.Output['outputs.ContactDetailsResponse']:
        """
        Contact details for the address
        """
        return pulumi.get(self, "contact_details")

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
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> pulumi.Output[Optional['outputs.ShippingAddressResponse']]:
        """
        Shipping details for the address
        """
        return pulumi.get(self, "shipping_address")

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

