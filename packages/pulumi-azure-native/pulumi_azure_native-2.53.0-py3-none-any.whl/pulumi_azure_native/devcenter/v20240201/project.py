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

__all__ = ['ProjectArgs', 'Project']

@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 catalog_settings: Optional[pulumi.Input['ProjectCatalogSettingsArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dev_center_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_dev_boxes_per_user: Optional[pulumi.Input[int]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Project resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['ProjectCatalogSettingsArgs'] catalog_settings: Settings to be used when associating a project with a catalog.
        :param pulumi.Input[str] description: Description of the project.
        :param pulumi.Input[str] dev_center_id: Resource Id of an associated DevCenter
        :param pulumi.Input[str] display_name: The display name of the project.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: Managed identity properties
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[int] max_dev_boxes_per_user: When specified, limits the maximum number of Dev Boxes a single user can create across all pools in the project. This will have no effect on existing Dev Boxes when reduced.
        :param pulumi.Input[str] project_name: The name of the project.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if catalog_settings is not None:
            pulumi.set(__self__, "catalog_settings", catalog_settings)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dev_center_id is not None:
            pulumi.set(__self__, "dev_center_id", dev_center_id)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if max_dev_boxes_per_user is not None:
            pulumi.set(__self__, "max_dev_boxes_per_user", max_dev_boxes_per_user)
        if project_name is not None:
            pulumi.set(__self__, "project_name", project_name)
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
    @pulumi.getter(name="catalogSettings")
    def catalog_settings(self) -> Optional[pulumi.Input['ProjectCatalogSettingsArgs']]:
        """
        Settings to be used when associating a project with a catalog.
        """
        return pulumi.get(self, "catalog_settings")

    @catalog_settings.setter
    def catalog_settings(self, value: Optional[pulumi.Input['ProjectCatalogSettingsArgs']]):
        pulumi.set(self, "catalog_settings", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the project.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="devCenterId")
    def dev_center_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id of an associated DevCenter
        """
        return pulumi.get(self, "dev_center_id")

    @dev_center_id.setter
    def dev_center_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dev_center_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the project.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        Managed identity properties
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
    @pulumi.getter(name="maxDevBoxesPerUser")
    def max_dev_boxes_per_user(self) -> Optional[pulumi.Input[int]]:
        """
        When specified, limits the maximum number of Dev Boxes a single user can create across all pools in the project. This will have no effect on existing Dev Boxes when reduced.
        """
        return pulumi.get(self, "max_dev_boxes_per_user")

    @max_dev_boxes_per_user.setter
    def max_dev_boxes_per_user(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_dev_boxes_per_user", value)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the project.
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_name", value)

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


class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_settings: Optional[pulumi.Input[Union['ProjectCatalogSettingsArgs', 'ProjectCatalogSettingsArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dev_center_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_dev_boxes_per_user: Optional[pulumi.Input[int]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Represents a project resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ProjectCatalogSettingsArgs', 'ProjectCatalogSettingsArgsDict']] catalog_settings: Settings to be used when associating a project with a catalog.
        :param pulumi.Input[str] description: Description of the project.
        :param pulumi.Input[str] dev_center_id: Resource Id of an associated DevCenter
        :param pulumi.Input[str] display_name: The display name of the project.
        :param pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']] identity: Managed identity properties
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[int] max_dev_boxes_per_user: When specified, limits the maximum number of Dev Boxes a single user can create across all pools in the project. This will have no effect on existing Dev Boxes when reduced.
        :param pulumi.Input[str] project_name: The name of the project.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a project resource.

        :param str resource_name: The name of the resource.
        :param ProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_settings: Optional[pulumi.Input[Union['ProjectCatalogSettingsArgs', 'ProjectCatalogSettingsArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dev_center_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_dev_boxes_per_user: Optional[pulumi.Input[int]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectArgs.__new__(ProjectArgs)

            __props__.__dict__["catalog_settings"] = catalog_settings
            __props__.__dict__["description"] = description
            __props__.__dict__["dev_center_id"] = dev_center_id
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["max_dev_boxes_per_user"] = max_dev_boxes_per_user
            __props__.__dict__["project_name"] = project_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["dev_center_uri"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devcenter:Project"), pulumi.Alias(type_="azure-native:devcenter/v20220801preview:Project"), pulumi.Alias(type_="azure-native:devcenter/v20220901preview:Project"), pulumi.Alias(type_="azure-native:devcenter/v20221012preview:Project"), pulumi.Alias(type_="azure-native:devcenter/v20221111preview:Project"), pulumi.Alias(type_="azure-native:devcenter/v20230101preview:Project"), pulumi.Alias(type_="azure-native:devcenter/v20230401:Project"), pulumi.Alias(type_="azure-native:devcenter/v20230801preview:Project"), pulumi.Alias(type_="azure-native:devcenter/v20231001preview:Project"), pulumi.Alias(type_="azure-native:devcenter/v20240501preview:Project"), pulumi.Alias(type_="azure-native:devcenter/v20240601preview:Project"), pulumi.Alias(type_="azure-native:devcenter/v20240701preview:Project")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Project, __self__).__init__(
            'azure-native:devcenter/v20240201:Project',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Project':
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProjectArgs.__new__(ProjectArgs)

        __props__.__dict__["catalog_settings"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["dev_center_id"] = None
        __props__.__dict__["dev_center_uri"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["max_dev_boxes_per_user"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Project(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="catalogSettings")
    def catalog_settings(self) -> pulumi.Output[Optional['outputs.ProjectCatalogSettingsResponse']]:
        """
        Settings to be used when associating a project with a catalog.
        """
        return pulumi.get(self, "catalog_settings")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the project.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="devCenterId")
    def dev_center_id(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Id of an associated DevCenter
        """
        return pulumi.get(self, "dev_center_id")

    @property
    @pulumi.getter(name="devCenterUri")
    def dev_center_uri(self) -> pulumi.Output[str]:
        """
        The URI of the Dev Center resource this project is associated with.
        """
        return pulumi.get(self, "dev_center_uri")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the project.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        Managed identity properties
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
    @pulumi.getter(name="maxDevBoxesPerUser")
    def max_dev_boxes_per_user(self) -> pulumi.Output[Optional[int]]:
        """
        When specified, limits the maximum number of Dev Boxes a single user can create across all pools in the project. This will have no effect on existing Dev Boxes when reduced.
        """
        return pulumi.get(self, "max_dev_boxes_per_user")

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
        The provisioning state of the resource.
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

