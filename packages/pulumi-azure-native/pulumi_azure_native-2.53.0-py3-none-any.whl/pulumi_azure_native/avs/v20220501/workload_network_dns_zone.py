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

__all__ = ['WorkloadNetworkDnsZoneArgs', 'WorkloadNetworkDnsZone']

@pulumi.input_type
class WorkloadNetworkDnsZoneArgs:
    def __init__(__self__, *,
                 private_cloud_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 display_name: Optional[pulumi.Input[str]] = None,
                 dns_server_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dns_services: Optional[pulumi.Input[float]] = None,
                 dns_zone_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 revision: Optional[pulumi.Input[float]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkloadNetworkDnsZone resource.
        :param pulumi.Input[str] private_cloud_name: Name of the private cloud
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] display_name: Display name of the DNS Zone.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_server_ips: DNS Server IP array of the DNS Zone.
        :param pulumi.Input[float] dns_services: Number of DNS Services using the DNS zone.
        :param pulumi.Input[str] dns_zone_id: NSX DNS Zone identifier. Generally the same as the DNS Zone's display name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain: Domain names of the DNS Zone.
        :param pulumi.Input[float] revision: NSX revision number.
        :param pulumi.Input[str] source_ip: Source IP of the DNS Zone.
        """
        pulumi.set(__self__, "private_cloud_name", private_cloud_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if dns_server_ips is not None:
            pulumi.set(__self__, "dns_server_ips", dns_server_ips)
        if dns_services is not None:
            pulumi.set(__self__, "dns_services", dns_services)
        if dns_zone_id is not None:
            pulumi.set(__self__, "dns_zone_id", dns_zone_id)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if revision is not None:
            pulumi.set(__self__, "revision", revision)
        if source_ip is not None:
            pulumi.set(__self__, "source_ip", source_ip)

    @property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[str]:
        """
        Name of the private cloud
        """
        return pulumi.get(self, "private_cloud_name")

    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_cloud_name", value)

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
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the DNS Zone.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="dnsServerIps")
    def dns_server_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        DNS Server IP array of the DNS Zone.
        """
        return pulumi.get(self, "dns_server_ips")

    @dns_server_ips.setter
    def dns_server_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dns_server_ips", value)

    @property
    @pulumi.getter(name="dnsServices")
    def dns_services(self) -> Optional[pulumi.Input[float]]:
        """
        Number of DNS Services using the DNS zone.
        """
        return pulumi.get(self, "dns_services")

    @dns_services.setter
    def dns_services(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "dns_services", value)

    @property
    @pulumi.getter(name="dnsZoneId")
    def dns_zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        NSX DNS Zone identifier. Generally the same as the DNS Zone's display name
        """
        return pulumi.get(self, "dns_zone_id")

    @dns_zone_id.setter
    def dns_zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_zone_id", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Domain names of the DNS Zone.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[float]]:
        """
        NSX revision number.
        """
        return pulumi.get(self, "revision")

    @revision.setter
    def revision(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "revision", value)

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Source IP of the DNS Zone.
        """
        return pulumi.get(self, "source_ip")

    @source_ip.setter
    def source_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_ip", value)


class WorkloadNetworkDnsZone(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 dns_server_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dns_services: Optional[pulumi.Input[float]] = None,
                 dns_zone_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[float]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        NSX DNS Zone

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: Display name of the DNS Zone.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dns_server_ips: DNS Server IP array of the DNS Zone.
        :param pulumi.Input[float] dns_services: Number of DNS Services using the DNS zone.
        :param pulumi.Input[str] dns_zone_id: NSX DNS Zone identifier. Generally the same as the DNS Zone's display name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain: Domain names of the DNS Zone.
        :param pulumi.Input[str] private_cloud_name: Name of the private cloud
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[float] revision: NSX revision number.
        :param pulumi.Input[str] source_ip: Source IP of the DNS Zone.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkloadNetworkDnsZoneArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        NSX DNS Zone

        :param str resource_name: The name of the resource.
        :param WorkloadNetworkDnsZoneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkloadNetworkDnsZoneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 dns_server_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 dns_services: Optional[pulumi.Input[float]] = None,
                 dns_zone_id: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[float]] = None,
                 source_ip: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkloadNetworkDnsZoneArgs.__new__(WorkloadNetworkDnsZoneArgs)

            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["dns_server_ips"] = dns_server_ips
            __props__.__dict__["dns_services"] = dns_services
            __props__.__dict__["dns_zone_id"] = dns_zone_id
            __props__.__dict__["domain"] = domain
            if private_cloud_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_cloud_name'")
            __props__.__dict__["private_cloud_name"] = private_cloud_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["revision"] = revision
            __props__.__dict__["source_ip"] = source_ip
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:avs:WorkloadNetworkDnsZone"), pulumi.Alias(type_="azure-native:avs/v20200717preview:WorkloadNetworkDnsZone"), pulumi.Alias(type_="azure-native:avs/v20210101preview:WorkloadNetworkDnsZone"), pulumi.Alias(type_="azure-native:avs/v20210601:WorkloadNetworkDnsZone"), pulumi.Alias(type_="azure-native:avs/v20211201:WorkloadNetworkDnsZone"), pulumi.Alias(type_="azure-native:avs/v20230301:WorkloadNetworkDnsZone"), pulumi.Alias(type_="azure-native:avs/v20230901:WorkloadNetworkDnsZone")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkloadNetworkDnsZone, __self__).__init__(
            'azure-native:avs/v20220501:WorkloadNetworkDnsZone',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkloadNetworkDnsZone':
        """
        Get an existing WorkloadNetworkDnsZone resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkloadNetworkDnsZoneArgs.__new__(WorkloadNetworkDnsZoneArgs)

        __props__.__dict__["display_name"] = None
        __props__.__dict__["dns_server_ips"] = None
        __props__.__dict__["dns_services"] = None
        __props__.__dict__["domain"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["revision"] = None
        __props__.__dict__["source_ip"] = None
        __props__.__dict__["type"] = None
        return WorkloadNetworkDnsZone(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Display name of the DNS Zone.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="dnsServerIps")
    def dns_server_ips(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        DNS Server IP array of the DNS Zone.
        """
        return pulumi.get(self, "dns_server_ips")

    @property
    @pulumi.getter(name="dnsServices")
    def dns_services(self) -> pulumi.Output[Optional[float]]:
        """
        Number of DNS Services using the DNS zone.
        """
        return pulumi.get(self, "dns_services")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Domain names of the DNS Zone.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def revision(self) -> pulumi.Output[Optional[float]]:
        """
        NSX revision number.
        """
        return pulumi.get(self, "revision")

    @property
    @pulumi.getter(name="sourceIp")
    def source_ip(self) -> pulumi.Output[Optional[str]]:
        """
        Source IP of the DNS Zone.
        """
        return pulumi.get(self, "source_ip")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

