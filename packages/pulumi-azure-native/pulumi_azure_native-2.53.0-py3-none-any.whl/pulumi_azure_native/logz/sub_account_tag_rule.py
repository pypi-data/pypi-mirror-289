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

__all__ = ['SubAccountTagRuleArgs', 'SubAccountTagRule']

@pulumi.input_type
class SubAccountTagRuleArgs:
    def __init__(__self__, *,
                 monitor_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 sub_account_name: pulumi.Input[str],
                 properties: Optional[pulumi.Input['MonitoringTagRulesPropertiesArgs']] = None,
                 rule_set_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SubAccountTagRule resource.
        :param pulumi.Input[str] monitor_name: Monitor resource name
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sub_account_name: Sub Account resource name
        :param pulumi.Input['MonitoringTagRulesPropertiesArgs'] properties: Definition of the properties for a TagRules resource.
        """
        pulumi.set(__self__, "monitor_name", monitor_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sub_account_name", sub_account_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if rule_set_name is not None:
            pulumi.set(__self__, "rule_set_name", rule_set_name)

    @property
    @pulumi.getter(name="monitorName")
    def monitor_name(self) -> pulumi.Input[str]:
        """
        Monitor resource name
        """
        return pulumi.get(self, "monitor_name")

    @monitor_name.setter
    def monitor_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "monitor_name", value)

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
    @pulumi.getter(name="subAccountName")
    def sub_account_name(self) -> pulumi.Input[str]:
        """
        Sub Account resource name
        """
        return pulumi.get(self, "sub_account_name")

    @sub_account_name.setter
    def sub_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sub_account_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['MonitoringTagRulesPropertiesArgs']]:
        """
        Definition of the properties for a TagRules resource.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['MonitoringTagRulesPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="ruleSetName")
    def rule_set_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "rule_set_name")

    @rule_set_name.setter
    def rule_set_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_set_name", value)


class SubAccountTagRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 monitor_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['MonitoringTagRulesPropertiesArgs', 'MonitoringTagRulesPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_set_name: Optional[pulumi.Input[str]] = None,
                 sub_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Capture logs and metrics of Azure resources based on ARM tags.
        Azure REST API version: 2022-01-01-preview. Prior API version in Azure Native 1.x: 2020-10-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] monitor_name: Monitor resource name
        :param pulumi.Input[Union['MonitoringTagRulesPropertiesArgs', 'MonitoringTagRulesPropertiesArgsDict']] properties: Definition of the properties for a TagRules resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sub_account_name: Sub Account resource name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubAccountTagRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Capture logs and metrics of Azure resources based on ARM tags.
        Azure REST API version: 2022-01-01-preview. Prior API version in Azure Native 1.x: 2020-10-01.

        :param str resource_name: The name of the resource.
        :param SubAccountTagRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubAccountTagRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 monitor_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['MonitoringTagRulesPropertiesArgs', 'MonitoringTagRulesPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_set_name: Optional[pulumi.Input[str]] = None,
                 sub_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubAccountTagRuleArgs.__new__(SubAccountTagRuleArgs)

            if monitor_name is None and not opts.urn:
                raise TypeError("Missing required property 'monitor_name'")
            __props__.__dict__["monitor_name"] = monitor_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["rule_set_name"] = rule_set_name
            if sub_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'sub_account_name'")
            __props__.__dict__["sub_account_name"] = sub_account_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:logz/v20201001:SubAccountTagRule"), pulumi.Alias(type_="azure-native:logz/v20201001preview:SubAccountTagRule"), pulumi.Alias(type_="azure-native:logz/v20220101preview:SubAccountTagRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SubAccountTagRule, __self__).__init__(
            'azure-native:logz:SubAccountTagRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SubAccountTagRule':
        """
        Get an existing SubAccountTagRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SubAccountTagRuleArgs.__new__(SubAccountTagRuleArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return SubAccountTagRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the rule set.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.MonitoringTagRulesPropertiesResponse']:
        """
        Definition of the properties for a TagRules resource.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to this resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the rule set.
        """
        return pulumi.get(self, "type")

