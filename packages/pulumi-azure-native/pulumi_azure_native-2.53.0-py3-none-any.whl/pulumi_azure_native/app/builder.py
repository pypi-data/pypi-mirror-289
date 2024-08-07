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

__all__ = ['BuilderArgs', 'Builder']

@pulumi.input_type
class BuilderArgs:
    def __init__(__self__, *,
                 environment_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 builder_name: Optional[pulumi.Input[str]] = None,
                 container_registries: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerRegistryArgs']]]] = None,
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Builder resource.
        :param pulumi.Input[str] environment_id: Resource ID of the container apps environment that the builder is associated with.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] builder_name: The name of the builder.
        :param pulumi.Input[Sequence[pulumi.Input['ContainerRegistryArgs']]] container_registries: List of mappings of container registries and the managed identity used to connect to it.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: The managed service identities assigned to this resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "environment_id", environment_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if builder_name is not None:
            pulumi.set(__self__, "builder_name", builder_name)
        if container_registries is not None:
            pulumi.set(__self__, "container_registries", container_registries)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Input[str]:
        """
        Resource ID of the container apps environment that the builder is associated with.
        """
        return pulumi.get(self, "environment_id")

    @environment_id.setter
    def environment_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_id", value)

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
    @pulumi.getter(name="builderName")
    def builder_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the builder.
        """
        return pulumi.get(self, "builder_name")

    @builder_name.setter
    def builder_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "builder_name", value)

    @property
    @pulumi.getter(name="containerRegistries")
    def container_registries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContainerRegistryArgs']]]]:
        """
        List of mappings of container registries and the managed identity used to connect to it.
        """
        return pulumi.get(self, "container_registries")

    @container_registries.setter
    def container_registries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerRegistryArgs']]]]):
        pulumi.set(self, "container_registries", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        The managed service identities assigned to this resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Builder(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 builder_name: Optional[pulumi.Input[str]] = None,
                 container_registries: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ContainerRegistryArgs', 'ContainerRegistryArgsDict']]]]] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Information about the SourceToCloud builder resource.
        Azure REST API version: 2023-08-01-preview.

        Other available API versions: 2023-11-02-preview, 2024-02-02-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] builder_name: The name of the builder.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ContainerRegistryArgs', 'ContainerRegistryArgsDict']]]] container_registries: List of mappings of container registries and the managed identity used to connect to it.
        :param pulumi.Input[str] environment_id: Resource ID of the container apps environment that the builder is associated with.
        :param pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']] identity: The managed service identities assigned to this resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BuilderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Information about the SourceToCloud builder resource.
        Azure REST API version: 2023-08-01-preview.

        Other available API versions: 2023-11-02-preview, 2024-02-02-preview.

        :param str resource_name: The name of the resource.
        :param BuilderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BuilderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 builder_name: Optional[pulumi.Input[str]] = None,
                 container_registries: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ContainerRegistryArgs', 'ContainerRegistryArgsDict']]]]] = None,
                 environment_id: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BuilderArgs.__new__(BuilderArgs)

            __props__.__dict__["builder_name"] = builder_name
            __props__.__dict__["container_registries"] = container_registries
            if environment_id is None and not opts.urn:
                raise TypeError("Missing required property 'environment_id'")
            __props__.__dict__["environment_id"] = environment_id
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:app/v20230801preview:Builder"), pulumi.Alias(type_="azure-native:app/v20231102preview:Builder"), pulumi.Alias(type_="azure-native:app/v20240202preview:Builder")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Builder, __self__).__init__(
            'azure-native:app:Builder',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Builder':
        """
        Get an existing Builder resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BuilderArgs.__new__(BuilderArgs)

        __props__.__dict__["container_registries"] = None
        __props__.__dict__["environment_id"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Builder(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerRegistries")
    def container_registries(self) -> pulumi.Output[Optional[Sequence['outputs.ContainerRegistryResponse']]]:
        """
        List of mappings of container registries and the managed identity used to connect to it.
        """
        return pulumi.get(self, "container_registries")

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> pulumi.Output[str]:
        """
        Resource ID of the container apps environment that the builder is associated with.
        """
        return pulumi.get(self, "environment_id")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        The managed service identities assigned to this resource.
        """
        return pulumi.get(self, "identity")

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
        Provisioning state of a builder resource.
        """
        return pulumi.get(self, "provisioning_state")

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

