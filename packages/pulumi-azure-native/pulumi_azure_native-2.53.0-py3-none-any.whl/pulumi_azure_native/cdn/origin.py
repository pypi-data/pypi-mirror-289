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

__all__ = ['OriginArgs', 'Origin']

@pulumi.input_type
class OriginArgs:
    def __init__(__self__, *,
                 endpoint_name: pulumi.Input[str],
                 host_name: pulumi.Input[str],
                 profile_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 http_port: Optional[pulumi.Input[int]] = None,
                 https_port: Optional[pulumi.Input[int]] = None,
                 origin_host_header: Optional[pulumi.Input[str]] = None,
                 origin_name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 private_link_alias: Optional[pulumi.Input[str]] = None,
                 private_link_approval_message: Optional[pulumi.Input[str]] = None,
                 private_link_location: Optional[pulumi.Input[str]] = None,
                 private_link_resource_id: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a Origin resource.
        :param pulumi.Input[str] endpoint_name: Name of the endpoint under the profile which is unique globally.
        :param pulumi.Input[str] host_name: The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint.
        :param pulumi.Input[str] profile_name: Name of the CDN profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[bool] enabled: Origin is enabled for load balancing or not
        :param pulumi.Input[int] http_port: The value of the HTTP port. Must be between 1 and 65535.
        :param pulumi.Input[int] https_port: The value of the HTTPS port. Must be between 1 and 65535.
        :param pulumi.Input[str] origin_host_header: The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint
        :param pulumi.Input[str] origin_name: Name of the origin that is unique within the endpoint.
        :param pulumi.Input[int] priority: Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5
        :param pulumi.Input[str] private_link_alias: The Alias of the Private Link resource. Populating this optional field indicates that this origin is 'Private'
        :param pulumi.Input[str] private_link_approval_message: A custom message to be included in the approval request to connect to the Private Link.
        :param pulumi.Input[str] private_link_location: The location of the Private Link resource. Required only if 'privateLinkResourceId' is populated
        :param pulumi.Input[str] private_link_resource_id: The Resource Id of the Private Link resource. Populating this optional field indicates that this backend is 'Private'
        :param pulumi.Input[int] weight: Weight of the origin in given origin group for load balancing. Must be between 1 and 1000
        """
        pulumi.set(__self__, "endpoint_name", endpoint_name)
        pulumi.set(__self__, "host_name", host_name)
        pulumi.set(__self__, "profile_name", profile_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if http_port is not None:
            pulumi.set(__self__, "http_port", http_port)
        if https_port is not None:
            pulumi.set(__self__, "https_port", https_port)
        if origin_host_header is not None:
            pulumi.set(__self__, "origin_host_header", origin_host_header)
        if origin_name is not None:
            pulumi.set(__self__, "origin_name", origin_name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if private_link_alias is not None:
            pulumi.set(__self__, "private_link_alias", private_link_alias)
        if private_link_approval_message is not None:
            pulumi.set(__self__, "private_link_approval_message", private_link_approval_message)
        if private_link_location is not None:
            pulumi.set(__self__, "private_link_location", private_link_location)
        if private_link_resource_id is not None:
            pulumi.set(__self__, "private_link_resource_id", private_link_resource_id)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[str]:
        """
        Name of the endpoint under the profile which is unique globally.
        """
        return pulumi.get(self, "endpoint_name")

    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_name", value)

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[str]:
        """
        The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint.
        """
        return pulumi.get(self, "host_name")

    @host_name.setter
    def host_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "host_name", value)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[str]:
        """
        Name of the CDN profile which is unique within the resource group.
        """
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "profile_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Origin is enabled for load balancing or not
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> Optional[pulumi.Input[int]]:
        """
        The value of the HTTP port. Must be between 1 and 65535.
        """
        return pulumi.get(self, "http_port")

    @http_port.setter
    def http_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "http_port", value)

    @property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> Optional[pulumi.Input[int]]:
        """
        The value of the HTTPS port. Must be between 1 and 65535.
        """
        return pulumi.get(self, "https_port")

    @https_port.setter
    def https_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "https_port", value)

    @property
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> Optional[pulumi.Input[str]]:
        """
        The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint
        """
        return pulumi.get(self, "origin_host_header")

    @origin_host_header.setter
    def origin_host_header(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "origin_host_header", value)

    @property
    @pulumi.getter(name="originName")
    def origin_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the origin that is unique within the endpoint.
        """
        return pulumi.get(self, "origin_name")

    @origin_name.setter
    def origin_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "origin_name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="privateLinkAlias")
    def private_link_alias(self) -> Optional[pulumi.Input[str]]:
        """
        The Alias of the Private Link resource. Populating this optional field indicates that this origin is 'Private'
        """
        return pulumi.get(self, "private_link_alias")

    @private_link_alias.setter
    def private_link_alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_alias", value)

    @property
    @pulumi.getter(name="privateLinkApprovalMessage")
    def private_link_approval_message(self) -> Optional[pulumi.Input[str]]:
        """
        A custom message to be included in the approval request to connect to the Private Link.
        """
        return pulumi.get(self, "private_link_approval_message")

    @private_link_approval_message.setter
    def private_link_approval_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_approval_message", value)

    @property
    @pulumi.getter(name="privateLinkLocation")
    def private_link_location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the Private Link resource. Required only if 'privateLinkResourceId' is populated
        """
        return pulumi.get(self, "private_link_location")

    @private_link_location.setter
    def private_link_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_location", value)

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Resource Id of the Private Link resource. Populating this optional field indicates that this backend is 'Private'
        """
        return pulumi.get(self, "private_link_resource_id")

    @private_link_resource_id.setter
    def private_link_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_resource_id", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        Weight of the origin in given origin group for load balancing. Must be between 1 and 1000
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


class Origin(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 http_port: Optional[pulumi.Input[int]] = None,
                 https_port: Optional[pulumi.Input[int]] = None,
                 origin_host_header: Optional[pulumi.Input[str]] = None,
                 origin_name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 private_link_alias: Optional[pulumi.Input[str]] = None,
                 private_link_approval_message: Optional[pulumi.Input[str]] = None,
                 private_link_location: Optional[pulumi.Input[str]] = None,
                 private_link_resource_id: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        CDN origin is the source of the content being delivered via CDN. When the edge nodes represented by an endpoint do not have the requested content cached, they attempt to fetch it from one or more of the configured origins.
        Azure REST API version: 2023-05-01. Prior API version in Azure Native 1.x: 2020-09-01.

        Other available API versions: 2023-07-01-preview, 2024-02-01, 2024-05-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] enabled: Origin is enabled for load balancing or not
        :param pulumi.Input[str] endpoint_name: Name of the endpoint under the profile which is unique globally.
        :param pulumi.Input[str] host_name: The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint.
        :param pulumi.Input[int] http_port: The value of the HTTP port. Must be between 1 and 65535.
        :param pulumi.Input[int] https_port: The value of the HTTPS port. Must be between 1 and 65535.
        :param pulumi.Input[str] origin_host_header: The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint
        :param pulumi.Input[str] origin_name: Name of the origin that is unique within the endpoint.
        :param pulumi.Input[int] priority: Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5
        :param pulumi.Input[str] private_link_alias: The Alias of the Private Link resource. Populating this optional field indicates that this origin is 'Private'
        :param pulumi.Input[str] private_link_approval_message: A custom message to be included in the approval request to connect to the Private Link.
        :param pulumi.Input[str] private_link_location: The location of the Private Link resource. Required only if 'privateLinkResourceId' is populated
        :param pulumi.Input[str] private_link_resource_id: The Resource Id of the Private Link resource. Populating this optional field indicates that this backend is 'Private'
        :param pulumi.Input[str] profile_name: Name of the CDN profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[int] weight: Weight of the origin in given origin group for load balancing. Must be between 1 and 1000
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OriginArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        CDN origin is the source of the content being delivered via CDN. When the edge nodes represented by an endpoint do not have the requested content cached, they attempt to fetch it from one or more of the configured origins.
        Azure REST API version: 2023-05-01. Prior API version in Azure Native 1.x: 2020-09-01.

        Other available API versions: 2023-07-01-preview, 2024-02-01, 2024-05-01-preview.

        :param str resource_name: The name of the resource.
        :param OriginArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OriginArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 http_port: Optional[pulumi.Input[int]] = None,
                 https_port: Optional[pulumi.Input[int]] = None,
                 origin_host_header: Optional[pulumi.Input[str]] = None,
                 origin_name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 private_link_alias: Optional[pulumi.Input[str]] = None,
                 private_link_approval_message: Optional[pulumi.Input[str]] = None,
                 private_link_location: Optional[pulumi.Input[str]] = None,
                 private_link_resource_id: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = OriginArgs.__new__(OriginArgs)

            __props__.__dict__["enabled"] = enabled
            if endpoint_name is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_name'")
            __props__.__dict__["endpoint_name"] = endpoint_name
            if host_name is None and not opts.urn:
                raise TypeError("Missing required property 'host_name'")
            __props__.__dict__["host_name"] = host_name
            __props__.__dict__["http_port"] = http_port
            __props__.__dict__["https_port"] = https_port
            __props__.__dict__["origin_host_header"] = origin_host_header
            __props__.__dict__["origin_name"] = origin_name
            __props__.__dict__["priority"] = priority
            __props__.__dict__["private_link_alias"] = private_link_alias
            __props__.__dict__["private_link_approval_message"] = private_link_approval_message
            __props__.__dict__["private_link_location"] = private_link_location
            __props__.__dict__["private_link_resource_id"] = private_link_resource_id
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["weight"] = weight
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_status"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cdn/v20150601:Origin"), pulumi.Alias(type_="azure-native:cdn/v20160402:Origin"), pulumi.Alias(type_="azure-native:cdn/v20191231:Origin"), pulumi.Alias(type_="azure-native:cdn/v20200331:Origin"), pulumi.Alias(type_="azure-native:cdn/v20200415:Origin"), pulumi.Alias(type_="azure-native:cdn/v20200901:Origin"), pulumi.Alias(type_="azure-native:cdn/v20210601:Origin"), pulumi.Alias(type_="azure-native:cdn/v20220501preview:Origin"), pulumi.Alias(type_="azure-native:cdn/v20221101preview:Origin"), pulumi.Alias(type_="azure-native:cdn/v20230501:Origin"), pulumi.Alias(type_="azure-native:cdn/v20230701preview:Origin"), pulumi.Alias(type_="azure-native:cdn/v20240201:Origin"), pulumi.Alias(type_="azure-native:cdn/v20240501preview:Origin")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Origin, __self__).__init__(
            'azure-native:cdn:Origin',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Origin':
        """
        Get an existing Origin resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OriginArgs.__new__(OriginArgs)

        __props__.__dict__["enabled"] = None
        __props__.__dict__["host_name"] = None
        __props__.__dict__["http_port"] = None
        __props__.__dict__["https_port"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["origin_host_header"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["private_endpoint_status"] = None
        __props__.__dict__["private_link_alias"] = None
        __props__.__dict__["private_link_approval_message"] = None
        __props__.__dict__["private_link_location"] = None
        __props__.__dict__["private_link_resource_id"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["weight"] = None
        return Origin(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Origin is enabled for load balancing or not
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[str]:
        """
        The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> pulumi.Output[Optional[int]]:
        """
        The value of the HTTP port. Must be between 1 and 65535.
        """
        return pulumi.get(self, "http_port")

    @property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> pulumi.Output[Optional[int]]:
        """
        The value of the HTTPS port. Must be between 1 and 65535.
        """
        return pulumi.get(self, "https_port")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> pulumi.Output[Optional[str]]:
        """
        The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint
        """
        return pulumi.get(self, "origin_host_header")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="privateEndpointStatus")
    def private_endpoint_status(self) -> pulumi.Output[str]:
        """
        The approval status for the connection to the Private Link
        """
        return pulumi.get(self, "private_endpoint_status")

    @property
    @pulumi.getter(name="privateLinkAlias")
    def private_link_alias(self) -> pulumi.Output[Optional[str]]:
        """
        The Alias of the Private Link resource. Populating this optional field indicates that this origin is 'Private'
        """
        return pulumi.get(self, "private_link_alias")

    @property
    @pulumi.getter(name="privateLinkApprovalMessage")
    def private_link_approval_message(self) -> pulumi.Output[Optional[str]]:
        """
        A custom message to be included in the approval request to connect to the Private Link.
        """
        return pulumi.get(self, "private_link_approval_message")

    @property
    @pulumi.getter(name="privateLinkLocation")
    def private_link_location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the Private Link resource. Required only if 'privateLinkResourceId' is populated
        """
        return pulumi.get(self, "private_link_location")

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Resource Id of the Private Link resource. Populating this optional field indicates that this backend is 'Private'
        """
        return pulumi.get(self, "private_link_resource_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning status of the origin.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[str]:
        """
        Resource status of the origin.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Output[Optional[int]]:
        """
        Weight of the origin in given origin group for load balancing. Must be between 1 and 1000
        """
        return pulumi.get(self, "weight")

