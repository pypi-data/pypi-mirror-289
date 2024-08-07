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
from . import outputs
from ._inputs import *

__all__ = ['VNetPeeringArgs', 'VNetPeering']

@pulumi.input_type
class VNetPeeringArgs:
    def __init__(__self__, *,
                 remote_virtual_network: pulumi.Input['VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgs'],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 allow_forwarded_traffic: Optional[pulumi.Input[bool]] = None,
                 allow_gateway_transit: Optional[pulumi.Input[bool]] = None,
                 allow_virtual_network_access: Optional[pulumi.Input[bool]] = None,
                 databricks_address_space: Optional[pulumi.Input['AddressSpaceArgs']] = None,
                 databricks_virtual_network: Optional[pulumi.Input['VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgs']] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 remote_address_space: Optional[pulumi.Input['AddressSpaceArgs']] = None,
                 use_remote_gateways: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a VNetPeering resource.
        :param pulumi.Input['VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgs'] remote_virtual_network:  The remote virtual network should be in the same region. See here to learn more (https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering).
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[bool] allow_forwarded_traffic: Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.
        :param pulumi.Input[bool] allow_gateway_transit: If gateway links can be used in remote virtual networking to link to this virtual network.
        :param pulumi.Input[bool] allow_virtual_network_access: Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.
        :param pulumi.Input['AddressSpaceArgs'] databricks_address_space: The reference to the databricks virtual network address space.
        :param pulumi.Input['VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgs'] databricks_virtual_network:  The remote virtual network should be in the same region. See here to learn more (https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering).
        :param pulumi.Input[str] peering_name: The name of the workspace vNet peering.
        :param pulumi.Input['AddressSpaceArgs'] remote_address_space: The reference to the remote virtual network address space.
        :param pulumi.Input[bool] use_remote_gateways: If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.
        """
        pulumi.set(__self__, "remote_virtual_network", remote_virtual_network)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if allow_forwarded_traffic is not None:
            pulumi.set(__self__, "allow_forwarded_traffic", allow_forwarded_traffic)
        if allow_gateway_transit is not None:
            pulumi.set(__self__, "allow_gateway_transit", allow_gateway_transit)
        if allow_virtual_network_access is not None:
            pulumi.set(__self__, "allow_virtual_network_access", allow_virtual_network_access)
        if databricks_address_space is not None:
            pulumi.set(__self__, "databricks_address_space", databricks_address_space)
        if databricks_virtual_network is not None:
            pulumi.set(__self__, "databricks_virtual_network", databricks_virtual_network)
        if peering_name is not None:
            pulumi.set(__self__, "peering_name", peering_name)
        if remote_address_space is not None:
            pulumi.set(__self__, "remote_address_space", remote_address_space)
        if use_remote_gateways is not None:
            pulumi.set(__self__, "use_remote_gateways", use_remote_gateways)

    @property
    @pulumi.getter(name="remoteVirtualNetwork")
    def remote_virtual_network(self) -> pulumi.Input['VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgs']:
        """
         The remote virtual network should be in the same region. See here to learn more (https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering).
        """
        return pulumi.get(self, "remote_virtual_network")

    @remote_virtual_network.setter
    def remote_virtual_network(self, value: pulumi.Input['VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgs']):
        pulumi.set(self, "remote_virtual_network", value)

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
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="allowForwardedTraffic")
    def allow_forwarded_traffic(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.
        """
        return pulumi.get(self, "allow_forwarded_traffic")

    @allow_forwarded_traffic.setter
    def allow_forwarded_traffic(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_forwarded_traffic", value)

    @property
    @pulumi.getter(name="allowGatewayTransit")
    def allow_gateway_transit(self) -> Optional[pulumi.Input[bool]]:
        """
        If gateway links can be used in remote virtual networking to link to this virtual network.
        """
        return pulumi.get(self, "allow_gateway_transit")

    @allow_gateway_transit.setter
    def allow_gateway_transit(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_gateway_transit", value)

    @property
    @pulumi.getter(name="allowVirtualNetworkAccess")
    def allow_virtual_network_access(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.
        """
        return pulumi.get(self, "allow_virtual_network_access")

    @allow_virtual_network_access.setter
    def allow_virtual_network_access(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_virtual_network_access", value)

    @property
    @pulumi.getter(name="databricksAddressSpace")
    def databricks_address_space(self) -> Optional[pulumi.Input['AddressSpaceArgs']]:
        """
        The reference to the databricks virtual network address space.
        """
        return pulumi.get(self, "databricks_address_space")

    @databricks_address_space.setter
    def databricks_address_space(self, value: Optional[pulumi.Input['AddressSpaceArgs']]):
        pulumi.set(self, "databricks_address_space", value)

    @property
    @pulumi.getter(name="databricksVirtualNetwork")
    def databricks_virtual_network(self) -> Optional[pulumi.Input['VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgs']]:
        """
         The remote virtual network should be in the same region. See here to learn more (https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering).
        """
        return pulumi.get(self, "databricks_virtual_network")

    @databricks_virtual_network.setter
    def databricks_virtual_network(self, value: Optional[pulumi.Input['VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgs']]):
        pulumi.set(self, "databricks_virtual_network", value)

    @property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the workspace vNet peering.
        """
        return pulumi.get(self, "peering_name")

    @peering_name.setter
    def peering_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peering_name", value)

    @property
    @pulumi.getter(name="remoteAddressSpace")
    def remote_address_space(self) -> Optional[pulumi.Input['AddressSpaceArgs']]:
        """
        The reference to the remote virtual network address space.
        """
        return pulumi.get(self, "remote_address_space")

    @remote_address_space.setter
    def remote_address_space(self, value: Optional[pulumi.Input['AddressSpaceArgs']]):
        pulumi.set(self, "remote_address_space", value)

    @property
    @pulumi.getter(name="useRemoteGateways")
    def use_remote_gateways(self) -> Optional[pulumi.Input[bool]]:
        """
        If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.
        """
        return pulumi.get(self, "use_remote_gateways")

    @use_remote_gateways.setter
    def use_remote_gateways(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_remote_gateways", value)


class VNetPeering(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_forwarded_traffic: Optional[pulumi.Input[bool]] = None,
                 allow_gateway_transit: Optional[pulumi.Input[bool]] = None,
                 allow_virtual_network_access: Optional[pulumi.Input[bool]] = None,
                 databricks_address_space: Optional[pulumi.Input[Union['AddressSpaceArgs', 'AddressSpaceArgsDict']]] = None,
                 databricks_virtual_network: Optional[pulumi.Input[Union['VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgs', 'VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgsDict']]] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 remote_address_space: Optional[pulumi.Input[Union['AddressSpaceArgs', 'AddressSpaceArgsDict']]] = None,
                 remote_virtual_network: Optional[pulumi.Input[Union['VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgs', 'VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 use_remote_gateways: Optional[pulumi.Input[bool]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Peerings in a VirtualNetwork resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_forwarded_traffic: Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.
        :param pulumi.Input[bool] allow_gateway_transit: If gateway links can be used in remote virtual networking to link to this virtual network.
        :param pulumi.Input[bool] allow_virtual_network_access: Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.
        :param pulumi.Input[Union['AddressSpaceArgs', 'AddressSpaceArgsDict']] databricks_address_space: The reference to the databricks virtual network address space.
        :param pulumi.Input[Union['VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgs', 'VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgsDict']] databricks_virtual_network:  The remote virtual network should be in the same region. See here to learn more (https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering).
        :param pulumi.Input[str] peering_name: The name of the workspace vNet peering.
        :param pulumi.Input[Union['AddressSpaceArgs', 'AddressSpaceArgsDict']] remote_address_space: The reference to the remote virtual network address space.
        :param pulumi.Input[Union['VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgs', 'VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgsDict']] remote_virtual_network:  The remote virtual network should be in the same region. See here to learn more (https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering).
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[bool] use_remote_gateways: If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VNetPeeringArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Peerings in a VirtualNetwork resource

        :param str resource_name: The name of the resource.
        :param VNetPeeringArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VNetPeeringArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_forwarded_traffic: Optional[pulumi.Input[bool]] = None,
                 allow_gateway_transit: Optional[pulumi.Input[bool]] = None,
                 allow_virtual_network_access: Optional[pulumi.Input[bool]] = None,
                 databricks_address_space: Optional[pulumi.Input[Union['AddressSpaceArgs', 'AddressSpaceArgsDict']]] = None,
                 databricks_virtual_network: Optional[pulumi.Input[Union['VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgs', 'VirtualNetworkPeeringPropertiesFormatDatabricksVirtualNetworkArgsDict']]] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 remote_address_space: Optional[pulumi.Input[Union['AddressSpaceArgs', 'AddressSpaceArgsDict']]] = None,
                 remote_virtual_network: Optional[pulumi.Input[Union['VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgs', 'VirtualNetworkPeeringPropertiesFormatRemoteVirtualNetworkArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 use_remote_gateways: Optional[pulumi.Input[bool]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VNetPeeringArgs.__new__(VNetPeeringArgs)

            __props__.__dict__["allow_forwarded_traffic"] = allow_forwarded_traffic
            __props__.__dict__["allow_gateway_transit"] = allow_gateway_transit
            __props__.__dict__["allow_virtual_network_access"] = allow_virtual_network_access
            __props__.__dict__["databricks_address_space"] = databricks_address_space
            __props__.__dict__["databricks_virtual_network"] = databricks_virtual_network
            __props__.__dict__["peering_name"] = peering_name
            __props__.__dict__["remote_address_space"] = remote_address_space
            if remote_virtual_network is None and not opts.urn:
                raise TypeError("Missing required property 'remote_virtual_network'")
            __props__.__dict__["remote_virtual_network"] = remote_virtual_network
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["use_remote_gateways"] = use_remote_gateways
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["peering_state"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:databricks/v20230915preview:vNetPeering"), pulumi.Alias(type_="azure-native:databricks:VNetPeering"), pulumi.Alias(type_="azure-native:databricks:vNetPeering"), pulumi.Alias(type_="azure-native:databricks/v20180401:VNetPeering"), pulumi.Alias(type_="azure-native:databricks/v20180401:vNetPeering"), pulumi.Alias(type_="azure-native:databricks/v20210401preview:VNetPeering"), pulumi.Alias(type_="azure-native:databricks/v20210401preview:vNetPeering"), pulumi.Alias(type_="azure-native:databricks/v20220401preview:VNetPeering"), pulumi.Alias(type_="azure-native:databricks/v20220401preview:vNetPeering"), pulumi.Alias(type_="azure-native:databricks/v20230201:VNetPeering"), pulumi.Alias(type_="azure-native:databricks/v20230201:vNetPeering"), pulumi.Alias(type_="azure-native:databricks/v20240501:VNetPeering"), pulumi.Alias(type_="azure-native:databricks/v20240501:vNetPeering")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VNetPeering, __self__).__init__(
            'azure-native:databricks/v20230915preview:VNetPeering',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VNetPeering':
        """
        Get an existing VNetPeering resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VNetPeeringArgs.__new__(VNetPeeringArgs)

        __props__.__dict__["allow_forwarded_traffic"] = None
        __props__.__dict__["allow_gateway_transit"] = None
        __props__.__dict__["allow_virtual_network_access"] = None
        __props__.__dict__["databricks_address_space"] = None
        __props__.__dict__["databricks_virtual_network"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peering_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["remote_address_space"] = None
        __props__.__dict__["remote_virtual_network"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["use_remote_gateways"] = None
        return VNetPeering(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowForwardedTraffic")
    def allow_forwarded_traffic(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the forwarded traffic from the VMs in the local virtual network will be allowed/disallowed in remote virtual network.
        """
        return pulumi.get(self, "allow_forwarded_traffic")

    @property
    @pulumi.getter(name="allowGatewayTransit")
    def allow_gateway_transit(self) -> pulumi.Output[Optional[bool]]:
        """
        If gateway links can be used in remote virtual networking to link to this virtual network.
        """
        return pulumi.get(self, "allow_gateway_transit")

    @property
    @pulumi.getter(name="allowVirtualNetworkAccess")
    def allow_virtual_network_access(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the VMs in the local virtual network space would be able to access the VMs in remote virtual network space.
        """
        return pulumi.get(self, "allow_virtual_network_access")

    @property
    @pulumi.getter(name="databricksAddressSpace")
    def databricks_address_space(self) -> pulumi.Output[Optional['outputs.AddressSpaceResponse']]:
        """
        The reference to the databricks virtual network address space.
        """
        return pulumi.get(self, "databricks_address_space")

    @property
    @pulumi.getter(name="databricksVirtualNetwork")
    def databricks_virtual_network(self) -> pulumi.Output[Optional['outputs.VirtualNetworkPeeringPropertiesFormatResponseDatabricksVirtualNetwork']]:
        """
         The remote virtual network should be in the same region. See here to learn more (https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering).
        """
        return pulumi.get(self, "databricks_virtual_network")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the virtual network peering resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peeringState")
    def peering_state(self) -> pulumi.Output[str]:
        """
        The status of the virtual network peering.
        """
        return pulumi.get(self, "peering_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the virtual network peering resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="remoteAddressSpace")
    def remote_address_space(self) -> pulumi.Output[Optional['outputs.AddressSpaceResponse']]:
        """
        The reference to the remote virtual network address space.
        """
        return pulumi.get(self, "remote_address_space")

    @property
    @pulumi.getter(name="remoteVirtualNetwork")
    def remote_virtual_network(self) -> pulumi.Output['outputs.VirtualNetworkPeeringPropertiesFormatResponseRemoteVirtualNetwork']:
        """
         The remote virtual network should be in the same region. See here to learn more (https://docs.microsoft.com/en-us/azure/databricks/administration-guide/cloud-configurations/azure/vnet-peering).
        """
        return pulumi.get(self, "remote_virtual_network")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        type of the virtual network peering resource
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="useRemoteGateways")
    def use_remote_gateways(self) -> pulumi.Output[Optional[bool]]:
        """
        If remote gateways can be used on this virtual network. If the flag is set to true, and allowGatewayTransit on remote peering is also true, virtual network will use gateways of remote virtual network for transit. Only one peering can have this flag set to true. This flag cannot be set if virtual network already has a gateway.
        """
        return pulumi.get(self, "use_remote_gateways")

