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
from ._enums import *
from ._inputs import *

__all__ = ['GatewayArgs', 'Gateway']

@pulumi.input_type
class GatewayArgs:
    def __init__(__self__, *,
                 destination_network: pulumi.Input['NetworkRefArgs'],
                 resource_group_name: pulumi.Input[str],
                 source_network: pulumi.Input['NetworkRefArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 gateway_resource_name: Optional[pulumi.Input[str]] = None,
                 http: Optional[pulumi.Input[Sequence[pulumi.Input['HttpConfigArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tcp: Optional[pulumi.Input[Sequence[pulumi.Input['TcpConfigArgs']]]] = None):
        """
        The set of arguments for constructing a Gateway resource.
        :param pulumi.Input['NetworkRefArgs'] destination_network: Network that the Application is using.
        :param pulumi.Input[str] resource_group_name: Azure resource group name
        :param pulumi.Input['NetworkRefArgs'] source_network: Network the gateway should listen on for requests.
        :param pulumi.Input[str] description: User readable description of the gateway.
        :param pulumi.Input[str] gateway_resource_name: The identity of the gateway.
        :param pulumi.Input[Sequence[pulumi.Input['HttpConfigArgs']]] http: Configuration for http connectivity for this gateway.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input['TcpConfigArgs']]] tcp: Configuration for tcp connectivity for this gateway.
        """
        pulumi.set(__self__, "destination_network", destination_network)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source_network", source_network)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if gateway_resource_name is not None:
            pulumi.set(__self__, "gateway_resource_name", gateway_resource_name)
        if http is not None:
            pulumi.set(__self__, "http", http)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tcp is not None:
            pulumi.set(__self__, "tcp", tcp)

    @property
    @pulumi.getter(name="destinationNetwork")
    def destination_network(self) -> pulumi.Input['NetworkRefArgs']:
        """
        Network that the Application is using.
        """
        return pulumi.get(self, "destination_network")

    @destination_network.setter
    def destination_network(self, value: pulumi.Input['NetworkRefArgs']):
        pulumi.set(self, "destination_network", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Azure resource group name
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sourceNetwork")
    def source_network(self) -> pulumi.Input['NetworkRefArgs']:
        """
        Network the gateway should listen on for requests.
        """
        return pulumi.get(self, "source_network")

    @source_network.setter
    def source_network(self, value: pulumi.Input['NetworkRefArgs']):
        pulumi.set(self, "source_network", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        User readable description of the gateway.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="gatewayResourceName")
    def gateway_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The identity of the gateway.
        """
        return pulumi.get(self, "gateway_resource_name")

    @gateway_resource_name.setter
    def gateway_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_resource_name", value)

    @property
    @pulumi.getter
    def http(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['HttpConfigArgs']]]]:
        """
        Configuration for http connectivity for this gateway.
        """
        return pulumi.get(self, "http")

    @http.setter
    def http(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['HttpConfigArgs']]]]):
        pulumi.set(self, "http", value)

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
    @pulumi.getter
    def tcp(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TcpConfigArgs']]]]:
        """
        Configuration for tcp connectivity for this gateway.
        """
        return pulumi.get(self, "tcp")

    @tcp.setter
    def tcp(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TcpConfigArgs']]]]):
        pulumi.set(self, "tcp", value)


class Gateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_network: Optional[pulumi.Input[Union['NetworkRefArgs', 'NetworkRefArgsDict']]] = None,
                 gateway_resource_name: Optional[pulumi.Input[str]] = None,
                 http: Optional[pulumi.Input[Sequence[pulumi.Input[Union['HttpConfigArgs', 'HttpConfigArgsDict']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_network: Optional[pulumi.Input[Union['NetworkRefArgs', 'NetworkRefArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tcp: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TcpConfigArgs', 'TcpConfigArgsDict']]]]] = None,
                 __props__=None):
        """
        This type describes a gateway resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: User readable description of the gateway.
        :param pulumi.Input[Union['NetworkRefArgs', 'NetworkRefArgsDict']] destination_network: Network that the Application is using.
        :param pulumi.Input[str] gateway_resource_name: The identity of the gateway.
        :param pulumi.Input[Sequence[pulumi.Input[Union['HttpConfigArgs', 'HttpConfigArgsDict']]]] http: Configuration for http connectivity for this gateway.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: Azure resource group name
        :param pulumi.Input[Union['NetworkRefArgs', 'NetworkRefArgsDict']] source_network: Network the gateway should listen on for requests.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[Union['TcpConfigArgs', 'TcpConfigArgsDict']]]] tcp: Configuration for tcp connectivity for this gateway.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This type describes a gateway resource.

        :param str resource_name: The name of the resource.
        :param GatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 destination_network: Optional[pulumi.Input[Union['NetworkRefArgs', 'NetworkRefArgsDict']]] = None,
                 gateway_resource_name: Optional[pulumi.Input[str]] = None,
                 http: Optional[pulumi.Input[Sequence[pulumi.Input[Union['HttpConfigArgs', 'HttpConfigArgsDict']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_network: Optional[pulumi.Input[Union['NetworkRefArgs', 'NetworkRefArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tcp: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TcpConfigArgs', 'TcpConfigArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GatewayArgs.__new__(GatewayArgs)

            __props__.__dict__["description"] = description
            if destination_network is None and not opts.urn:
                raise TypeError("Missing required property 'destination_network'")
            __props__.__dict__["destination_network"] = destination_network
            __props__.__dict__["gateway_resource_name"] = gateway_resource_name
            __props__.__dict__["http"] = http
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if source_network is None and not opts.urn:
                raise TypeError("Missing required property 'source_network'")
            __props__.__dict__["source_network"] = source_network
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tcp"] = tcp
            __props__.__dict__["ip_address"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["status_details"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:servicefabricmesh:Gateway")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Gateway, __self__).__init__(
            'azure-native:servicefabricmesh/v20180901preview:Gateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Gateway':
        """
        Get an existing Gateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GatewayArgs.__new__(GatewayArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["destination_network"] = None
        __props__.__dict__["http"] = None
        __props__.__dict__["ip_address"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source_network"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["status_details"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tcp"] = None
        __props__.__dict__["type"] = None
        return Gateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        User readable description of the gateway.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationNetwork")
    def destination_network(self) -> pulumi.Output['outputs.NetworkRefResponse']:
        """
        Network that the Application is using.
        """
        return pulumi.get(self, "destination_network")

    @property
    @pulumi.getter
    def http(self) -> pulumi.Output[Optional[Sequence['outputs.HttpConfigResponse']]]:
        """
        Configuration for http connectivity for this gateway.
        """
        return pulumi.get(self, "http")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
        IP address of the gateway. This is populated in the response and is ignored for incoming requests.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        State of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourceNetwork")
    def source_network(self) -> pulumi.Output['outputs.NetworkRefResponse']:
        """
        Network the gateway should listen on for requests.
        """
        return pulumi.get(self, "source_network")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the resource.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusDetails")
    def status_details(self) -> pulumi.Output[str]:
        """
        Gives additional information about the current status of the gateway.
        """
        return pulumi.get(self, "status_details")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tcp(self) -> pulumi.Output[Optional[Sequence['outputs.TcpConfigResponse']]]:
        """
        Configuration for tcp connectivity for this gateway.
        """
        return pulumi.get(self, "tcp")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")

