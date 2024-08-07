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

__all__ = ['MigrateProjectsControllerMigrateProjectArgs', 'MigrateProjectsControllerMigrateProject']

@pulumi.input_type
class MigrateProjectsControllerMigrateProjectArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 e_tag: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 migrate_project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['MigrateProjectPropertiesArgs']] = None):
        """
        The set of arguments for constructing a MigrateProjectsControllerMigrateProject resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] e_tag: For optimistic concurrency control.
        :param pulumi.Input[str] location: Azure location in which project is created.
        :param pulumi.Input[str] migrate_project_name: Name of the Azure Migrate project.
        :param pulumi.Input['MigrateProjectPropertiesArgs'] properties: Properties of a migrate project.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if migrate_project_name is not None:
            pulumi.set(__self__, "migrate_project_name", migrate_project_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

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
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[str]]:
        """
        For optimistic concurrency control.
        """
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_tag", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Azure location in which project is created.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="migrateProjectName")
    def migrate_project_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Azure Migrate project.
        """
        return pulumi.get(self, "migrate_project_name")

    @migrate_project_name.setter
    def migrate_project_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "migrate_project_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['MigrateProjectPropertiesArgs']]:
        """
        Properties of a migrate project.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['MigrateProjectPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class MigrateProjectsControllerMigrateProject(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 migrate_project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['MigrateProjectPropertiesArgs', 'MigrateProjectPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Migrate project.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] e_tag: For optimistic concurrency control.
        :param pulumi.Input[str] location: Azure location in which project is created.
        :param pulumi.Input[str] migrate_project_name: Name of the Azure Migrate project.
        :param pulumi.Input[Union['MigrateProjectPropertiesArgs', 'MigrateProjectPropertiesArgsDict']] properties: Properties of a migrate project.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MigrateProjectsControllerMigrateProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Migrate project.

        :param str resource_name: The name of the resource.
        :param MigrateProjectsControllerMigrateProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MigrateProjectsControllerMigrateProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 migrate_project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['MigrateProjectPropertiesArgs', 'MigrateProjectPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MigrateProjectsControllerMigrateProjectArgs.__new__(MigrateProjectsControllerMigrateProjectArgs)

            __props__.__dict__["e_tag"] = e_tag
            __props__.__dict__["location"] = location
            __props__.__dict__["migrate_project_name"] = migrate_project_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:migrate:MigrateProjectsControllerMigrateProject"), pulumi.Alias(type_="azure-native:migrate/v20180901preview:MigrateProjectsControllerMigrateProject"), pulumi.Alias(type_="azure-native:migrate/v20200501:MigrateProjectsControllerMigrateProject")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(MigrateProjectsControllerMigrateProject, __self__).__init__(
            'azure-native:migrate/v20230101:MigrateProjectsControllerMigrateProject',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MigrateProjectsControllerMigrateProject':
        """
        Get an existing MigrateProjectsControllerMigrateProject resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MigrateProjectsControllerMigrateProjectArgs.__new__(MigrateProjectsControllerMigrateProjectArgs)

        __props__.__dict__["e_tag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return MigrateProjectsControllerMigrateProject(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        For optimistic concurrency control.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Azure location in which project is created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the project.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.MigrateProjectPropertiesResponse']:
        """
        Properties of a migrate project.
        """
        return pulumi.get(self, "properties")

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
        Type of the object = [Microsoft.Migrate/migrateProjects].
        """
        return pulumi.get(self, "type")

