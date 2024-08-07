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
from ._enums import *

__all__ = [
    'AttestationEvidenceArgs',
    'AttestationEvidenceArgsDict',
    'RemediationFiltersArgs',
    'RemediationFiltersArgsDict',
    'RemediationPropertiesFailureThresholdArgs',
    'RemediationPropertiesFailureThresholdArgsDict',
]

MYPY = False

if not MYPY:
    class AttestationEvidenceArgsDict(TypedDict):
        """
        A piece of evidence supporting the compliance state set in the attestation.
        """
        description: NotRequired[pulumi.Input[str]]
        """
        The description for this piece of evidence.
        """
        source_uri: NotRequired[pulumi.Input[str]]
        """
        The URI location of the evidence.
        """
elif False:
    AttestationEvidenceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class AttestationEvidenceArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 source_uri: Optional[pulumi.Input[str]] = None):
        """
        A piece of evidence supporting the compliance state set in the attestation.
        :param pulumi.Input[str] description: The description for this piece of evidence.
        :param pulumi.Input[str] source_uri: The URI location of the evidence.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if source_uri is not None:
            pulumi.set(__self__, "source_uri", source_uri)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description for this piece of evidence.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="sourceUri")
    def source_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The URI location of the evidence.
        """
        return pulumi.get(self, "source_uri")

    @source_uri.setter
    def source_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_uri", value)


if not MYPY:
    class RemediationFiltersArgsDict(TypedDict):
        """
        The filters that will be applied to determine which resources to remediate.
        """
        locations: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        The resource locations that will be remediated.
        """
elif False:
    RemediationFiltersArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class RemediationFiltersArgs:
    def __init__(__self__, *,
                 locations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The filters that will be applied to determine which resources to remediate.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] locations: The resource locations that will be remediated.
        """
        if locations is not None:
            pulumi.set(__self__, "locations", locations)

    @property
    @pulumi.getter
    def locations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The resource locations that will be remediated.
        """
        return pulumi.get(self, "locations")

    @locations.setter
    def locations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "locations", value)


if not MYPY:
    class RemediationPropertiesFailureThresholdArgsDict(TypedDict):
        """
        The remediation failure threshold settings
        """
        percentage: NotRequired[pulumi.Input[float]]
        """
        A number between 0.0 to 1.0 representing the percentage failure threshold. The remediation will fail if the percentage of failed remediation operations (i.e. failed deployments) exceeds this threshold.
        """
elif False:
    RemediationPropertiesFailureThresholdArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class RemediationPropertiesFailureThresholdArgs:
    def __init__(__self__, *,
                 percentage: Optional[pulumi.Input[float]] = None):
        """
        The remediation failure threshold settings
        :param pulumi.Input[float] percentage: A number between 0.0 to 1.0 representing the percentage failure threshold. The remediation will fail if the percentage of failed remediation operations (i.e. failed deployments) exceeds this threshold.
        """
        if percentage is not None:
            pulumi.set(__self__, "percentage", percentage)

    @property
    @pulumi.getter
    def percentage(self) -> Optional[pulumi.Input[float]]:
        """
        A number between 0.0 to 1.0 representing the percentage failure threshold. The remediation will fail if the percentage of failed remediation operations (i.e. failed deployments) exceeds this threshold.
        """
        return pulumi.get(self, "percentage")

    @percentage.setter
    def percentage(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "percentage", value)


