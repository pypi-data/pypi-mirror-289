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

__all__ = ['AssessmentMetadataInSubscriptionArgs', 'AssessmentMetadataInSubscription']

@pulumi.input_type
class AssessmentMetadataInSubscriptionArgs:
    def __init__(__self__, *,
                 assessment_type: pulumi.Input[Union[str, 'AssessmentType']],
                 display_name: pulumi.Input[str],
                 severity: pulumi.Input[Union[str, 'Severity']],
                 assessment_metadata_name: Optional[pulumi.Input[str]] = None,
                 categories: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Categories']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 implementation_effort: Optional[pulumi.Input[Union[str, 'ImplementationEffort']]] = None,
                 partner_data: Optional[pulumi.Input['SecurityAssessmentMetadataPartnerDataArgs']] = None,
                 planned_deprecation_date: Optional[pulumi.Input[str]] = None,
                 preview: Optional[pulumi.Input[bool]] = None,
                 publish_dates: Optional[pulumi.Input['SecurityAssessmentMetadataPropertiesResponsePublishDatesArgs']] = None,
                 remediation_description: Optional[pulumi.Input[str]] = None,
                 tactics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Tactics']]]]] = None,
                 techniques: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Techniques']]]]] = None,
                 threats: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Threats']]]]] = None,
                 user_impact: Optional[pulumi.Input[Union[str, 'UserImpact']]] = None):
        """
        The set of arguments for constructing a AssessmentMetadataInSubscription resource.
        :param pulumi.Input[Union[str, 'AssessmentType']] assessment_type: BuiltIn if the assessment based on built-in Azure Policy definition, Custom if the assessment based on custom Azure Policy definition
        :param pulumi.Input[str] display_name: User friendly display name of the assessment
        :param pulumi.Input[Union[str, 'Severity']] severity: The severity level of the assessment
        :param pulumi.Input[str] assessment_metadata_name: The Assessment Key - Unique key for the assessment type
        :param pulumi.Input[str] description: Human readable description of the assessment
        :param pulumi.Input[Union[str, 'ImplementationEffort']] implementation_effort: The implementation effort required to remediate this assessment
        :param pulumi.Input['SecurityAssessmentMetadataPartnerDataArgs'] partner_data: Describes the partner that created the assessment
        :param pulumi.Input[bool] preview: True if this assessment is in preview release status
        :param pulumi.Input[str] remediation_description: Human readable description of what you should do to mitigate this security issue
        :param pulumi.Input[Union[str, 'UserImpact']] user_impact: The user impact of the assessment
        """
        pulumi.set(__self__, "assessment_type", assessment_type)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "severity", severity)
        if assessment_metadata_name is not None:
            pulumi.set(__self__, "assessment_metadata_name", assessment_metadata_name)
        if categories is not None:
            pulumi.set(__self__, "categories", categories)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if implementation_effort is not None:
            pulumi.set(__self__, "implementation_effort", implementation_effort)
        if partner_data is not None:
            pulumi.set(__self__, "partner_data", partner_data)
        if planned_deprecation_date is not None:
            pulumi.set(__self__, "planned_deprecation_date", planned_deprecation_date)
        if preview is not None:
            pulumi.set(__self__, "preview", preview)
        if publish_dates is not None:
            pulumi.set(__self__, "publish_dates", publish_dates)
        if remediation_description is not None:
            pulumi.set(__self__, "remediation_description", remediation_description)
        if tactics is not None:
            pulumi.set(__self__, "tactics", tactics)
        if techniques is not None:
            pulumi.set(__self__, "techniques", techniques)
        if threats is not None:
            pulumi.set(__self__, "threats", threats)
        if user_impact is not None:
            pulumi.set(__self__, "user_impact", user_impact)

    @property
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> pulumi.Input[Union[str, 'AssessmentType']]:
        """
        BuiltIn if the assessment based on built-in Azure Policy definition, Custom if the assessment based on custom Azure Policy definition
        """
        return pulumi.get(self, "assessment_type")

    @assessment_type.setter
    def assessment_type(self, value: pulumi.Input[Union[str, 'AssessmentType']]):
        pulumi.set(self, "assessment_type", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        User friendly display name of the assessment
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Input[Union[str, 'Severity']]:
        """
        The severity level of the assessment
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: pulumi.Input[Union[str, 'Severity']]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter(name="assessmentMetadataName")
    def assessment_metadata_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Assessment Key - Unique key for the assessment type
        """
        return pulumi.get(self, "assessment_metadata_name")

    @assessment_metadata_name.setter
    def assessment_metadata_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assessment_metadata_name", value)

    @property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Categories']]]]]:
        return pulumi.get(self, "categories")

    @categories.setter
    def categories(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Categories']]]]]):
        pulumi.set(self, "categories", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable description of the assessment
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="implementationEffort")
    def implementation_effort(self) -> Optional[pulumi.Input[Union[str, 'ImplementationEffort']]]:
        """
        The implementation effort required to remediate this assessment
        """
        return pulumi.get(self, "implementation_effort")

    @implementation_effort.setter
    def implementation_effort(self, value: Optional[pulumi.Input[Union[str, 'ImplementationEffort']]]):
        pulumi.set(self, "implementation_effort", value)

    @property
    @pulumi.getter(name="partnerData")
    def partner_data(self) -> Optional[pulumi.Input['SecurityAssessmentMetadataPartnerDataArgs']]:
        """
        Describes the partner that created the assessment
        """
        return pulumi.get(self, "partner_data")

    @partner_data.setter
    def partner_data(self, value: Optional[pulumi.Input['SecurityAssessmentMetadataPartnerDataArgs']]):
        pulumi.set(self, "partner_data", value)

    @property
    @pulumi.getter(name="plannedDeprecationDate")
    def planned_deprecation_date(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "planned_deprecation_date")

    @planned_deprecation_date.setter
    def planned_deprecation_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "planned_deprecation_date", value)

    @property
    @pulumi.getter
    def preview(self) -> Optional[pulumi.Input[bool]]:
        """
        True if this assessment is in preview release status
        """
        return pulumi.get(self, "preview")

    @preview.setter
    def preview(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "preview", value)

    @property
    @pulumi.getter(name="publishDates")
    def publish_dates(self) -> Optional[pulumi.Input['SecurityAssessmentMetadataPropertiesResponsePublishDatesArgs']]:
        return pulumi.get(self, "publish_dates")

    @publish_dates.setter
    def publish_dates(self, value: Optional[pulumi.Input['SecurityAssessmentMetadataPropertiesResponsePublishDatesArgs']]):
        pulumi.set(self, "publish_dates", value)

    @property
    @pulumi.getter(name="remediationDescription")
    def remediation_description(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable description of what you should do to mitigate this security issue
        """
        return pulumi.get(self, "remediation_description")

    @remediation_description.setter
    def remediation_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "remediation_description", value)

    @property
    @pulumi.getter
    def tactics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Tactics']]]]]:
        return pulumi.get(self, "tactics")

    @tactics.setter
    def tactics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Tactics']]]]]):
        pulumi.set(self, "tactics", value)

    @property
    @pulumi.getter
    def techniques(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Techniques']]]]]:
        return pulumi.get(self, "techniques")

    @techniques.setter
    def techniques(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Techniques']]]]]):
        pulumi.set(self, "techniques", value)

    @property
    @pulumi.getter
    def threats(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Threats']]]]]:
        return pulumi.get(self, "threats")

    @threats.setter
    def threats(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Threats']]]]]):
        pulumi.set(self, "threats", value)

    @property
    @pulumi.getter(name="userImpact")
    def user_impact(self) -> Optional[pulumi.Input[Union[str, 'UserImpact']]]:
        """
        The user impact of the assessment
        """
        return pulumi.get(self, "user_impact")

    @user_impact.setter
    def user_impact(self, value: Optional[pulumi.Input[Union[str, 'UserImpact']]]):
        pulumi.set(self, "user_impact", value)


class AssessmentMetadataInSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_metadata_name: Optional[pulumi.Input[str]] = None,
                 assessment_type: Optional[pulumi.Input[Union[str, 'AssessmentType']]] = None,
                 categories: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Categories']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 implementation_effort: Optional[pulumi.Input[Union[str, 'ImplementationEffort']]] = None,
                 partner_data: Optional[pulumi.Input[Union['SecurityAssessmentMetadataPartnerDataArgs', 'SecurityAssessmentMetadataPartnerDataArgsDict']]] = None,
                 planned_deprecation_date: Optional[pulumi.Input[str]] = None,
                 preview: Optional[pulumi.Input[bool]] = None,
                 publish_dates: Optional[pulumi.Input[Union['SecurityAssessmentMetadataPropertiesResponsePublishDatesArgs', 'SecurityAssessmentMetadataPropertiesResponsePublishDatesArgsDict']]] = None,
                 remediation_description: Optional[pulumi.Input[str]] = None,
                 severity: Optional[pulumi.Input[Union[str, 'Severity']]] = None,
                 tactics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Tactics']]]]] = None,
                 techniques: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Techniques']]]]] = None,
                 threats: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Threats']]]]] = None,
                 user_impact: Optional[pulumi.Input[Union[str, 'UserImpact']]] = None,
                 __props__=None):
        """
        Security assessment metadata response
        Azure REST API version: 2021-06-01. Prior API version in Azure Native 1.x: 2020-01-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] assessment_metadata_name: The Assessment Key - Unique key for the assessment type
        :param pulumi.Input[Union[str, 'AssessmentType']] assessment_type: BuiltIn if the assessment based on built-in Azure Policy definition, Custom if the assessment based on custom Azure Policy definition
        :param pulumi.Input[str] description: Human readable description of the assessment
        :param pulumi.Input[str] display_name: User friendly display name of the assessment
        :param pulumi.Input[Union[str, 'ImplementationEffort']] implementation_effort: The implementation effort required to remediate this assessment
        :param pulumi.Input[Union['SecurityAssessmentMetadataPartnerDataArgs', 'SecurityAssessmentMetadataPartnerDataArgsDict']] partner_data: Describes the partner that created the assessment
        :param pulumi.Input[bool] preview: True if this assessment is in preview release status
        :param pulumi.Input[str] remediation_description: Human readable description of what you should do to mitigate this security issue
        :param pulumi.Input[Union[str, 'Severity']] severity: The severity level of the assessment
        :param pulumi.Input[Union[str, 'UserImpact']] user_impact: The user impact of the assessment
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssessmentMetadataInSubscriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Security assessment metadata response
        Azure REST API version: 2021-06-01. Prior API version in Azure Native 1.x: 2020-01-01.

        :param str resource_name: The name of the resource.
        :param AssessmentMetadataInSubscriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssessmentMetadataInSubscriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assessment_metadata_name: Optional[pulumi.Input[str]] = None,
                 assessment_type: Optional[pulumi.Input[Union[str, 'AssessmentType']]] = None,
                 categories: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Categories']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 implementation_effort: Optional[pulumi.Input[Union[str, 'ImplementationEffort']]] = None,
                 partner_data: Optional[pulumi.Input[Union['SecurityAssessmentMetadataPartnerDataArgs', 'SecurityAssessmentMetadataPartnerDataArgsDict']]] = None,
                 planned_deprecation_date: Optional[pulumi.Input[str]] = None,
                 preview: Optional[pulumi.Input[bool]] = None,
                 publish_dates: Optional[pulumi.Input[Union['SecurityAssessmentMetadataPropertiesResponsePublishDatesArgs', 'SecurityAssessmentMetadataPropertiesResponsePublishDatesArgsDict']]] = None,
                 remediation_description: Optional[pulumi.Input[str]] = None,
                 severity: Optional[pulumi.Input[Union[str, 'Severity']]] = None,
                 tactics: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Tactics']]]]] = None,
                 techniques: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Techniques']]]]] = None,
                 threats: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'Threats']]]]] = None,
                 user_impact: Optional[pulumi.Input[Union[str, 'UserImpact']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssessmentMetadataInSubscriptionArgs.__new__(AssessmentMetadataInSubscriptionArgs)

            __props__.__dict__["assessment_metadata_name"] = assessment_metadata_name
            if assessment_type is None and not opts.urn:
                raise TypeError("Missing required property 'assessment_type'")
            __props__.__dict__["assessment_type"] = assessment_type
            __props__.__dict__["categories"] = categories
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["implementation_effort"] = implementation_effort
            __props__.__dict__["partner_data"] = partner_data
            __props__.__dict__["planned_deprecation_date"] = planned_deprecation_date
            __props__.__dict__["preview"] = preview
            __props__.__dict__["publish_dates"] = publish_dates
            __props__.__dict__["remediation_description"] = remediation_description
            if severity is None and not opts.urn:
                raise TypeError("Missing required property 'severity'")
            __props__.__dict__["severity"] = severity
            __props__.__dict__["tactics"] = tactics
            __props__.__dict__["techniques"] = techniques
            __props__.__dict__["threats"] = threats
            __props__.__dict__["user_impact"] = user_impact
            __props__.__dict__["name"] = None
            __props__.__dict__["policy_definition_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:security/v20190101preview:AssessmentMetadataInSubscription"), pulumi.Alias(type_="azure-native:security/v20200101:AssessmentMetadataInSubscription"), pulumi.Alias(type_="azure-native:security/v20210601:AssessmentMetadataInSubscription")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AssessmentMetadataInSubscription, __self__).__init__(
            'azure-native:security:AssessmentMetadataInSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AssessmentMetadataInSubscription':
        """
        Get an existing AssessmentMetadataInSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AssessmentMetadataInSubscriptionArgs.__new__(AssessmentMetadataInSubscriptionArgs)

        __props__.__dict__["assessment_type"] = None
        __props__.__dict__["categories"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["implementation_effort"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partner_data"] = None
        __props__.__dict__["planned_deprecation_date"] = None
        __props__.__dict__["policy_definition_id"] = None
        __props__.__dict__["preview"] = None
        __props__.__dict__["publish_dates"] = None
        __props__.__dict__["remediation_description"] = None
        __props__.__dict__["severity"] = None
        __props__.__dict__["tactics"] = None
        __props__.__dict__["techniques"] = None
        __props__.__dict__["threats"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_impact"] = None
        return AssessmentMetadataInSubscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="assessmentType")
    def assessment_type(self) -> pulumi.Output[str]:
        """
        BuiltIn if the assessment based on built-in Azure Policy definition, Custom if the assessment based on custom Azure Policy definition
        """
        return pulumi.get(self, "assessment_type")

    @property
    @pulumi.getter
    def categories(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Human readable description of the assessment
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        User friendly display name of the assessment
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="implementationEffort")
    def implementation_effort(self) -> pulumi.Output[Optional[str]]:
        """
        The implementation effort required to remediate this assessment
        """
        return pulumi.get(self, "implementation_effort")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerData")
    def partner_data(self) -> pulumi.Output[Optional['outputs.SecurityAssessmentMetadataPartnerDataResponse']]:
        """
        Describes the partner that created the assessment
        """
        return pulumi.get(self, "partner_data")

    @property
    @pulumi.getter(name="plannedDeprecationDate")
    def planned_deprecation_date(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "planned_deprecation_date")

    @property
    @pulumi.getter(name="policyDefinitionId")
    def policy_definition_id(self) -> pulumi.Output[str]:
        """
        Azure resource ID of the policy definition that turns this assessment calculation on
        """
        return pulumi.get(self, "policy_definition_id")

    @property
    @pulumi.getter
    def preview(self) -> pulumi.Output[Optional[bool]]:
        """
        True if this assessment is in preview release status
        """
        return pulumi.get(self, "preview")

    @property
    @pulumi.getter(name="publishDates")
    def publish_dates(self) -> pulumi.Output[Optional['outputs.SecurityAssessmentMetadataPropertiesResponseResponsePublishDates']]:
        return pulumi.get(self, "publish_dates")

    @property
    @pulumi.getter(name="remediationDescription")
    def remediation_description(self) -> pulumi.Output[Optional[str]]:
        """
        Human readable description of what you should do to mitigate this security issue
        """
        return pulumi.get(self, "remediation_description")

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Output[str]:
        """
        The severity level of the assessment
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter
    def tactics(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "tactics")

    @property
    @pulumi.getter
    def techniques(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "techniques")

    @property
    @pulumi.getter
    def threats(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "threats")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userImpact")
    def user_impact(self) -> pulumi.Output[Optional[str]]:
        """
        The user impact of the assessment
        """
        return pulumi.get(self, "user_impact")

