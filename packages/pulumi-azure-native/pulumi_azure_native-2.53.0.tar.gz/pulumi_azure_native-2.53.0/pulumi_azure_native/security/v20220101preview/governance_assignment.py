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

__all__ = ['GovernanceAssignmentArgs', 'GovernanceAssignment']

@pulumi.input_type
class GovernanceAssignmentArgs:
    def __init__(__self__, *,
                 assessment_name: pulumi.Input[str],
                 remediation_due_date: pulumi.Input[str],
                 scope: pulumi.Input[str],
                 additional_data: Optional[pulumi.Input['GovernanceAssignmentAdditionalDataArgs']] = None,
                 assignment_key: Optional[pulumi.Input[str]] = None,
                 governance_email_notification: Optional[pulumi.Input['GovernanceEmailNotificationArgs']] = None,
                 is_grace_period: Optional[pulumi.Input[bool]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 remediation_eta: Optional[pulumi.Input['RemediationEtaArgs']] = None):
        """
        The set of arguments for constructing a GovernanceAssignment resource.
        :param pulumi.Input[str] assessment_name: The Assessment Key - A unique key for the assessment type
        :param pulumi.Input[str] remediation_due_date: The remediation due-date - after this date Secure Score will be affected (in case of  active grace-period)
        :param pulumi.Input[str] scope: The scope of the Governance assignments. Valid scopes are: subscription (format: 'subscriptions/{subscriptionId}'), or security connector (format: 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName})'
        :param pulumi.Input['GovernanceAssignmentAdditionalDataArgs'] additional_data: The additional data for the governance assignment - e.g. links to ticket (optional), see example
        :param pulumi.Input[str] assignment_key: The governance assignment key - the assessment key of the required governance assignment
        :param pulumi.Input['GovernanceEmailNotificationArgs'] governance_email_notification: The email notifications settings for the governance rule, states whether to disable notifications for mangers and owners
        :param pulumi.Input[bool] is_grace_period: Defines whether there is a grace period on the governance assignment
        :param pulumi.Input[str] owner: The Owner for the governance assignment - e.g. user@contoso.com - see example
        :param pulumi.Input['RemediationEtaArgs'] remediation_eta: The ETA (estimated time of arrival) for remediation (optional), see example
        """
        pulumi.set(__self__, "assessment_name", assessment_name)
        pulumi.set(__self__, "remediation_due_date", remediation_due_date)
        pulumi.set(__self__, "scope", scope)
        if additional_data is not None:
            pulumi.set(__self__, "additional_data", additional_data)
        if assignment_key is not None:
            pulumi.set(__self__, "assignment_key", assignment_key)
        if governance_email_notification is not None:
            pulumi.set(__self__, "governance_email_notification", governance_email_notification)
        if is_grace_period is not None:
            pulumi.set(__self__, "is_grace_period", is_grace_period)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if remediation_eta is not None:
            pulumi.set(__self__, "remediation_eta", remediation_eta)

    @property
    @pulumi.getter(name="assessmentName")
    def assessment_name(self) -> pulumi.Input[str]:
        """
        The Assessment Key - A unique key for the assessment type
        """
        return pulumi.get(self, "assessment_name")

    @assessment_name.setter
    def assessment_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "assessment_name", value)

    @property
    @pulumi.getter(name="remediationDueDate")
    def remediation_due_date(self) -> pulumi.Input[str]:
        """
        The remediation due-date - after this date Secure Score will be affected (in case of  active grace-period)
        """
        return pulumi.get(self, "remediation_due_date")

    @remediation_due_date.setter
    def remediation_due_date(self, value: pulumi.Input[str]):
        pulumi.set(self, "remediation_due_date", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope of the Governance assignments. Valid scopes are: subscription (format: 'subscriptions/{subscriptionId}'), or security connector (format: 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName})'
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> Optional[pulumi.Input['GovernanceAssignmentAdditionalDataArgs']]:
        """
        The additional data for the governance assignment - e.g. links to ticket (optional), see example
        """
        return pulumi.get(self, "additional_data")

    @additional_data.setter
    def additional_data(self, value: Optional[pulumi.Input['GovernanceAssignmentAdditionalDataArgs']]):
        pulumi.set(self, "additional_data", value)

    @property
    @pulumi.getter(name="assignmentKey")
    def assignment_key(self) -> Optional[pulumi.Input[str]]:
        """
        The governance assignment key - the assessment key of the required governance assignment
        """
        return pulumi.get(self, "assignment_key")

    @assignment_key.setter
    def assignment_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assignment_key", value)

    @property
    @pulumi.getter(name="governanceEmailNotification")
    def governance_email_notification(self) -> Optional[pulumi.Input['GovernanceEmailNotificationArgs']]:
        """
        The email notifications settings for the governance rule, states whether to disable notifications for mangers and owners
        """
        return pulumi.get(self, "governance_email_notification")

    @governance_email_notification.setter
    def governance_email_notification(self, value: Optional[pulumi.Input['GovernanceEmailNotificationArgs']]):
        pulumi.set(self, "governance_email_notification", value)

    @property
    @pulumi.getter(name="isGracePeriod")
    def is_grace_period(self) -> Optional[pulumi.Input[bool]]:
        """
        Defines whether there is a grace period on the governance assignment
        """
        return pulumi.get(self, "is_grace_period")

    @is_grace_period.setter
    def is_grace_period(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_grace_period", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        The Owner for the governance assignment - e.g. user@contoso.com - see example
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter(name="remediationEta")
    def remediation_eta(self) -> Optional[pulumi.Input['RemediationEtaArgs']]:
        """
        The ETA (estimated time of arrival) for remediation (optional), see example
        """
        return pulumi.get(self, "remediation_eta")

    @remediation_eta.setter
    def remediation_eta(self, value: Optional[pulumi.Input['RemediationEtaArgs']]):
        pulumi.set(self, "remediation_eta", value)


class GovernanceAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_data: Optional[pulumi.Input[Union['GovernanceAssignmentAdditionalDataArgs', 'GovernanceAssignmentAdditionalDataArgsDict']]] = None,
                 assessment_name: Optional[pulumi.Input[str]] = None,
                 assignment_key: Optional[pulumi.Input[str]] = None,
                 governance_email_notification: Optional[pulumi.Input[Union['GovernanceEmailNotificationArgs', 'GovernanceEmailNotificationArgsDict']]] = None,
                 is_grace_period: Optional[pulumi.Input[bool]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 remediation_due_date: Optional[pulumi.Input[str]] = None,
                 remediation_eta: Optional[pulumi.Input[Union['RemediationEtaArgs', 'RemediationEtaArgsDict']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Governance assignment over a given scope

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['GovernanceAssignmentAdditionalDataArgs', 'GovernanceAssignmentAdditionalDataArgsDict']] additional_data: The additional data for the governance assignment - e.g. links to ticket (optional), see example
        :param pulumi.Input[str] assessment_name: The Assessment Key - A unique key for the assessment type
        :param pulumi.Input[str] assignment_key: The governance assignment key - the assessment key of the required governance assignment
        :param pulumi.Input[Union['GovernanceEmailNotificationArgs', 'GovernanceEmailNotificationArgsDict']] governance_email_notification: The email notifications settings for the governance rule, states whether to disable notifications for mangers and owners
        :param pulumi.Input[bool] is_grace_period: Defines whether there is a grace period on the governance assignment
        :param pulumi.Input[str] owner: The Owner for the governance assignment - e.g. user@contoso.com - see example
        :param pulumi.Input[str] remediation_due_date: The remediation due-date - after this date Secure Score will be affected (in case of  active grace-period)
        :param pulumi.Input[Union['RemediationEtaArgs', 'RemediationEtaArgsDict']] remediation_eta: The ETA (estimated time of arrival) for remediation (optional), see example
        :param pulumi.Input[str] scope: The scope of the Governance assignments. Valid scopes are: subscription (format: 'subscriptions/{subscriptionId}'), or security connector (format: 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/securityConnectors/{securityConnectorName})'
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GovernanceAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Governance assignment over a given scope

        :param str resource_name: The name of the resource.
        :param GovernanceAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GovernanceAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_data: Optional[pulumi.Input[Union['GovernanceAssignmentAdditionalDataArgs', 'GovernanceAssignmentAdditionalDataArgsDict']]] = None,
                 assessment_name: Optional[pulumi.Input[str]] = None,
                 assignment_key: Optional[pulumi.Input[str]] = None,
                 governance_email_notification: Optional[pulumi.Input[Union['GovernanceEmailNotificationArgs', 'GovernanceEmailNotificationArgsDict']]] = None,
                 is_grace_period: Optional[pulumi.Input[bool]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 remediation_due_date: Optional[pulumi.Input[str]] = None,
                 remediation_eta: Optional[pulumi.Input[Union['RemediationEtaArgs', 'RemediationEtaArgsDict']]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GovernanceAssignmentArgs.__new__(GovernanceAssignmentArgs)

            __props__.__dict__["additional_data"] = additional_data
            if assessment_name is None and not opts.urn:
                raise TypeError("Missing required property 'assessment_name'")
            __props__.__dict__["assessment_name"] = assessment_name
            __props__.__dict__["assignment_key"] = assignment_key
            __props__.__dict__["governance_email_notification"] = governance_email_notification
            __props__.__dict__["is_grace_period"] = is_grace_period
            __props__.__dict__["owner"] = owner
            if remediation_due_date is None and not opts.urn:
                raise TypeError("Missing required property 'remediation_due_date'")
            __props__.__dict__["remediation_due_date"] = remediation_due_date
            __props__.__dict__["remediation_eta"] = remediation_eta
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:security:GovernanceAssignment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GovernanceAssignment, __self__).__init__(
            'azure-native:security/v20220101preview:GovernanceAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GovernanceAssignment':
        """
        Get an existing GovernanceAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GovernanceAssignmentArgs.__new__(GovernanceAssignmentArgs)

        __props__.__dict__["additional_data"] = None
        __props__.__dict__["governance_email_notification"] = None
        __props__.__dict__["is_grace_period"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["owner"] = None
        __props__.__dict__["remediation_due_date"] = None
        __props__.__dict__["remediation_eta"] = None
        __props__.__dict__["type"] = None
        return GovernanceAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> pulumi.Output[Optional['outputs.GovernanceAssignmentAdditionalDataResponse']]:
        """
        The additional data for the governance assignment - e.g. links to ticket (optional), see example
        """
        return pulumi.get(self, "additional_data")

    @property
    @pulumi.getter(name="governanceEmailNotification")
    def governance_email_notification(self) -> pulumi.Output[Optional['outputs.GovernanceEmailNotificationResponse']]:
        """
        The email notifications settings for the governance rule, states whether to disable notifications for mangers and owners
        """
        return pulumi.get(self, "governance_email_notification")

    @property
    @pulumi.getter(name="isGracePeriod")
    def is_grace_period(self) -> pulumi.Output[Optional[bool]]:
        """
        Defines whether there is a grace period on the governance assignment
        """
        return pulumi.get(self, "is_grace_period")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[Optional[str]]:
        """
        The Owner for the governance assignment - e.g. user@contoso.com - see example
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="remediationDueDate")
    def remediation_due_date(self) -> pulumi.Output[str]:
        """
        The remediation due-date - after this date Secure Score will be affected (in case of  active grace-period)
        """
        return pulumi.get(self, "remediation_due_date")

    @property
    @pulumi.getter(name="remediationEta")
    def remediation_eta(self) -> pulumi.Output[Optional['outputs.RemediationEtaResponse']]:
        """
        The ETA (estimated time of arrival) for remediation (optional), see example
        """
        return pulumi.get(self, "remediation_eta")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

