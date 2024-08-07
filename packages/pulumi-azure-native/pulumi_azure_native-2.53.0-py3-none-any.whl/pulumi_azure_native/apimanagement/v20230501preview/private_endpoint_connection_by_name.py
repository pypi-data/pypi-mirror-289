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

__all__ = ['PrivateEndpointConnectionByNameArgs', 'PrivateEndpointConnectionByName']

@pulumi.input_type
class PrivateEndpointConnectionByNameArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 id: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['PrivateEndpointConnectionRequestPropertiesArgs']] = None):
        """
        The set of arguments for constructing a PrivateEndpointConnectionByName resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] id: Private Endpoint Connection Resource Id.
        :param pulumi.Input[str] private_endpoint_connection_name: Name of the private endpoint connection.
        :param pulumi.Input['PrivateEndpointConnectionRequestPropertiesArgs'] properties: The connection state of the private endpoint connection.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if private_endpoint_connection_name is not None:
            pulumi.set(__self__, "private_endpoint_connection_name", private_endpoint_connection_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

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
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Private Endpoint Connection Resource Id.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="privateEndpointConnectionName")
    def private_endpoint_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the private endpoint connection.
        """
        return pulumi.get(self, "private_endpoint_connection_name")

    @private_endpoint_connection_name.setter
    def private_endpoint_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_endpoint_connection_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['PrivateEndpointConnectionRequestPropertiesArgs']]:
        """
        The connection state of the private endpoint connection.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['PrivateEndpointConnectionRequestPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class PrivateEndpointConnectionByName(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['PrivateEndpointConnectionRequestPropertiesArgs', 'PrivateEndpointConnectionRequestPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Private Endpoint Connection resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] id: Private Endpoint Connection Resource Id.
        :param pulumi.Input[str] private_endpoint_connection_name: Name of the private endpoint connection.
        :param pulumi.Input[Union['PrivateEndpointConnectionRequestPropertiesArgs', 'PrivateEndpointConnectionRequestPropertiesArgsDict']] properties: The connection state of the private endpoint connection.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateEndpointConnectionByNameArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Private Endpoint Connection resource.

        :param str resource_name: The name of the resource.
        :param PrivateEndpointConnectionByNameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateEndpointConnectionByNameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['PrivateEndpointConnectionRequestPropertiesArgs', 'PrivateEndpointConnectionRequestPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivateEndpointConnectionByNameArgs.__new__(PrivateEndpointConnectionByNameArgs)

            __props__.__dict__["id"] = id
            __props__.__dict__["private_endpoint_connection_name"] = private_endpoint_connection_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint"] = None
            __props__.__dict__["private_link_service_connection_state"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:PrivateEndpointConnectionByName"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:PrivateEndpointConnectionByName"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:PrivateEndpointConnectionByName"), pulumi.Alias(type_="azure-native:apimanagement/v20211201preview:PrivateEndpointConnectionByName"), pulumi.Alias(type_="azure-native:apimanagement/v20220401preview:PrivateEndpointConnectionByName"), pulumi.Alias(type_="azure-native:apimanagement/v20220801:PrivateEndpointConnectionByName"), pulumi.Alias(type_="azure-native:apimanagement/v20220901preview:PrivateEndpointConnectionByName"), pulumi.Alias(type_="azure-native:apimanagement/v20230301preview:PrivateEndpointConnectionByName"), pulumi.Alias(type_="azure-native:apimanagement/v20230901preview:PrivateEndpointConnectionByName")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateEndpointConnectionByName, __self__).__init__(
            'azure-native:apimanagement/v20230501preview:PrivateEndpointConnectionByName',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateEndpointConnectionByName':
        """
        Get an existing PrivateEndpointConnectionByName resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrivateEndpointConnectionByNameArgs.__new__(PrivateEndpointConnectionByNameArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint"] = None
        __props__.__dict__["private_link_service_connection_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return PrivateEndpointConnectionByName(resource_name, opts=opts, __props__=__props__)

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
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

