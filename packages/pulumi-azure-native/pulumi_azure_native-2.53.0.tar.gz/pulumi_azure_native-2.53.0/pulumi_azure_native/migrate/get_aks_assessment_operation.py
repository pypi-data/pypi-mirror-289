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
    'GetAksAssessmentOperationResult',
    'AwaitableGetAksAssessmentOperationResult',
    'get_aks_assessment_operation',
    'get_aks_assessment_operation_output',
]

@pulumi.output_type
class GetAksAssessmentOperationResult:
    """
    ARM model of AKS Assessment.
    """
    def __init__(__self__, details=None, e_tag=None, id=None, name=None, provisioning_state=None, scope=None, settings=None, system_data=None, type=None):
        if details and not isinstance(details, dict):
            raise TypeError("Expected argument 'details' to be a dict")
        pulumi.set(__self__, "details", details)
        if e_tag and not isinstance(e_tag, str):
            raise TypeError("Expected argument 'e_tag' to be a str")
        pulumi.set(__self__, "e_tag", e_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if scope and not isinstance(scope, dict):
            raise TypeError("Expected argument 'scope' to be a dict")
        pulumi.set(__self__, "scope", scope)
        if settings and not isinstance(settings, dict):
            raise TypeError("Expected argument 'settings' to be a dict")
        pulumi.set(__self__, "settings", settings)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def details(self) -> 'outputs.AKSAssessmentDetailsResponse':
        """
        Gets AKS Assessment Details.
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> str:
        """
        If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields.
        """
        return pulumi.get(self, "e_tag")

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
        Gets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def scope(self) -> Optional['outputs.AssessmentScopeParametersResponse']:
        """
        Gets or sets scope parameters to identify inventory items for assessment.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def settings(self) -> 'outputs.AKSAssessmentSettingsResponse':
        """
        Gets or sets AKS Assessment Settings.
        """
        return pulumi.get(self, "settings")

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


class AwaitableGetAksAssessmentOperationResult(GetAksAssessmentOperationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAksAssessmentOperationResult(
            details=self.details,
            e_tag=self.e_tag,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            scope=self.scope,
            settings=self.settings,
            system_data=self.system_data,
            type=self.type)


def get_aks_assessment_operation(assessment_name: Optional[str] = None,
                                 project_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAksAssessmentOperationResult:
    """
    Get a AKSAssessment
    Azure REST API version: 2023-04-01-preview.


    :param str assessment_name: AKS Assessment Name.
    :param str project_name: Assessment Project Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['assessmentName'] = assessment_name
    __args__['projectName'] = project_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:migrate:getAksAssessmentOperation', __args__, opts=opts, typ=GetAksAssessmentOperationResult).value

    return AwaitableGetAksAssessmentOperationResult(
        details=pulumi.get(__ret__, 'details'),
        e_tag=pulumi.get(__ret__, 'e_tag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        scope=pulumi.get(__ret__, 'scope'),
        settings=pulumi.get(__ret__, 'settings'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_aks_assessment_operation)
def get_aks_assessment_operation_output(assessment_name: Optional[pulumi.Input[str]] = None,
                                        project_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAksAssessmentOperationResult]:
    """
    Get a AKSAssessment
    Azure REST API version: 2023-04-01-preview.


    :param str assessment_name: AKS Assessment Name.
    :param str project_name: Assessment Project Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
