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
    'GetRoutePolicyResult',
    'AwaitableGetRoutePolicyResult',
    'get_route_policy',
    'get_route_policy_output',
]

@pulumi.output_type
class GetRoutePolicyResult:
    """
    The RoutePolicy resource definition.
    """
    def __init__(__self__, annotation=None, id=None, location=None, name=None, provisioning_state=None, statements=None, system_data=None, tags=None, type=None):
        if annotation and not isinstance(annotation, str):
            raise TypeError("Expected argument 'annotation' to be a str")
        pulumi.set(__self__, "annotation", annotation)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if statements and not isinstance(statements, list):
            raise TypeError("Expected argument 'statements' to be a list")
        pulumi.set(__self__, "statements", statements)
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
    @pulumi.getter
    def annotation(self) -> Optional[str]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

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
        Gets the provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def statements(self) -> Sequence['outputs.RoutePolicyStatementPropertiesResponse']:
        """
        Route Policy statements.
        """
        return pulumi.get(self, "statements")

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
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetRoutePolicyResult(GetRoutePolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoutePolicyResult(
            annotation=self.annotation,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            statements=self.statements,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_route_policy(resource_group_name: Optional[str] = None,
                     route_policy_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRoutePolicyResult:
    """
    Implements Route Policy GET method.
    Azure REST API version: 2023-02-01-preview.

    Other available API versions: 2023-06-15.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str route_policy_name: Name of the Route Policy
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['routePolicyName'] = route_policy_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetworkfabric:getRoutePolicy', __args__, opts=opts, typ=GetRoutePolicyResult).value

    return AwaitableGetRoutePolicyResult(
        annotation=pulumi.get(__ret__, 'annotation'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        statements=pulumi.get(__ret__, 'statements'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_route_policy)
def get_route_policy_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                            route_policy_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRoutePolicyResult]:
    """
    Implements Route Policy GET method.
    Azure REST API version: 2023-02-01-preview.

    Other available API versions: 2023-06-15.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str route_policy_name: Name of the Route Policy
    """
    ...
