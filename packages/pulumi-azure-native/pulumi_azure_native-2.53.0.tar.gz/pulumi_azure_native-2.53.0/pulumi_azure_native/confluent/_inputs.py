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

__all__ = [
    'OfferDetailArgs',
    'OfferDetailArgsDict',
    'UserDetailArgs',
    'UserDetailArgsDict',
]

MYPY = False

if not MYPY:
    class OfferDetailArgsDict(TypedDict):
        """
        Confluent Offer detail
        """
        id: pulumi.Input[str]
        """
        Offer Id
        """
        plan_id: pulumi.Input[str]
        """
        Offer Plan Id
        """
        plan_name: pulumi.Input[str]
        """
        Offer Plan Name
        """
        publisher_id: pulumi.Input[str]
        """
        Publisher Id
        """
        term_unit: pulumi.Input[str]
        """
        Offer Plan Term unit
        """
elif False:
    OfferDetailArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class OfferDetailArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 plan_id: pulumi.Input[str],
                 plan_name: pulumi.Input[str],
                 publisher_id: pulumi.Input[str],
                 term_unit: pulumi.Input[str]):
        """
        Confluent Offer detail
        :param pulumi.Input[str] id: Offer Id
        :param pulumi.Input[str] plan_id: Offer Plan Id
        :param pulumi.Input[str] plan_name: Offer Plan Name
        :param pulumi.Input[str] publisher_id: Publisher Id
        :param pulumi.Input[str] term_unit: Offer Plan Term unit
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "plan_id", plan_id)
        pulumi.set(__self__, "plan_name", plan_name)
        pulumi.set(__self__, "publisher_id", publisher_id)
        pulumi.set(__self__, "term_unit", term_unit)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        Offer Id
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="planId")
    def plan_id(self) -> pulumi.Input[str]:
        """
        Offer Plan Id
        """
        return pulumi.get(self, "plan_id")

    @plan_id.setter
    def plan_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "plan_id", value)

    @property
    @pulumi.getter(name="planName")
    def plan_name(self) -> pulumi.Input[str]:
        """
        Offer Plan Name
        """
        return pulumi.get(self, "plan_name")

    @plan_name.setter
    def plan_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "plan_name", value)

    @property
    @pulumi.getter(name="publisherId")
    def publisher_id(self) -> pulumi.Input[str]:
        """
        Publisher Id
        """
        return pulumi.get(self, "publisher_id")

    @publisher_id.setter
    def publisher_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "publisher_id", value)

    @property
    @pulumi.getter(name="termUnit")
    def term_unit(self) -> pulumi.Input[str]:
        """
        Offer Plan Term unit
        """
        return pulumi.get(self, "term_unit")

    @term_unit.setter
    def term_unit(self, value: pulumi.Input[str]):
        pulumi.set(self, "term_unit", value)


if not MYPY:
    class UserDetailArgsDict(TypedDict):
        """
        Subscriber detail
        """
        email_address: pulumi.Input[str]
        """
        Email address
        """
        first_name: NotRequired[pulumi.Input[str]]
        """
        First name
        """
        last_name: NotRequired[pulumi.Input[str]]
        """
        Last name
        """
elif False:
    UserDetailArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class UserDetailArgs:
    def __init__(__self__, *,
                 email_address: pulumi.Input[str],
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None):
        """
        Subscriber detail
        :param pulumi.Input[str] email_address: Email address
        :param pulumi.Input[str] first_name: First name
        :param pulumi.Input[str] last_name: Last name
        """
        pulumi.set(__self__, "email_address", email_address)
        if first_name is not None:
            pulumi.set(__self__, "first_name", first_name)
        if last_name is not None:
            pulumi.set(__self__, "last_name", last_name)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Input[str]:
        """
        Email address
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[str]]:
        """
        First name
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[str]]:
        """
        Last name
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_name", value)


