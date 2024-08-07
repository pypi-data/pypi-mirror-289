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
from ._inputs import *

__all__ = ['NetworkFabricControllerArgs', 'NetworkFabricController']

@pulumi.input_type
class NetworkFabricControllerArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 annotation: Optional[pulumi.Input[str]] = None,
                 infrastructure_express_route_connections: Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteConnectionInformationArgs']]]] = None,
                 ipv4_address_space: Optional[pulumi.Input[str]] = None,
                 ipv6_address_space: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_configuration: Optional[pulumi.Input['ManagedResourceGroupConfigurationArgs']] = None,
                 network_fabric_controller_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workload_express_route_connections: Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteConnectionInformationArgs']]]] = None):
        """
        The set of arguments for constructing a NetworkFabricController resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[Sequence[pulumi.Input['ExpressRouteConnectionInformationArgs']]] infrastructure_express_route_connections: As part of an update, the Infrastructure ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Infrastructure services. (This is a Mandatory attribute)
        :param pulumi.Input[str] ipv4_address_space: IPv4 Network Fabric Controller Address Space.
        :param pulumi.Input[str] ipv6_address_space: IPv6 Network Fabric Controller Address Space.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['ManagedResourceGroupConfigurationArgs'] managed_resource_group_configuration: Managed Resource Group configuration properties.
        :param pulumi.Input[str] network_fabric_controller_name: Name of the Network Fabric Controller
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input['ExpressRouteConnectionInformationArgs']]] workload_express_route_connections: As part of an update, the workload ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Workload services. (This is a Mandatory attribute).
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if annotation is not None:
            pulumi.set(__self__, "annotation", annotation)
        if infrastructure_express_route_connections is not None:
            pulumi.set(__self__, "infrastructure_express_route_connections", infrastructure_express_route_connections)
        if ipv4_address_space is not None:
            pulumi.set(__self__, "ipv4_address_space", ipv4_address_space)
        if ipv6_address_space is not None:
            pulumi.set(__self__, "ipv6_address_space", ipv6_address_space)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_resource_group_configuration is not None:
            pulumi.set(__self__, "managed_resource_group_configuration", managed_resource_group_configuration)
        if network_fabric_controller_name is not None:
            pulumi.set(__self__, "network_fabric_controller_name", network_fabric_controller_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if workload_express_route_connections is not None:
            pulumi.set(__self__, "workload_express_route_connections", workload_express_route_connections)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def annotation(self) -> Optional[pulumi.Input[str]]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @annotation.setter
    def annotation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "annotation", value)

    @property
    @pulumi.getter(name="infrastructureExpressRouteConnections")
    def infrastructure_express_route_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteConnectionInformationArgs']]]]:
        """
        As part of an update, the Infrastructure ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Infrastructure services. (This is a Mandatory attribute)
        """
        return pulumi.get(self, "infrastructure_express_route_connections")

    @infrastructure_express_route_connections.setter
    def infrastructure_express_route_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteConnectionInformationArgs']]]]):
        pulumi.set(self, "infrastructure_express_route_connections", value)

    @property
    @pulumi.getter(name="ipv4AddressSpace")
    def ipv4_address_space(self) -> Optional[pulumi.Input[str]]:
        """
        IPv4 Network Fabric Controller Address Space.
        """
        return pulumi.get(self, "ipv4_address_space")

    @ipv4_address_space.setter
    def ipv4_address_space(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_address_space", value)

    @property
    @pulumi.getter(name="ipv6AddressSpace")
    def ipv6_address_space(self) -> Optional[pulumi.Input[str]]:
        """
        IPv6 Network Fabric Controller Address Space.
        """
        return pulumi.get(self, "ipv6_address_space")

    @ipv6_address_space.setter
    def ipv6_address_space(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_address_space", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(self) -> Optional[pulumi.Input['ManagedResourceGroupConfigurationArgs']]:
        """
        Managed Resource Group configuration properties.
        """
        return pulumi.get(self, "managed_resource_group_configuration")

    @managed_resource_group_configuration.setter
    def managed_resource_group_configuration(self, value: Optional[pulumi.Input['ManagedResourceGroupConfigurationArgs']]):
        pulumi.set(self, "managed_resource_group_configuration", value)

    @property
    @pulumi.getter(name="networkFabricControllerName")
    def network_fabric_controller_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Network Fabric Controller
        """
        return pulumi.get(self, "network_fabric_controller_name")

    @network_fabric_controller_name.setter
    def network_fabric_controller_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_fabric_controller_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workloadExpressRouteConnections")
    def workload_express_route_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteConnectionInformationArgs']]]]:
        """
        As part of an update, the workload ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Workload services. (This is a Mandatory attribute).
        """
        return pulumi.get(self, "workload_express_route_connections")

    @workload_express_route_connections.setter
    def workload_express_route_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteConnectionInformationArgs']]]]):
        pulumi.set(self, "workload_express_route_connections", value)


class NetworkFabricController(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 infrastructure_express_route_connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ExpressRouteConnectionInformationArgs', 'ExpressRouteConnectionInformationArgsDict']]]]] = None,
                 ipv4_address_space: Optional[pulumi.Input[str]] = None,
                 ipv6_address_space: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_configuration: Optional[pulumi.Input[Union['ManagedResourceGroupConfigurationArgs', 'ManagedResourceGroupConfigurationArgsDict']]] = None,
                 network_fabric_controller_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workload_express_route_connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ExpressRouteConnectionInformationArgs', 'ExpressRouteConnectionInformationArgsDict']]]]] = None,
                 __props__=None):
        """
        The NetworkFabricController resource definition.
        Azure REST API version: 2023-02-01-preview. Prior API version in Azure Native 1.x: 2023-02-01-preview.

        Other available API versions: 2023-06-15.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ExpressRouteConnectionInformationArgs', 'ExpressRouteConnectionInformationArgsDict']]]] infrastructure_express_route_connections: As part of an update, the Infrastructure ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Infrastructure services. (This is a Mandatory attribute)
        :param pulumi.Input[str] ipv4_address_space: IPv4 Network Fabric Controller Address Space.
        :param pulumi.Input[str] ipv6_address_space: IPv6 Network Fabric Controller Address Space.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union['ManagedResourceGroupConfigurationArgs', 'ManagedResourceGroupConfigurationArgsDict']] managed_resource_group_configuration: Managed Resource Group configuration properties.
        :param pulumi.Input[str] network_fabric_controller_name: Name of the Network Fabric Controller
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ExpressRouteConnectionInformationArgs', 'ExpressRouteConnectionInformationArgsDict']]]] workload_express_route_connections: As part of an update, the workload ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Workload services. (This is a Mandatory attribute).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkFabricControllerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The NetworkFabricController resource definition.
        Azure REST API version: 2023-02-01-preview. Prior API version in Azure Native 1.x: 2023-02-01-preview.

        Other available API versions: 2023-06-15.

        :param str resource_name: The name of the resource.
        :param NetworkFabricControllerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkFabricControllerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 infrastructure_express_route_connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ExpressRouteConnectionInformationArgs', 'ExpressRouteConnectionInformationArgsDict']]]]] = None,
                 ipv4_address_space: Optional[pulumi.Input[str]] = None,
                 ipv6_address_space: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_resource_group_configuration: Optional[pulumi.Input[Union['ManagedResourceGroupConfigurationArgs', 'ManagedResourceGroupConfigurationArgsDict']]] = None,
                 network_fabric_controller_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workload_express_route_connections: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ExpressRouteConnectionInformationArgs', 'ExpressRouteConnectionInformationArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkFabricControllerArgs.__new__(NetworkFabricControllerArgs)

            __props__.__dict__["annotation"] = annotation
            __props__.__dict__["infrastructure_express_route_connections"] = infrastructure_express_route_connections
            __props__.__dict__["ipv4_address_space"] = ipv4_address_space
            __props__.__dict__["ipv6_address_space"] = ipv6_address_space
            __props__.__dict__["location"] = location
            __props__.__dict__["managed_resource_group_configuration"] = managed_resource_group_configuration
            __props__.__dict__["network_fabric_controller_name"] = network_fabric_controller_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["workload_express_route_connections"] = workload_express_route_connections
            __props__.__dict__["infrastructure_services"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["network_fabric_ids"] = None
            __props__.__dict__["operational_state"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["workload_management_network"] = None
            __props__.__dict__["workload_services"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:managednetworkfabric/v20230201preview:NetworkFabricController"), pulumi.Alias(type_="azure-native:managednetworkfabric/v20230615:NetworkFabricController")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NetworkFabricController, __self__).__init__(
            'azure-native:managednetworkfabric:NetworkFabricController',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkFabricController':
        """
        Get an existing NetworkFabricController resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkFabricControllerArgs.__new__(NetworkFabricControllerArgs)

        __props__.__dict__["annotation"] = None
        __props__.__dict__["infrastructure_express_route_connections"] = None
        __props__.__dict__["infrastructure_services"] = None
        __props__.__dict__["ipv4_address_space"] = None
        __props__.__dict__["ipv6_address_space"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_resource_group_configuration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_fabric_ids"] = None
        __props__.__dict__["operational_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["workload_express_route_connections"] = None
        __props__.__dict__["workload_management_network"] = None
        __props__.__dict__["workload_services"] = None
        return NetworkFabricController(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotation(self) -> pulumi.Output[Optional[str]]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter(name="infrastructureExpressRouteConnections")
    def infrastructure_express_route_connections(self) -> pulumi.Output[Optional[Sequence['outputs.ExpressRouteConnectionInformationResponse']]]:
        """
        As part of an update, the Infrastructure ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Infrastructure services. (This is a Mandatory attribute)
        """
        return pulumi.get(self, "infrastructure_express_route_connections")

    @property
    @pulumi.getter(name="infrastructureServices")
    def infrastructure_services(self) -> pulumi.Output['outputs.InfrastructureServicesResponse']:
        """
        InfrastructureServices IP ranges.
        """
        return pulumi.get(self, "infrastructure_services")

    @property
    @pulumi.getter(name="ipv4AddressSpace")
    def ipv4_address_space(self) -> pulumi.Output[Optional[str]]:
        """
        IPv4 Network Fabric Controller Address Space.
        """
        return pulumi.get(self, "ipv4_address_space")

    @property
    @pulumi.getter(name="ipv6AddressSpace")
    def ipv6_address_space(self) -> pulumi.Output[Optional[str]]:
        """
        IPv6 Network Fabric Controller Address Space.
        """
        return pulumi.get(self, "ipv6_address_space")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedResourceGroupConfiguration")
    def managed_resource_group_configuration(self) -> pulumi.Output[Optional['outputs.ManagedResourceGroupConfigurationResponse']]:
        """
        Managed Resource Group configuration properties.
        """
        return pulumi.get(self, "managed_resource_group_configuration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkFabricIds")
    def network_fabric_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The NF-ID will be an input parameter used by the NF to link and get associated with the parent NFC Service.
        """
        return pulumi.get(self, "network_fabric_ids")

    @property
    @pulumi.getter(name="operationalState")
    def operational_state(self) -> pulumi.Output[str]:
        """
        The Operational Status would always be NULL. Look only in to the Provisioning state for the latest status.
        """
        return pulumi.get(self, "operational_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provides you the latest status of the NFC service, whether it is Accepted, updating, Succeeded or Failed. During this process, the states keep changing based on the status of NFC provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workloadExpressRouteConnections")
    def workload_express_route_connections(self) -> pulumi.Output[Optional[Sequence['outputs.ExpressRouteConnectionInformationResponse']]]:
        """
        As part of an update, the workload ExpressRoute CircuitID should be provided to create and Provision a NFC. This Express route is dedicated for Workload services. (This is a Mandatory attribute).
        """
        return pulumi.get(self, "workload_express_route_connections")

    @property
    @pulumi.getter(name="workloadManagementNetwork")
    def workload_management_network(self) -> pulumi.Output[bool]:
        """
        A workload management network is required for all the tenant (workload) traffic. This traffic is only dedicated for Tenant workloads which are required to access internet or any other MSFT/Public endpoints.
        """
        return pulumi.get(self, "workload_management_network")

    @property
    @pulumi.getter(name="workloadServices")
    def workload_services(self) -> pulumi.Output['outputs.WorkloadServicesResponse']:
        """
        WorkloadServices IP ranges.
        """
        return pulumi.get(self, "workload_services")

