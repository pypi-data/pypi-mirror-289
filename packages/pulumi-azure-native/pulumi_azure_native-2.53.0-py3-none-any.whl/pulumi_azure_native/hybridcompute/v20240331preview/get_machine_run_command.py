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
    'GetMachineRunCommandResult',
    'AwaitableGetMachineRunCommandResult',
    'get_machine_run_command',
    'get_machine_run_command_output',
]

@pulumi.output_type
class GetMachineRunCommandResult:
    """
    Describes a Run Command
    """
    def __init__(__self__, async_execution=None, error_blob_managed_identity=None, error_blob_uri=None, id=None, instance_view=None, location=None, name=None, output_blob_managed_identity=None, output_blob_uri=None, parameters=None, protected_parameters=None, provisioning_state=None, run_as_password=None, run_as_user=None, source=None, system_data=None, tags=None, timeout_in_seconds=None, type=None):
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
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if timeout_in_seconds and not isinstance(timeout_in_seconds, int):
            raise TypeError("Expected argument 'timeout_in_seconds' to be a int")
        pulumi.set(__self__, "timeout_in_seconds", timeout_in_seconds)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="asyncExecution")
    def async_execution(self) -> Optional[bool]:
        """
        Optional. If set to true, provisioning will complete as soon as script starts and will not wait for script to complete.
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
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> 'outputs.MachineRunCommandInstanceViewResponse':
        """
        The machine run command instance view.
        """
        return pulumi.get(self, "instance_view")

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
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="runAsPassword")
    def run_as_password(self) -> Optional[str]:
        """
        Specifies the user account password on the machine when executing the run command.
        """
        return pulumi.get(self, "run_as_password")

    @property
    @pulumi.getter(name="runAsUser")
    def run_as_user(self) -> Optional[str]:
        """
        Specifies the user account on the machine when executing the run command.
        """
        return pulumi.get(self, "run_as_user")

    @property
    @pulumi.getter
    def source(self) -> Optional['outputs.MachineRunCommandScriptSourceResponse']:
        """
        The source of the run command script.
        """
        return pulumi.get(self, "source")

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
    @pulumi.getter(name="timeoutInSeconds")
    def timeout_in_seconds(self) -> Optional[int]:
        """
        The timeout in seconds to execute the run command.
        """
        return pulumi.get(self, "timeout_in_seconds")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetMachineRunCommandResult(GetMachineRunCommandResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMachineRunCommandResult(
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
            system_data=self.system_data,
            tags=self.tags,
            timeout_in_seconds=self.timeout_in_seconds,
            type=self.type)


def get_machine_run_command(machine_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            run_command_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMachineRunCommandResult:
    """
    The operation to get a run command.


    :param str machine_name: The name of the hybrid machine.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str run_command_name: The name of the run command.
    """
    __args__ = dict()
    __args__['machineName'] = machine_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['runCommandName'] = run_command_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hybridcompute/v20240331preview:getMachineRunCommand', __args__, opts=opts, typ=GetMachineRunCommandResult).value

    return AwaitableGetMachineRunCommandResult(
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
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        timeout_in_seconds=pulumi.get(__ret__, 'timeout_in_seconds'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_machine_run_command)
def get_machine_run_command_output(machine_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   run_command_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMachineRunCommandResult]:
    """
    The operation to get a run command.


    :param str machine_name: The name of the hybrid machine.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str run_command_name: The name of the run command.
    """
    ...
