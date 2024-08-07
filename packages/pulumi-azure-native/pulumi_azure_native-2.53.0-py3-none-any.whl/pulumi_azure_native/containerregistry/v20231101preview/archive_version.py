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

__all__ = ['ArchiveVersionArgs', 'ArchiveVersion']

@pulumi.input_type
class ArchiveVersionArgs:
    def __init__(__self__, *,
                 archive_name: pulumi.Input[str],
                 package_type: pulumi.Input[str],
                 registry_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 archive_version_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ArchiveVersion resource.
        :param pulumi.Input[str] archive_name: The name of the archive resource.
        :param pulumi.Input[str] package_type: The type of the package resource.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] archive_version_name: The name of the archive version resource.
        """
        pulumi.set(__self__, "archive_name", archive_name)
        pulumi.set(__self__, "package_type", package_type)
        pulumi.set(__self__, "registry_name", registry_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if archive_version_name is not None:
            pulumi.set(__self__, "archive_version_name", archive_version_name)

    @property
    @pulumi.getter(name="archiveName")
    def archive_name(self) -> pulumi.Input[str]:
        """
        The name of the archive resource.
        """
        return pulumi.get(self, "archive_name")

    @archive_name.setter
    def archive_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "archive_name", value)

    @property
    @pulumi.getter(name="packageType")
    def package_type(self) -> pulumi.Input[str]:
        """
        The type of the package resource.
        """
        return pulumi.get(self, "package_type")

    @package_type.setter
    def package_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "package_type", value)

    @property
    @pulumi.getter(name="registryName")
    def registry_name(self) -> pulumi.Input[str]:
        """
        The name of the container registry.
        """
        return pulumi.get(self, "registry_name")

    @registry_name.setter
    def registry_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "registry_name", value)

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
    @pulumi.getter(name="archiveVersionName")
    def archive_version_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the archive version resource.
        """
        return pulumi.get(self, "archive_version_name")

    @archive_version_name.setter
    def archive_version_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "archive_version_name", value)


class ArchiveVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 archive_name: Optional[pulumi.Input[str]] = None,
                 archive_version_name: Optional[pulumi.Input[str]] = None,
                 package_type: Optional[pulumi.Input[str]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An object that represents an export pipeline for a container registry.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] archive_name: The name of the archive resource.
        :param pulumi.Input[str] archive_version_name: The name of the archive version resource.
        :param pulumi.Input[str] package_type: The type of the package resource.
        :param pulumi.Input[str] registry_name: The name of the container registry.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ArchiveVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An object that represents an export pipeline for a container registry.

        :param str resource_name: The name of the resource.
        :param ArchiveVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ArchiveVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 archive_name: Optional[pulumi.Input[str]] = None,
                 archive_version_name: Optional[pulumi.Input[str]] = None,
                 package_type: Optional[pulumi.Input[str]] = None,
                 registry_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ArchiveVersionArgs.__new__(ArchiveVersionArgs)

            if archive_name is None and not opts.urn:
                raise TypeError("Missing required property 'archive_name'")
            __props__.__dict__["archive_name"] = archive_name
            __props__.__dict__["archive_version_name"] = archive_version_name
            if package_type is None and not opts.urn:
                raise TypeError("Missing required property 'package_type'")
            __props__.__dict__["package_type"] = package_type
            if registry_name is None and not opts.urn:
                raise TypeError("Missing required property 'registry_name'")
            __props__.__dict__["registry_name"] = registry_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["archive_version_error_message"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerregistry:ArchiveVersion"), pulumi.Alias(type_="azure-native:containerregistry/v20230601preview:ArchiveVersion"), pulumi.Alias(type_="azure-native:containerregistry/v20230801preview:ArchiveVersion")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ArchiveVersion, __self__).__init__(
            'azure-native:containerregistry/v20231101preview:ArchiveVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ArchiveVersion':
        """
        Get an existing ArchiveVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ArchiveVersionArgs.__new__(ArchiveVersionArgs)

        __props__.__dict__["archive_version_error_message"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ArchiveVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="archiveVersionErrorMessage")
    def archive_version_error_message(self) -> pulumi.Output[Optional[str]]:
        """
        The detailed error message for the archive version in the case of failure.
        """
        return pulumi.get(self, "archive_version_error_message")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the archive at the time the operation was called.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

