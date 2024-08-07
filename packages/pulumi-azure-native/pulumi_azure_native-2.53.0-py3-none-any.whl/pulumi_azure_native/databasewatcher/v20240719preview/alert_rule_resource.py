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

__all__ = ['AlertRuleResourceArgs', 'AlertRuleResource']

@pulumi.input_type
class AlertRuleResourceArgs:
    def __init__(__self__, *,
                 alert_rule_resource_id: pulumi.Input[str],
                 alert_rule_template_id: pulumi.Input[str],
                 alert_rule_template_version: pulumi.Input[str],
                 created_with_properties: pulumi.Input[Union[str, 'AlertRuleCreationProperties']],
                 creation_time: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 watcher_name: pulumi.Input[str],
                 alert_rule_resource_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AlertRuleResource resource.
        :param pulumi.Input[str] alert_rule_resource_id: The resource ID of the alert rule resource.
        :param pulumi.Input[str] alert_rule_template_id: The template ID associated with alert rule resource.
        :param pulumi.Input[str] alert_rule_template_version: The alert rule template version.
        :param pulumi.Input[Union[str, 'AlertRuleCreationProperties']] created_with_properties: The properties with which the alert rule resource was created.
        :param pulumi.Input[str] creation_time: The creation time of the alert rule resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] watcher_name: The database watcher name.
        :param pulumi.Input[str] alert_rule_resource_name: The alert rule proxy resource name.
        """
        pulumi.set(__self__, "alert_rule_resource_id", alert_rule_resource_id)
        pulumi.set(__self__, "alert_rule_template_id", alert_rule_template_id)
        pulumi.set(__self__, "alert_rule_template_version", alert_rule_template_version)
        pulumi.set(__self__, "created_with_properties", created_with_properties)
        pulumi.set(__self__, "creation_time", creation_time)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "watcher_name", watcher_name)
        if alert_rule_resource_name is not None:
            pulumi.set(__self__, "alert_rule_resource_name", alert_rule_resource_name)

    @property
    @pulumi.getter(name="alertRuleResourceId")
    def alert_rule_resource_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the alert rule resource.
        """
        return pulumi.get(self, "alert_rule_resource_id")

    @alert_rule_resource_id.setter
    def alert_rule_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "alert_rule_resource_id", value)

    @property
    @pulumi.getter(name="alertRuleTemplateId")
    def alert_rule_template_id(self) -> pulumi.Input[str]:
        """
        The template ID associated with alert rule resource.
        """
        return pulumi.get(self, "alert_rule_template_id")

    @alert_rule_template_id.setter
    def alert_rule_template_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "alert_rule_template_id", value)

    @property
    @pulumi.getter(name="alertRuleTemplateVersion")
    def alert_rule_template_version(self) -> pulumi.Input[str]:
        """
        The alert rule template version.
        """
        return pulumi.get(self, "alert_rule_template_version")

    @alert_rule_template_version.setter
    def alert_rule_template_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "alert_rule_template_version", value)

    @property
    @pulumi.getter(name="createdWithProperties")
    def created_with_properties(self) -> pulumi.Input[Union[str, 'AlertRuleCreationProperties']]:
        """
        The properties with which the alert rule resource was created.
        """
        return pulumi.get(self, "created_with_properties")

    @created_with_properties.setter
    def created_with_properties(self, value: pulumi.Input[Union[str, 'AlertRuleCreationProperties']]):
        pulumi.set(self, "created_with_properties", value)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Input[str]:
        """
        The creation time of the alert rule resource.
        """
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: pulumi.Input[str]):
        pulumi.set(self, "creation_time", value)

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
    @pulumi.getter(name="watcherName")
    def watcher_name(self) -> pulumi.Input[str]:
        """
        The database watcher name.
        """
        return pulumi.get(self, "watcher_name")

    @watcher_name.setter
    def watcher_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "watcher_name", value)

    @property
    @pulumi.getter(name="alertRuleResourceName")
    def alert_rule_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The alert rule proxy resource name.
        """
        return pulumi.get(self, "alert_rule_resource_name")

    @alert_rule_resource_name.setter
    def alert_rule_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_rule_resource_name", value)


class AlertRuleResource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alert_rule_resource_id: Optional[pulumi.Input[str]] = None,
                 alert_rule_resource_name: Optional[pulumi.Input[str]] = None,
                 alert_rule_template_id: Optional[pulumi.Input[str]] = None,
                 alert_rule_template_version: Optional[pulumi.Input[str]] = None,
                 created_with_properties: Optional[pulumi.Input[Union[str, 'AlertRuleCreationProperties']]] = None,
                 creation_time: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 watcher_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Concrete proxy resource types can be created by aliasing this type using a specific property type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alert_rule_resource_id: The resource ID of the alert rule resource.
        :param pulumi.Input[str] alert_rule_resource_name: The alert rule proxy resource name.
        :param pulumi.Input[str] alert_rule_template_id: The template ID associated with alert rule resource.
        :param pulumi.Input[str] alert_rule_template_version: The alert rule template version.
        :param pulumi.Input[Union[str, 'AlertRuleCreationProperties']] created_with_properties: The properties with which the alert rule resource was created.
        :param pulumi.Input[str] creation_time: The creation time of the alert rule resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] watcher_name: The database watcher name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AlertRuleResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Concrete proxy resource types can be created by aliasing this type using a specific property type.

        :param str resource_name: The name of the resource.
        :param AlertRuleResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AlertRuleResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alert_rule_resource_id: Optional[pulumi.Input[str]] = None,
                 alert_rule_resource_name: Optional[pulumi.Input[str]] = None,
                 alert_rule_template_id: Optional[pulumi.Input[str]] = None,
                 alert_rule_template_version: Optional[pulumi.Input[str]] = None,
                 created_with_properties: Optional[pulumi.Input[Union[str, 'AlertRuleCreationProperties']]] = None,
                 creation_time: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 watcher_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AlertRuleResourceArgs.__new__(AlertRuleResourceArgs)

            if alert_rule_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'alert_rule_resource_id'")
            __props__.__dict__["alert_rule_resource_id"] = alert_rule_resource_id
            __props__.__dict__["alert_rule_resource_name"] = alert_rule_resource_name
            if alert_rule_template_id is None and not opts.urn:
                raise TypeError("Missing required property 'alert_rule_template_id'")
            __props__.__dict__["alert_rule_template_id"] = alert_rule_template_id
            if alert_rule_template_version is None and not opts.urn:
                raise TypeError("Missing required property 'alert_rule_template_version'")
            __props__.__dict__["alert_rule_template_version"] = alert_rule_template_version
            if created_with_properties is None and not opts.urn:
                raise TypeError("Missing required property 'created_with_properties'")
            __props__.__dict__["created_with_properties"] = created_with_properties
            if creation_time is None and not opts.urn:
                raise TypeError("Missing required property 'creation_time'")
            __props__.__dict__["creation_time"] = creation_time
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if watcher_name is None and not opts.urn:
                raise TypeError("Missing required property 'watcher_name'")
            __props__.__dict__["watcher_name"] = watcher_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:databasewatcher:AlertRuleResource")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AlertRuleResource, __self__).__init__(
            'azure-native:databasewatcher/v20240719preview:AlertRuleResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AlertRuleResource':
        """
        Get an existing AlertRuleResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AlertRuleResourceArgs.__new__(AlertRuleResourceArgs)

        __props__.__dict__["alert_rule_resource_id"] = None
        __props__.__dict__["alert_rule_template_id"] = None
        __props__.__dict__["alert_rule_template_version"] = None
        __props__.__dict__["created_with_properties"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return AlertRuleResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alertRuleResourceId")
    def alert_rule_resource_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the alert rule resource.
        """
        return pulumi.get(self, "alert_rule_resource_id")

    @property
    @pulumi.getter(name="alertRuleTemplateId")
    def alert_rule_template_id(self) -> pulumi.Output[str]:
        """
        The template ID associated with alert rule resource.
        """
        return pulumi.get(self, "alert_rule_template_id")

    @property
    @pulumi.getter(name="alertRuleTemplateVersion")
    def alert_rule_template_version(self) -> pulumi.Output[str]:
        """
        The alert rule template version.
        """
        return pulumi.get(self, "alert_rule_template_version")

    @property
    @pulumi.getter(name="createdWithProperties")
    def created_with_properties(self) -> pulumi.Output[str]:
        """
        The properties with which the alert rule resource was created.
        """
        return pulumi.get(self, "created_with_properties")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The creation time of the alert rule resource.
        """
        return pulumi.get(self, "creation_time")

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
        The provisioning state of the alert rule resource.
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

