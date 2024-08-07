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
from ._enums import *

__all__ = [
    'ResourceMetadataArgs',
    'ResourceMetadataArgsDict',
    'ScopingAnswerArgs',
    'ScopingAnswerArgsDict',
    'StorageInfoArgs',
    'StorageInfoArgsDict',
]

MYPY = False

if not MYPY:
    class ResourceMetadataArgsDict(TypedDict):
        """
        Single resource Id's metadata.
        """
        resource_id: pulumi.Input[str]
        """
        Resource Id - e.g. "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Compute/virtualMachines/vm1".
        """
        account_id: NotRequired[pulumi.Input[str]]
        """
        Account Id. For example - the AWS account id.
        """
        resource_kind: NotRequired[pulumi.Input[str]]
        """
        Resource kind.
        """
        resource_origin: NotRequired[pulumi.Input[Union[str, 'ResourceOrigin']]]
        """
        Resource Origin.
        """
        resource_type: NotRequired[pulumi.Input[str]]
        """
        Resource type. e.g. "Microsoft.Compute/virtualMachines"
        """
elif False:
    ResourceMetadataArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ResourceMetadataArgs:
    def __init__(__self__, *,
                 resource_id: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 resource_kind: Optional[pulumi.Input[str]] = None,
                 resource_origin: Optional[pulumi.Input[Union[str, 'ResourceOrigin']]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None):
        """
        Single resource Id's metadata.
        :param pulumi.Input[str] resource_id: Resource Id - e.g. "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Compute/virtualMachines/vm1".
        :param pulumi.Input[str] account_id: Account Id. For example - the AWS account id.
        :param pulumi.Input[str] resource_kind: Resource kind.
        :param pulumi.Input[Union[str, 'ResourceOrigin']] resource_origin: Resource Origin.
        :param pulumi.Input[str] resource_type: Resource type. e.g. "Microsoft.Compute/virtualMachines"
        """
        pulumi.set(__self__, "resource_id", resource_id)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if resource_kind is not None:
            pulumi.set(__self__, "resource_kind", resource_kind)
        if resource_origin is not None:
            pulumi.set(__self__, "resource_origin", resource_origin)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        Resource Id - e.g. "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/rg1/providers/Microsoft.Compute/virtualMachines/vm1".
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Account Id. For example - the AWS account id.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="resourceKind")
    def resource_kind(self) -> Optional[pulumi.Input[str]]:
        """
        Resource kind.
        """
        return pulumi.get(self, "resource_kind")

    @resource_kind.setter
    def resource_kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_kind", value)

    @property
    @pulumi.getter(name="resourceOrigin")
    def resource_origin(self) -> Optional[pulumi.Input[Union[str, 'ResourceOrigin']]]:
        """
        Resource Origin.
        """
        return pulumi.get(self, "resource_origin")

    @resource_origin.setter
    def resource_origin(self, value: Optional[pulumi.Input[Union[str, 'ResourceOrigin']]]):
        pulumi.set(self, "resource_origin", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        Resource type. e.g. "Microsoft.Compute/virtualMachines"
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_type", value)


if not MYPY:
    class ScopingAnswerArgsDict(TypedDict):
        """
        Scoping answer.
        """
        answers: pulumi.Input[Sequence[pulumi.Input[str]]]
        """
        Question answer value list.
        """
        question_id: pulumi.Input[str]
        """
        Question id.
        """
elif False:
    ScopingAnswerArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ScopingAnswerArgs:
    def __init__(__self__, *,
                 answers: pulumi.Input[Sequence[pulumi.Input[str]]],
                 question_id: pulumi.Input[str]):
        """
        Scoping answer.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] answers: Question answer value list.
        :param pulumi.Input[str] question_id: Question id.
        """
        pulumi.set(__self__, "answers", answers)
        pulumi.set(__self__, "question_id", question_id)

    @property
    @pulumi.getter
    def answers(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Question answer value list.
        """
        return pulumi.get(self, "answers")

    @answers.setter
    def answers(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "answers", value)

    @property
    @pulumi.getter(name="questionId")
    def question_id(self) -> pulumi.Input[str]:
        """
        Question id.
        """
        return pulumi.get(self, "question_id")

    @question_id.setter
    def question_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "question_id", value)


if not MYPY:
    class StorageInfoArgsDict(TypedDict):
        """
        The information of 'bring your own storage' account binding to the report
        """
        account_name: NotRequired[pulumi.Input[str]]
        """
        'bring your own storage' account name
        """
        location: NotRequired[pulumi.Input[str]]
        """
        The region of 'bring your own storage' account
        """
        resource_group: NotRequired[pulumi.Input[str]]
        """
        The resourceGroup which 'bring your own storage' account belongs to
        """
        subscription_id: NotRequired[pulumi.Input[str]]
        """
        The subscription id which 'bring your own storage' account belongs to
        """
elif False:
    StorageInfoArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class StorageInfoArgs:
    def __init__(__self__, *,
                 account_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None):
        """
        The information of 'bring your own storage' account binding to the report
        :param pulumi.Input[str] account_name: 'bring your own storage' account name
        :param pulumi.Input[str] location: The region of 'bring your own storage' account
        :param pulumi.Input[str] resource_group: The resourceGroup which 'bring your own storage' account belongs to
        :param pulumi.Input[str] subscription_id: The subscription id which 'bring your own storage' account belongs to
        """
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if resource_group is not None:
            pulumi.set(__self__, "resource_group", resource_group)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        'bring your own storage' account name
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The region of 'bring your own storage' account
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[str]]:
        """
        The resourceGroup which 'bring your own storage' account belongs to
        """
        return pulumi.get(self, "resource_group")

    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The subscription id which 'bring your own storage' account belongs to
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)


