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

__all__ = ['StoragecontainerRetrieveArgs', 'StoragecontainerRetrieve']

@pulumi.input_type
class StoragecontainerRetrieveArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 extended_location: Optional[pulumi.Input['StoragecontainersExtendedLocationArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 storagecontainers_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a StoragecontainerRetrieve resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] location: The resource location
        :param pulumi.Input[str] path: Path of the storage container on the disk
        :param pulumi.Input[str] resource_name: name of the object to be used in moc
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if storagecontainers_name is not None:
            pulumi.set(__self__, "storagecontainers_name", storagecontainers_name)
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
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['StoragecontainersExtendedLocationArgs']]:
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['StoragecontainersExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Path of the storage container on the disk
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        name of the object to be used in moc
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="storagecontainersName")
    def storagecontainers_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "storagecontainers_name")

    @storagecontainers_name.setter
    def storagecontainers_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storagecontainers_name", value)

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


class StoragecontainerRetrieve(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[Union['StoragecontainersExtendedLocationArgs', 'StoragecontainersExtendedLocationArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 storagecontainers_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The storage container resource definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: The resource location
        :param pulumi.Input[str] path: Path of the storage container on the disk
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: name of the object to be used in moc
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StoragecontainerRetrieveArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The storage container resource definition.

        :param str resource_name: The name of the resource.
        :param StoragecontainerRetrieveArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StoragecontainerRetrieveArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 extended_location: Optional[pulumi.Input[Union['StoragecontainersExtendedLocationArgs', 'StoragecontainersExtendedLocationArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 storagecontainers_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StoragecontainerRetrieveArgs.__new__(StoragecontainerRetrieveArgs)

            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["location"] = location
            __props__.__dict__["path"] = path
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["storagecontainers_name"] = storagecontainers_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["available_size_mb"] = None
            __props__.__dict__["container_size_mb"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestackhci/v20210901preview:storagecontainerRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci:StoragecontainerRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci:storagecontainerRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20221215preview:StoragecontainerRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20221215preview:storagecontainerRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20230701preview:StoragecontainerRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20230701preview:storagecontainerRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20230901preview:StoragecontainerRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20230901preview:storagecontainerRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20240101:StoragecontainerRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20240101:storagecontainerRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20240201preview:StoragecontainerRetrieve"), pulumi.Alias(type_="azure-native:azurestackhci/v20240201preview:storagecontainerRetrieve")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StoragecontainerRetrieve, __self__).__init__(
            'azure-native:azurestackhci/v20210901preview:StoragecontainerRetrieve',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StoragecontainerRetrieve':
        """
        Get an existing StoragecontainerRetrieve resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StoragecontainerRetrieveArgs.__new__(StoragecontainerRetrieveArgs)

        __props__.__dict__["available_size_mb"] = None
        __props__.__dict__["container_size_mb"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["path"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return StoragecontainerRetrieve(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="availableSizeMB")
    def available_size_mb(self) -> pulumi.Output[float]:
        """
        Amount of space available on the disk in MB
        """
        return pulumi.get(self, "available_size_mb")

    @property
    @pulumi.getter(name="containerSizeMB")
    def container_size_mb(self) -> pulumi.Output[float]:
        """
        Total size of the disk in MB
        """
        return pulumi.get(self, "container_size_mb")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.StoragecontainersResponseExtendedLocation']]:
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The resource location
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
    @pulumi.getter
    def path(self) -> pulumi.Output[Optional[str]]:
        """
        Path of the storage container on the disk
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Output[Optional[str]]:
        """
        name of the object to be used in moc
        """
        return pulumi.get(self, "resource_name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.StorageContainerStatusResponse']:
        """
        storageContainerStatus defines the observed state of storagecontainers
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
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

