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
from ._inputs import *

__all__ = ['ScriptExecutionArgs', 'ScriptExecution']

@pulumi.input_type
class ScriptExecutionArgs:
    def __init__(__self__, *,
                 private_cloud_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 timeout: pulumi.Input[str],
                 failure_reason: Optional[pulumi.Input[str]] = None,
                 hidden_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PSCredentialExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgs']]]]] = None,
                 named_outputs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 output: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PSCredentialExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgs']]]]] = None,
                 retention: Optional[pulumi.Input[str]] = None,
                 script_cmdlet_id: Optional[pulumi.Input[str]] = None,
                 script_execution_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ScriptExecution resource.
        :param pulumi.Input[str] private_cloud_name: The name of the private cloud.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] timeout: Time limit for execution
        :param pulumi.Input[str] failure_reason: Error message if the script was able to run, but if the script itself had errors or powershell threw an exception
        :param pulumi.Input[Sequence[pulumi.Input[Union['PSCredentialExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgs']]]] hidden_parameters: Parameters that will be hidden/not visible to ARM, such as passwords and credentials
        :param pulumi.Input[Mapping[str, Any]] named_outputs: User-defined dictionary.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] output: Standard output stream from the powershell execution
        :param pulumi.Input[Sequence[pulumi.Input[Union['PSCredentialExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgs']]]] parameters: Parameters the script will accept
        :param pulumi.Input[str] retention: Time to live for the resource. If not provided, will be available for 60 days
        :param pulumi.Input[str] script_cmdlet_id: A reference to the script cmdlet resource if user is running a AVS script
        :param pulumi.Input[str] script_execution_name: Name of the user-invoked script execution resource
        """
        pulumi.set(__self__, "private_cloud_name", private_cloud_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "timeout", timeout)
        if failure_reason is not None:
            pulumi.set(__self__, "failure_reason", failure_reason)
        if hidden_parameters is not None:
            pulumi.set(__self__, "hidden_parameters", hidden_parameters)
        if named_outputs is not None:
            pulumi.set(__self__, "named_outputs", named_outputs)
        if output is not None:
            pulumi.set(__self__, "output", output)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if retention is not None:
            pulumi.set(__self__, "retention", retention)
        if script_cmdlet_id is not None:
            pulumi.set(__self__, "script_cmdlet_id", script_cmdlet_id)
        if script_execution_name is not None:
            pulumi.set(__self__, "script_execution_name", script_execution_name)

    @property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[str]:
        """
        The name of the private cloud.
        """
        return pulumi.get(self, "private_cloud_name")

    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_cloud_name", value)

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
    @pulumi.getter
    def timeout(self) -> pulumi.Input[str]:
        """
        Time limit for execution
        """
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: pulumi.Input[str]):
        pulumi.set(self, "timeout", value)

    @property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[pulumi.Input[str]]:
        """
        Error message if the script was able to run, but if the script itself had errors or powershell threw an exception
        """
        return pulumi.get(self, "failure_reason")

    @failure_reason.setter
    def failure_reason(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "failure_reason", value)

    @property
    @pulumi.getter(name="hiddenParameters")
    def hidden_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union['PSCredentialExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgs']]]]]:
        """
        Parameters that will be hidden/not visible to ARM, such as passwords and credentials
        """
        return pulumi.get(self, "hidden_parameters")

    @hidden_parameters.setter
    def hidden_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PSCredentialExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgs']]]]]):
        pulumi.set(self, "hidden_parameters", value)

    @property
    @pulumi.getter(name="namedOutputs")
    def named_outputs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        User-defined dictionary.
        """
        return pulumi.get(self, "named_outputs")

    @named_outputs.setter
    def named_outputs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "named_outputs", value)

    @property
    @pulumi.getter
    def output(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Standard output stream from the powershell execution
        """
        return pulumi.get(self, "output")

    @output.setter
    def output(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "output", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union['PSCredentialExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgs']]]]]:
        """
        Parameters the script will accept
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PSCredentialExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgs']]]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def retention(self) -> Optional[pulumi.Input[str]]:
        """
        Time to live for the resource. If not provided, will be available for 60 days
        """
        return pulumi.get(self, "retention")

    @retention.setter
    def retention(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "retention", value)

    @property
    @pulumi.getter(name="scriptCmdletId")
    def script_cmdlet_id(self) -> Optional[pulumi.Input[str]]:
        """
        A reference to the script cmdlet resource if user is running a AVS script
        """
        return pulumi.get(self, "script_cmdlet_id")

    @script_cmdlet_id.setter
    def script_cmdlet_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script_cmdlet_id", value)

    @property
    @pulumi.getter(name="scriptExecutionName")
    def script_execution_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the user-invoked script execution resource
        """
        return pulumi.get(self, "script_execution_name")

    @script_execution_name.setter
    def script_execution_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "script_execution_name", value)


class ScriptExecution(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 failure_reason: Optional[pulumi.Input[str]] = None,
                 hidden_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[Union['PSCredentialExecutionParameterArgs', 'PSCredentialExecutionParameterArgsDict'], Union['ScriptSecureStringExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgsDict'], Union['ScriptStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgsDict']]]]]] = None,
                 named_outputs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 output: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[Union['PSCredentialExecutionParameterArgs', 'PSCredentialExecutionParameterArgsDict'], Union['ScriptSecureStringExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgsDict'], Union['ScriptStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgsDict']]]]]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retention: Optional[pulumi.Input[str]] = None,
                 script_cmdlet_id: Optional[pulumi.Input[str]] = None,
                 script_execution_name: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An instance of a script executed by a user - custom or AVS

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] failure_reason: Error message if the script was able to run, but if the script itself had errors or powershell threw an exception
        :param pulumi.Input[Sequence[pulumi.Input[Union[Union['PSCredentialExecutionParameterArgs', 'PSCredentialExecutionParameterArgsDict'], Union['ScriptSecureStringExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgsDict'], Union['ScriptStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgsDict']]]]] hidden_parameters: Parameters that will be hidden/not visible to ARM, such as passwords and credentials
        :param pulumi.Input[Mapping[str, Any]] named_outputs: User-defined dictionary.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] output: Standard output stream from the powershell execution
        :param pulumi.Input[Sequence[pulumi.Input[Union[Union['PSCredentialExecutionParameterArgs', 'PSCredentialExecutionParameterArgsDict'], Union['ScriptSecureStringExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgsDict'], Union['ScriptStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgsDict']]]]] parameters: Parameters the script will accept
        :param pulumi.Input[str] private_cloud_name: The name of the private cloud.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] retention: Time to live for the resource. If not provided, will be available for 60 days
        :param pulumi.Input[str] script_cmdlet_id: A reference to the script cmdlet resource if user is running a AVS script
        :param pulumi.Input[str] script_execution_name: Name of the user-invoked script execution resource
        :param pulumi.Input[str] timeout: Time limit for execution
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScriptExecutionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An instance of a script executed by a user - custom or AVS

        :param str resource_name: The name of the resource.
        :param ScriptExecutionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScriptExecutionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 failure_reason: Optional[pulumi.Input[str]] = None,
                 hidden_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[Union['PSCredentialExecutionParameterArgs', 'PSCredentialExecutionParameterArgsDict'], Union['ScriptSecureStringExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgsDict'], Union['ScriptStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgsDict']]]]]] = None,
                 named_outputs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 output: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 parameters: Optional[pulumi.Input[Sequence[pulumi.Input[Union[Union['PSCredentialExecutionParameterArgs', 'PSCredentialExecutionParameterArgsDict'], Union['ScriptSecureStringExecutionParameterArgs', 'ScriptSecureStringExecutionParameterArgsDict'], Union['ScriptStringExecutionParameterArgs', 'ScriptStringExecutionParameterArgsDict']]]]]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 retention: Optional[pulumi.Input[str]] = None,
                 script_cmdlet_id: Optional[pulumi.Input[str]] = None,
                 script_execution_name: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScriptExecutionArgs.__new__(ScriptExecutionArgs)

            __props__.__dict__["failure_reason"] = failure_reason
            __props__.__dict__["hidden_parameters"] = hidden_parameters
            __props__.__dict__["named_outputs"] = named_outputs
            __props__.__dict__["output"] = output
            __props__.__dict__["parameters"] = parameters
            if private_cloud_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_cloud_name'")
            __props__.__dict__["private_cloud_name"] = private_cloud_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["retention"] = retention
            __props__.__dict__["script_cmdlet_id"] = script_cmdlet_id
            __props__.__dict__["script_execution_name"] = script_execution_name
            if timeout is None and not opts.urn:
                raise TypeError("Missing required property 'timeout'")
            __props__.__dict__["timeout"] = timeout
            __props__.__dict__["errors"] = None
            __props__.__dict__["finished_at"] = None
            __props__.__dict__["information"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["started_at"] = None
            __props__.__dict__["submitted_at"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["warnings"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:avs:ScriptExecution"), pulumi.Alias(type_="azure-native:avs/v20210601:ScriptExecution"), pulumi.Alias(type_="azure-native:avs/v20211201:ScriptExecution"), pulumi.Alias(type_="azure-native:avs/v20220501:ScriptExecution"), pulumi.Alias(type_="azure-native:avs/v20230901:ScriptExecution")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ScriptExecution, __self__).__init__(
            'azure-native:avs/v20230301:ScriptExecution',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScriptExecution':
        """
        Get an existing ScriptExecution resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScriptExecutionArgs.__new__(ScriptExecutionArgs)

        __props__.__dict__["errors"] = None
        __props__.__dict__["failure_reason"] = None
        __props__.__dict__["finished_at"] = None
        __props__.__dict__["hidden_parameters"] = None
        __props__.__dict__["information"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["named_outputs"] = None
        __props__.__dict__["output"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["retention"] = None
        __props__.__dict__["script_cmdlet_id"] = None
        __props__.__dict__["started_at"] = None
        __props__.__dict__["submitted_at"] = None
        __props__.__dict__["timeout"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["warnings"] = None
        return ScriptExecution(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def errors(self) -> pulumi.Output[Sequence[str]]:
        """
        Standard error output stream from the powershell execution
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> pulumi.Output[Optional[str]]:
        """
        Error message if the script was able to run, but if the script itself had errors or powershell threw an exception
        """
        return pulumi.get(self, "failure_reason")

    @property
    @pulumi.getter(name="finishedAt")
    def finished_at(self) -> pulumi.Output[str]:
        """
        Time the script execution was finished
        """
        return pulumi.get(self, "finished_at")

    @property
    @pulumi.getter(name="hiddenParameters")
    def hidden_parameters(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        """
        Parameters that will be hidden/not visible to ARM, such as passwords and credentials
        """
        return pulumi.get(self, "hidden_parameters")

    @property
    @pulumi.getter
    def information(self) -> pulumi.Output[Sequence[str]]:
        """
        Standard information out stream from the powershell execution
        """
        return pulumi.get(self, "information")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namedOutputs")
    def named_outputs(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        User-defined dictionary.
        """
        return pulumi.get(self, "named_outputs")

    @property
    @pulumi.getter
    def output(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Standard output stream from the powershell execution
        """
        return pulumi.get(self, "output")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        """
        Parameters the script will accept
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The state of the script execution resource
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def retention(self) -> pulumi.Output[Optional[str]]:
        """
        Time to live for the resource. If not provided, will be available for 60 days
        """
        return pulumi.get(self, "retention")

    @property
    @pulumi.getter(name="scriptCmdletId")
    def script_cmdlet_id(self) -> pulumi.Output[Optional[str]]:
        """
        A reference to the script cmdlet resource if user is running a AVS script
        """
        return pulumi.get(self, "script_cmdlet_id")

    @property
    @pulumi.getter(name="startedAt")
    def started_at(self) -> pulumi.Output[str]:
        """
        Time the script execution was started
        """
        return pulumi.get(self, "started_at")

    @property
    @pulumi.getter(name="submittedAt")
    def submitted_at(self) -> pulumi.Output[str]:
        """
        Time the script execution was submitted
        """
        return pulumi.get(self, "submitted_at")

    @property
    @pulumi.getter
    def timeout(self) -> pulumi.Output[str]:
        """
        Time limit for execution
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def warnings(self) -> pulumi.Output[Sequence[str]]:
        """
        Standard warning out stream from the powershell execution
        """
        return pulumi.get(self, "warnings")

