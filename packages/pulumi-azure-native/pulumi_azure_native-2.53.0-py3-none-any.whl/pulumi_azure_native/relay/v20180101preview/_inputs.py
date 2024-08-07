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
    'PrivateEndpointArgs',
    'PrivateEndpointArgsDict',
    'PrivateLinkServiceConnectionStateArgs',
    'PrivateLinkServiceConnectionStateArgsDict',
]

MYPY = False

if not MYPY:
    class PrivateEndpointArgsDict(TypedDict):
        """
        Private endpoint object properties.
        """
        id: NotRequired[pulumi.Input[str]]
        """
        Full identifier of the private endpoint resource.
        """
elif False:
    PrivateEndpointArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateEndpointArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        Private endpoint object properties.
        :param pulumi.Input[str] id: Full identifier of the private endpoint resource.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Full identifier of the private endpoint resource.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


if not MYPY:
    class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
        """
        An object that represents the approval state of the private link connection.
        """
        action_required: NotRequired[pulumi.Input[str]]
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        description: NotRequired[pulumi.Input[str]]
        """
        The reason for approval or rejection.
        """
        status: NotRequired[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]
        """
        Indicates whether the connection has been approved, rejected or removed by the Relay Namespace owner.
        """
elif False:
    PrivateLinkServiceConnectionStateArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 action_required: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]] = None):
        """
        An object that represents the approval state of the private link connection.
        :param pulumi.Input[str] action_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param pulumi.Input[str] description: The reason for approval or rejection.
        :param pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']] status: Indicates whether the connection has been approved, rejected or removed by the Relay Namespace owner.
        """
        if action_required is not None:
            pulumi.set(__self__, "action_required", action_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionRequired")
    def action_required(self) -> Optional[pulumi.Input[str]]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "action_required")

    @action_required.setter
    def action_required(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The reason for approval or rejection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]:
        """
        Indicates whether the connection has been approved, rejected or removed by the Relay Namespace owner.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]):
        pulumi.set(self, "status", value)


