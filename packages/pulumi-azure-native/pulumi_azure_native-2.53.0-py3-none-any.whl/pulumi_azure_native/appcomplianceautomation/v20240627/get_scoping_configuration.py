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
    'GetScopingConfigurationResult',
    'AwaitableGetScopingConfigurationResult',
    'get_scoping_configuration',
    'get_scoping_configuration_output',
]

@pulumi.output_type
class GetScopingConfigurationResult:
    """
    A class represent an AppComplianceAutomation scoping configuration resource.
    """
    def __init__(__self__, answers=None, id=None, name=None, provisioning_state=None, system_data=None, type=None):
        if answers and not isinstance(answers, list):
            raise TypeError("Expected argument 'answers' to be a list")
        pulumi.set(__self__, "answers", answers)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def answers(self) -> Optional[Sequence['outputs.ScopingAnswerResponse']]:
        """
        List of scoping question answers.
        """
        return pulumi.get(self, "answers")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
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
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

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


class AwaitableGetScopingConfigurationResult(GetScopingConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScopingConfigurationResult(
            answers=self.answers,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_scoping_configuration(report_name: Optional[str] = None,
                              scoping_configuration_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScopingConfigurationResult:
    """
    Get the AppComplianceAutomation scoping configuration of the specific report.


    :param str report_name: Report Name.
    :param str scoping_configuration_name: The scoping configuration of the specific report.
    """
    __args__ = dict()
    __args__['reportName'] = report_name
    __args__['scopingConfigurationName'] = scoping_configuration_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appcomplianceautomation/v20240627:getScopingConfiguration', __args__, opts=opts, typ=GetScopingConfigurationResult).value

    return AwaitableGetScopingConfigurationResult(
        answers=pulumi.get(__ret__, 'answers'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_scoping_configuration)
def get_scoping_configuration_output(report_name: Optional[pulumi.Input[str]] = None,
                                     scoping_configuration_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScopingConfigurationResult]:
    """
    Get the AppComplianceAutomation scoping configuration of the specific report.


    :param str report_name: Report Name.
    :param str scoping_configuration_name: The scoping configuration of the specific report.
    """
    ...
