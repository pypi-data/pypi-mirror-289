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
    'LogSettingsArgs',
    'LogSettingsArgsDict',
    'PrivateEndpointArgs',
    'PrivateEndpointArgsDict',
    'PrivateLinkServiceConnectionStateArgs',
    'PrivateLinkServiceConnectionStateArgsDict',
    'RetentionPolicyArgs',
    'RetentionPolicyArgsDict',
    'TagsResourceArgs',
    'TagsResourceArgsDict',
]

MYPY = False

if not MYPY:
    class LogSettingsArgsDict(TypedDict):
        """
        Part of MultiTenantDiagnosticSettings. Specifies the settings for a particular log.
        """
        enabled: pulumi.Input[bool]
        """
        A value indicating whether this log is enabled.
        """
        category: NotRequired[pulumi.Input[Union[str, 'Category']]]
        """
        Name of a Diagnostic Log category for a resource type this setting is applied to. To obtain the list of Diagnostic Log categories for a resource, first perform a GET diagnostic settings operation.
        """
        retention_policy: NotRequired[pulumi.Input['RetentionPolicyArgsDict']]
        """
        The retention policy for this log.
        """
elif False:
    LogSettingsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class LogSettingsArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 category: Optional[pulumi.Input[Union[str, 'Category']]] = None,
                 retention_policy: Optional[pulumi.Input['RetentionPolicyArgs']] = None):
        """
        Part of MultiTenantDiagnosticSettings. Specifies the settings for a particular log.
        :param pulumi.Input[bool] enabled: A value indicating whether this log is enabled.
        :param pulumi.Input[Union[str, 'Category']] category: Name of a Diagnostic Log category for a resource type this setting is applied to. To obtain the list of Diagnostic Log categories for a resource, first perform a GET diagnostic settings operation.
        :param pulumi.Input['RetentionPolicyArgs'] retention_policy: The retention policy for this log.
        """
        pulumi.set(__self__, "enabled", enabled)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if retention_policy is not None:
            pulumi.set(__self__, "retention_policy", retention_policy)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        A value indicating whether this log is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[Union[str, 'Category']]]:
        """
        Name of a Diagnostic Log category for a resource type this setting is applied to. To obtain the list of Diagnostic Log categories for a resource, first perform a GET diagnostic settings operation.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[Union[str, 'Category']]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter(name="retentionPolicy")
    def retention_policy(self) -> Optional[pulumi.Input['RetentionPolicyArgs']]:
        """
        The retention policy for this log.
        """
        return pulumi.get(self, "retention_policy")

    @retention_policy.setter
    def retention_policy(self, value: Optional[pulumi.Input['RetentionPolicyArgs']]):
        pulumi.set(self, "retention_policy", value)


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
        actions_required: NotRequired[pulumi.Input[str]]
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        description: NotRequired[pulumi.Input[str]]
        """
        The reason for approval or rejection.
        """
        status: NotRequired[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]
        """
        Indicates whether the connection has been approved, rejected or removed by the given policy owner.
        """
elif False:
    PrivateLinkServiceConnectionStateArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 actions_required: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]] = None):
        """
        An object that represents the approval state of the private link connection.
        :param pulumi.Input[str] actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param pulumi.Input[str] description: The reason for approval or rejection.
        :param pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']] status: Indicates whether the connection has been approved, rejected or removed by the given policy owner.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[str]]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "actions_required", value)

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
        Indicates whether the connection has been approved, rejected or removed by the given policy owner.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]):
        pulumi.set(self, "status", value)


if not MYPY:
    class RetentionPolicyArgsDict(TypedDict):
        """
        Specifies the retention policy for the log.
        """
        days: pulumi.Input[int]
        """
        The number of days for the retention in days. A value of 0 will retain the events indefinitely.
        """
        enabled: pulumi.Input[bool]
        """
        A value indicating whether the retention policy is enabled.
        """
elif False:
    RetentionPolicyArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class RetentionPolicyArgs:
    def __init__(__self__, *,
                 days: pulumi.Input[int],
                 enabled: pulumi.Input[bool]):
        """
        Specifies the retention policy for the log.
        :param pulumi.Input[int] days: The number of days for the retention in days. A value of 0 will retain the events indefinitely.
        :param pulumi.Input[bool] enabled: A value indicating whether the retention policy is enabled.
        """
        pulumi.set(__self__, "days", days)
        pulumi.set(__self__, "enabled", enabled)

    @property
    @pulumi.getter
    def days(self) -> pulumi.Input[int]:
        """
        The number of days for the retention in days. A value of 0 will retain the events indefinitely.
        """
        return pulumi.get(self, "days")

    @days.setter
    def days(self, value: pulumi.Input[int]):
        pulumi.set(self, "days", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        A value indicating whether the retention policy is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)


if not MYPY:
    class TagsResourceArgsDict(TypedDict):
        """
        A container holding only the Tags for a resource, allowing the user to update the tags on a PrivateLinkConnection instance.
        """
        tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[str]]]]
        """
        Resource tags
        """
elif False:
    TagsResourceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class TagsResourceArgs:
    def __init__(__self__, *,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        A container holding only the Tags for a resource, allowing the user to update the tags on a PrivateLinkConnection instance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


