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

__all__ = ['PrivateEndpointConnectionByHostPoolArgs', 'PrivateEndpointConnectionByHostPool']

@pulumi.input_type
class PrivateEndpointConnectionByHostPoolArgs:
    def __init__(__self__, *,
                 host_pool_name: pulumi.Input[str],
                 private_link_service_connection_state: pulumi.Input['PrivateLinkServiceConnectionStateArgs'],
                 resource_group_name: pulumi.Input[str],
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PrivateEndpointConnectionByHostPool resource.
        :param pulumi.Input[str] host_pool_name: The name of the host pool within the specified resource group
        :param pulumi.Input['PrivateLinkServiceConnectionStateArgs'] private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] private_endpoint_connection_name: The name of the private endpoint connection associated with the Azure resource
        """
        pulumi.set(__self__, "host_pool_name", host_pool_name)
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if private_endpoint_connection_name is not None:
            pulumi.set(__self__, "private_endpoint_connection_name", private_endpoint_connection_name)

    @property
    @pulumi.getter(name="hostPoolName")
    def host_pool_name(self) -> pulumi.Input[str]:
        """
        The name of the host pool within the specified resource group
        """
        return pulumi.get(self, "host_pool_name")

    @host_pool_name.setter
    def host_pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "host_pool_name", value)

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Input['PrivateLinkServiceConnectionStateArgs']:
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: pulumi.Input['PrivateLinkServiceConnectionStateArgs']):
        pulumi.set(self, "private_link_service_connection_state", value)

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
    @pulumi.getter(name="privateEndpointConnectionName")
    def private_endpoint_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the private endpoint connection associated with the Azure resource
        """
        return pulumi.get(self, "private_endpoint_connection_name")

    @private_endpoint_connection_name.setter
    def private_endpoint_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_endpoint_connection_name", value)


class PrivateEndpointConnectionByHostPool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 host_pool_name: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[Union['PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Private Endpoint Connection resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] host_pool_name: The name of the host pool within the specified resource group
        :param pulumi.Input[str] private_endpoint_connection_name: The name of the private endpoint connection associated with the Azure resource
        :param pulumi.Input[Union['PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict']] private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateEndpointConnectionByHostPoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Private Endpoint Connection resource.

        :param str resource_name: The name of the resource.
        :param PrivateEndpointConnectionByHostPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateEndpointConnectionByHostPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 host_pool_name: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[Union['PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivateEndpointConnectionByHostPoolArgs.__new__(PrivateEndpointConnectionByHostPoolArgs)

            if host_pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'host_pool_name'")
            __props__.__dict__["host_pool_name"] = host_pool_name
            __props__.__dict__["private_endpoint_connection_name"] = private_endpoint_connection_name
            if private_link_service_connection_state is None and not opts.urn:
                raise TypeError("Missing required property 'private_link_service_connection_state'")
            __props__.__dict__["private_link_service_connection_state"] = private_link_service_connection_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:desktopvirtualization:PrivateEndpointConnectionByHostPool"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20210401preview:PrivateEndpointConnectionByHostPool"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20210903preview:PrivateEndpointConnectionByHostPool"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20220210preview:PrivateEndpointConnectionByHostPool"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20220401preview:PrivateEndpointConnectionByHostPool"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20221014preview:PrivateEndpointConnectionByHostPool"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20230707preview:PrivateEndpointConnectionByHostPool"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20230905:PrivateEndpointConnectionByHostPool"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20231101preview:PrivateEndpointConnectionByHostPool"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20240116preview:PrivateEndpointConnectionByHostPool"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20240306preview:PrivateEndpointConnectionByHostPool"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20240403:PrivateEndpointConnectionByHostPool"), pulumi.Alias(type_="azure-native:desktopvirtualization/v20240408preview:PrivateEndpointConnectionByHostPool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateEndpointConnectionByHostPool, __self__).__init__(
            'azure-native:desktopvirtualization/v20231004preview:PrivateEndpointConnectionByHostPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateEndpointConnectionByHostPool':
        """
        Get an existing PrivateEndpointConnectionByHostPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrivateEndpointConnectionByHostPoolArgs.__new__(PrivateEndpointConnectionByHostPoolArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint"] = None
        __props__.__dict__["private_link_service_connection_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return PrivateEndpointConnectionByHostPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> pulumi.Output[Optional['outputs.PrivateEndpointResponse']]:
        """
        The resource of private end point.
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Output['outputs.PrivateLinkServiceConnectionStateResponse']:
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the private endpoint connection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

