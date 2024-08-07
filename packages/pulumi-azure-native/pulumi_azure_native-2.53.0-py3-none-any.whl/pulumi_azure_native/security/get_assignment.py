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
    'GetAssignmentResult',
    'AwaitableGetAssignmentResult',
    'get_assignment',
    'get_assignment_output',
]

@pulumi.output_type
class GetAssignmentResult:
    """
    Security Assignment on a resource group over a given scope
    """
    def __init__(__self__, additional_data=None, assigned_component=None, assigned_standard=None, description=None, display_name=None, effect=None, etag=None, expires_on=None, id=None, kind=None, location=None, metadata=None, name=None, scope=None, system_data=None, tags=None, type=None):
        if additional_data and not isinstance(additional_data, dict):
            raise TypeError("Expected argument 'additional_data' to be a dict")
        pulumi.set(__self__, "additional_data", additional_data)
        if assigned_component and not isinstance(assigned_component, dict):
            raise TypeError("Expected argument 'assigned_component' to be a dict")
        pulumi.set(__self__, "assigned_component", assigned_component)
        if assigned_standard and not isinstance(assigned_standard, dict):
            raise TypeError("Expected argument 'assigned_standard' to be a dict")
        pulumi.set(__self__, "assigned_standard", assigned_standard)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if effect and not isinstance(effect, str):
            raise TypeError("Expected argument 'effect' to be a str")
        pulumi.set(__self__, "effect", effect)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if expires_on and not isinstance(expires_on, str):
            raise TypeError("Expected argument 'expires_on' to be a str")
        pulumi.set(__self__, "expires_on", expires_on)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> Optional['outputs.AssignmentPropertiesResponseAdditionalData']:
        """
        Additional data about the assignment
        """
        return pulumi.get(self, "additional_data")

    @property
    @pulumi.getter(name="assignedComponent")
    def assigned_component(self) -> Optional['outputs.AssignedComponentItemResponse']:
        """
        Component item with key as applied to this standard assignment over the given scope
        """
        return pulumi.get(self, "assigned_component")

    @property
    @pulumi.getter(name="assignedStandard")
    def assigned_standard(self) -> Optional['outputs.AssignedStandardItemResponse']:
        """
        Standard item with key as applied to this standard assignment over the given scope
        """
        return pulumi.get(self, "assigned_standard")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        description of the standardAssignment
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        display name of the standardAssignment
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def effect(self) -> Optional[str]:
        """
        expected effect of this assignment (Disable/Exempt/etc)
        """
        return pulumi.get(self, "effect")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Entity tag is used for comparing two or more entities from the same requested resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expiresOn")
    def expires_on(self) -> Optional[str]:
        """
        Expiration date of this assignment as a full ISO date
        """
        return pulumi.get(self, "expires_on")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of the resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Location where the resource is stored
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The assignment metadata. Metadata is an open ended object and is typically a collection of key value pairs.
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
    @pulumi.getter
    def scope(self) -> Optional[str]:
        """
        Scope to which the standardAssignment applies - can be a subscription path or a resource group under that subscription
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A list of key value pairs that describe the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetAssignmentResult(GetAssignmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAssignmentResult(
            additional_data=self.additional_data,
            assigned_component=self.assigned_component,
            assigned_standard=self.assigned_standard,
            description=self.description,
            display_name=self.display_name,
            effect=self.effect,
            etag=self.etag,
            expires_on=self.expires_on,
            id=self.id,
            kind=self.kind,
            location=self.location,
            metadata=self.metadata,
            name=self.name,
            scope=self.scope,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_assignment(assignment_id: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAssignmentResult:
    """
    Get a specific standard assignment for the requested scope by resourceId
    Azure REST API version: 2021-08-01-preview.


    :param str assignment_id: The security assignment key - unique key for the standard assignment
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    __args__ = dict()
    __args__['assignmentId'] = assignment_id
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:security:getAssignment', __args__, opts=opts, typ=GetAssignmentResult).value

    return AwaitableGetAssignmentResult(
        additional_data=pulumi.get(__ret__, 'additional_data'),
        assigned_component=pulumi.get(__ret__, 'assigned_component'),
        assigned_standard=pulumi.get(__ret__, 'assigned_standard'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        effect=pulumi.get(__ret__, 'effect'),
        etag=pulumi.get(__ret__, 'etag'),
        expires_on=pulumi.get(__ret__, 'expires_on'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        metadata=pulumi.get(__ret__, 'metadata'),
        name=pulumi.get(__ret__, 'name'),
        scope=pulumi.get(__ret__, 'scope'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_assignment)
def get_assignment_output(assignment_id: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAssignmentResult]:
    """
    Get a specific standard assignment for the requested scope by resourceId
    Azure REST API version: 2021-08-01-preview.


    :param str assignment_id: The security assignment key - unique key for the standard assignment
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    ...
