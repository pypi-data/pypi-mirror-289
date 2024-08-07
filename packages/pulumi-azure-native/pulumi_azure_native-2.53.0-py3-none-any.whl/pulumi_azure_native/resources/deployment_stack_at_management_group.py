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

__all__ = ['DeploymentStackAtManagementGroupArgs', 'DeploymentStackAtManagementGroup']

@pulumi.input_type
class DeploymentStackAtManagementGroupArgs:
    def __init__(__self__, *,
                 action_on_unmanage: pulumi.Input['DeploymentStackPropertiesActionOnUnmanageArgs'],
                 deny_settings: pulumi.Input['DenySettingsArgs'],
                 management_group_id: pulumi.Input[str],
                 debug_setting: Optional[pulumi.Input['DeploymentStacksDebugSettingArgs']] = None,
                 deployment_scope: Optional[pulumi.Input[str]] = None,
                 deployment_stack_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 parameters_link: Optional[pulumi.Input['DeploymentStacksParametersLinkArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template: Optional[Any] = None,
                 template_link: Optional[pulumi.Input['DeploymentStacksTemplateLinkArgs']] = None):
        """
        The set of arguments for constructing a DeploymentStackAtManagementGroup resource.
        :param pulumi.Input['DeploymentStackPropertiesActionOnUnmanageArgs'] action_on_unmanage: Defines the behavior of resources that are not managed immediately after the stack is updated.
        :param pulumi.Input['DenySettingsArgs'] deny_settings: Defines how resources deployed by the stack are locked.
        :param pulumi.Input[str] management_group_id: Management Group.
        :param pulumi.Input['DeploymentStacksDebugSettingArgs'] debug_setting: The debug setting of the deployment.
        :param pulumi.Input[str] deployment_scope: The scope at which the initial deployment should be created. If a scope is not specified, it will default to the scope of the deployment stack. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroupId}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}').
        :param pulumi.Input[str] deployment_stack_name: Name of the deployment stack.
        :param pulumi.Input[str] description: Deployment stack description.
        :param pulumi.Input[str] location: The location of the deployment stack. It cannot be changed after creation. It must be one of the supported Azure locations.
        :param Any parameters: Name and value pairs that define the deployment parameters for the template. Use this element when providing the parameter values directly in the request, rather than linking to an existing parameter file. Use either the parametersLink property or the parameters property, but not both. It can be a JObject or a well formed JSON string.
        :param pulumi.Input['DeploymentStacksParametersLinkArgs'] parameters_link: The URI of parameters file. Use this element to link to an existing parameters file. Use either the parametersLink property or the parameters property, but not both.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Deployment stack resource tags.
        :param Any template: The template content. You use this element when you want to pass the template syntax directly in the request rather than link to an existing template. It can be a JObject or well-formed JSON string. Use either the templateLink property or the template property, but not both.
        :param pulumi.Input['DeploymentStacksTemplateLinkArgs'] template_link: The URI of the template. Use either the templateLink property or the template property, but not both.
        """
        pulumi.set(__self__, "action_on_unmanage", action_on_unmanage)
        pulumi.set(__self__, "deny_settings", deny_settings)
        pulumi.set(__self__, "management_group_id", management_group_id)
        if debug_setting is not None:
            pulumi.set(__self__, "debug_setting", debug_setting)
        if deployment_scope is not None:
            pulumi.set(__self__, "deployment_scope", deployment_scope)
        if deployment_stack_name is not None:
            pulumi.set(__self__, "deployment_stack_name", deployment_stack_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if parameters_link is not None:
            pulumi.set(__self__, "parameters_link", parameters_link)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if template is not None:
            pulumi.set(__self__, "template", template)
        if template_link is not None:
            pulumi.set(__self__, "template_link", template_link)

    @property
    @pulumi.getter(name="actionOnUnmanage")
    def action_on_unmanage(self) -> pulumi.Input['DeploymentStackPropertiesActionOnUnmanageArgs']:
        """
        Defines the behavior of resources that are not managed immediately after the stack is updated.
        """
        return pulumi.get(self, "action_on_unmanage")

    @action_on_unmanage.setter
    def action_on_unmanage(self, value: pulumi.Input['DeploymentStackPropertiesActionOnUnmanageArgs']):
        pulumi.set(self, "action_on_unmanage", value)

    @property
    @pulumi.getter(name="denySettings")
    def deny_settings(self) -> pulumi.Input['DenySettingsArgs']:
        """
        Defines how resources deployed by the stack are locked.
        """
        return pulumi.get(self, "deny_settings")

    @deny_settings.setter
    def deny_settings(self, value: pulumi.Input['DenySettingsArgs']):
        pulumi.set(self, "deny_settings", value)

    @property
    @pulumi.getter(name="managementGroupId")
    def management_group_id(self) -> pulumi.Input[str]:
        """
        Management Group.
        """
        return pulumi.get(self, "management_group_id")

    @management_group_id.setter
    def management_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "management_group_id", value)

    @property
    @pulumi.getter(name="debugSetting")
    def debug_setting(self) -> Optional[pulumi.Input['DeploymentStacksDebugSettingArgs']]:
        """
        The debug setting of the deployment.
        """
        return pulumi.get(self, "debug_setting")

    @debug_setting.setter
    def debug_setting(self, value: Optional[pulumi.Input['DeploymentStacksDebugSettingArgs']]):
        pulumi.set(self, "debug_setting", value)

    @property
    @pulumi.getter(name="deploymentScope")
    def deployment_scope(self) -> Optional[pulumi.Input[str]]:
        """
        The scope at which the initial deployment should be created. If a scope is not specified, it will default to the scope of the deployment stack. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroupId}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}').
        """
        return pulumi.get(self, "deployment_scope")

    @deployment_scope.setter
    def deployment_scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_scope", value)

    @property
    @pulumi.getter(name="deploymentStackName")
    def deployment_stack_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the deployment stack.
        """
        return pulumi.get(self, "deployment_stack_name")

    @deployment_stack_name.setter
    def deployment_stack_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_stack_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Deployment stack description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the deployment stack. It cannot be changed after creation. It must be one of the supported Azure locations.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Any]:
        """
        Name and value pairs that define the deployment parameters for the template. Use this element when providing the parameter values directly in the request, rather than linking to an existing parameter file. Use either the parametersLink property or the parameters property, but not both. It can be a JObject or a well formed JSON string.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[Any]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="parametersLink")
    def parameters_link(self) -> Optional[pulumi.Input['DeploymentStacksParametersLinkArgs']]:
        """
        The URI of parameters file. Use this element to link to an existing parameters file. Use either the parametersLink property or the parameters property, but not both.
        """
        return pulumi.get(self, "parameters_link")

    @parameters_link.setter
    def parameters_link(self, value: Optional[pulumi.Input['DeploymentStacksParametersLinkArgs']]):
        pulumi.set(self, "parameters_link", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Deployment stack resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def template(self) -> Optional[Any]:
        """
        The template content. You use this element when you want to pass the template syntax directly in the request rather than link to an existing template. It can be a JObject or well-formed JSON string. Use either the templateLink property or the template property, but not both.
        """
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: Optional[Any]):
        pulumi.set(self, "template", value)

    @property
    @pulumi.getter(name="templateLink")
    def template_link(self) -> Optional[pulumi.Input['DeploymentStacksTemplateLinkArgs']]:
        """
        The URI of the template. Use either the templateLink property or the template property, but not both.
        """
        return pulumi.get(self, "template_link")

    @template_link.setter
    def template_link(self, value: Optional[pulumi.Input['DeploymentStacksTemplateLinkArgs']]):
        pulumi.set(self, "template_link", value)


class DeploymentStackAtManagementGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_on_unmanage: Optional[pulumi.Input[Union['DeploymentStackPropertiesActionOnUnmanageArgs', 'DeploymentStackPropertiesActionOnUnmanageArgsDict']]] = None,
                 debug_setting: Optional[pulumi.Input[Union['DeploymentStacksDebugSettingArgs', 'DeploymentStacksDebugSettingArgsDict']]] = None,
                 deny_settings: Optional[pulumi.Input[Union['DenySettingsArgs', 'DenySettingsArgsDict']]] = None,
                 deployment_scope: Optional[pulumi.Input[str]] = None,
                 deployment_stack_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 parameters_link: Optional[pulumi.Input[Union['DeploymentStacksParametersLinkArgs', 'DeploymentStacksParametersLinkArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template: Optional[Any] = None,
                 template_link: Optional[pulumi.Input[Union['DeploymentStacksTemplateLinkArgs', 'DeploymentStacksTemplateLinkArgsDict']]] = None,
                 __props__=None):
        """
        Deployment stack object.
        Azure REST API version: 2022-08-01-preview.

        Other available API versions: 2024-03-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['DeploymentStackPropertiesActionOnUnmanageArgs', 'DeploymentStackPropertiesActionOnUnmanageArgsDict']] action_on_unmanage: Defines the behavior of resources that are not managed immediately after the stack is updated.
        :param pulumi.Input[Union['DeploymentStacksDebugSettingArgs', 'DeploymentStacksDebugSettingArgsDict']] debug_setting: The debug setting of the deployment.
        :param pulumi.Input[Union['DenySettingsArgs', 'DenySettingsArgsDict']] deny_settings: Defines how resources deployed by the stack are locked.
        :param pulumi.Input[str] deployment_scope: The scope at which the initial deployment should be created. If a scope is not specified, it will default to the scope of the deployment stack. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroupId}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}').
        :param pulumi.Input[str] deployment_stack_name: Name of the deployment stack.
        :param pulumi.Input[str] description: Deployment stack description.
        :param pulumi.Input[str] location: The location of the deployment stack. It cannot be changed after creation. It must be one of the supported Azure locations.
        :param pulumi.Input[str] management_group_id: Management Group.
        :param Any parameters: Name and value pairs that define the deployment parameters for the template. Use this element when providing the parameter values directly in the request, rather than linking to an existing parameter file. Use either the parametersLink property or the parameters property, but not both. It can be a JObject or a well formed JSON string.
        :param pulumi.Input[Union['DeploymentStacksParametersLinkArgs', 'DeploymentStacksParametersLinkArgsDict']] parameters_link: The URI of parameters file. Use this element to link to an existing parameters file. Use either the parametersLink property or the parameters property, but not both.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Deployment stack resource tags.
        :param Any template: The template content. You use this element when you want to pass the template syntax directly in the request rather than link to an existing template. It can be a JObject or well-formed JSON string. Use either the templateLink property or the template property, but not both.
        :param pulumi.Input[Union['DeploymentStacksTemplateLinkArgs', 'DeploymentStacksTemplateLinkArgsDict']] template_link: The URI of the template. Use either the templateLink property or the template property, but not both.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentStackAtManagementGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Deployment stack object.
        Azure REST API version: 2022-08-01-preview.

        Other available API versions: 2024-03-01.

        :param str resource_name: The name of the resource.
        :param DeploymentStackAtManagementGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentStackAtManagementGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_on_unmanage: Optional[pulumi.Input[Union['DeploymentStackPropertiesActionOnUnmanageArgs', 'DeploymentStackPropertiesActionOnUnmanageArgsDict']]] = None,
                 debug_setting: Optional[pulumi.Input[Union['DeploymentStacksDebugSettingArgs', 'DeploymentStacksDebugSettingArgsDict']]] = None,
                 deny_settings: Optional[pulumi.Input[Union['DenySettingsArgs', 'DenySettingsArgsDict']]] = None,
                 deployment_scope: Optional[pulumi.Input[str]] = None,
                 deployment_stack_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 management_group_id: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[Any] = None,
                 parameters_link: Optional[pulumi.Input[Union['DeploymentStacksParametersLinkArgs', 'DeploymentStacksParametersLinkArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 template: Optional[Any] = None,
                 template_link: Optional[pulumi.Input[Union['DeploymentStacksTemplateLinkArgs', 'DeploymentStacksTemplateLinkArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentStackAtManagementGroupArgs.__new__(DeploymentStackAtManagementGroupArgs)

            if action_on_unmanage is None and not opts.urn:
                raise TypeError("Missing required property 'action_on_unmanage'")
            __props__.__dict__["action_on_unmanage"] = action_on_unmanage
            __props__.__dict__["debug_setting"] = debug_setting
            if deny_settings is None and not opts.urn:
                raise TypeError("Missing required property 'deny_settings'")
            __props__.__dict__["deny_settings"] = deny_settings
            __props__.__dict__["deployment_scope"] = deployment_scope
            __props__.__dict__["deployment_stack_name"] = deployment_stack_name
            __props__.__dict__["description"] = description
            __props__.__dict__["location"] = location
            if management_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'management_group_id'")
            __props__.__dict__["management_group_id"] = management_group_id
            __props__.__dict__["parameters"] = parameters
            __props__.__dict__["parameters_link"] = parameters_link
            __props__.__dict__["tags"] = tags
            __props__.__dict__["template"] = template
            __props__.__dict__["template_link"] = template_link
            __props__.__dict__["deleted_resources"] = None
            __props__.__dict__["deployment_id"] = None
            __props__.__dict__["detached_resources"] = None
            __props__.__dict__["duration"] = None
            __props__.__dict__["error"] = None
            __props__.__dict__["failed_resources"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["outputs"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resources"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:resources/v20220801preview:DeploymentStackAtManagementGroup"), pulumi.Alias(type_="azure-native:resources/v20240301:DeploymentStackAtManagementGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DeploymentStackAtManagementGroup, __self__).__init__(
            'azure-native:resources:DeploymentStackAtManagementGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DeploymentStackAtManagementGroup':
        """
        Get an existing DeploymentStackAtManagementGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeploymentStackAtManagementGroupArgs.__new__(DeploymentStackAtManagementGroupArgs)

        __props__.__dict__["action_on_unmanage"] = None
        __props__.__dict__["debug_setting"] = None
        __props__.__dict__["deleted_resources"] = None
        __props__.__dict__["deny_settings"] = None
        __props__.__dict__["deployment_id"] = None
        __props__.__dict__["deployment_scope"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["detached_resources"] = None
        __props__.__dict__["duration"] = None
        __props__.__dict__["error"] = None
        __props__.__dict__["failed_resources"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["outputs"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["parameters_link"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resources"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return DeploymentStackAtManagementGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="actionOnUnmanage")
    def action_on_unmanage(self) -> pulumi.Output['outputs.DeploymentStackPropertiesResponseActionOnUnmanage']:
        """
        Defines the behavior of resources that are not managed immediately after the stack is updated.
        """
        return pulumi.get(self, "action_on_unmanage")

    @property
    @pulumi.getter(name="debugSetting")
    def debug_setting(self) -> pulumi.Output[Optional['outputs.DeploymentStacksDebugSettingResponse']]:
        """
        The debug setting of the deployment.
        """
        return pulumi.get(self, "debug_setting")

    @property
    @pulumi.getter(name="deletedResources")
    def deleted_resources(self) -> pulumi.Output[Sequence['outputs.ResourceReferenceResponse']]:
        """
        An array of resources that were deleted during the most recent update.
        """
        return pulumi.get(self, "deleted_resources")

    @property
    @pulumi.getter(name="denySettings")
    def deny_settings(self) -> pulumi.Output['outputs.DenySettingsResponse']:
        """
        Defines how resources deployed by the stack are locked.
        """
        return pulumi.get(self, "deny_settings")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> pulumi.Output[str]:
        """
        The resourceId of the deployment resource created by the deployment stack.
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter(name="deploymentScope")
    def deployment_scope(self) -> pulumi.Output[Optional[str]]:
        """
        The scope at which the initial deployment should be created. If a scope is not specified, it will default to the scope of the deployment stack. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroupId}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}').
        """
        return pulumi.get(self, "deployment_scope")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Deployment stack description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="detachedResources")
    def detached_resources(self) -> pulumi.Output[Sequence['outputs.ResourceReferenceResponse']]:
        """
        An array of resources that were detached during the most recent update.
        """
        return pulumi.get(self, "detached_resources")

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Output[str]:
        """
        The duration of the deployment stack update.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter
    def error(self) -> pulumi.Output[Optional['outputs.ErrorResponseResponse']]:
        """
        Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.).
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter(name="failedResources")
    def failed_resources(self) -> pulumi.Output[Sequence['outputs.ResourceReferenceExtendedResponse']]:
        """
        An array of resources that failed to reach goal state during the most recent update.
        """
        return pulumi.get(self, "failed_resources")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the deployment stack. It cannot be changed after creation. It must be one of the supported Azure locations.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of this resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def outputs(self) -> pulumi.Output[Any]:
        """
        The outputs of the underlying deployment.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Any]]:
        """
        Name and value pairs that define the deployment parameters for the template. Use this element when providing the parameter values directly in the request, rather than linking to an existing parameter file. Use either the parametersLink property or the parameters property, but not both. It can be a JObject or a well formed JSON string.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="parametersLink")
    def parameters_link(self) -> pulumi.Output[Optional['outputs.DeploymentStacksParametersLinkResponse']]:
        """
        The URI of parameters file. Use this element to link to an existing parameters file. Use either the parametersLink property or the parameters property, but not both.
        """
        return pulumi.get(self, "parameters_link")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        State of the deployment stack.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Sequence['outputs.ManagedResourceReferenceResponse']]:
        """
        An array of resources currently managed by the deployment stack.
        """
        return pulumi.get(self, "resources")

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
        Deployment stack resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of this resource.
        """
        return pulumi.get(self, "type")

