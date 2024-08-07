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

__all__ = [
    'GetExportResult',
    'AwaitableGetExportResult',
    'get_export',
    'get_export_output',
]

@pulumi.output_type
class GetExportResult:
    """
    An export resource.
    """
    def __init__(__self__, definition=None, delivery_info=None, e_tag=None, format=None, id=None, identity=None, location=None, name=None, next_run_time_estimate=None, partition_data=None, run_history=None, schedule=None, type=None):
        if definition and not isinstance(definition, dict):
            raise TypeError("Expected argument 'definition' to be a dict")
        pulumi.set(__self__, "definition", definition)
        if delivery_info and not isinstance(delivery_info, dict):
            raise TypeError("Expected argument 'delivery_info' to be a dict")
        pulumi.set(__self__, "delivery_info", delivery_info)
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if format and not isinstance(format, str):
            raise TypeError("Expected argument 'format' to be a str")
        pulumi.set(__self__, "format", format)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if next_run_time_estimate and not isinstance(next_run_time_estimate, str):
            raise TypeError("Expected argument 'next_run_time_estimate' to be a str")
        pulumi.set(__self__, "next_run_time_estimate", next_run_time_estimate)
        if partition_data and not isinstance(partition_data, bool):
            raise TypeError("Expected argument 'partition_data' to be a bool")
        pulumi.set(__self__, "partition_data", partition_data)
        if run_history and not isinstance(run_history, dict):
            raise TypeError("Expected argument 'run_history' to be a dict")
        pulumi.set(__self__, "run_history", run_history)
        if schedule and not isinstance(schedule, dict):
            raise TypeError("Expected argument 'schedule' to be a dict")
        pulumi.set(__self__, "schedule", schedule)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def definition(self) -> 'outputs.ExportDefinitionResponse':
        """
        Has the definition for the export.
        """
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter(name="deliveryInfo")
    def delivery_info(self) -> 'outputs.ExportDeliveryInfoResponse':
        """
        Has delivery information for the export.
        """
        return pulumi.get(self, "delivery_info")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[str]:
        """
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def format(self) -> Optional[str]:
        """
        The format of the export being delivered. Currently only 'Csv' is supported.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.SystemAssignedServiceIdentityResponse']:
        """
        The managed identity associated with Export
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the Export's managed identity. Only required when utilizing managed identity.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nextRunTimeEstimate")
    def next_run_time_estimate(self) -> str:
        """
        If the export has an active schedule, provides an estimate of the next run time.
        """
        return pulumi.get(self, "next_run_time_estimate")

    @property
    @pulumi.getter(name="partitionData")
    def partition_data(self) -> Optional[bool]:
        """
        If set to true, exported data will be partitioned by size and placed in a blob directory together with a manifest file. Note: this option is currently available only for Microsoft Customer Agreement commerce scopes.
        """
        return pulumi.get(self, "partition_data")

    @property
    @pulumi.getter(name="runHistory")
    def run_history(self) -> Optional['outputs.ExportExecutionListResultResponse']:
        """
        If requested, has the most recent run history for the export.
        """
        return pulumi.get(self, "run_history")

    @property
    @pulumi.getter
    def schedule(self) -> Optional['outputs.ExportScheduleResponse']:
        """
        Has schedule information for the export.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetExportResult(GetExportResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExportResult(
            definition=self.definition,
            delivery_info=self.delivery_info,
            e_tag=self.e_tag,
            format=self.format,
            id=self.id,
            identity=self.identity,
            location=self.location,
            name=self.name,
            next_run_time_estimate=self.next_run_time_estimate,
            partition_data=self.partition_data,
            run_history=self.run_history,
            schedule=self.schedule,
            type=self.type)


def get_export(expand: Optional[str] = None,
               export_name: Optional[str] = None,
               scope: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExportResult:
    """
    The operation to get the export for the defined scope by export name.


    :param str expand: May be used to expand the properties within an export. Currently only 'runHistory' is supported and will return information for the last 10 runs of the export.
    :param str export_name: Export Name.
    :param str scope: The scope associated with export operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope, and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' specific for partners.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['exportName'] = export_name
    __args__['scope'] = scope
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:costmanagement/v20231101:getExport', __args__, opts=opts, typ=GetExportResult).value

    return AwaitableGetExportResult(
        definition=pulumi.get(__ret__, 'definition'),
        delivery_info=pulumi.get(__ret__, 'delivery_info'),
        e_tag=pulumi.get(__ret__, 'e_tag'),
        format=pulumi.get(__ret__, 'format'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        next_run_time_estimate=pulumi.get(__ret__, 'next_run_time_estimate'),
        partition_data=pulumi.get(__ret__, 'partition_data'),
        run_history=pulumi.get(__ret__, 'run_history'),
        schedule=pulumi.get(__ret__, 'schedule'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_export)
def get_export_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                      export_name: Optional[pulumi.Input[str]] = None,
                      scope: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExportResult]:
    """
    The operation to get the export for the defined scope by export name.


    :param str expand: May be used to expand the properties within an export. Currently only 'runHistory' is supported and will return information for the last 10 runs of the export.
    :param str export_name: Export Name.
    :param str scope: The scope associated with export operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, '/providers/Microsoft.Management/managementGroups/{managementGroupId} for Management Group scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope, and '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/customers/{customerId}' specific for partners.
    """
    ...
