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

__all__ = ['WorkspaceManagerMemberArgs', 'WorkspaceManagerMember']

@pulumi.input_type
class WorkspaceManagerMemberArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 target_workspace_resource_id: pulumi.Input[str],
                 target_workspace_tenant_id: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 workspace_manager_member_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkspaceManagerMember resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] target_workspace_resource_id: Fully qualified resource ID of the target Sentinel workspace joining the given Sentinel workspace manager
        :param pulumi.Input[str] target_workspace_tenant_id: Tenant id of the target Sentinel workspace joining the given Sentinel workspace manager
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] workspace_manager_member_name: The name of the workspace manager member
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "target_workspace_resource_id", target_workspace_resource_id)
        pulumi.set(__self__, "target_workspace_tenant_id", target_workspace_tenant_id)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if workspace_manager_member_name is not None:
            pulumi.set(__self__, "workspace_manager_member_name", workspace_manager_member_name)

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
    @pulumi.getter(name="targetWorkspaceResourceId")
    def target_workspace_resource_id(self) -> pulumi.Input[str]:
        """
        Fully qualified resource ID of the target Sentinel workspace joining the given Sentinel workspace manager
        """
        return pulumi.get(self, "target_workspace_resource_id")

    @target_workspace_resource_id.setter
    def target_workspace_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_workspace_resource_id", value)

    @property
    @pulumi.getter(name="targetWorkspaceTenantId")
    def target_workspace_tenant_id(self) -> pulumi.Input[str]:
        """
        Tenant id of the target Sentinel workspace joining the given Sentinel workspace manager
        """
        return pulumi.get(self, "target_workspace_tenant_id")

    @target_workspace_tenant_id.setter
    def target_workspace_tenant_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_workspace_tenant_id", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="workspaceManagerMemberName")
    def workspace_manager_member_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the workspace manager member
        """
        return pulumi.get(self, "workspace_manager_member_name")

    @workspace_manager_member_name.setter
    def workspace_manager_member_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_manager_member_name", value)


class WorkspaceManagerMember(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_workspace_resource_id: Optional[pulumi.Input[str]] = None,
                 target_workspace_tenant_id: Optional[pulumi.Input[str]] = None,
                 workspace_manager_member_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The workspace manager member

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] target_workspace_resource_id: Fully qualified resource ID of the target Sentinel workspace joining the given Sentinel workspace manager
        :param pulumi.Input[str] target_workspace_tenant_id: Tenant id of the target Sentinel workspace joining the given Sentinel workspace manager
        :param pulumi.Input[str] workspace_manager_member_name: The name of the workspace manager member
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceManagerMemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The workspace manager member

        :param str resource_name: The name of the resource.
        :param WorkspaceManagerMemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceManagerMemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_workspace_resource_id: Optional[pulumi.Input[str]] = None,
                 target_workspace_tenant_id: Optional[pulumi.Input[str]] = None,
                 workspace_manager_member_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceManagerMemberArgs.__new__(WorkspaceManagerMemberArgs)

            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if target_workspace_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_workspace_resource_id'")
            __props__.__dict__["target_workspace_resource_id"] = target_workspace_resource_id
            if target_workspace_tenant_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_workspace_tenant_id'")
            __props__.__dict__["target_workspace_tenant_id"] = target_workspace_tenant_id
            __props__.__dict__["workspace_manager_member_name"] = workspace_manager_member_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:WorkspaceManagerMember"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:WorkspaceManagerMember"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:WorkspaceManagerMember"), pulumi.Alias(type_="azure-native:securityinsights/v20230601preview:WorkspaceManagerMember"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:WorkspaceManagerMember"), pulumi.Alias(type_="azure-native:securityinsights/v20230901preview:WorkspaceManagerMember"), pulumi.Alias(type_="azure-native:securityinsights/v20231001preview:WorkspaceManagerMember"), pulumi.Alias(type_="azure-native:securityinsights/v20231201preview:WorkspaceManagerMember"), pulumi.Alias(type_="azure-native:securityinsights/v20240101preview:WorkspaceManagerMember")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkspaceManagerMember, __self__).__init__(
            'azure-native:securityinsights/v20230701preview:WorkspaceManagerMember',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkspaceManagerMember':
        """
        Get an existing WorkspaceManagerMember resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceManagerMemberArgs.__new__(WorkspaceManagerMemberArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["target_workspace_resource_id"] = None
        __props__.__dict__["target_workspace_tenant_id"] = None
        __props__.__dict__["type"] = None
        return WorkspaceManagerMember(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Resource Etag.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetWorkspaceResourceId")
    def target_workspace_resource_id(self) -> pulumi.Output[str]:
        """
        Fully qualified resource ID of the target Sentinel workspace joining the given Sentinel workspace manager
        """
        return pulumi.get(self, "target_workspace_resource_id")

    @property
    @pulumi.getter(name="targetWorkspaceTenantId")
    def target_workspace_tenant_id(self) -> pulumi.Output[str]:
        """
        Tenant id of the target Sentinel workspace joining the given Sentinel workspace manager
        """
        return pulumi.get(self, "target_workspace_tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

