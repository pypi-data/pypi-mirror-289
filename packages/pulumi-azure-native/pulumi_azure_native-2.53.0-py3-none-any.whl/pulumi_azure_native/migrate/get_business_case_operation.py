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

__all__ = [
    'GetBusinessCaseOperationResult',
    'AwaitableGetBusinessCaseOperationResult',
    'get_business_case_operation',
    'get_business_case_operation_output',
]

@pulumi.output_type
class GetBusinessCaseOperationResult:
    """
    Business case resource.
    """
    def __init__(__self__, id=None, name=None, provisioning_state=None, report_status_details=None, settings=None, state=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if report_status_details and not isinstance(report_status_details, list):
            raise TypeError("Expected argument 'report_status_details' to be a list")
        pulumi.set(__self__, "report_status_details", report_status_details)
        if settings and not isinstance(settings, dict):
            raise TypeError("Expected argument 'settings' to be a dict")
        pulumi.set(__self__, "settings", settings)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="reportStatusDetails")
    def report_status_details(self) -> Sequence['outputs.ReportDetailsResponse']:
        """
        Gets the state of business case reports.
        """
        return pulumi.get(self, "report_status_details")

    @property
    @pulumi.getter
    def settings(self) -> Optional['outputs.SettingsResponse']:
        """
        Business case settings.
        """
        return pulumi.get(self, "settings")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Business case state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetBusinessCaseOperationResult(GetBusinessCaseOperationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBusinessCaseOperationResult(
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            report_status_details=self.report_status_details,
            settings=self.settings,
            state=self.state,
            system_data=self.system_data,
            type=self.type)


def get_business_case_operation(business_case_name: Optional[str] = None,
                                project_name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBusinessCaseOperationResult:
    """
    Get a BusinessCase
    Azure REST API version: 2023-04-01-preview.


    :param str business_case_name: Business case ARM name
    :param str project_name: Assessment Project Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['businessCaseName'] = business_case_name
    __args__['projectName'] = project_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:migrate:getBusinessCaseOperation', __args__, opts=opts, typ=GetBusinessCaseOperationResult).value

    return AwaitableGetBusinessCaseOperationResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        report_status_details=pulumi.get(__ret__, 'report_status_details'),
        settings=pulumi.get(__ret__, 'settings'),
        state=pulumi.get(__ret__, 'state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_business_case_operation)
def get_business_case_operation_output(business_case_name: Optional[pulumi.Input[str]] = None,
                                       project_name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBusinessCaseOperationResult]:
    """
    Get a BusinessCase
    Azure REST API version: 2023-04-01-preview.


    :param str business_case_name: Business case ARM name
    :param str project_name: Assessment Project Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
