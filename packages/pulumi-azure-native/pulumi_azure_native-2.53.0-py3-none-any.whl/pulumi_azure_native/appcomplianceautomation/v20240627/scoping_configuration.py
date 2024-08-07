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

__all__ = ['ScopingConfigurationArgs', 'ScopingConfiguration']

@pulumi.input_type
class ScopingConfigurationArgs:
    def __init__(__self__, *,
                 report_name: pulumi.Input[str],
                 answers: Optional[pulumi.Input[Sequence[pulumi.Input['ScopingAnswerArgs']]]] = None,
                 scoping_configuration_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ScopingConfiguration resource.
        :param pulumi.Input[str] report_name: Report Name.
        :param pulumi.Input[Sequence[pulumi.Input['ScopingAnswerArgs']]] answers: List of scoping question answers.
        :param pulumi.Input[str] scoping_configuration_name: The scoping configuration of the specific report.
        """
        pulumi.set(__self__, "report_name", report_name)
        if answers is not None:
            pulumi.set(__self__, "answers", answers)
        if scoping_configuration_name is not None:
            pulumi.set(__self__, "scoping_configuration_name", scoping_configuration_name)

    @property
    @pulumi.getter(name="reportName")
    def report_name(self) -> pulumi.Input[str]:
        """
        Report Name.
        """
        return pulumi.get(self, "report_name")

    @report_name.setter
    def report_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "report_name", value)

    @property
    @pulumi.getter
    def answers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScopingAnswerArgs']]]]:
        """
        List of scoping question answers.
        """
        return pulumi.get(self, "answers")

    @answers.setter
    def answers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScopingAnswerArgs']]]]):
        pulumi.set(self, "answers", value)

    @property
    @pulumi.getter(name="scopingConfigurationName")
    def scoping_configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The scoping configuration of the specific report.
        """
        return pulumi.get(self, "scoping_configuration_name")

    @scoping_configuration_name.setter
    def scoping_configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scoping_configuration_name", value)


class ScopingConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 answers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ScopingAnswerArgs', 'ScopingAnswerArgsDict']]]]] = None,
                 report_name: Optional[pulumi.Input[str]] = None,
                 scoping_configuration_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A class represent an AppComplianceAutomation scoping configuration resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ScopingAnswerArgs', 'ScopingAnswerArgsDict']]]] answers: List of scoping question answers.
        :param pulumi.Input[str] report_name: Report Name.
        :param pulumi.Input[str] scoping_configuration_name: The scoping configuration of the specific report.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScopingConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A class represent an AppComplianceAutomation scoping configuration resource.

        :param str resource_name: The name of the resource.
        :param ScopingConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScopingConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 answers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ScopingAnswerArgs', 'ScopingAnswerArgsDict']]]]] = None,
                 report_name: Optional[pulumi.Input[str]] = None,
                 scoping_configuration_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScopingConfigurationArgs.__new__(ScopingConfigurationArgs)

            __props__.__dict__["answers"] = answers
            if report_name is None and not opts.urn:
                raise TypeError("Missing required property 'report_name'")
            __props__.__dict__["report_name"] = report_name
            __props__.__dict__["scoping_configuration_name"] = scoping_configuration_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:appcomplianceautomation:ScopingConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ScopingConfiguration, __self__).__init__(
            'azure-native:appcomplianceautomation/v20240627:ScopingConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScopingConfiguration':
        """
        Get an existing ScopingConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScopingConfigurationArgs.__new__(ScopingConfigurationArgs)

        __props__.__dict__["answers"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ScopingConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def answers(self) -> pulumi.Output[Optional[Sequence['outputs.ScopingAnswerResponse']]]:
        """
        List of scoping question answers.
        """
        return pulumi.get(self, "answers")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

