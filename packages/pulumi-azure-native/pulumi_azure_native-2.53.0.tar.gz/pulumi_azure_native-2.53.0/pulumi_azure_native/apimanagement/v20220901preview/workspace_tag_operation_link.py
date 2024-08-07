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

__all__ = ['WorkspaceTagOperationLinkArgs', 'WorkspaceTagOperationLink']

@pulumi.input_type
class WorkspaceTagOperationLinkArgs:
    def __init__(__self__, *,
                 operation_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 tag_id: pulumi.Input[str],
                 workspace_id: pulumi.Input[str],
                 operation_link_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkspaceTagOperationLink resource.
        :param pulumi.Input[str] operation_id: Full resource Id of an API operation.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] tag_id: Tag identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] operation_link_id: Tag-operation link identifier. Must be unique in the current API Management service instance.
        """
        pulumi.set(__self__, "operation_id", operation_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "tag_id", tag_id)
        pulumi.set(__self__, "workspace_id", workspace_id)
        if operation_link_id is not None:
            pulumi.set(__self__, "operation_link_id", operation_link_id)

    @property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> pulumi.Input[str]:
        """
        Full resource Id of an API operation.
        """
        return pulumi.get(self, "operation_id")

    @operation_id.setter
    def operation_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "operation_id", value)

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
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="tagId")
    def tag_id(self) -> pulumi.Input[str]:
        """
        Tag identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "tag_id")

    @tag_id.setter
    def tag_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "tag_id", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[str]:
        """
        Workspace identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_id", value)

    @property
    @pulumi.getter(name="operationLinkId")
    def operation_link_id(self) -> Optional[pulumi.Input[str]]:
        """
        Tag-operation link identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "operation_link_id")

    @operation_link_id.setter
    def operation_link_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "operation_link_id", value)


class WorkspaceTagOperationLink(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 operation_id: Optional[pulumi.Input[str]] = None,
                 operation_link_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 tag_id: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Tag-operation link details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] operation_id: Full resource Id of an API operation.
        :param pulumi.Input[str] operation_link_id: Tag-operation link identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] tag_id: Tag identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceTagOperationLinkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Tag-operation link details.

        :param str resource_name: The name of the resource.
        :param WorkspaceTagOperationLinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceTagOperationLinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 operation_id: Optional[pulumi.Input[str]] = None,
                 operation_link_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 tag_id: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceTagOperationLinkArgs.__new__(WorkspaceTagOperationLinkArgs)

            if operation_id is None and not opts.urn:
                raise TypeError("Missing required property 'operation_id'")
            __props__.__dict__["operation_id"] = operation_id
            __props__.__dict__["operation_link_id"] = operation_link_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if tag_id is None and not opts.urn:
                raise TypeError("Missing required property 'tag_id'")
            __props__.__dict__["tag_id"] = tag_id
            if workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_id'")
            __props__.__dict__["workspace_id"] = workspace_id
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:WorkspaceTagOperationLink"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:WorkspaceTagOperationLink"), pulumi.Alias(type_="azure-native:apimanagement/v20230501preview:WorkspaceTagOperationLink"), pulumi.Alias(type_="azure-native:apimanagement/v20230901preview:WorkspaceTagOperationLink")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkspaceTagOperationLink, __self__).__init__(
            'azure-native:apimanagement/v20220901preview:WorkspaceTagOperationLink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkspaceTagOperationLink':
        """
        Get an existing WorkspaceTagOperationLink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceTagOperationLinkArgs.__new__(WorkspaceTagOperationLinkArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["operation_id"] = None
        __props__.__dict__["type"] = None
        return WorkspaceTagOperationLink(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> pulumi.Output[str]:
        """
        Full resource Id of an API operation.
        """
        return pulumi.get(self, "operation_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

