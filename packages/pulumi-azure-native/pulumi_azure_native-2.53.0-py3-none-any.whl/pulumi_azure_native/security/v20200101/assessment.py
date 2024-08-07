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

__all__ = ['AssessmentArgs', 'Assessment']

@pulumi.input_type
class AssessmentArgs:
    def __init__(__self__, *,
                 resource_details: pulumi.Input[Union['AzureResourceDetailsArgs', 'OnPremiseResourceDetailsArgs', 'OnPremiseSqlResourceDetailsArgs']],
                 resource_id: pulumi.Input[str],
                 status: pulumi.Input['AssessmentStatusArgs'],
                 additional_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 assessment_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['SecurityAssessmentMetadataPropertiesArgs']] = None,
                 partners_data: Optional[pulumi.Input['SecurityAssessmentPartnerDataArgs']] = None):
        """
        The set of arguments for constructing a Assessment resource.
        :param pulumi.Input[Union['AzureResourceDetailsArgs', 'OnPremiseResourceDetailsArgs', 'OnPremiseSqlResourceDetailsArgs']] resource_details: Details of the resource that was assessed
        :param pulumi.Input[str] resource_id: The identifier of the resource.
        :param pulumi.Input['AssessmentStatusArgs'] status: The result of the assessment
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_data: Additional data regarding the assessment
        :param pulumi.Input[str] assessment_name: The Assessment Key - Unique key for the assessment type
        :param pulumi.Input['SecurityAssessmentMetadataPropertiesArgs'] metadata: Describes properties of an assessment metadata.
        :param pulumi.Input['SecurityAssessmentPartnerDataArgs'] partners_data: Data regarding 3rd party partner integration
        """
        pulumi.set(__self__, "resource_details", resource_details)
        pulumi.set(__self__, "resource_id", resource_id)
        pulumi.set(__self__, "status", status)
        if additional_data is not None:
            pulumi.set(__self__, "additional_data", additional_data)
        if assessment_name is not None:
            pulumi.set(__self__, "assessment_name", assessment_name)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if partners_data is not None:
            pulumi.set(__self__, "partners_data", partners_data)

    @property
    @pulumi.getter(name="resourceDetails")
    def resource_details(self) -> pulumi.Input[Union['AzureResourceDetailsArgs', 'OnPremiseResourceDetailsArgs', 'OnPremiseSqlResourceDetailsArgs']]:
        """
        Details of the resource that was assessed
        """
        return pulumi.get(self, "resource_details")

    @resource_details.setter
    def resource_details(self, value: pulumi.Input[Union['AzureResourceDetailsArgs', 'OnPremiseResourceDetailsArgs', 'OnPremiseSqlResourceDetailsArgs']]):
        pulumi.set(self, "resource_details", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input['AssessmentStatusArgs']:
        """
        The result of the assessment
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input['AssessmentStatusArgs']):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Additional data regarding the assessment
        """
        return pulumi.get(self, "additional_data")

    @additional_data.setter
    def additional_data(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "additional_data", value)

    @property
    @pulumi.getter(name="assessmentName")
    def assessment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Assessment Key - Unique key for the assessment type
        """
        return pulumi.get(self, "assessment_name")

    @assessment_name.setter
    def assessment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assessment_name", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['SecurityAssessmentMetadataPropertiesArgs']]:
        """
        Describes properties of an assessment metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['SecurityAssessmentMetadataPropertiesArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="partnersData")
    def partners_data(self) -> Optional[pulumi.Input['SecurityAssessmentPartnerDataArgs']]:
        """
        Data regarding 3rd party partner integration
        """
        return pulumi.get(self, "partners_data")

    @partners_data.setter
    def partners_data(self, value: Optional[pulumi.Input['SecurityAssessmentPartnerDataArgs']]):
        pulumi.set(self, "partners_data", value)


class Assessment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 assessment_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Union['SecurityAssessmentMetadataPropertiesArgs', 'SecurityAssessmentMetadataPropertiesArgsDict']]] = None,
                 partners_data: Optional[pulumi.Input[Union['SecurityAssessmentPartnerDataArgs', 'SecurityAssessmentPartnerDataArgsDict']]] = None,
                 resource_details: Optional[pulumi.Input[Union[Union['AzureResourceDetailsArgs', 'AzureResourceDetailsArgsDict'], Union['OnPremiseResourceDetailsArgs', 'OnPremiseResourceDetailsArgsDict'], Union['OnPremiseSqlResourceDetailsArgs', 'OnPremiseSqlResourceDetailsArgsDict']]]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union['AssessmentStatusArgs', 'AssessmentStatusArgsDict']]] = None,
                 __props__=None):
        """
        Security assessment on a resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] additional_data: Additional data regarding the assessment
        :param pulumi.Input[str] assessment_name: The Assessment Key - Unique key for the assessment type
        :param pulumi.Input[Union['SecurityAssessmentMetadataPropertiesArgs', 'SecurityAssessmentMetadataPropertiesArgsDict']] metadata: Describes properties of an assessment metadata.
        :param pulumi.Input[Union['SecurityAssessmentPartnerDataArgs', 'SecurityAssessmentPartnerDataArgsDict']] partners_data: Data regarding 3rd party partner integration
        :param pulumi.Input[Union[Union['AzureResourceDetailsArgs', 'AzureResourceDetailsArgsDict'], Union['OnPremiseResourceDetailsArgs', 'OnPremiseResourceDetailsArgsDict'], Union['OnPremiseSqlResourceDetailsArgs', 'OnPremiseSqlResourceDetailsArgsDict']]] resource_details: Details of the resource that was assessed
        :param pulumi.Input[str] resource_id: The identifier of the resource.
        :param pulumi.Input[Union['AssessmentStatusArgs', 'AssessmentStatusArgsDict']] status: The result of the assessment
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssessmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Security assessment on a resource

        :param str resource_name: The name of the resource.
        :param AssessmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssessmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 additional_data: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 assessment_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Union['SecurityAssessmentMetadataPropertiesArgs', 'SecurityAssessmentMetadataPropertiesArgsDict']]] = None,
                 partners_data: Optional[pulumi.Input[Union['SecurityAssessmentPartnerDataArgs', 'SecurityAssessmentPartnerDataArgsDict']]] = None,
                 resource_details: Optional[pulumi.Input[Union[Union['AzureResourceDetailsArgs', 'AzureResourceDetailsArgsDict'], Union['OnPremiseResourceDetailsArgs', 'OnPremiseResourceDetailsArgsDict'], Union['OnPremiseSqlResourceDetailsArgs', 'OnPremiseSqlResourceDetailsArgsDict']]]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union['AssessmentStatusArgs', 'AssessmentStatusArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssessmentArgs.__new__(AssessmentArgs)

            __props__.__dict__["additional_data"] = additional_data
            __props__.__dict__["assessment_name"] = assessment_name
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["partners_data"] = partners_data
            if resource_details is None and not opts.urn:
                raise TypeError("Missing required property 'resource_details'")
            __props__.__dict__["resource_details"] = resource_details
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            if status is None and not opts.urn:
                raise TypeError("Missing required property 'status'")
            __props__.__dict__["status"] = status
            __props__.__dict__["display_name"] = None
            __props__.__dict__["links"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:security:Assessment"), pulumi.Alias(type_="azure-native:security/v20190101preview:Assessment"), pulumi.Alias(type_="azure-native:security/v20210601:Assessment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Assessment, __self__).__init__(
            'azure-native:security/v20200101:Assessment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Assessment':
        """
        Get an existing Assessment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AssessmentArgs.__new__(AssessmentArgs)

        __props__.__dict__["additional_data"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["links"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partners_data"] = None
        __props__.__dict__["resource_details"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["type"] = None
        return Assessment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Additional data regarding the assessment
        """
        return pulumi.get(self, "additional_data")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        User friendly display name of the assessment
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def links(self) -> pulumi.Output['outputs.AssessmentLinksResponse']:
        """
        Links relevant to the assessment
        """
        return pulumi.get(self, "links")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional['outputs.SecurityAssessmentMetadataPropertiesResponse']]:
        """
        Describes properties of an assessment metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnersData")
    def partners_data(self) -> pulumi.Output[Optional['outputs.SecurityAssessmentPartnerDataResponse']]:
        """
        Data regarding 3rd party partner integration
        """
        return pulumi.get(self, "partners_data")

    @property
    @pulumi.getter(name="resourceDetails")
    def resource_details(self) -> pulumi.Output[Any]:
        """
        Details of the resource that was assessed
        """
        return pulumi.get(self, "resource_details")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.AssessmentStatusResponse']:
        """
        The result of the assessment
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

