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
from ._enums import *
from ._inputs import *

__all__ = ['AlertProcessingRuleByNameArgs', 'AlertProcessingRuleByName']

@pulumi.input_type
class AlertProcessingRuleByNameArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 alert_processing_rule_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['AlertProcessingRulePropertiesArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a AlertProcessingRuleByName resource.
        :param pulumi.Input[str] resource_group_name: Resource group name where the resource is created.
        :param pulumi.Input[str] alert_processing_rule_name: The name of the alert processing rule that needs to be created/updated.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input['AlertProcessingRulePropertiesArgs'] properties: Alert processing rule properties.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if alert_processing_rule_name is not None:
            pulumi.set(__self__, "alert_processing_rule_name", alert_processing_rule_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Resource group name where the resource is created.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="alertProcessingRuleName")
    def alert_processing_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the alert processing rule that needs to be created/updated.
        """
        return pulumi.get(self, "alert_processing_rule_name")

    @alert_processing_rule_name.setter
    def alert_processing_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_processing_rule_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['AlertProcessingRulePropertiesArgs']]:
        """
        Alert processing rule properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['AlertProcessingRulePropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class AlertProcessingRuleByName(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alert_processing_rule_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['AlertProcessingRulePropertiesArgs', 'AlertProcessingRulePropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Alert processing rule object containing target scopes, conditions and scheduling logic.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alert_processing_rule_name: The name of the alert processing rule that needs to be created/updated.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Union['AlertProcessingRulePropertiesArgs', 'AlertProcessingRulePropertiesArgsDict']] properties: Alert processing rule properties.
        :param pulumi.Input[str] resource_group_name: Resource group name where the resource is created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AlertProcessingRuleByNameArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Alert processing rule object containing target scopes, conditions and scheduling logic.

        :param str resource_name: The name of the resource.
        :param AlertProcessingRuleByNameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AlertProcessingRuleByNameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alert_processing_rule_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['AlertProcessingRulePropertiesArgs', 'AlertProcessingRulePropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AlertProcessingRuleByNameArgs.__new__(AlertProcessingRuleByNameArgs)

            __props__.__dict__["alert_processing_rule_name"] = alert_processing_rule_name
            __props__.__dict__["location"] = location
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:alertsmanagement:AlertProcessingRuleByName"), pulumi.Alias(type_="azure-native:alertsmanagement/v20181102privatepreview:AlertProcessingRuleByName"), pulumi.Alias(type_="azure-native:alertsmanagement/v20190505preview:AlertProcessingRuleByName"), pulumi.Alias(type_="azure-native:alertsmanagement/v20210808preview:AlertProcessingRuleByName"), pulumi.Alias(type_="azure-native:alertsmanagement/v20230501preview:AlertProcessingRuleByName"), pulumi.Alias(type_="azure-native:alertsmanagement/v20240301preview:AlertProcessingRuleByName")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AlertProcessingRuleByName, __self__).__init__(
            'azure-native:alertsmanagement/v20210808:AlertProcessingRuleByName',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AlertProcessingRuleByName':
        """
        Get an existing AlertProcessingRuleByName resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AlertProcessingRuleByNameArgs.__new__(AlertProcessingRuleByNameArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return AlertProcessingRuleByName(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.AlertProcessingRulePropertiesResponse']:
        """
        Alert processing rule properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Alert processing rule system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

