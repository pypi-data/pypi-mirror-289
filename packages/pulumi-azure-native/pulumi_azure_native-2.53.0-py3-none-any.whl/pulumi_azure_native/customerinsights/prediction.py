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
from ._inputs import *

__all__ = ['PredictionArgs', 'Prediction']

@pulumi.input_type
class PredictionArgs:
    def __init__(__self__, *,
                 auto_analyze: pulumi.Input[bool],
                 hub_name: pulumi.Input[str],
                 mappings: pulumi.Input['PredictionMappingsArgs'],
                 negative_outcome_expression: pulumi.Input[str],
                 positive_outcome_expression: pulumi.Input[str],
                 primary_profile_type: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 scope_expression: pulumi.Input[str],
                 score_label: pulumi.Input[str],
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 grades: Optional[pulumi.Input[Sequence[pulumi.Input['PredictionGradesArgs']]]] = None,
                 involved_interaction_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 involved_kpi_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 involved_relationships: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 prediction_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Prediction resource.
        :param pulumi.Input[bool] auto_analyze: Whether do auto analyze.
        :param pulumi.Input[str] hub_name: The name of the hub.
        :param pulumi.Input['PredictionMappingsArgs'] mappings: Definition of the link mapping of prediction.
        :param pulumi.Input[str] negative_outcome_expression: Negative outcome expression.
        :param pulumi.Input[str] positive_outcome_expression: Positive outcome expression.
        :param pulumi.Input[str] primary_profile_type: Primary profile type.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] scope_expression: Scope expression.
        :param pulumi.Input[str] score_label: Score label.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] description: Description of the prediction.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] display_name: Display name of the prediction.
        :param pulumi.Input[Sequence[pulumi.Input['PredictionGradesArgs']]] grades: The prediction grades.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] involved_interaction_types: Interaction types involved in the prediction.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] involved_kpi_types: KPI types involved in the prediction.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] involved_relationships: Relationships involved in the prediction.
        :param pulumi.Input[str] prediction_name: Name of the prediction.
        """
        pulumi.set(__self__, "auto_analyze", auto_analyze)
        pulumi.set(__self__, "hub_name", hub_name)
        pulumi.set(__self__, "mappings", mappings)
        pulumi.set(__self__, "negative_outcome_expression", negative_outcome_expression)
        pulumi.set(__self__, "positive_outcome_expression", positive_outcome_expression)
        pulumi.set(__self__, "primary_profile_type", primary_profile_type)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "scope_expression", scope_expression)
        pulumi.set(__self__, "score_label", score_label)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if grades is not None:
            pulumi.set(__self__, "grades", grades)
        if involved_interaction_types is not None:
            pulumi.set(__self__, "involved_interaction_types", involved_interaction_types)
        if involved_kpi_types is not None:
            pulumi.set(__self__, "involved_kpi_types", involved_kpi_types)
        if involved_relationships is not None:
            pulumi.set(__self__, "involved_relationships", involved_relationships)
        if prediction_name is not None:
            pulumi.set(__self__, "prediction_name", prediction_name)

    @property
    @pulumi.getter(name="autoAnalyze")
    def auto_analyze(self) -> pulumi.Input[bool]:
        """
        Whether do auto analyze.
        """
        return pulumi.get(self, "auto_analyze")

    @auto_analyze.setter
    def auto_analyze(self, value: pulumi.Input[bool]):
        pulumi.set(self, "auto_analyze", value)

    @property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[str]:
        """
        The name of the hub.
        """
        return pulumi.get(self, "hub_name")

    @hub_name.setter
    def hub_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "hub_name", value)

    @property
    @pulumi.getter
    def mappings(self) -> pulumi.Input['PredictionMappingsArgs']:
        """
        Definition of the link mapping of prediction.
        """
        return pulumi.get(self, "mappings")

    @mappings.setter
    def mappings(self, value: pulumi.Input['PredictionMappingsArgs']):
        pulumi.set(self, "mappings", value)

    @property
    @pulumi.getter(name="negativeOutcomeExpression")
    def negative_outcome_expression(self) -> pulumi.Input[str]:
        """
        Negative outcome expression.
        """
        return pulumi.get(self, "negative_outcome_expression")

    @negative_outcome_expression.setter
    def negative_outcome_expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "negative_outcome_expression", value)

    @property
    @pulumi.getter(name="positiveOutcomeExpression")
    def positive_outcome_expression(self) -> pulumi.Input[str]:
        """
        Positive outcome expression.
        """
        return pulumi.get(self, "positive_outcome_expression")

    @positive_outcome_expression.setter
    def positive_outcome_expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "positive_outcome_expression", value)

    @property
    @pulumi.getter(name="primaryProfileType")
    def primary_profile_type(self) -> pulumi.Input[str]:
        """
        Primary profile type.
        """
        return pulumi.get(self, "primary_profile_type")

    @primary_profile_type.setter
    def primary_profile_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "primary_profile_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="scopeExpression")
    def scope_expression(self) -> pulumi.Input[str]:
        """
        Scope expression.
        """
        return pulumi.get(self, "scope_expression")

    @scope_expression.setter
    def scope_expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope_expression", value)

    @property
    @pulumi.getter(name="scoreLabel")
    def score_label(self) -> pulumi.Input[str]:
        """
        Score label.
        """
        return pulumi.get(self, "score_label")

    @score_label.setter
    def score_label(self, value: pulumi.Input[str]):
        pulumi.set(self, "score_label", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Description of the prediction.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Display name of the prediction.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def grades(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PredictionGradesArgs']]]]:
        """
        The prediction grades.
        """
        return pulumi.get(self, "grades")

    @grades.setter
    def grades(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PredictionGradesArgs']]]]):
        pulumi.set(self, "grades", value)

    @property
    @pulumi.getter(name="involvedInteractionTypes")
    def involved_interaction_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Interaction types involved in the prediction.
        """
        return pulumi.get(self, "involved_interaction_types")

    @involved_interaction_types.setter
    def involved_interaction_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "involved_interaction_types", value)

    @property
    @pulumi.getter(name="involvedKpiTypes")
    def involved_kpi_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        KPI types involved in the prediction.
        """
        return pulumi.get(self, "involved_kpi_types")

    @involved_kpi_types.setter
    def involved_kpi_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "involved_kpi_types", value)

    @property
    @pulumi.getter(name="involvedRelationships")
    def involved_relationships(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Relationships involved in the prediction.
        """
        return pulumi.get(self, "involved_relationships")

    @involved_relationships.setter
    def involved_relationships(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "involved_relationships", value)

    @property
    @pulumi.getter(name="predictionName")
    def prediction_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the prediction.
        """
        return pulumi.get(self, "prediction_name")

    @prediction_name.setter
    def prediction_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prediction_name", value)


class Prediction(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_analyze: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 grades: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PredictionGradesArgs', 'PredictionGradesArgsDict']]]]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 involved_interaction_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 involved_kpi_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 involved_relationships: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mappings: Optional[pulumi.Input[Union['PredictionMappingsArgs', 'PredictionMappingsArgsDict']]] = None,
                 negative_outcome_expression: Optional[pulumi.Input[str]] = None,
                 positive_outcome_expression: Optional[pulumi.Input[str]] = None,
                 prediction_name: Optional[pulumi.Input[str]] = None,
                 primary_profile_type: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope_expression: Optional[pulumi.Input[str]] = None,
                 score_label: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The prediction resource format.
        Azure REST API version: 2017-04-26. Prior API version in Azure Native 1.x: 2017-04-26.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_analyze: Whether do auto analyze.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] description: Description of the prediction.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] display_name: Display name of the prediction.
        :param pulumi.Input[Sequence[pulumi.Input[Union['PredictionGradesArgs', 'PredictionGradesArgsDict']]]] grades: The prediction grades.
        :param pulumi.Input[str] hub_name: The name of the hub.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] involved_interaction_types: Interaction types involved in the prediction.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] involved_kpi_types: KPI types involved in the prediction.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] involved_relationships: Relationships involved in the prediction.
        :param pulumi.Input[Union['PredictionMappingsArgs', 'PredictionMappingsArgsDict']] mappings: Definition of the link mapping of prediction.
        :param pulumi.Input[str] negative_outcome_expression: Negative outcome expression.
        :param pulumi.Input[str] positive_outcome_expression: Positive outcome expression.
        :param pulumi.Input[str] prediction_name: Name of the prediction.
        :param pulumi.Input[str] primary_profile_type: Primary profile type.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] scope_expression: Scope expression.
        :param pulumi.Input[str] score_label: Score label.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PredictionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The prediction resource format.
        Azure REST API version: 2017-04-26. Prior API version in Azure Native 1.x: 2017-04-26.

        :param str resource_name: The name of the resource.
        :param PredictionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PredictionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_analyze: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 grades: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PredictionGradesArgs', 'PredictionGradesArgsDict']]]]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 involved_interaction_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 involved_kpi_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 involved_relationships: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 mappings: Optional[pulumi.Input[Union['PredictionMappingsArgs', 'PredictionMappingsArgsDict']]] = None,
                 negative_outcome_expression: Optional[pulumi.Input[str]] = None,
                 positive_outcome_expression: Optional[pulumi.Input[str]] = None,
                 prediction_name: Optional[pulumi.Input[str]] = None,
                 primary_profile_type: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope_expression: Optional[pulumi.Input[str]] = None,
                 score_label: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PredictionArgs.__new__(PredictionArgs)

            if auto_analyze is None and not opts.urn:
                raise TypeError("Missing required property 'auto_analyze'")
            __props__.__dict__["auto_analyze"] = auto_analyze
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["grades"] = grades
            if hub_name is None and not opts.urn:
                raise TypeError("Missing required property 'hub_name'")
            __props__.__dict__["hub_name"] = hub_name
            __props__.__dict__["involved_interaction_types"] = involved_interaction_types
            __props__.__dict__["involved_kpi_types"] = involved_kpi_types
            __props__.__dict__["involved_relationships"] = involved_relationships
            if mappings is None and not opts.urn:
                raise TypeError("Missing required property 'mappings'")
            __props__.__dict__["mappings"] = mappings
            if negative_outcome_expression is None and not opts.urn:
                raise TypeError("Missing required property 'negative_outcome_expression'")
            __props__.__dict__["negative_outcome_expression"] = negative_outcome_expression
            if positive_outcome_expression is None and not opts.urn:
                raise TypeError("Missing required property 'positive_outcome_expression'")
            __props__.__dict__["positive_outcome_expression"] = positive_outcome_expression
            __props__.__dict__["prediction_name"] = prediction_name
            if primary_profile_type is None and not opts.urn:
                raise TypeError("Missing required property 'primary_profile_type'")
            __props__.__dict__["primary_profile_type"] = primary_profile_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if scope_expression is None and not opts.urn:
                raise TypeError("Missing required property 'scope_expression'")
            __props__.__dict__["scope_expression"] = scope_expression
            if score_label is None and not opts.urn:
                raise TypeError("Missing required property 'score_label'")
            __props__.__dict__["score_label"] = score_label
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_generated_entities"] = None
            __props__.__dict__["tenant_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:customerinsights/v20170426:Prediction")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Prediction, __self__).__init__(
            'azure-native:customerinsights:Prediction',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Prediction':
        """
        Get an existing Prediction resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PredictionArgs.__new__(PredictionArgs)

        __props__.__dict__["auto_analyze"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["grades"] = None
        __props__.__dict__["involved_interaction_types"] = None
        __props__.__dict__["involved_kpi_types"] = None
        __props__.__dict__["involved_relationships"] = None
        __props__.__dict__["mappings"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["negative_outcome_expression"] = None
        __props__.__dict__["positive_outcome_expression"] = None
        __props__.__dict__["prediction_name"] = None
        __props__.__dict__["primary_profile_type"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["scope_expression"] = None
        __props__.__dict__["score_label"] = None
        __props__.__dict__["system_generated_entities"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        return Prediction(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoAnalyze")
    def auto_analyze(self) -> pulumi.Output[bool]:
        """
        Whether do auto analyze.
        """
        return pulumi.get(self, "auto_analyze")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Description of the prediction.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Display name of the prediction.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def grades(self) -> pulumi.Output[Optional[Sequence['outputs.PredictionResponseGrades']]]:
        """
        The prediction grades.
        """
        return pulumi.get(self, "grades")

    @property
    @pulumi.getter(name="involvedInteractionTypes")
    def involved_interaction_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Interaction types involved in the prediction.
        """
        return pulumi.get(self, "involved_interaction_types")

    @property
    @pulumi.getter(name="involvedKpiTypes")
    def involved_kpi_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        KPI types involved in the prediction.
        """
        return pulumi.get(self, "involved_kpi_types")

    @property
    @pulumi.getter(name="involvedRelationships")
    def involved_relationships(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Relationships involved in the prediction.
        """
        return pulumi.get(self, "involved_relationships")

    @property
    @pulumi.getter
    def mappings(self) -> pulumi.Output['outputs.PredictionResponseMappings']:
        """
        Definition of the link mapping of prediction.
        """
        return pulumi.get(self, "mappings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="negativeOutcomeExpression")
    def negative_outcome_expression(self) -> pulumi.Output[str]:
        """
        Negative outcome expression.
        """
        return pulumi.get(self, "negative_outcome_expression")

    @property
    @pulumi.getter(name="positiveOutcomeExpression")
    def positive_outcome_expression(self) -> pulumi.Output[str]:
        """
        Positive outcome expression.
        """
        return pulumi.get(self, "positive_outcome_expression")

    @property
    @pulumi.getter(name="predictionName")
    def prediction_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the prediction.
        """
        return pulumi.get(self, "prediction_name")

    @property
    @pulumi.getter(name="primaryProfileType")
    def primary_profile_type(self) -> pulumi.Output[str]:
        """
        Primary profile type.
        """
        return pulumi.get(self, "primary_profile_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="scopeExpression")
    def scope_expression(self) -> pulumi.Output[str]:
        """
        Scope expression.
        """
        return pulumi.get(self, "scope_expression")

    @property
    @pulumi.getter(name="scoreLabel")
    def score_label(self) -> pulumi.Output[str]:
        """
        Score label.
        """
        return pulumi.get(self, "score_label")

    @property
    @pulumi.getter(name="systemGeneratedEntities")
    def system_generated_entities(self) -> pulumi.Output['outputs.PredictionResponseSystemGeneratedEntities']:
        """
        System generated entities.
        """
        return pulumi.get(self, "system_generated_entities")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The hub name.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

