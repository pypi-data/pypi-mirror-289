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

__all__ = [
    'GetVirtualMachineImageTemplateResult',
    'AwaitableGetVirtualMachineImageTemplateResult',
    'get_virtual_machine_image_template',
    'get_virtual_machine_image_template_output',
]

@pulumi.output_type
class GetVirtualMachineImageTemplateResult:
    """
    Image template is an ARM resource managed by Microsoft.VirtualMachineImages provider
    """
    def __init__(__self__, build_timeout_in_minutes=None, customize=None, distribute=None, exact_staging_resource_group=None, id=None, identity=None, last_run_status=None, location=None, name=None, optimize=None, provisioning_error=None, provisioning_state=None, source=None, staging_resource_group=None, system_data=None, tags=None, type=None, validate=None, vm_profile=None):
        if build_timeout_in_minutes and not isinstance(build_timeout_in_minutes, int):
            raise TypeError("Expected argument 'build_timeout_in_minutes' to be a int")
        pulumi.set(__self__, "build_timeout_in_minutes", build_timeout_in_minutes)
        if customize and not isinstance(customize, list):
            raise TypeError("Expected argument 'customize' to be a list")
        pulumi.set(__self__, "customize", customize)
        if distribute and not isinstance(distribute, list):
            raise TypeError("Expected argument 'distribute' to be a list")
        pulumi.set(__self__, "distribute", distribute)
        if exact_staging_resource_group and not isinstance(exact_staging_resource_group, str):
            raise TypeError("Expected argument 'exact_staging_resource_group' to be a str")
        pulumi.set(__self__, "exact_staging_resource_group", exact_staging_resource_group)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if last_run_status and not isinstance(last_run_status, dict):
            raise TypeError("Expected argument 'last_run_status' to be a dict")
        pulumi.set(__self__, "last_run_status", last_run_status)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if optimize and not isinstance(optimize, dict):
            raise TypeError("Expected argument 'optimize' to be a dict")
        pulumi.set(__self__, "optimize", optimize)
        if provisioning_error and not isinstance(provisioning_error, dict):
            raise TypeError("Expected argument 'provisioning_error' to be a dict")
        pulumi.set(__self__, "provisioning_error", provisioning_error)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if source and not isinstance(source, dict):
            raise TypeError("Expected argument 'source' to be a dict")
        pulumi.set(__self__, "source", source)
        if staging_resource_group and not isinstance(staging_resource_group, str):
            raise TypeError("Expected argument 'staging_resource_group' to be a str")
        pulumi.set(__self__, "staging_resource_group", staging_resource_group)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if validate and not isinstance(validate, dict):
            raise TypeError("Expected argument 'validate' to be a dict")
        pulumi.set(__self__, "validate", validate)
        if vm_profile and not isinstance(vm_profile, dict):
            raise TypeError("Expected argument 'vm_profile' to be a dict")
        pulumi.set(__self__, "vm_profile", vm_profile)

    @property
    @pulumi.getter(name="buildTimeoutInMinutes")
    def build_timeout_in_minutes(self) -> Optional[int]:
        """
        Maximum duration to wait while building the image template (includes all customizations, optimization, validations, and distributions). Omit or specify 0 to use the default (4 hours).
        """
        return pulumi.get(self, "build_timeout_in_minutes")

    @property
    @pulumi.getter
    def customize(self) -> Optional[Sequence[Any]]:
        """
        Specifies the properties used to describe the customization steps of the image, like Image source etc
        """
        return pulumi.get(self, "customize")

    @property
    @pulumi.getter
    def distribute(self) -> Sequence[Any]:
        """
        The distribution targets where the image output needs to go to.
        """
        return pulumi.get(self, "distribute")

    @property
    @pulumi.getter(name="exactStagingResourceGroup")
    def exact_staging_resource_group(self) -> str:
        """
        The staging resource group id in the same subscription as the image template that will be used to build the image. This read-only field differs from 'stagingResourceGroup' only if the value specified in the 'stagingResourceGroup' field is empty.
        """
        return pulumi.get(self, "exact_staging_resource_group")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> 'outputs.ImageTemplateIdentityResponse':
        """
        The identity of the image template, if configured.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="lastRunStatus")
    def last_run_status(self) -> 'outputs.ImageTemplateLastRunStatusResponse':
        """
        State of 'run' that is currently executing or was last executed.
        """
        return pulumi.get(self, "last_run_status")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def optimize(self) -> Optional['outputs.ImageTemplatePropertiesResponseOptimize']:
        """
        Specifies optimization to be performed on image.
        """
        return pulumi.get(self, "optimize")

    @property
    @pulumi.getter(name="provisioningError")
    def provisioning_error(self) -> 'outputs.ProvisioningErrorResponse':
        """
        Provisioning error, if any
        """
        return pulumi.get(self, "provisioning_error")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def source(self) -> Any:
        """
        Specifies the properties used to describe the source image.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="stagingResourceGroup")
    def staging_resource_group(self) -> Optional[str]:
        """
        The staging resource group id in the same subscription as the image template that will be used to build the image. If this field is empty, a resource group with a random name will be created. If the resource group specified in this field doesn't exist, it will be created with the same name. If the resource group specified exists, it must be empty and in the same region as the image template. The resource group created will be deleted during template deletion if this field is empty or the resource group specified doesn't exist, but if the resource group specified exists the resources created in the resource group will be deleted during template deletion and the resource group itself will remain.
        """
        return pulumi.get(self, "staging_resource_group")

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
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def validate(self) -> Optional['outputs.ImageTemplatePropertiesResponseValidate']:
        """
        Configuration options and list of validations to be performed on the resulting image.
        """
        return pulumi.get(self, "validate")

    @property
    @pulumi.getter(name="vmProfile")
    def vm_profile(self) -> Optional['outputs.ImageTemplateVmProfileResponse']:
        """
        Describes how virtual machine is set up to build images
        """
        return pulumi.get(self, "vm_profile")


class AwaitableGetVirtualMachineImageTemplateResult(GetVirtualMachineImageTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualMachineImageTemplateResult(
            build_timeout_in_minutes=self.build_timeout_in_minutes,
            customize=self.customize,
            distribute=self.distribute,
            exact_staging_resource_group=self.exact_staging_resource_group,
            id=self.id,
            identity=self.identity,
            last_run_status=self.last_run_status,
            location=self.location,
            name=self.name,
            optimize=self.optimize,
            provisioning_error=self.provisioning_error,
            provisioning_state=self.provisioning_state,
            source=self.source,
            staging_resource_group=self.staging_resource_group,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            validate=self.validate,
            vm_profile=self.vm_profile)


def get_virtual_machine_image_template(image_template_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualMachineImageTemplateResult:
    """
    Get information about a virtual machine image template
    Azure REST API version: 2022-07-01.

    Other available API versions: 2018-02-01-preview, 2019-05-01-preview, 2023-07-01, 2024-02-01.


    :param str image_template_name: The name of the image Template
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['imageTemplateName'] = image_template_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:virtualmachineimages:getVirtualMachineImageTemplate', __args__, opts=opts, typ=GetVirtualMachineImageTemplateResult).value

    return AwaitableGetVirtualMachineImageTemplateResult(
        build_timeout_in_minutes=pulumi.get(__ret__, 'build_timeout_in_minutes'),
        customize=pulumi.get(__ret__, 'customize'),
        distribute=pulumi.get(__ret__, 'distribute'),
        exact_staging_resource_group=pulumi.get(__ret__, 'exact_staging_resource_group'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        last_run_status=pulumi.get(__ret__, 'last_run_status'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        optimize=pulumi.get(__ret__, 'optimize'),
        provisioning_error=pulumi.get(__ret__, 'provisioning_error'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        source=pulumi.get(__ret__, 'source'),
        staging_resource_group=pulumi.get(__ret__, 'staging_resource_group'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        validate=pulumi.get(__ret__, 'validate'),
        vm_profile=pulumi.get(__ret__, 'vm_profile'))


@_utilities.lift_output_func(get_virtual_machine_image_template)
def get_virtual_machine_image_template_output(image_template_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualMachineImageTemplateResult]:
    """
    Get information about a virtual machine image template
    Azure REST API version: 2022-07-01.

    Other available API versions: 2018-02-01-preview, 2019-05-01-preview, 2023-07-01, 2024-02-01.


    :param str image_template_name: The name of the image Template
    :param str resource_group_name: The name of the resource group.
    """
    ...
