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

__all__ = ['ActivityLogAlertArgs', 'ActivityLogAlert']

@pulumi.input_type
class ActivityLogAlertArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input['ActivityLogAlertActionListArgs'],
                 condition: pulumi.Input['ActivityLogAlertAllOfConditionArgs'],
                 resource_group_name: pulumi.Input[str],
                 scopes: pulumi.Input[Sequence[pulumi.Input[str]]],
                 activity_log_alert_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ActivityLogAlert resource.
        :param pulumi.Input['ActivityLogAlertActionListArgs'] actions: The actions that will activate when the condition is met.
        :param pulumi.Input['ActivityLogAlertAllOfConditionArgs'] condition: The condition that will cause this alert to activate.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: A list of resourceIds that will be used as prefixes. The alert will only apply to activityLogs with resourceIds that fall under one of these prefixes. This list must include at least one item.
        :param pulumi.Input[str] activity_log_alert_name: The name of the activity log alert.
        :param pulumi.Input[str] description: A description of this activity log alert.
        :param pulumi.Input[bool] enabled: Indicates whether this activity log alert is enabled. If an activity log alert is not enabled, then none of its actions will be activated.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "condition", condition)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "scopes", scopes)
        if activity_log_alert_name is not None:
            pulumi.set(__self__, "activity_log_alert_name", activity_log_alert_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enabled is None:
            enabled = True
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input['ActivityLogAlertActionListArgs']:
        """
        The actions that will activate when the condition is met.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input['ActivityLogAlertActionListArgs']):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def condition(self) -> pulumi.Input['ActivityLogAlertAllOfConditionArgs']:
        """
        The condition that will cause this alert to activate.
        """
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: pulumi.Input['ActivityLogAlertAllOfConditionArgs']):
        pulumi.set(self, "condition", value)

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
    def scopes(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of resourceIds that will be used as prefixes. The alert will only apply to activityLogs with resourceIds that fall under one of these prefixes. This list must include at least one item.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter(name="activityLogAlertName")
    def activity_log_alert_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the activity log alert.
        """
        return pulumi.get(self, "activity_log_alert_name")

    @activity_log_alert_name.setter
    def activity_log_alert_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "activity_log_alert_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of this activity log alert.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether this activity log alert is enabled. If an activity log alert is not enabled, then none of its actions will be activated.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ActivityLogAlert(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Union['ActivityLogAlertActionListArgs', 'ActivityLogAlertActionListArgsDict']]] = None,
                 activity_log_alert_name: Optional[pulumi.Input[str]] = None,
                 condition: Optional[pulumi.Input[Union['ActivityLogAlertAllOfConditionArgs', 'ActivityLogAlertAllOfConditionArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        An activity log alert resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ActivityLogAlertActionListArgs', 'ActivityLogAlertActionListArgsDict']] actions: The actions that will activate when the condition is met.
        :param pulumi.Input[str] activity_log_alert_name: The name of the activity log alert.
        :param pulumi.Input[Union['ActivityLogAlertAllOfConditionArgs', 'ActivityLogAlertAllOfConditionArgsDict']] condition: The condition that will cause this alert to activate.
        :param pulumi.Input[str] description: A description of this activity log alert.
        :param pulumi.Input[bool] enabled: Indicates whether this activity log alert is enabled. If an activity log alert is not enabled, then none of its actions will be activated.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: A list of resourceIds that will be used as prefixes. The alert will only apply to activityLogs with resourceIds that fall under one of these prefixes. This list must include at least one item.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ActivityLogAlertArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An activity log alert resource.

        :param str resource_name: The name of the resource.
        :param ActivityLogAlertArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ActivityLogAlertArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Union['ActivityLogAlertActionListArgs', 'ActivityLogAlertActionListArgsDict']]] = None,
                 activity_log_alert_name: Optional[pulumi.Input[str]] = None,
                 condition: Optional[pulumi.Input[Union['ActivityLogAlertAllOfConditionArgs', 'ActivityLogAlertAllOfConditionArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ActivityLogAlertArgs.__new__(ActivityLogAlertArgs)

            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__.__dict__["actions"] = actions
            __props__.__dict__["activity_log_alert_name"] = activity_log_alert_name
            if condition is None and not opts.urn:
                raise TypeError("Missing required property 'condition'")
            __props__.__dict__["condition"] = condition
            __props__.__dict__["description"] = description
            if enabled is None:
                enabled = True
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if scopes is None and not opts.urn:
                raise TypeError("Missing required property 'scopes'")
            __props__.__dict__["scopes"] = scopes
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights:ActivityLogAlert"), pulumi.Alias(type_="azure-native:insights/v20201001:ActivityLogAlert"), pulumi.Alias(type_="azure-native:insights/v20230101preview:ActivityLogAlert")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ActivityLogAlert, __self__).__init__(
            'azure-native:insights/v20170401:ActivityLogAlert',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ActivityLogAlert':
        """
        Get an existing ActivityLogAlert resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ActivityLogAlertArgs.__new__(ActivityLogAlertArgs)

        __props__.__dict__["actions"] = None
        __props__.__dict__["condition"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["scopes"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ActivityLogAlert(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output['outputs.ActivityLogAlertActionListResponse']:
        """
        The actions that will activate when the condition is met.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def condition(self) -> pulumi.Output['outputs.ActivityLogAlertAllOfConditionResponse']:
        """
        The condition that will cause this alert to activate.
        """
        return pulumi.get(self, "condition")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of this activity log alert.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether this activity log alert is enabled. If an activity log alert is not enabled, then none of its actions will be activated.
        """
        return pulumi.get(self, "enabled")

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
    def scopes(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of resourceIds that will be used as prefixes. The alert will only apply to activityLogs with resourceIds that fall under one of these prefixes. This list must include at least one item.
        """
        return pulumi.get(self, "scopes")

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

