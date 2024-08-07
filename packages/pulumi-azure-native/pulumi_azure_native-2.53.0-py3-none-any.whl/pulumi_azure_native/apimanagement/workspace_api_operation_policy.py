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
from ._enums import *

__all__ = ['WorkspaceApiOperationPolicyArgs', 'WorkspaceApiOperationPolicy']

@pulumi.input_type
class WorkspaceApiOperationPolicyArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 operation_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 value: pulumi.Input[str],
                 workspace_id: pulumi.Input[str],
                 format: Optional[pulumi.Input[Union[str, 'PolicyContentFormat']]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkspaceApiOperationPolicy resource.
        :param pulumi.Input[str] api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        :param pulumi.Input[str] operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] value: Contents of the Policy as defined by the format.
        :param pulumi.Input[str] workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[Union[str, 'PolicyContentFormat']] format: Format of the policyContent.
        :param pulumi.Input[str] policy_id: The identifier of the Policy.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "operation_id", operation_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "value", value)
        pulumi.set(__self__, "workspace_id", workspace_id)
        if format is None:
            format = 'xml'
        if format is not None:
            pulumi.set(__self__, "format", format)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        """
        API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter(name="operationId")
    def operation_id(self) -> pulumi.Input[str]:
        """
        Operation identifier within an API. Must be unique in the current API Management service instance.
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
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Contents of the Policy as defined by the format.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

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
    @pulumi.getter
    def format(self) -> Optional[pulumi.Input[Union[str, 'PolicyContentFormat']]]:
        """
        Format of the policyContent.
        """
        return pulumi.get(self, "format")

    @format.setter
    def format(self, value: Optional[pulumi.Input[Union[str, 'PolicyContentFormat']]]):
        pulumi.set(self, "format", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the Policy.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)


class WorkspaceApiOperationPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[Union[str, 'PolicyContentFormat']]] = None,
                 operation_id: Optional[pulumi.Input[str]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Policy Contract details.
        Azure REST API version: 2022-09-01-preview.

        Other available API versions: 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
        :param pulumi.Input[Union[str, 'PolicyContentFormat']] format: Format of the policyContent.
        :param pulumi.Input[str] operation_id: Operation identifier within an API. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] policy_id: The identifier of the Policy.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] value: Contents of the Policy as defined by the format.
        :param pulumi.Input[str] workspace_id: Workspace identifier. Must be unique in the current API Management service instance.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceApiOperationPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Policy Contract details.
        Azure REST API version: 2022-09-01-preview.

        Other available API versions: 2023-03-01-preview, 2023-05-01-preview, 2023-09-01-preview.

        :param str resource_name: The name of the resource.
        :param WorkspaceApiOperationPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceApiOperationPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 format: Optional[pulumi.Input[Union[str, 'PolicyContentFormat']]] = None,
                 operation_id: Optional[pulumi.Input[str]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceApiOperationPolicyArgs.__new__(WorkspaceApiOperationPolicyArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            if format is None:
                format = 'xml'
            __props__.__dict__["format"] = format
            if operation_id is None and not opts.urn:
                raise TypeError("Missing required property 'operation_id'")
            __props__.__dict__["operation_id"] = operation_id
            __props__.__dict__["policy_id"] = policy_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
            if workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_id'")
            __props__.__dict__["workspace_id"] = workspace_id
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement/v20220901preview:WorkspaceApiOperationPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:WorkspaceApiOperationPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20230501preview:WorkspaceApiOperationPolicy"), pulumi.Alias(type_="azure-native:apimanagement/v20230901preview:WorkspaceApiOperationPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkspaceApiOperationPolicy, __self__).__init__(
            'azure-native:apimanagement:WorkspaceApiOperationPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkspaceApiOperationPolicy':
        """
        Get an existing WorkspaceApiOperationPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceApiOperationPolicyArgs.__new__(WorkspaceApiOperationPolicyArgs)

        __props__.__dict__["format"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["value"] = None
        return WorkspaceApiOperationPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[Optional[str]]:
        """
        Format of the policyContent.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        Contents of the Policy as defined by the format.
        """
        return pulumi.get(self, "value")

