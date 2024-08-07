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
    'GetAssessmentResult',
    'AwaitableGetAssessmentResult',
    'get_assessment',
    'get_assessment_output',
]

@pulumi.output_type
class GetAssessmentResult:
    """
    Security assessment on a resource - response format
    """
    def __init__(__self__, additional_data=None, display_name=None, id=None, links=None, metadata=None, name=None, partners_data=None, resource_details=None, status=None, type=None):
        if additional_data and not isinstance(additional_data, dict):
            raise TypeError("Expected argument 'additional_data' to be a dict")
        pulumi.set(__self__, "additional_data", additional_data)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if links and not isinstance(links, dict):
            raise TypeError("Expected argument 'links' to be a dict")
        pulumi.set(__self__, "links", links)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partners_data and not isinstance(partners_data, dict):
            raise TypeError("Expected argument 'partners_data' to be a dict")
        pulumi.set(__self__, "partners_data", partners_data)
        if resource_details and not isinstance(resource_details, dict):
            raise TypeError("Expected argument 'resource_details' to be a dict")
        pulumi.set(__self__, "resource_details", resource_details)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> Optional[Mapping[str, str]]:
        """
        Additional data regarding the assessment
        """
        return pulumi.get(self, "additional_data")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        User friendly display name of the assessment
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def links(self) -> 'outputs.AssessmentLinksResponse':
        """
        Links relevant to the assessment
        """
        return pulumi.get(self, "links")

    @property
    @pulumi.getter
    def metadata(self) -> Optional['outputs.SecurityAssessmentMetadataPropertiesResponse']:
        """
        Describes properties of an assessment metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnersData")
    def partners_data(self) -> Optional['outputs.SecurityAssessmentPartnerDataResponse']:
        """
        Data regarding 3rd party partner integration
        """
        return pulumi.get(self, "partners_data")

    @property
    @pulumi.getter(name="resourceDetails")
    def resource_details(self) -> Any:
        """
        Details of the resource that was assessed
        """
        return pulumi.get(self, "resource_details")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.AssessmentStatusResponseResponse':
        """
        The result of the assessment
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetAssessmentResult(GetAssessmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAssessmentResult(
            additional_data=self.additional_data,
            display_name=self.display_name,
            id=self.id,
            links=self.links,
            metadata=self.metadata,
            name=self.name,
            partners_data=self.partners_data,
            resource_details=self.resource_details,
            status=self.status,
            type=self.type)


def get_assessment(assessment_name: Optional[str] = None,
                   expand: Optional[str] = None,
                   resource_id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAssessmentResult:
    """
    Get a security assessment on your scanned resource
    Azure REST API version: 2021-06-01.

    Other available API versions: 2020-01-01.


    :param str assessment_name: The Assessment Key - Unique key for the assessment type
    :param str expand: OData expand. Optional.
    :param str resource_id: The identifier of the resource.
    """
    __args__ = dict()
    __args__['assessmentName'] = assessment_name
    __args__['expand'] = expand
    __args__['resourceId'] = resource_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:security:getAssessment', __args__, opts=opts, typ=GetAssessmentResult).value

    return AwaitableGetAssessmentResult(
        additional_data=pulumi.get(__ret__, 'additional_data'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        links=pulumi.get(__ret__, 'links'),
        metadata=pulumi.get(__ret__, 'metadata'),
        name=pulumi.get(__ret__, 'name'),
        partners_data=pulumi.get(__ret__, 'partners_data'),
        resource_details=pulumi.get(__ret__, 'resource_details'),
        status=pulumi.get(__ret__, 'status'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_assessment)
def get_assessment_output(assessment_name: Optional[pulumi.Input[str]] = None,
                          expand: Optional[pulumi.Input[Optional[str]]] = None,
                          resource_id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAssessmentResult]:
    """
    Get a security assessment on your scanned resource
    Azure REST API version: 2021-06-01.

    Other available API versions: 2020-01-01.


    :param str assessment_name: The Assessment Key - Unique key for the assessment type
    :param str expand: OData expand. Optional.
    :param str resource_id: The identifier of the resource.
    """
    ...
