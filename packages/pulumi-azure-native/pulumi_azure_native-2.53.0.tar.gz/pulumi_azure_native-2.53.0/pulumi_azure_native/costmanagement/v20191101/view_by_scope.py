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

__all__ = ['ViewByScopeArgs', 'ViewByScope']

@pulumi.input_type
class ViewByScopeArgs:
    def __init__(__self__, *,
                 scope: pulumi.Input[str],
                 timeframe: pulumi.Input[Union[str, 'ReportTimeframeType']],
                 type: pulumi.Input[Union[str, 'ReportType']],
                 accumulated: Optional[pulumi.Input[Union[str, 'AccumulatedType']]] = None,
                 chart: Optional[pulumi.Input[Union[str, 'ChartType']]] = None,
                 data_set: Optional[pulumi.Input['ReportConfigDatasetArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 kpis: Optional[pulumi.Input[Sequence[pulumi.Input['KpiPropertiesArgs']]]] = None,
                 metric: Optional[pulumi.Input[Union[str, 'MetricType']]] = None,
                 pivots: Optional[pulumi.Input[Sequence[pulumi.Input['PivotPropertiesArgs']]]] = None,
                 time_period: Optional[pulumi.Input['ReportConfigTimePeriodArgs']] = None,
                 view_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ViewByScope resource.
        :param pulumi.Input[str] scope: Cost Management scope to save the view on. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for ExternalSubscription scope.
        :param pulumi.Input[Union[str, 'ReportTimeframeType']] timeframe: The time frame for pulling data for the report. If custom, then a specific time period must be provided.
        :param pulumi.Input[Union[str, 'ReportType']] type: The type of the report. Usage represents actual usage, forecast represents forecasted data and UsageAndForecast represents both usage and forecasted data. Actual usage and forecasted data can be differentiated based on dates.
        :param pulumi.Input[Union[str, 'AccumulatedType']] accumulated: Show costs accumulated over time.
        :param pulumi.Input[Union[str, 'ChartType']] chart: Chart type of the main view in Cost Analysis. Required.
        :param pulumi.Input['ReportConfigDatasetArgs'] data_set: Has definition for data in this report config.
        :param pulumi.Input[str] display_name: User input name of the view. Required.
        :param pulumi.Input[str] e_tag: eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        :param pulumi.Input[Sequence[pulumi.Input['KpiPropertiesArgs']]] kpis: List of KPIs to show in Cost Analysis UI.
        :param pulumi.Input[Union[str, 'MetricType']] metric: Metric to use when displaying costs.
        :param pulumi.Input[Sequence[pulumi.Input['PivotPropertiesArgs']]] pivots: Configuration of 3 sub-views in the Cost Analysis UI.
        :param pulumi.Input['ReportConfigTimePeriodArgs'] time_period: Has time period for pulling data for the report.
        :param pulumi.Input[str] view_name: View name
        """
        pulumi.set(__self__, "scope", scope)
        pulumi.set(__self__, "timeframe", timeframe)
        pulumi.set(__self__, "type", type)
        if accumulated is not None:
            pulumi.set(__self__, "accumulated", accumulated)
        if chart is not None:
            pulumi.set(__self__, "chart", chart)
        if data_set is not None:
            pulumi.set(__self__, "data_set", data_set)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)
        if kpis is not None:
            pulumi.set(__self__, "kpis", kpis)
        if metric is not None:
            pulumi.set(__self__, "metric", metric)
        if pivots is not None:
            pulumi.set(__self__, "pivots", pivots)
        if time_period is not None:
            pulumi.set(__self__, "time_period", time_period)
        if view_name is not None:
            pulumi.set(__self__, "view_name", view_name)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        Cost Management scope to save the view on. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for ExternalSubscription scope.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def timeframe(self) -> pulumi.Input[Union[str, 'ReportTimeframeType']]:
        """
        The time frame for pulling data for the report. If custom, then a specific time period must be provided.
        """
        return pulumi.get(self, "timeframe")

    @timeframe.setter
    def timeframe(self, value: pulumi.Input[Union[str, 'ReportTimeframeType']]):
        pulumi.set(self, "timeframe", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'ReportType']]:
        """
        The type of the report. Usage represents actual usage, forecast represents forecasted data and UsageAndForecast represents both usage and forecasted data. Actual usage and forecasted data can be differentiated based on dates.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'ReportType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def accumulated(self) -> Optional[pulumi.Input[Union[str, 'AccumulatedType']]]:
        """
        Show costs accumulated over time.
        """
        return pulumi.get(self, "accumulated")

    @accumulated.setter
    def accumulated(self, value: Optional[pulumi.Input[Union[str, 'AccumulatedType']]]):
        pulumi.set(self, "accumulated", value)

    @property
    @pulumi.getter
    def chart(self) -> Optional[pulumi.Input[Union[str, 'ChartType']]]:
        """
        Chart type of the main view in Cost Analysis. Required.
        """
        return pulumi.get(self, "chart")

    @chart.setter
    def chart(self, value: Optional[pulumi.Input[Union[str, 'ChartType']]]):
        pulumi.set(self, "chart", value)

    @property
    @pulumi.getter(name="dataSet")
    def data_set(self) -> Optional[pulumi.Input['ReportConfigDatasetArgs']]:
        """
        Has definition for data in this report config.
        """
        return pulumi.get(self, "data_set")

    @data_set.setter
    def data_set(self, value: Optional[pulumi.Input['ReportConfigDatasetArgs']]):
        pulumi.set(self, "data_set", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        User input name of the view. Required.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[str]]:
        """
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        """
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_tag", value)

    @property
    @pulumi.getter
    def kpis(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KpiPropertiesArgs']]]]:
        """
        List of KPIs to show in Cost Analysis UI.
        """
        return pulumi.get(self, "kpis")

    @kpis.setter
    def kpis(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KpiPropertiesArgs']]]]):
        pulumi.set(self, "kpis", value)

    @property
    @pulumi.getter
    def metric(self) -> Optional[pulumi.Input[Union[str, 'MetricType']]]:
        """
        Metric to use when displaying costs.
        """
        return pulumi.get(self, "metric")

    @metric.setter
    def metric(self, value: Optional[pulumi.Input[Union[str, 'MetricType']]]):
        pulumi.set(self, "metric", value)

    @property
    @pulumi.getter
    def pivots(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PivotPropertiesArgs']]]]:
        """
        Configuration of 3 sub-views in the Cost Analysis UI.
        """
        return pulumi.get(self, "pivots")

    @pivots.setter
    def pivots(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PivotPropertiesArgs']]]]):
        pulumi.set(self, "pivots", value)

    @property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> Optional[pulumi.Input['ReportConfigTimePeriodArgs']]:
        """
        Has time period for pulling data for the report.
        """
        return pulumi.get(self, "time_period")

    @time_period.setter
    def time_period(self, value: Optional[pulumi.Input['ReportConfigTimePeriodArgs']]):
        pulumi.set(self, "time_period", value)

    @property
    @pulumi.getter(name="viewName")
    def view_name(self) -> Optional[pulumi.Input[str]]:
        """
        View name
        """
        return pulumi.get(self, "view_name")

    @view_name.setter
    def view_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "view_name", value)


class ViewByScope(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accumulated: Optional[pulumi.Input[Union[str, 'AccumulatedType']]] = None,
                 chart: Optional[pulumi.Input[Union[str, 'ChartType']]] = None,
                 data_set: Optional[pulumi.Input[Union['ReportConfigDatasetArgs', 'ReportConfigDatasetArgsDict']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 kpis: Optional[pulumi.Input[Sequence[pulumi.Input[Union['KpiPropertiesArgs', 'KpiPropertiesArgsDict']]]]] = None,
                 metric: Optional[pulumi.Input[Union[str, 'MetricType']]] = None,
                 pivots: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PivotPropertiesArgs', 'PivotPropertiesArgsDict']]]]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 time_period: Optional[pulumi.Input[Union['ReportConfigTimePeriodArgs', 'ReportConfigTimePeriodArgsDict']]] = None,
                 timeframe: Optional[pulumi.Input[Union[str, 'ReportTimeframeType']]] = None,
                 type: Optional[pulumi.Input[Union[str, 'ReportType']]] = None,
                 view_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        States and configurations of Cost Analysis.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'AccumulatedType']] accumulated: Show costs accumulated over time.
        :param pulumi.Input[Union[str, 'ChartType']] chart: Chart type of the main view in Cost Analysis. Required.
        :param pulumi.Input[Union['ReportConfigDatasetArgs', 'ReportConfigDatasetArgsDict']] data_set: Has definition for data in this report config.
        :param pulumi.Input[str] display_name: User input name of the view. Required.
        :param pulumi.Input[str] e_tag: eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        :param pulumi.Input[Sequence[pulumi.Input[Union['KpiPropertiesArgs', 'KpiPropertiesArgsDict']]]] kpis: List of KPIs to show in Cost Analysis UI.
        :param pulumi.Input[Union[str, 'MetricType']] metric: Metric to use when displaying costs.
        :param pulumi.Input[Sequence[pulumi.Input[Union['PivotPropertiesArgs', 'PivotPropertiesArgsDict']]]] pivots: Configuration of 3 sub-views in the Cost Analysis UI.
        :param pulumi.Input[str] scope: Cost Management scope to save the view on. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for ExternalSubscription scope.
        :param pulumi.Input[Union['ReportConfigTimePeriodArgs', 'ReportConfigTimePeriodArgsDict']] time_period: Has time period for pulling data for the report.
        :param pulumi.Input[Union[str, 'ReportTimeframeType']] timeframe: The time frame for pulling data for the report. If custom, then a specific time period must be provided.
        :param pulumi.Input[Union[str, 'ReportType']] type: The type of the report. Usage represents actual usage, forecast represents forecasted data and UsageAndForecast represents both usage and forecasted data. Actual usage and forecasted data can be differentiated based on dates.
        :param pulumi.Input[str] view_name: View name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ViewByScopeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        States and configurations of Cost Analysis.

        :param str resource_name: The name of the resource.
        :param ViewByScopeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ViewByScopeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accumulated: Optional[pulumi.Input[Union[str, 'AccumulatedType']]] = None,
                 chart: Optional[pulumi.Input[Union[str, 'ChartType']]] = None,
                 data_set: Optional[pulumi.Input[Union['ReportConfigDatasetArgs', 'ReportConfigDatasetArgsDict']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 kpis: Optional[pulumi.Input[Sequence[pulumi.Input[Union['KpiPropertiesArgs', 'KpiPropertiesArgsDict']]]]] = None,
                 metric: Optional[pulumi.Input[Union[str, 'MetricType']]] = None,
                 pivots: Optional[pulumi.Input[Sequence[pulumi.Input[Union['PivotPropertiesArgs', 'PivotPropertiesArgsDict']]]]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 time_period: Optional[pulumi.Input[Union['ReportConfigTimePeriodArgs', 'ReportConfigTimePeriodArgsDict']]] = None,
                 timeframe: Optional[pulumi.Input[Union[str, 'ReportTimeframeType']]] = None,
                 type: Optional[pulumi.Input[Union[str, 'ReportType']]] = None,
                 view_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ViewByScopeArgs.__new__(ViewByScopeArgs)

            __props__.__dict__["accumulated"] = accumulated
            __props__.__dict__["chart"] = chart
            __props__.__dict__["data_set"] = data_set
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["e_tag"] = e_tag
            __props__.__dict__["kpis"] = kpis
            __props__.__dict__["metric"] = metric
            __props__.__dict__["pivots"] = pivots
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["time_period"] = time_period
            if timeframe is None and not opts.urn:
                raise TypeError("Missing required property 'timeframe'")
            __props__.__dict__["timeframe"] = timeframe
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["view_name"] = view_name
            __props__.__dict__["created_on"] = None
            __props__.__dict__["currency"] = None
            __props__.__dict__["date_range"] = None
            __props__.__dict__["include_monetary_commitment"] = None
            __props__.__dict__["modified_on"] = None
            __props__.__dict__["name"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:costmanagement:ViewByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20190401preview:ViewByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20200601:ViewByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20211001:ViewByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20220801preview:ViewByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20221001:ViewByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20221001preview:ViewByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20221005preview:ViewByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20230301:ViewByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20230401preview:ViewByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20230701preview:ViewByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20230801:ViewByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20230901:ViewByScope"), pulumi.Alias(type_="azure-native:costmanagement/v20231101:ViewByScope")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ViewByScope, __self__).__init__(
            'azure-native:costmanagement/v20191101:ViewByScope',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ViewByScope':
        """
        Get an existing ViewByScope resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ViewByScopeArgs.__new__(ViewByScopeArgs)

        __props__.__dict__["accumulated"] = None
        __props__.__dict__["chart"] = None
        __props__.__dict__["created_on"] = None
        __props__.__dict__["currency"] = None
        __props__.__dict__["data_set"] = None
        __props__.__dict__["date_range"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["e_tag"] = None
        __props__.__dict__["include_monetary_commitment"] = None
        __props__.__dict__["kpis"] = None
        __props__.__dict__["metric"] = None
        __props__.__dict__["modified_on"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["pivots"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["time_period"] = None
        __props__.__dict__["timeframe"] = None
        __props__.__dict__["type"] = None
        return ViewByScope(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def accumulated(self) -> pulumi.Output[Optional[str]]:
        """
        Show costs accumulated over time.
        """
        return pulumi.get(self, "accumulated")

    @property
    @pulumi.getter
    def chart(self) -> pulumi.Output[Optional[str]]:
        """
        Chart type of the main view in Cost Analysis. Required.
        """
        return pulumi.get(self, "chart")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[str]:
        """
        Date the user created this view.
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def currency(self) -> pulumi.Output[str]:
        """
        Selected currency.
        """
        return pulumi.get(self, "currency")

    @property
    @pulumi.getter(name="dataSet")
    def data_set(self) -> pulumi.Output[Optional['outputs.ReportConfigDatasetResponse']]:
        """
        Has definition for data in this report config.
        """
        return pulumi.get(self, "data_set")

    @property
    @pulumi.getter(name="dateRange")
    def date_range(self) -> pulumi.Output[str]:
        """
        Selected date range for viewing cost in.
        """
        return pulumi.get(self, "date_range")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        User input name of the view. Required.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter(name="includeMonetaryCommitment")
    def include_monetary_commitment(self) -> pulumi.Output[bool]:
        """
        Include monetary commitment
        """
        return pulumi.get(self, "include_monetary_commitment")

    @property
    @pulumi.getter
    def kpis(self) -> pulumi.Output[Optional[Sequence['outputs.KpiPropertiesResponse']]]:
        """
        List of KPIs to show in Cost Analysis UI.
        """
        return pulumi.get(self, "kpis")

    @property
    @pulumi.getter
    def metric(self) -> pulumi.Output[Optional[str]]:
        """
        Metric to use when displaying costs.
        """
        return pulumi.get(self, "metric")

    @property
    @pulumi.getter(name="modifiedOn")
    def modified_on(self) -> pulumi.Output[str]:
        """
        Date when the user last modified this view.
        """
        return pulumi.get(self, "modified_on")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def pivots(self) -> pulumi.Output[Optional[Sequence['outputs.PivotPropertiesResponse']]]:
        """
        Configuration of 3 sub-views in the Cost Analysis UI.
        """
        return pulumi.get(self, "pivots")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        Cost Management scope to save the view on. This includes 'subscriptions/{subscriptionId}' for subscription scope, 'subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for BillingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for InvoiceSection scope, 'providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope, '/providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}' for ExternalBillingAccount scope, and '/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName}' for ExternalSubscription scope.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> pulumi.Output[Optional['outputs.ReportConfigTimePeriodResponse']]:
        """
        Has time period for pulling data for the report.
        """
        return pulumi.get(self, "time_period")

    @property
    @pulumi.getter
    def timeframe(self) -> pulumi.Output[str]:
        """
        The time frame for pulling data for the report. If custom, then a specific time period must be provided.
        """
        return pulumi.get(self, "timeframe")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

