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

__all__ = ['ExpressRoutePortAuthorizationArgs', 'ExpressRoutePortAuthorization']

@pulumi.input_type
class ExpressRoutePortAuthorizationArgs:
    def __init__(__self__, *,
                 express_route_port_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 authorization_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ExpressRoutePortAuthorization resource.
        :param pulumi.Input[str] express_route_port_name: The name of the express route port.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] authorization_name: The name of the authorization.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        pulumi.set(__self__, "express_route_port_name", express_route_port_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if authorization_name is not None:
            pulumi.set(__self__, "authorization_name", authorization_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="expressRoutePortName")
    def express_route_port_name(self) -> pulumi.Input[str]:
        """
        The name of the express route port.
        """
        return pulumi.get(self, "express_route_port_name")

    @express_route_port_name.setter
    def express_route_port_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "express_route_port_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="authorizationName")
    def authorization_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the authorization.
        """
        return pulumi.get(self, "authorization_name")

    @authorization_name.setter
    def authorization_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_name", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class ExpressRoutePortAuthorization(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_name: Optional[pulumi.Input[str]] = None,
                 express_route_port_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ExpressRoutePort Authorization resource definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorization_name: The name of the authorization.
        :param pulumi.Input[str] express_route_port_name: The name of the express route port.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExpressRoutePortAuthorizationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ExpressRoutePort Authorization resource definition.

        :param str resource_name: The name of the resource.
        :param ExpressRoutePortAuthorizationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExpressRoutePortAuthorizationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_name: Optional[pulumi.Input[str]] = None,
                 express_route_port_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ExpressRoutePortAuthorizationArgs.__new__(ExpressRoutePortAuthorizationArgs)

            __props__.__dict__["authorization_name"] = authorization_name
            if express_route_port_name is None and not opts.urn:
                raise TypeError("Missing required property 'express_route_port_name'")
            __props__.__dict__["express_route_port_name"] = express_route_port_name
            __props__.__dict__["id"] = id
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["authorization_key"] = None
            __props__.__dict__["authorization_use_status"] = None
            __props__.__dict__["circuit_resource_uri"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:ExpressRoutePortAuthorization"), pulumi.Alias(type_="azure-native:network/v20210801:ExpressRoutePortAuthorization"), pulumi.Alias(type_="azure-native:network/v20220101:ExpressRoutePortAuthorization"), pulumi.Alias(type_="azure-native:network/v20220501:ExpressRoutePortAuthorization"), pulumi.Alias(type_="azure-native:network/v20220701:ExpressRoutePortAuthorization"), pulumi.Alias(type_="azure-native:network/v20220901:ExpressRoutePortAuthorization"), pulumi.Alias(type_="azure-native:network/v20221101:ExpressRoutePortAuthorization"), pulumi.Alias(type_="azure-native:network/v20230201:ExpressRoutePortAuthorization"), pulumi.Alias(type_="azure-native:network/v20230401:ExpressRoutePortAuthorization"), pulumi.Alias(type_="azure-native:network/v20230601:ExpressRoutePortAuthorization"), pulumi.Alias(type_="azure-native:network/v20230901:ExpressRoutePortAuthorization"), pulumi.Alias(type_="azure-native:network/v20231101:ExpressRoutePortAuthorization"), pulumi.Alias(type_="azure-native:network/v20240101:ExpressRoutePortAuthorization")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ExpressRoutePortAuthorization, __self__).__init__(
            'azure-native:network/v20230501:ExpressRoutePortAuthorization',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ExpressRoutePortAuthorization':
        """
        Get an existing ExpressRoutePortAuthorization resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExpressRoutePortAuthorizationArgs.__new__(ExpressRoutePortAuthorizationArgs)

        __props__.__dict__["authorization_key"] = None
        __props__.__dict__["authorization_use_status"] = None
        __props__.__dict__["circuit_resource_uri"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return ExpressRoutePortAuthorization(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> pulumi.Output[str]:
        """
        The authorization key.
        """
        return pulumi.get(self, "authorization_key")

    @property
    @pulumi.getter(name="authorizationUseStatus")
    def authorization_use_status(self) -> pulumi.Output[str]:
        """
        The authorization use status.
        """
        return pulumi.get(self, "authorization_use_status")

    @property
    @pulumi.getter(name="circuitResourceUri")
    def circuit_resource_uri(self) -> pulumi.Output[str]:
        """
        The reference to the ExpressRoute circuit resource using the authorization.
        """
        return pulumi.get(self, "circuit_resource_uri")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the authorization resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

