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

__all__ = ['GrafanaArgs', 'Grafana']

@pulumi.input_type
class GrafanaArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['ManagedGrafanaPropertiesArgs']] = None,
                 sku: Optional[pulumi.Input['ResourceSkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Grafana resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: The managed identity of the grafana resource.
        :param pulumi.Input[str] location: The geo-location where the grafana resource lives
        :param pulumi.Input['ManagedGrafanaPropertiesArgs'] properties: Properties specific to the grafana resource.
        :param pulumi.Input['ResourceSkuArgs'] sku: The Sku of the grafana resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags for grafana resource.
        :param pulumi.Input[str] workspace_name: The workspace name of Azure Managed Grafana.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if workspace_name is not None:
            pulumi.set(__self__, "workspace_name", workspace_name)

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
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        The managed identity of the grafana resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the grafana resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['ManagedGrafanaPropertiesArgs']]:
        """
        Properties specific to the grafana resource.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['ManagedGrafanaPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['ResourceSkuArgs']]:
        """
        The Sku of the grafana resource.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['ResourceSkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags for grafana resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The workspace name of Azure Managed Grafana.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_name", value)


class Grafana(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['ManagedGrafanaPropertiesArgs', 'ManagedGrafanaPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[Union['ResourceSkuArgs', 'ResourceSkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The grafana resource type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']] identity: The managed identity of the grafana resource.
        :param pulumi.Input[str] location: The geo-location where the grafana resource lives
        :param pulumi.Input[Union['ManagedGrafanaPropertiesArgs', 'ManagedGrafanaPropertiesArgsDict']] properties: Properties specific to the grafana resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union['ResourceSkuArgs', 'ResourceSkuArgsDict']] sku: The Sku of the grafana resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags for grafana resource.
        :param pulumi.Input[str] workspace_name: The workspace name of Azure Managed Grafana.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GrafanaArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The grafana resource type.

        :param str resource_name: The name of the resource.
        :param GrafanaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GrafanaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['ManagedGrafanaPropertiesArgs', 'ManagedGrafanaPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[Union['ResourceSkuArgs', 'ResourceSkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GrafanaArgs.__new__(GrafanaArgs)

            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:dashboard:Grafana"), pulumi.Alias(type_="azure-native:dashboard/v20210901preview:Grafana"), pulumi.Alias(type_="azure-native:dashboard/v20220501preview:Grafana"), pulumi.Alias(type_="azure-native:dashboard/v20220801:Grafana"), pulumi.Alias(type_="azure-native:dashboard/v20221001preview:Grafana")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Grafana, __self__).__init__(
            'azure-native:dashboard/v20230901:Grafana',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Grafana':
        """
        Get an existing Grafana resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GrafanaArgs.__new__(GrafanaArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Grafana(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        The managed identity of the grafana resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The geo-location where the grafana resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the grafana resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.ManagedGrafanaPropertiesResponse']:
        """
        Properties specific to the grafana resource.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.ResourceSkuResponse']]:
        """
        The Sku of the grafana resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system meta data relating to this grafana resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags for grafana resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the grafana resource.
        """
        return pulumi.get(self, "type")

