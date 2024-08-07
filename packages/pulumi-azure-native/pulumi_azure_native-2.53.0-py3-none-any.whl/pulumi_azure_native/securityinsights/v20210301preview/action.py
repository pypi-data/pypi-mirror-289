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

__all__ = ['ActionArgs', 'Action']

@pulumi.input_type
class ActionArgs:
    def __init__(__self__, *,
                 logic_app_resource_id: pulumi.Input[str],
                 operational_insights_resource_provider: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 rule_id: pulumi.Input[str],
                 trigger_uri: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 action_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Action resource.
        :param pulumi.Input[str] logic_app_resource_id: Logic App Resource Id, /subscriptions/{my-subscription}/resourceGroups/{my-resource-group}/providers/Microsoft.Logic/workflows/{my-workflow-id}.
        :param pulumi.Input[str] operational_insights_resource_provider: The namespace of workspaces resource provider- Microsoft.OperationalInsights.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] rule_id: Alert rule ID
        :param pulumi.Input[str] trigger_uri: Logic App Callback URL for this specific workflow.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] action_id: Action ID
        """
        pulumi.set(__self__, "logic_app_resource_id", logic_app_resource_id)
        pulumi.set(__self__, "operational_insights_resource_provider", operational_insights_resource_provider)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "rule_id", rule_id)
        pulumi.set(__self__, "trigger_uri", trigger_uri)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if action_id is not None:
            pulumi.set(__self__, "action_id", action_id)

    @property
    @pulumi.getter(name="logicAppResourceId")
    def logic_app_resource_id(self) -> pulumi.Input[str]:
        """
        Logic App Resource Id, /subscriptions/{my-subscription}/resourceGroups/{my-resource-group}/providers/Microsoft.Logic/workflows/{my-workflow-id}.
        """
        return pulumi.get(self, "logic_app_resource_id")

    @logic_app_resource_id.setter
    def logic_app_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "logic_app_resource_id", value)

    @property
    @pulumi.getter(name="operationalInsightsResourceProvider")
    def operational_insights_resource_provider(self) -> pulumi.Input[str]:
        """
        The namespace of workspaces resource provider- Microsoft.OperationalInsights.
        """
        return pulumi.get(self, "operational_insights_resource_provider")

    @operational_insights_resource_provider.setter
    def operational_insights_resource_provider(self, value: pulumi.Input[str]):
        pulumi.set(self, "operational_insights_resource_provider", value)

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
    @pulumi.getter(name="ruleId")
    def rule_id(self) -> pulumi.Input[str]:
        """
        Alert rule ID
        """
        return pulumi.get(self, "rule_id")

    @rule_id.setter
    def rule_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "rule_id", value)

    @property
    @pulumi.getter(name="triggerUri")
    def trigger_uri(self) -> pulumi.Input[str]:
        """
        Logic App Callback URL for this specific workflow.
        """
        return pulumi.get(self, "trigger_uri")

    @trigger_uri.setter
    def trigger_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "trigger_uri", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="actionId")
    def action_id(self) -> Optional[pulumi.Input[str]]:
        """
        Action ID
        """
        return pulumi.get(self, "action_id")

    @action_id.setter
    def action_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_id", value)


class Action(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_id: Optional[pulumi.Input[str]] = None,
                 logic_app_resource_id: Optional[pulumi.Input[str]] = None,
                 operational_insights_resource_provider: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_id: Optional[pulumi.Input[str]] = None,
                 trigger_uri: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Action for alert rule.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action_id: Action ID
        :param pulumi.Input[str] logic_app_resource_id: Logic App Resource Id, /subscriptions/{my-subscription}/resourceGroups/{my-resource-group}/providers/Microsoft.Logic/workflows/{my-workflow-id}.
        :param pulumi.Input[str] operational_insights_resource_provider: The namespace of workspaces resource provider- Microsoft.OperationalInsights.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] rule_id: Alert rule ID
        :param pulumi.Input[str] trigger_uri: Logic App Callback URL for this specific workflow.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ActionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Action for alert rule.

        :param str resource_name: The name of the resource.
        :param ActionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ActionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action_id: Optional[pulumi.Input[str]] = None,
                 logic_app_resource_id: Optional[pulumi.Input[str]] = None,
                 operational_insights_resource_provider: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_id: Optional[pulumi.Input[str]] = None,
                 trigger_uri: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ActionArgs.__new__(ActionArgs)

            __props__.__dict__["action_id"] = action_id
            if logic_app_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'logic_app_resource_id'")
            __props__.__dict__["logic_app_resource_id"] = logic_app_resource_id
            if operational_insights_resource_provider is None and not opts.urn:
                raise TypeError("Missing required property 'operational_insights_resource_provider'")
            __props__.__dict__["operational_insights_resource_provider"] = operational_insights_resource_provider
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if rule_id is None and not opts.urn:
                raise TypeError("Missing required property 'rule_id'")
            __props__.__dict__["rule_id"] = rule_id
            if trigger_uri is None and not opts.urn:
                raise TypeError("Missing required property 'trigger_uri'")
            __props__.__dict__["trigger_uri"] = trigger_uri
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["workflow_id"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20190101preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20200101:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20211001:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20220801:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20221001preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20221101:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20221101preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20221201preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20230201:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20230201preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20230301preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20230601preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20230701preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20230901preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20231001preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20231101:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20231201preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20240101preview:Action"), pulumi.Alias(type_="azure-native:securityinsights/v20240301:Action")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Action, __self__).__init__(
            'azure-native:securityinsights/v20210301preview:Action',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Action':
        """
        Get an existing Action resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ActionArgs.__new__(ActionArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["logic_app_resource_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["workflow_id"] = None
        return Action(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="logicAppResourceId")
    def logic_app_resource_id(self) -> pulumi.Output[str]:
        """
        Logic App Resource Id, /subscriptions/{my-subscription}/resourceGroups/{my-resource-group}/providers/Microsoft.Logic/workflows/{my-workflow-id}.
        """
        return pulumi.get(self, "logic_app_resource_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

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
        Azure resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workflowId")
    def workflow_id(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the logic app's workflow.
        """
        return pulumi.get(self, "workflow_id")

