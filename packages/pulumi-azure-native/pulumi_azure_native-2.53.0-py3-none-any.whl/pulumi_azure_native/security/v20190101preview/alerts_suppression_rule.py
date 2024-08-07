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

__all__ = ['AlertsSuppressionRuleArgs', 'AlertsSuppressionRule']

@pulumi.input_type
class AlertsSuppressionRuleArgs:
    def __init__(__self__, *,
                 alert_type: pulumi.Input[str],
                 reason: pulumi.Input[str],
                 state: pulumi.Input[Union[str, 'RuleState']],
                 alerts_suppression_rule_name: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 expiration_date_utc: Optional[pulumi.Input[str]] = None,
                 suppression_alerts_scope: Optional[pulumi.Input['SuppressionAlertsScopeArgs']] = None):
        """
        The set of arguments for constructing a AlertsSuppressionRule resource.
        :param pulumi.Input[str] alert_type: Type of the alert to automatically suppress. For all alert types, use '*'
        :param pulumi.Input[str] reason: The reason for dismissing the alert
        :param pulumi.Input[Union[str, 'RuleState']] state: Possible states of the rule
        :param pulumi.Input[str] alerts_suppression_rule_name: The unique name of the suppression alert rule
        :param pulumi.Input[str] comment: Any comment regarding the rule
        :param pulumi.Input[str] expiration_date_utc: Expiration date of the rule, if value is not provided or provided as null there will no expiration at all
        :param pulumi.Input['SuppressionAlertsScopeArgs'] suppression_alerts_scope: The suppression conditions
        """
        pulumi.set(__self__, "alert_type", alert_type)
        pulumi.set(__self__, "reason", reason)
        pulumi.set(__self__, "state", state)
        if alerts_suppression_rule_name is not None:
            pulumi.set(__self__, "alerts_suppression_rule_name", alerts_suppression_rule_name)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if expiration_date_utc is not None:
            pulumi.set(__self__, "expiration_date_utc", expiration_date_utc)
        if suppression_alerts_scope is not None:
            pulumi.set(__self__, "suppression_alerts_scope", suppression_alerts_scope)

    @property
    @pulumi.getter(name="alertType")
    def alert_type(self) -> pulumi.Input[str]:
        """
        Type of the alert to automatically suppress. For all alert types, use '*'
        """
        return pulumi.get(self, "alert_type")

    @alert_type.setter
    def alert_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "alert_type", value)

    @property
    @pulumi.getter
    def reason(self) -> pulumi.Input[str]:
        """
        The reason for dismissing the alert
        """
        return pulumi.get(self, "reason")

    @reason.setter
    def reason(self, value: pulumi.Input[str]):
        pulumi.set(self, "reason", value)

    @property
    @pulumi.getter
    def state(self) -> pulumi.Input[Union[str, 'RuleState']]:
        """
        Possible states of the rule
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: pulumi.Input[Union[str, 'RuleState']]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="alertsSuppressionRuleName")
    def alerts_suppression_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The unique name of the suppression alert rule
        """
        return pulumi.get(self, "alerts_suppression_rule_name")

    @alerts_suppression_rule_name.setter
    def alerts_suppression_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alerts_suppression_rule_name", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Any comment regarding the rule
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="expirationDateUtc")
    def expiration_date_utc(self) -> Optional[pulumi.Input[str]]:
        """
        Expiration date of the rule, if value is not provided or provided as null there will no expiration at all
        """
        return pulumi.get(self, "expiration_date_utc")

    @expiration_date_utc.setter
    def expiration_date_utc(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_date_utc", value)

    @property
    @pulumi.getter(name="suppressionAlertsScope")
    def suppression_alerts_scope(self) -> Optional[pulumi.Input['SuppressionAlertsScopeArgs']]:
        """
        The suppression conditions
        """
        return pulumi.get(self, "suppression_alerts_scope")

    @suppression_alerts_scope.setter
    def suppression_alerts_scope(self, value: Optional[pulumi.Input['SuppressionAlertsScopeArgs']]):
        pulumi.set(self, "suppression_alerts_scope", value)


class AlertsSuppressionRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alert_type: Optional[pulumi.Input[str]] = None,
                 alerts_suppression_rule_name: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 expiration_date_utc: Optional[pulumi.Input[str]] = None,
                 reason: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'RuleState']]] = None,
                 suppression_alerts_scope: Optional[pulumi.Input[Union['SuppressionAlertsScopeArgs', 'SuppressionAlertsScopeArgsDict']]] = None,
                 __props__=None):
        """
        Describes the suppression rule

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] alert_type: Type of the alert to automatically suppress. For all alert types, use '*'
        :param pulumi.Input[str] alerts_suppression_rule_name: The unique name of the suppression alert rule
        :param pulumi.Input[str] comment: Any comment regarding the rule
        :param pulumi.Input[str] expiration_date_utc: Expiration date of the rule, if value is not provided or provided as null there will no expiration at all
        :param pulumi.Input[str] reason: The reason for dismissing the alert
        :param pulumi.Input[Union[str, 'RuleState']] state: Possible states of the rule
        :param pulumi.Input[Union['SuppressionAlertsScopeArgs', 'SuppressionAlertsScopeArgsDict']] suppression_alerts_scope: The suppression conditions
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AlertsSuppressionRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes the suppression rule

        :param str resource_name: The name of the resource.
        :param AlertsSuppressionRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AlertsSuppressionRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alert_type: Optional[pulumi.Input[str]] = None,
                 alerts_suppression_rule_name: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 expiration_date_utc: Optional[pulumi.Input[str]] = None,
                 reason: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'RuleState']]] = None,
                 suppression_alerts_scope: Optional[pulumi.Input[Union['SuppressionAlertsScopeArgs', 'SuppressionAlertsScopeArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AlertsSuppressionRuleArgs.__new__(AlertsSuppressionRuleArgs)

            if alert_type is None and not opts.urn:
                raise TypeError("Missing required property 'alert_type'")
            __props__.__dict__["alert_type"] = alert_type
            __props__.__dict__["alerts_suppression_rule_name"] = alerts_suppression_rule_name
            __props__.__dict__["comment"] = comment
            __props__.__dict__["expiration_date_utc"] = expiration_date_utc
            if reason is None and not opts.urn:
                raise TypeError("Missing required property 'reason'")
            __props__.__dict__["reason"] = reason
            if state is None and not opts.urn:
                raise TypeError("Missing required property 'state'")
            __props__.__dict__["state"] = state
            __props__.__dict__["suppression_alerts_scope"] = suppression_alerts_scope
            __props__.__dict__["last_modified_utc"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:security:AlertsSuppressionRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AlertsSuppressionRule, __self__).__init__(
            'azure-native:security/v20190101preview:AlertsSuppressionRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AlertsSuppressionRule':
        """
        Get an existing AlertsSuppressionRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AlertsSuppressionRuleArgs.__new__(AlertsSuppressionRuleArgs)

        __props__.__dict__["alert_type"] = None
        __props__.__dict__["comment"] = None
        __props__.__dict__["expiration_date_utc"] = None
        __props__.__dict__["last_modified_utc"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["reason"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["suppression_alerts_scope"] = None
        __props__.__dict__["type"] = None
        return AlertsSuppressionRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alertType")
    def alert_type(self) -> pulumi.Output[str]:
        """
        Type of the alert to automatically suppress. For all alert types, use '*'
        """
        return pulumi.get(self, "alert_type")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        Any comment regarding the rule
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter(name="expirationDateUtc")
    def expiration_date_utc(self) -> pulumi.Output[Optional[str]]:
        """
        Expiration date of the rule, if value is not provided or provided as null there will no expiration at all
        """
        return pulumi.get(self, "expiration_date_utc")

    @property
    @pulumi.getter(name="lastModifiedUtc")
    def last_modified_utc(self) -> pulumi.Output[str]:
        """
        The last time this rule was modified
        """
        return pulumi.get(self, "last_modified_utc")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def reason(self) -> pulumi.Output[str]:
        """
        The reason for dismissing the alert
        """
        return pulumi.get(self, "reason")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        Possible states of the rule
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="suppressionAlertsScope")
    def suppression_alerts_scope(self) -> pulumi.Output[Optional['outputs.SuppressionAlertsScopeResponse']]:
        """
        The suppression conditions
        """
        return pulumi.get(self, "suppression_alerts_scope")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

