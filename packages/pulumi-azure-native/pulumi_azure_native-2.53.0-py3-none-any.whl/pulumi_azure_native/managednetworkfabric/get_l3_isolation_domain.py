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
    'GetL3IsolationDomainResult',
    'AwaitableGetL3IsolationDomainResult',
    'get_l3_isolation_domain',
    'get_l3_isolation_domain_output',
]

@pulumi.output_type
class GetL3IsolationDomainResult:
    """
    The L3IsolationDomain resource definition.
    """
    def __init__(__self__, administrative_state=None, aggregate_route_configuration=None, annotation=None, connected_subnet_route_policy=None, description=None, disabled_on_resources=None, id=None, location=None, name=None, network_fabric_id=None, option_b_disabled_on_resources=None, provisioning_state=None, redistribute_connected_subnets=None, redistribute_static_routes=None, system_data=None, tags=None, type=None):
        if administrative_state and not isinstance(administrative_state, str):
            raise TypeError("Expected argument 'administrative_state' to be a str")
        pulumi.set(__self__, "administrative_state", administrative_state)
        if aggregate_route_configuration and not isinstance(aggregate_route_configuration, dict):
            raise TypeError("Expected argument 'aggregate_route_configuration' to be a dict")
        pulumi.set(__self__, "aggregate_route_configuration", aggregate_route_configuration)
        if annotation and not isinstance(annotation, str):
            raise TypeError("Expected argument 'annotation' to be a str")
        pulumi.set(__self__, "annotation", annotation)
        if connected_subnet_route_policy and not isinstance(connected_subnet_route_policy, dict):
            raise TypeError("Expected argument 'connected_subnet_route_policy' to be a dict")
        pulumi.set(__self__, "connected_subnet_route_policy", connected_subnet_route_policy)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disabled_on_resources and not isinstance(disabled_on_resources, list):
            raise TypeError("Expected argument 'disabled_on_resources' to be a list")
        pulumi.set(__self__, "disabled_on_resources", disabled_on_resources)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_fabric_id and not isinstance(network_fabric_id, str):
            raise TypeError("Expected argument 'network_fabric_id' to be a str")
        pulumi.set(__self__, "network_fabric_id", network_fabric_id)
        if option_b_disabled_on_resources and not isinstance(option_b_disabled_on_resources, list):
            raise TypeError("Expected argument 'option_b_disabled_on_resources' to be a list")
        pulumi.set(__self__, "option_b_disabled_on_resources", option_b_disabled_on_resources)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if redistribute_connected_subnets and not isinstance(redistribute_connected_subnets, str):
            raise TypeError("Expected argument 'redistribute_connected_subnets' to be a str")
        pulumi.set(__self__, "redistribute_connected_subnets", redistribute_connected_subnets)
        if redistribute_static_routes and not isinstance(redistribute_static_routes, str):
            raise TypeError("Expected argument 'redistribute_static_routes' to be a str")
        pulumi.set(__self__, "redistribute_static_routes", redistribute_static_routes)
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
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> str:
        """
        Administrative state of the IsolationDomain. Example: Enabled | Disabled.
        """
        return pulumi.get(self, "administrative_state")

    @property
    @pulumi.getter(name="aggregateRouteConfiguration")
    def aggregate_route_configuration(self) -> Optional['outputs.AggregateRouteConfigurationResponse']:
        """
        List of Ipv4 and Ipv6 route configurations.
        """
        return pulumi.get(self, "aggregate_route_configuration")

    @property
    @pulumi.getter
    def annotation(self) -> Optional[str]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter(name="connectedSubnetRoutePolicy")
    def connected_subnet_route_policy(self) -> Optional['outputs.L3IsolationDomainPatchPropertiesResponseConnectedSubnetRoutePolicy']:
        """
        Connected Subnet RoutePolicy
        """
        return pulumi.get(self, "connected_subnet_route_policy")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        L3 Isolation Domain description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disabledOnResources")
    def disabled_on_resources(self) -> Sequence[str]:
        """
        List of resources the L3 Isolation Domain is disabled on. Can be either entire NetworkFabric or NetworkRack.
        """
        return pulumi.get(self, "disabled_on_resources")

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
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> str:
        """
        Network Fabric ARM resource id.
        """
        return pulumi.get(self, "network_fabric_id")

    @property
    @pulumi.getter(name="optionBDisabledOnResources")
    def option_b_disabled_on_resources(self) -> Sequence[str]:
        """
        List of resources the OptionB is disabled on. Can be either entire NetworkFabric or NetworkRack.
        """
        return pulumi.get(self, "option_b_disabled_on_resources")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets the provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="redistributeConnectedSubnets")
    def redistribute_connected_subnets(self) -> Optional[str]:
        """
        Advertise Connected Subnets. Ex: "True" | "False".
        """
        return pulumi.get(self, "redistribute_connected_subnets")

    @property
    @pulumi.getter(name="redistributeStaticRoutes")
    def redistribute_static_routes(self) -> Optional[str]:
        """
        Advertise Static Routes. Ex: "True" | "False".
        """
        return pulumi.get(self, "redistribute_static_routes")

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


class AwaitableGetL3IsolationDomainResult(GetL3IsolationDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetL3IsolationDomainResult(
            administrative_state=self.administrative_state,
            aggregate_route_configuration=self.aggregate_route_configuration,
            annotation=self.annotation,
            connected_subnet_route_policy=self.connected_subnet_route_policy,
            description=self.description,
            disabled_on_resources=self.disabled_on_resources,
            id=self.id,
            location=self.location,
            name=self.name,
            network_fabric_id=self.network_fabric_id,
            option_b_disabled_on_resources=self.option_b_disabled_on_resources,
            provisioning_state=self.provisioning_state,
            redistribute_connected_subnets=self.redistribute_connected_subnets,
            redistribute_static_routes=self.redistribute_static_routes,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_l3_isolation_domain(l3_isolation_domain_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetL3IsolationDomainResult:
    """
    Retrieves details of this L3 Isolation Domain.
    Azure REST API version: 2023-02-01-preview.

    Other available API versions: 2023-06-15.


    :param str l3_isolation_domain_name: Name of the L3 Isolation Domain
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['l3IsolationDomainName'] = l3_isolation_domain_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetworkfabric:getL3IsolationDomain', __args__, opts=opts, typ=GetL3IsolationDomainResult).value

    return AwaitableGetL3IsolationDomainResult(
        administrative_state=pulumi.get(__ret__, 'administrative_state'),
        aggregate_route_configuration=pulumi.get(__ret__, 'aggregate_route_configuration'),
        annotation=pulumi.get(__ret__, 'annotation'),
        connected_subnet_route_policy=pulumi.get(__ret__, 'connected_subnet_route_policy'),
        description=pulumi.get(__ret__, 'description'),
        disabled_on_resources=pulumi.get(__ret__, 'disabled_on_resources'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_fabric_id=pulumi.get(__ret__, 'network_fabric_id'),
        option_b_disabled_on_resources=pulumi.get(__ret__, 'option_b_disabled_on_resources'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        redistribute_connected_subnets=pulumi.get(__ret__, 'redistribute_connected_subnets'),
        redistribute_static_routes=pulumi.get(__ret__, 'redistribute_static_routes'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_l3_isolation_domain)
def get_l3_isolation_domain_output(l3_isolation_domain_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetL3IsolationDomainResult]:
    """
    Retrieves details of this L3 Isolation Domain.
    Azure REST API version: 2023-02-01-preview.

    Other available API versions: 2023-06-15.


    :param str l3_isolation_domain_name: Name of the L3 Isolation Domain
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
