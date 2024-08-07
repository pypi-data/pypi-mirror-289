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
from ._inputs import *

__all__ = ['RoleDefinitionArgs', 'RoleDefinition']

@pulumi.input_type
class RoleDefinitionArgs:
    def __init__(__self__, *,
                 scope: pulumi.Input[str],
                 assignable_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['PermissionArgs']]]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 role_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RoleDefinition resource.
        :param pulumi.Input[str] scope: The scope of the operation or resource. Valid scopes are: subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
        :param pulumi.Input[Sequence[pulumi.Input[str]]] assignable_scopes: Role definition assignable scopes.
        :param pulumi.Input[str] description: The role definition description.
        :param pulumi.Input[Sequence[pulumi.Input['PermissionArgs']]] permissions: Role definition permissions.
        :param pulumi.Input[str] role_definition_id: The ID of the role definition.
        :param pulumi.Input[str] role_name: The role name.
        :param pulumi.Input[str] role_type: The role type.
        """
        pulumi.set(__self__, "scope", scope)
        if assignable_scopes is not None:
            pulumi.set(__self__, "assignable_scopes", assignable_scopes)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if role_definition_id is not None:
            pulumi.set(__self__, "role_definition_id", role_definition_id)
        if role_name is not None:
            pulumi.set(__self__, "role_name", role_name)
        if role_type is not None:
            pulumi.set(__self__, "role_type", role_type)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope of the operation or resource. Valid scopes are: subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="assignableScopes")
    def assignable_scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Role definition assignable scopes.
        """
        return pulumi.get(self, "assignable_scopes")

    @assignable_scopes.setter
    def assignable_scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "assignable_scopes", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The role definition description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PermissionArgs']]]]:
        """
        Role definition permissions.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PermissionArgs']]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="roleDefinitionId")
    def role_definition_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the role definition.
        """
        return pulumi.get(self, "role_definition_id")

    @role_definition_id.setter
    def role_definition_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_definition_id", value)

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> Optional[pulumi.Input[str]]:
        """
        The role name.
        """
        return pulumi.get(self, "role_name")

    @role_name.setter
    def role_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_name", value)

    @property
    @pulumi.getter(name="roleType")
    def role_type(self) -> Optional[pulumi.Input[str]]:
        """
        The role type.
        """
        return pulumi.get(self, "role_type")

    @role_type.setter
    def role_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_type", value)


class RoleDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignable_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PermissionArgs', 'PermissionArgsDict']]]]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 role_type: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Role definition.
        Azure REST API version: 2022-05-01-preview. Prior API version in Azure Native 1.x: 2018-01-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] assignable_scopes: Role definition assignable scopes.
        :param pulumi.Input[str] description: The role definition description.
        :param pulumi.Input[Sequence[pulumi.Input[Union['PermissionArgs', 'PermissionArgsDict']]]] permissions: Role definition permissions.
        :param pulumi.Input[str] role_definition_id: The ID of the role definition.
        :param pulumi.Input[str] role_name: The role name.
        :param pulumi.Input[str] role_type: The role type.
        :param pulumi.Input[str] scope: The scope of the operation or resource. Valid scopes are: subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}', or resource (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/[{parentResourcePath}/]{resourceType}/{resourceName}'
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoleDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Role definition.
        Azure REST API version: 2022-05-01-preview. Prior API version in Azure Native 1.x: 2018-01-01-preview.

        :param str resource_name: The name of the resource.
        :param RoleDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoleDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignable_scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PermissionArgs', 'PermissionArgsDict']]]]] = None,
                 role_definition_id: Optional[pulumi.Input[str]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 role_type: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RoleDefinitionArgs.__new__(RoleDefinitionArgs)

            __props__.__dict__["assignable_scopes"] = assignable_scopes
            __props__.__dict__["description"] = description
            __props__.__dict__["permissions"] = permissions
            __props__.__dict__["role_definition_id"] = role_definition_id
            __props__.__dict__["role_name"] = role_name
            __props__.__dict__["role_type"] = role_type
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["created_by"] = None
            __props__.__dict__["created_on"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_by"] = None
            __props__.__dict__["updated_on"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:authorization/v20150701:RoleDefinition"), pulumi.Alias(type_="azure-native:authorization/v20180101preview:RoleDefinition"), pulumi.Alias(type_="azure-native:authorization/v20220401:RoleDefinition"), pulumi.Alias(type_="azure-native:authorization/v20220501preview:RoleDefinition")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RoleDefinition, __self__).__init__(
            'azure-native:authorization:RoleDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RoleDefinition':
        """
        Get an existing RoleDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RoleDefinitionArgs.__new__(RoleDefinitionArgs)

        __props__.__dict__["assignable_scopes"] = None
        __props__.__dict__["created_by"] = None
        __props__.__dict__["created_on"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["permissions"] = None
        __props__.__dict__["role_name"] = None
        __props__.__dict__["role_type"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_by"] = None
        __props__.__dict__["updated_on"] = None
        return RoleDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assignableScopes")
    def assignable_scopes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Role definition assignable scopes.
        """
        return pulumi.get(self, "assignable_scopes")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[str]:
        """
        Id of the user who created the assignment
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[str]:
        """
        Time it was created
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The role definition description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The role definition name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Sequence['outputs.PermissionResponse']]]:
        """
        Role definition permissions.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Output[Optional[str]]:
        """
        The role name.
        """
        return pulumi.get(self, "role_name")

    @property
    @pulumi.getter(name="roleType")
    def role_type(self) -> pulumi.Output[Optional[str]]:
        """
        The role type.
        """
        return pulumi.get(self, "role_type")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The role definition type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Output[str]:
        """
        Id of the user who updated the assignment
        """
        return pulumi.get(self, "updated_by")

    @property
    @pulumi.getter(name="updatedOn")
    def updated_on(self) -> pulumi.Output[str]:
        """
        Time it was updated
        """
        return pulumi.get(self, "updated_on")

