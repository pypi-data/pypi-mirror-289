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

__all__ = [
    'GetDeploymentStackAtResourceGroupResult',
    'AwaitableGetDeploymentStackAtResourceGroupResult',
    'get_deployment_stack_at_resource_group',
    'get_deployment_stack_at_resource_group_output',
]

@pulumi.output_type
class GetDeploymentStackAtResourceGroupResult:
    """
    Deployment stack object.
    """
    def __init__(__self__, action_on_unmanage=None, correlation_id=None, debug_setting=None, deleted_resources=None, deny_settings=None, deployment_id=None, deployment_scope=None, description=None, detached_resources=None, duration=None, error=None, failed_resources=None, id=None, location=None, name=None, outputs=None, parameters=None, parameters_link=None, provisioning_state=None, resources=None, system_data=None, tags=None, type=None):
        if action_on_unmanage and not isinstance(action_on_unmanage, dict):
            raise TypeError("Expected argument 'action_on_unmanage' to be a dict")
        pulumi.set(__self__, "action_on_unmanage", action_on_unmanage)
        if correlation_id and not isinstance(correlation_id, str):
            raise TypeError("Expected argument 'correlation_id' to be a str")
        pulumi.set(__self__, "correlation_id", correlation_id)
        if debug_setting and not isinstance(debug_setting, dict):
            raise TypeError("Expected argument 'debug_setting' to be a dict")
        pulumi.set(__self__, "debug_setting", debug_setting)
        if deleted_resources and not isinstance(deleted_resources, list):
            raise TypeError("Expected argument 'deleted_resources' to be a list")
        pulumi.set(__self__, "deleted_resources", deleted_resources)
        if deny_settings and not isinstance(deny_settings, dict):
            raise TypeError("Expected argument 'deny_settings' to be a dict")
        pulumi.set(__self__, "deny_settings", deny_settings)
        if deployment_id and not isinstance(deployment_id, str):
            raise TypeError("Expected argument 'deployment_id' to be a str")
        pulumi.set(__self__, "deployment_id", deployment_id)
        if deployment_scope and not isinstance(deployment_scope, str):
            raise TypeError("Expected argument 'deployment_scope' to be a str")
        pulumi.set(__self__, "deployment_scope", deployment_scope)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if detached_resources and not isinstance(detached_resources, list):
            raise TypeError("Expected argument 'detached_resources' to be a list")
        pulumi.set(__self__, "detached_resources", detached_resources)
        if duration and not isinstance(duration, str):
            raise TypeError("Expected argument 'duration' to be a str")
        pulumi.set(__self__, "duration", duration)
        if error and not isinstance(error, dict):
            raise TypeError("Expected argument 'error' to be a dict")
        pulumi.set(__self__, "error", error)
        if failed_resources and not isinstance(failed_resources, list):
            raise TypeError("Expected argument 'failed_resources' to be a list")
        pulumi.set(__self__, "failed_resources", failed_resources)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if outputs and not isinstance(outputs, dict):
            raise TypeError("Expected argument 'outputs' to be a dict")
        pulumi.set(__self__, "outputs", outputs)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if parameters_link and not isinstance(parameters_link, dict):
            raise TypeError("Expected argument 'parameters_link' to be a dict")
        pulumi.set(__self__, "parameters_link", parameters_link)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resources and not isinstance(resources, list):
            raise TypeError("Expected argument 'resources' to be a list")
        pulumi.set(__self__, "resources", resources)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="actionOnUnmanage")
    def action_on_unmanage(self) -> 'outputs.ActionOnUnmanageResponse':
        """
        Defines the behavior of resources that are no longer managed after the Deployment stack is updated or deleted.
        """
        return pulumi.get(self, "action_on_unmanage")

    @property
    @pulumi.getter(name="correlationId")
    def correlation_id(self) -> str:
        """
        The correlation id of the last Deployment stack upsert or delete operation. It is in GUID format and is used for tracing.
        """
        return pulumi.get(self, "correlation_id")

    @property
    @pulumi.getter(name="debugSetting")
    def debug_setting(self) -> Optional['outputs.DeploymentStacksDebugSettingResponse']:
        """
        The debug setting of the deployment.
        """
        return pulumi.get(self, "debug_setting")

    @property
    @pulumi.getter(name="deletedResources")
    def deleted_resources(self) -> Sequence['outputs.ResourceReferenceResponse']:
        """
        An array of resources that were deleted during the most recent Deployment stack update. Deleted means that the resource was removed from the template and relevant deletion operations were specified.
        """
        return pulumi.get(self, "deleted_resources")

    @property
    @pulumi.getter(name="denySettings")
    def deny_settings(self) -> 'outputs.DenySettingsResponse':
        """
        Defines how resources deployed by the stack are locked.
        """
        return pulumi.get(self, "deny_settings")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> str:
        """
        The resourceId of the deployment resource created by the deployment stack.
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter(name="deploymentScope")
    def deployment_scope(self) -> Optional[str]:
        """
        The scope at which the initial deployment should be created. If a scope is not specified, it will default to the scope of the deployment stack. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroupId}'), subscription (format: '/subscriptions/{subscriptionId}'), resource group (format: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}').
        """
        return pulumi.get(self, "deployment_scope")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Deployment stack description. Max length of 4096 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="detachedResources")
    def detached_resources(self) -> Sequence['outputs.ResourceReferenceResponse']:
        """
        An array of resources that were detached during the most recent Deployment stack update. Detached means that the resource was removed from the template, but no relevant deletion operations were specified. So, the resource still exists while no longer being associated with the stack.
        """
        return pulumi.get(self, "detached_resources")

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        The duration of the last successful Deployment stack update.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter
    def error(self) -> Optional['outputs.ErrorDetailResponse']:
        """
        The error detail.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter(name="failedResources")
    def failed_resources(self) -> Sequence['outputs.ResourceReferenceExtendedResponse']:
        """
        An array of resources that failed to reach goal state during the most recent update. Each resourceId is accompanied by an error message.
        """
        return pulumi.get(self, "failed_resources")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        String Id used to locate any resource on Azure.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the Deployment stack. It cannot be changed after creation. It must be one of the supported Azure locations.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of this resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def outputs(self) -> Any:
        """
        The outputs of the deployment resource created by the deployment stack.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, 'outputs.DeploymentParameterResponse']]:
        """
        Name and value pairs that define the deployment parameters for the template. Use this element when providing the parameter values directly in the request, rather than linking to an existing parameter file. Use either the parametersLink property or the parameters property, but not both.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="parametersLink")
    def parameters_link(self) -> Optional['outputs.DeploymentStacksParametersLinkResponse']:
        """
        The URI of parameters file. Use this element to link to an existing parameters file. Use either the parametersLink property or the parameters property, but not both.
        """
        return pulumi.get(self, "parameters_link")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        State of the deployment stack.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def resources(self) -> Sequence['outputs.ManagedResourceReferenceResponse']:
        """
        An array of resources currently managed by the deployment stack.
        """
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Deployment stack resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of this resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetDeploymentStackAtResourceGroupResult(GetDeploymentStackAtResourceGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeploymentStackAtResourceGroupResult(
            action_on_unmanage=self.action_on_unmanage,
            correlation_id=self.correlation_id,
            debug_setting=self.debug_setting,
            deleted_resources=self.deleted_resources,
            deny_settings=self.deny_settings,
            deployment_id=self.deployment_id,
            deployment_scope=self.deployment_scope,
            description=self.description,
            detached_resources=self.detached_resources,
            duration=self.duration,
            error=self.error,
            failed_resources=self.failed_resources,
            id=self.id,
            location=self.location,
            name=self.name,
            outputs=self.outputs,
            parameters=self.parameters,
            parameters_link=self.parameters_link,
            provisioning_state=self.provisioning_state,
            resources=self.resources,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_deployment_stack_at_resource_group(deployment_stack_name: Optional[str] = None,
                                           resource_group_name: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeploymentStackAtResourceGroupResult:
    """
    Gets a Deployment stack with a given name at Resource Group scope.


    :param str deployment_stack_name: Name of the deployment stack.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['deploymentStackName'] = deployment_stack_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:resources/v20240301:getDeploymentStackAtResourceGroup', __args__, opts=opts, typ=GetDeploymentStackAtResourceGroupResult).value

    return AwaitableGetDeploymentStackAtResourceGroupResult(
        action_on_unmanage=pulumi.get(__ret__, 'action_on_unmanage'),
        correlation_id=pulumi.get(__ret__, 'correlation_id'),
        debug_setting=pulumi.get(__ret__, 'debug_setting'),
        deleted_resources=pulumi.get(__ret__, 'deleted_resources'),
        deny_settings=pulumi.get(__ret__, 'deny_settings'),
        deployment_id=pulumi.get(__ret__, 'deployment_id'),
        deployment_scope=pulumi.get(__ret__, 'deployment_scope'),
        description=pulumi.get(__ret__, 'description'),
        detached_resources=pulumi.get(__ret__, 'detached_resources'),
        duration=pulumi.get(__ret__, 'duration'),
        error=pulumi.get(__ret__, 'error'),
        failed_resources=pulumi.get(__ret__, 'failed_resources'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        outputs=pulumi.get(__ret__, 'outputs'),
        parameters=pulumi.get(__ret__, 'parameters'),
        parameters_link=pulumi.get(__ret__, 'parameters_link'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        resources=pulumi.get(__ret__, 'resources'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_deployment_stack_at_resource_group)
def get_deployment_stack_at_resource_group_output(deployment_stack_name: Optional[pulumi.Input[str]] = None,
                                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeploymentStackAtResourceGroupResult]:
    """
    Gets a Deployment stack with a given name at Resource Group scope.


    :param str deployment_stack_name: Name of the deployment stack.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
