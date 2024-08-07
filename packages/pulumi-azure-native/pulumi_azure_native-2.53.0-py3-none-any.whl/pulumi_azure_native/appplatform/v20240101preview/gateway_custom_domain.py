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

__all__ = ['GatewayCustomDomainArgs', 'GatewayCustomDomain']

@pulumi.input_type
class GatewayCustomDomainArgs:
    def __init__(__self__, *,
                 gateway_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 domain_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['GatewayCustomDomainPropertiesArgs']] = None):
        """
        The set of arguments for constructing a GatewayCustomDomain resource.
        :param pulumi.Input[str] gateway_name: The name of Spring Cloud Gateway.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] service_name: The name of the Service resource.
        :param pulumi.Input[str] domain_name: The name of the Spring Cloud Gateway custom domain.
        :param pulumi.Input['GatewayCustomDomainPropertiesArgs'] properties: The properties of custom domain for Spring Cloud Gateway
        """
        pulumi.set(__self__, "gateway_name", gateway_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> pulumi.Input[str]:
        """
        The name of Spring Cloud Gateway.
        """
        return pulumi.get(self, "gateway_name")

    @gateway_name.setter
    def gateway_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "gateway_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the Service resource.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Spring Cloud Gateway custom domain.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['GatewayCustomDomainPropertiesArgs']]:
        """
        The properties of custom domain for Spring Cloud Gateway
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['GatewayCustomDomainPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class GatewayCustomDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 gateway_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['GatewayCustomDomainPropertiesArgs', 'GatewayCustomDomainPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Custom domain of the Spring Cloud Gateway

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: The name of the Spring Cloud Gateway custom domain.
        :param pulumi.Input[str] gateway_name: The name of Spring Cloud Gateway.
        :param pulumi.Input[Union['GatewayCustomDomainPropertiesArgs', 'GatewayCustomDomainPropertiesArgsDict']] properties: The properties of custom domain for Spring Cloud Gateway
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] service_name: The name of the Service resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GatewayCustomDomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Custom domain of the Spring Cloud Gateway

        :param str resource_name: The name of the resource.
        :param GatewayCustomDomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GatewayCustomDomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 gateway_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['GatewayCustomDomainPropertiesArgs', 'GatewayCustomDomainPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GatewayCustomDomainArgs.__new__(GatewayCustomDomainArgs)

            __props__.__dict__["domain_name"] = domain_name
            if gateway_name is None and not opts.urn:
                raise TypeError("Missing required property 'gateway_name'")
            __props__.__dict__["gateway_name"] = gateway_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:appplatform:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20220101preview:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20220301preview:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20220501preview:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20220901preview:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20221101preview:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20221201:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20230101preview:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20230301preview:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20230501preview:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20230701preview:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20230901preview:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20231101preview:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20231201:GatewayCustomDomain"), pulumi.Alias(type_="azure-native:appplatform/v20240501preview:GatewayCustomDomain")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GatewayCustomDomain, __self__).__init__(
            'azure-native:appplatform/v20240101preview:GatewayCustomDomain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GatewayCustomDomain':
        """
        Get an existing GatewayCustomDomain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GatewayCustomDomainArgs.__new__(GatewayCustomDomainArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return GatewayCustomDomain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.GatewayCustomDomainPropertiesResponse']:
        """
        The properties of custom domain for Spring Cloud Gateway
        """
        return pulumi.get(self, "properties")

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
        The type of the resource.
        """
        return pulumi.get(self, "type")

