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

__all__ = ['SliceArgs', 'Slice']

@pulumi.input_type
class SliceArgs:
    def __init__(__self__, *,
                 mobile_network_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 snssai: pulumi.Input['SnssaiArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 slice_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Slice resource.
        :param pulumi.Input[str] mobile_network_name: The name of the mobile network.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['SnssaiArgs'] snssai: Single-network slice selection assistance information (S-NSSAI). Unique at the scope of a mobile network.
        :param pulumi.Input[str] description: An optional description for this network slice.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] slice_name: The name of the network slice.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "mobile_network_name", mobile_network_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "snssai", snssai)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if slice_name is not None:
            pulumi.set(__self__, "slice_name", slice_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="mobileNetworkName")
    def mobile_network_name(self) -> pulumi.Input[str]:
        """
        The name of the mobile network.
        """
        return pulumi.get(self, "mobile_network_name")

    @mobile_network_name.setter
    def mobile_network_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "mobile_network_name", value)

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
    def snssai(self) -> pulumi.Input['SnssaiArgs']:
        """
        Single-network slice selection assistance information (S-NSSAI). Unique at the scope of a mobile network.
        """
        return pulumi.get(self, "snssai")

    @snssai.setter
    def snssai(self, value: pulumi.Input['SnssaiArgs']):
        pulumi.set(self, "snssai", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description for this network slice.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

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
    @pulumi.getter(name="sliceName")
    def slice_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network slice.
        """
        return pulumi.get(self, "slice_name")

    @slice_name.setter
    def slice_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slice_name", value)

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


class Slice(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mobile_network_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 slice_name: Optional[pulumi.Input[str]] = None,
                 snssai: Optional[pulumi.Input[Union['SnssaiArgs', 'SnssaiArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Network slice resource. Must be created in the same location as its parent mobile network.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: An optional description for this network slice.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] mobile_network_name: The name of the mobile network.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] slice_name: The name of the network slice.
        :param pulumi.Input[Union['SnssaiArgs', 'SnssaiArgsDict']] snssai: Single-network slice selection assistance information (S-NSSAI). Unique at the scope of a mobile network.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SliceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Network slice resource. Must be created in the same location as its parent mobile network.

        :param str resource_name: The name of the resource.
        :param SliceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SliceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mobile_network_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 slice_name: Optional[pulumi.Input[str]] = None,
                 snssai: Optional[pulumi.Input[Union['SnssaiArgs', 'SnssaiArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SliceArgs.__new__(SliceArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["location"] = location
            if mobile_network_name is None and not opts.urn:
                raise TypeError("Missing required property 'mobile_network_name'")
            __props__.__dict__["mobile_network_name"] = mobile_network_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["slice_name"] = slice_name
            if snssai is None and not opts.urn:
                raise TypeError("Missing required property 'snssai'")
            __props__.__dict__["snssai"] = snssai
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:mobilenetwork:Slice"), pulumi.Alias(type_="azure-native:mobilenetwork/v20220301preview:Slice"), pulumi.Alias(type_="azure-native:mobilenetwork/v20220401preview:Slice"), pulumi.Alias(type_="azure-native:mobilenetwork/v20221101:Slice"), pulumi.Alias(type_="azure-native:mobilenetwork/v20230601:Slice"), pulumi.Alias(type_="azure-native:mobilenetwork/v20230901:Slice"), pulumi.Alias(type_="azure-native:mobilenetwork/v20240401:Slice")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Slice, __self__).__init__(
            'azure-native:mobilenetwork/v20240201:Slice',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Slice':
        """
        Get an existing Slice resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SliceArgs.__new__(SliceArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["snssai"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Slice(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        An optional description for this network slice.
        """
        return pulumi.get(self, "description")

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the network slice resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def snssai(self) -> pulumi.Output['outputs.SnssaiResponse']:
        """
        Single-network slice selection assistance information (S-NSSAI). Unique at the scope of a mobile network.
        """
        return pulumi.get(self, "snssai")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
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

