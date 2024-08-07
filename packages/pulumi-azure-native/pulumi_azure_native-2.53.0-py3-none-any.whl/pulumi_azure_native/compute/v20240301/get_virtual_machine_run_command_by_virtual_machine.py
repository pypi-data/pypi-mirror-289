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
    'GetVirtualMachineRunCommandByVirtualMachineResult',
    'AwaitableGetVirtualMachineRunCommandByVirtualMachineResult',
    'get_virtual_machine_run_command_by_virtual_machine',
    'get_virtual_machine_run_command_by_virtual_machine_output',
]

@pulumi.output_type
class GetVirtualMachineRunCommandByVirtualMachineResult:
    """
    Describes a Virtual Machine run command.
    """
    def __init__(__self__, async_execution=None, error_blob_managed_identity=None, error_blob_uri=None, id=None, instance_view=None, location=None, name=None, output_blob_managed_identity=None, output_blob_uri=None, parameters=None, protected_parameters=None, provisioning_state=None, run_as_password=None, run_as_user=None, source=None, tags=None, timeout_in_seconds=None, treat_failure_as_deployment_failure=None, type=None):
        if async_execution and not isinstance(async_execution, bool):
            raise TypeError("Expected argument 'async_execution' to be a bool")
        pulumi.set(__self__, "async_execution", async_execution)
        if error_blob_managed_identity and not isinstance(error_blob_managed_identity, dict):
            raise TypeError("Expected argument 'error_blob_managed_identity' to be a dict")
        pulumi.set(__self__, "error_blob_managed_identity", error_blob_managed_identity)
        if error_blob_uri and not isinstance(error_blob_uri, str):
            raise TypeError("Expected argument 'error_blob_uri' to be a str")
        pulumi.set(__self__, "error_blob_uri", error_blob_uri)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_view and not isinstance(instance_view, dict):
            raise TypeError("Expected argument 'instance_view' to be a dict")
        pulumi.set(__self__, "instance_view", instance_view)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if output_blob_managed_identity and not isinstance(output_blob_managed_identity, dict):
            raise TypeError("Expected argument 'output_blob_managed_identity' to be a dict")
        pulumi.set(__self__, "output_blob_managed_identity", output_blob_managed_identity)
        if output_blob_uri and not isinstance(output_blob_uri, str):
            raise TypeError("Expected argument 'output_blob_uri' to be a str")
        pulumi.set(__self__, "output_blob_uri", output_blob_uri)
        if parameters and not isinstance(parameters, list):
            raise TypeError("Expected argument 'parameters' to be a list")
        pulumi.set(__self__, "parameters", parameters)
        if protected_parameters and not isinstance(protected_parameters, list):
            raise TypeError("Expected argument 'protected_parameters' to be a list")
        pulumi.set(__self__, "protected_parameters", protected_parameters)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if run_as_password and not isinstance(run_as_password, str):
            raise TypeError("Expected argument 'run_as_password' to be a str")
        pulumi.set(__self__, "run_as_password", run_as_password)
        if run_as_user and not isinstance(run_as_user, str):
            raise TypeError("Expected argument 'run_as_user' to be a str")
        pulumi.set(__self__, "run_as_user", run_as_user)
        if source and not isinstance(source, dict):
            raise TypeError("Expected argument 'source' to be a dict")
        pulumi.set(__self__, "source", source)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if timeout_in_seconds and not isinstance(timeout_in_seconds, int):
            raise TypeError("Expected argument 'timeout_in_seconds' to be a int")
        pulumi.set(__self__, "timeout_in_seconds", timeout_in_seconds)
        if treat_failure_as_deployment_failure and not isinstance(treat_failure_as_deployment_failure, bool):
            raise TypeError("Expected argument 'treat_failure_as_deployment_failure' to be a bool")
        pulumi.set(__self__, "treat_failure_as_deployment_failure", treat_failure_as_deployment_failure)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="asyncExecution")
    def async_execution(self) -> Optional[bool]:
        """
        Optional. If set to true, provisioning will complete as soon as the script starts and will not wait for script to complete.
        """
        return pulumi.get(self, "async_execution")

    @property
    @pulumi.getter(name="errorBlobManagedIdentity")
    def error_blob_managed_identity(self) -> Optional['outputs.RunCommandManagedIdentityResponse']:
        """
        User-assigned managed identity that has access to errorBlobUri storage blob. Use an empty object in case of system-assigned identity. Make sure managed identity has been given access to blob's container with 'Storage Blob Data Contributor' role assignment. In case of user-assigned identity, make sure you add it under VM's identity. For more info on managed identity and Run Command, refer https://aka.ms/ManagedIdentity and https://aka.ms/RunCommandManaged 
        """
        return pulumi.get(self, "error_blob_managed_identity")

    @property
    @pulumi.getter(name="errorBlobUri")
    def error_blob_uri(self) -> Optional[str]:
        """
        Specifies the Azure storage blob where script error stream will be uploaded. Use a SAS URI with read, append, create, write access OR use managed identity to provide the VM access to the blob. Refer errorBlobManagedIdentity parameter.
        """
        return pulumi.get(self, "error_blob_uri")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> 'outputs.VirtualMachineRunCommandInstanceViewResponse':
        """
        The virtual machine run command instance view.
        """
        return pulumi.get(self, "instance_view")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputBlobManagedIdentity")
    def output_blob_managed_identity(self) -> Optional['outputs.RunCommandManagedIdentityResponse']:
        """
        User-assigned managed identity that has access to outputBlobUri storage blob. Use an empty object in case of system-assigned identity. Make sure managed identity has been given access to blob's container with 'Storage Blob Data Contributor' role assignment. In case of user-assigned identity, make sure you add it under VM's identity. For more info on managed identity and Run Command, refer https://aka.ms/ManagedIdentity and https://aka.ms/RunCommandManaged 
        """
        return pulumi.get(self, "output_blob_managed_identity")

    @property
    @pulumi.getter(name="outputBlobUri")
    def output_blob_uri(self) -> Optional[str]:
        """
        Specifies the Azure storage blob where script output stream will be uploaded. Use a SAS URI with read, append, create, write access OR use managed identity to provide the VM access to the blob. Refer outputBlobManagedIdentity parameter. 
        """
        return pulumi.get(self, "output_blob_uri")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence['outputs.RunCommandInputParameterResponse']]:
        """
        The parameters used by the script.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="protectedParameters")
    def protected_parameters(self) -> Optional[Sequence['outputs.RunCommandInputParameterResponse']]:
        """
        The parameters used by the script.
        """
        return pulumi.get(self, "protected_parameters")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state, which only appears in the response. If treatFailureAsDeploymentFailure set to true, any failure in the script will fail the deployment and ProvisioningState will be marked as Failed. If treatFailureAsDeploymentFailure set to false, ProvisioningState would only reflect whether the run command was run or not by the extensions platform, it would not indicate whether script failed in case of script failures. See instance view of run command in case of script failures to see executionMessage, output, error: https://aka.ms/runcommandmanaged#get-execution-status-and-results 
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="runAsPassword")
    def run_as_password(self) -> Optional[str]:
        """
        Specifies the user account password on the VM when executing the run command.
        """
        return pulumi.get(self, "run_as_password")

    @property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> Optional[str]:
        """
        Specifies the user account on the VM when executing the run command.
        """
        return pulumi.get(self, "run_as_user")

    @property
    @pulumi.getter
    def source(self) -> Optional['outputs.VirtualMachineRunCommandScriptSourceResponse']:
        """
        The source of the run command script.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[int]:
        """
        The timeout in seconds to execute the run command.
        """
        return pulumi.get(self, "timeout_in_seconds")

    @property
    @pulumi.getter(name="treatFailureAsDeploymentFailure")
    def treat_failure_as_deployment_failure(self) -> Optional[bool]:
        """
        Optional. If set to true, any failure in the script will fail the deployment and ProvisioningState will be marked as Failed. If set to false, ProvisioningState would only reflect whether the run command was run or not by the extensions platform, it would not indicate whether script failed in case of script failures. See instance view of run command in case of script failures to see executionMessage, output, error: https://aka.ms/runcommandmanaged#get-execution-status-and-results 
        """
        return pulumi.get(self, "treat_failure_as_deployment_failure")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetVirtualMachineRunCommandByVirtualMachineResult(GetVirtualMachineRunCommandByVirtualMachineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualMachineRunCommandByVirtualMachineResult(
            async_execution=self.async_execution,
            error_blob_managed_identity=self.error_blob_managed_identity,
            error_blob_uri=self.error_blob_uri,
            id=self.id,
            instance_view=self.instance_view,
            location=self.location,
            name=self.name,
            output_blob_managed_identity=self.output_blob_managed_identity,
            output_blob_uri=self.output_blob_uri,
            parameters=self.parameters,
            protected_parameters=self.protected_parameters,
            provisioning_state=self.provisioning_state,
            run_as_password=self.run_as_password,
            run_as_user=self.run_as_user,
            source=self.source,
            tags=self.tags,
            timeout_in_seconds=self.timeout_in_seconds,
            treat_failure_as_deployment_failure=self.treat_failure_as_deployment_failure,
            type=self.type)


def get_virtual_machine_run_command_by_virtual_machine(expand: Optional[str] = None,
                                                       resource_group_name: Optional[str] = None,
                                                       run_command_name: Optional[str] = None,
                                                       vm_name: Optional[str] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualMachineRunCommandByVirtualMachineResult:
    """
    The operation to get the run command.


    :param str expand: The expand expression to apply on the operation.
    :param str resource_group_name: The name of the resource group.
    :param str run_command_name: The name of the virtual machine run command.
    :param str vm_name: The name of the virtual machine containing the run command.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    __args__['runCommandName'] = run_command_name
    __args__['vmName'] = vm_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20240301:getVirtualMachineRunCommandByVirtualMachine', __args__, opts=opts, typ=GetVirtualMachineRunCommandByVirtualMachineResult).value

    return AwaitableGetVirtualMachineRunCommandByVirtualMachineResult(
        async_execution=pulumi.get(__ret__, 'async_execution'),
        error_blob_managed_identity=pulumi.get(__ret__, 'error_blob_managed_identity'),
        error_blob_uri=pulumi.get(__ret__, 'error_blob_uri'),
        id=pulumi.get(__ret__, 'id'),
        instance_view=pulumi.get(__ret__, 'instance_view'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        output_blob_managed_identity=pulumi.get(__ret__, 'output_blob_managed_identity'),
        output_blob_uri=pulumi.get(__ret__, 'output_blob_uri'),
        parameters=pulumi.get(__ret__, 'parameters'),
        protected_parameters=pulumi.get(__ret__, 'protected_parameters'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        run_as_password=pulumi.get(__ret__, 'run_as_password'),
        run_as_user=pulumi.get(__ret__, 'run_as_user'),
        source=pulumi.get(__ret__, 'source'),
        tags=pulumi.get(__ret__, 'tags'),
        timeout_in_seconds=pulumi.get(__ret__, 'timeout_in_seconds'),
        treat_failure_as_deployment_failure=pulumi.get(__ret__, 'treat_failure_as_deployment_failure'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_virtual_machine_run_command_by_virtual_machine)
def get_virtual_machine_run_command_by_virtual_machine_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                                              run_command_name: Optional[pulumi.Input[str]] = None,
                                                              vm_name: Optional[pulumi.Input[str]] = None,
                                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualMachineRunCommandByVirtualMachineResult]:
    """
    The operation to get the run command.


    :param str expand: The expand expression to apply on the operation.
    :param str resource_group_name: The name of the resource group.
    :param str run_command_name: The name of the virtual machine run command.
    :param str vm_name: The name of the virtual machine containing the run command.
    """
    ...
