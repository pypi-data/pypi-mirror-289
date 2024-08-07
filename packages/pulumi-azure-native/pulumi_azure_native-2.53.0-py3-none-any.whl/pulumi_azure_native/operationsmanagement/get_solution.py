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
    'GetSolutionResult',
    'AwaitableGetSolutionResult',
    'get_solution',
    'get_solution_output',
]

@pulumi.output_type
class GetSolutionResult:
    """
    The container for solution.
    """
    def __init__(__self__, id=None, location=None, name=None, plan=None, properties=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if plan and not isinstance(plan, dict):
            raise TypeError("Expected argument 'plan' to be a dict")
        pulumi.set(__self__, "plan", plan)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> Optional['outputs.SolutionPlanResponse']:
        """
        Plan for solution object supported by the OperationsManagement resource provider.
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.SolutionPropertiesResponse':
        """
        Properties for solution object supported by the OperationsManagement resource provider.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetSolutionResult(GetSolutionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSolutionResult(
            id=self.id,
            location=self.location,
            name=self.name,
            plan=self.plan,
            properties=self.properties,
            tags=self.tags,
            type=self.type)


def get_solution(resource_group_name: Optional[str] = None,
                 solution_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSolutionResult:
    """
    Retrieves the user solution.
    Azure REST API version: 2015-11-01-preview.


    :param str resource_group_name: The name of the resource group to get. The name is case insensitive.
    :param str solution_name: User Solution Name.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['solutionName'] = solution_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:operationsmanagement:getSolution', __args__, opts=opts, typ=GetSolutionResult).value

    return AwaitableGetSolutionResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        plan=pulumi.get(__ret__, 'plan'),
        properties=pulumi.get(__ret__, 'properties'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_solution)
def get_solution_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                        solution_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSolutionResult]:
    """
    Retrieves the user solution.
    Azure REST API version: 2015-11-01-preview.


    :param str resource_group_name: The name of the resource group to get. The name is case insensitive.
    :param str solution_name: User Solution Name.
    """
    ...
