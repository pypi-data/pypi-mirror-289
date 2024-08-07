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

__all__ = ['AzureBareMetalStorageInstanceArgs', 'AzureBareMetalStorageInstance']

@pulumi.input_type
class AzureBareMetalStorageInstanceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 azure_bare_metal_storage_instance_name: Optional[pulumi.Input[str]] = None,
                 azure_bare_metal_storage_instance_unique_identifier: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['AzureBareMetalStorageInstanceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 storage_properties: Optional[pulumi.Input['StoragePropertiesArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AzureBareMetalStorageInstance resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] azure_bare_metal_storage_instance_name: Name of the Azure Bare Metal Storage Instance, also known as the ResourceName.
        :param pulumi.Input[str] azure_bare_metal_storage_instance_unique_identifier: Specifies the AzureBareMetaStorageInstance unique ID.
        :param pulumi.Input['AzureBareMetalStorageInstanceIdentityArgs'] identity: The identity of Azure Bare Metal Storage Instance, if configured.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['StoragePropertiesArgs'] storage_properties: Specifies the storage properties for the AzureBareMetalStorage instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if azure_bare_metal_storage_instance_name is not None:
            pulumi.set(__self__, "azure_bare_metal_storage_instance_name", azure_bare_metal_storage_instance_name)
        if azure_bare_metal_storage_instance_unique_identifier is not None:
            pulumi.set(__self__, "azure_bare_metal_storage_instance_unique_identifier", azure_bare_metal_storage_instance_unique_identifier)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if storage_properties is not None:
            pulumi.set(__self__, "storage_properties", storage_properties)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="azureBareMetalStorageInstanceName")
    def azure_bare_metal_storage_instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Azure Bare Metal Storage Instance, also known as the ResourceName.
        """
        return pulumi.get(self, "azure_bare_metal_storage_instance_name")

    @azure_bare_metal_storage_instance_name.setter
    def azure_bare_metal_storage_instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_bare_metal_storage_instance_name", value)

    @property
    @pulumi.getter(name="azureBareMetalStorageInstanceUniqueIdentifier")
    def azure_bare_metal_storage_instance_unique_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the AzureBareMetaStorageInstance unique ID.
        """
        return pulumi.get(self, "azure_bare_metal_storage_instance_unique_identifier")

    @azure_bare_metal_storage_instance_unique_identifier.setter
    def azure_bare_metal_storage_instance_unique_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "azure_bare_metal_storage_instance_unique_identifier", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['AzureBareMetalStorageInstanceIdentityArgs']]:
        """
        The identity of Azure Bare Metal Storage Instance, if configured.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['AzureBareMetalStorageInstanceIdentityArgs']]):
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
    @pulumi.getter(name="storageProperties")
    def storage_properties(self) -> Optional[pulumi.Input['StoragePropertiesArgs']]:
        """
        Specifies the storage properties for the AzureBareMetalStorage instance.
        """
        return pulumi.get(self, "storage_properties")

    @storage_properties.setter
    def storage_properties(self, value: Optional[pulumi.Input['StoragePropertiesArgs']]):
        pulumi.set(self, "storage_properties", value)

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


class AzureBareMetalStorageInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_bare_metal_storage_instance_name: Optional[pulumi.Input[str]] = None,
                 azure_bare_metal_storage_instance_unique_identifier: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['AzureBareMetalStorageInstanceIdentityArgs', 'AzureBareMetalStorageInstanceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_properties: Optional[pulumi.Input[Union['StoragePropertiesArgs', 'StoragePropertiesArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        AzureBareMetalStorageInstance info on Azure (ARM properties and AzureBareMetalStorage properties)

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] azure_bare_metal_storage_instance_name: Name of the Azure Bare Metal Storage Instance, also known as the ResourceName.
        :param pulumi.Input[str] azure_bare_metal_storage_instance_unique_identifier: Specifies the AzureBareMetaStorageInstance unique ID.
        :param pulumi.Input[Union['AzureBareMetalStorageInstanceIdentityArgs', 'AzureBareMetalStorageInstanceIdentityArgsDict']] identity: The identity of Azure Bare Metal Storage Instance, if configured.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union['StoragePropertiesArgs', 'StoragePropertiesArgsDict']] storage_properties: Specifies the storage properties for the AzureBareMetalStorage instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AzureBareMetalStorageInstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        AzureBareMetalStorageInstance info on Azure (ARM properties and AzureBareMetalStorage properties)

        :param str resource_name: The name of the resource.
        :param AzureBareMetalStorageInstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AzureBareMetalStorageInstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_bare_metal_storage_instance_name: Optional[pulumi.Input[str]] = None,
                 azure_bare_metal_storage_instance_unique_identifier: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['AzureBareMetalStorageInstanceIdentityArgs', 'AzureBareMetalStorageInstanceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_properties: Optional[pulumi.Input[Union['StoragePropertiesArgs', 'StoragePropertiesArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AzureBareMetalStorageInstanceArgs.__new__(AzureBareMetalStorageInstanceArgs)

            __props__.__dict__["azure_bare_metal_storage_instance_name"] = azure_bare_metal_storage_instance_name
            __props__.__dict__["azure_bare_metal_storage_instance_unique_identifier"] = azure_bare_metal_storage_instance_unique_identifier
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["storage_properties"] = storage_properties
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:baremetalinfrastructure:AzureBareMetalStorageInstance"), pulumi.Alias(type_="azure-native:baremetalinfrastructure/v20230406:AzureBareMetalStorageInstance"), pulumi.Alias(type_="azure-native:baremetalinfrastructure/v20230804preview:AzureBareMetalStorageInstance")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AzureBareMetalStorageInstance, __self__).__init__(
            'azure-native:baremetalinfrastructure/v20231101preview:AzureBareMetalStorageInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AzureBareMetalStorageInstance':
        """
        Get an existing AzureBareMetalStorageInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AzureBareMetalStorageInstanceArgs.__new__(AzureBareMetalStorageInstanceArgs)

        __props__.__dict__["azure_bare_metal_storage_instance_unique_identifier"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["storage_properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return AzureBareMetalStorageInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureBareMetalStorageInstanceUniqueIdentifier")
    def azure_bare_metal_storage_instance_unique_identifier(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the AzureBareMetaStorageInstance unique ID.
        """
        return pulumi.get(self, "azure_bare_metal_storage_instance_unique_identifier")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.AzureBareMetalStorageInstanceIdentityResponse']]:
        """
        The identity of Azure Bare Metal Storage Instance, if configured.
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
    @pulumi.getter(name="storageProperties")
    def storage_properties(self) -> pulumi.Output[Optional['outputs.StoragePropertiesResponse']]:
        """
        Specifies the storage properties for the AzureBareMetalStorage instance.
        """
        return pulumi.get(self, "storage_properties")

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

