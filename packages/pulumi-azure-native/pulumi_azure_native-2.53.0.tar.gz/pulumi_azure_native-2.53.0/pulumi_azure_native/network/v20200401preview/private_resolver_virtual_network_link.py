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

__all__ = ['PrivateResolverVirtualNetworkLinkArgs', 'PrivateResolverVirtualNetworkLink']

@pulumi.input_type
class PrivateResolverVirtualNetworkLinkArgs:
    def __init__(__self__, *,
                 dns_forwarding_ruleset_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_network: Optional[pulumi.Input['SubResourceArgs']] = None,
                 virtual_network_link_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PrivateResolverVirtualNetworkLink resource.
        :param pulumi.Input[str] dns_forwarding_ruleset_name: The name of the DNS forwarding ruleset.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Metadata attached to the virtual network link.
        :param pulumi.Input['SubResourceArgs'] virtual_network: The reference to the virtual network. This cannot be changed after creation.
        :param pulumi.Input[str] virtual_network_link_name: The name of the virtual network link.
        """
        pulumi.set(__self__, "dns_forwarding_ruleset_name", dns_forwarding_ruleset_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if virtual_network is not None:
            pulumi.set(__self__, "virtual_network", virtual_network)
        if virtual_network_link_name is not None:
            pulumi.set(__self__, "virtual_network_link_name", virtual_network_link_name)

    @property
    @pulumi.getter(name="dnsForwardingRulesetName")
    def dns_forwarding_ruleset_name(self) -> pulumi.Input[str]:
        """
        The name of the DNS forwarding ruleset.
        """
        return pulumi.get(self, "dns_forwarding_ruleset_name")

    @dns_forwarding_ruleset_name.setter
    def dns_forwarding_ruleset_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "dns_forwarding_ruleset_name", value)

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
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Metadata attached to the virtual network link.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The reference to the virtual network. This cannot be changed after creation.
        """
        return pulumi.get(self, "virtual_network")

    @virtual_network.setter
    def virtual_network(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "virtual_network", value)

    @property
    @pulumi.getter(name="virtualNetworkLinkName")
    def virtual_network_link_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the virtual network link.
        """
        return pulumi.get(self, "virtual_network_link_name")

    @virtual_network_link_name.setter
    def virtual_network_link_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "virtual_network_link_name", value)


class PrivateResolverVirtualNetworkLink(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_forwarding_ruleset_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_network: Optional[pulumi.Input[Union['SubResourceArgs', 'SubResourceArgsDict']]] = None,
                 virtual_network_link_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Describes a virtual network link.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dns_forwarding_ruleset_name: The name of the DNS forwarding ruleset.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: Metadata attached to the virtual network link.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union['SubResourceArgs', 'SubResourceArgsDict']] virtual_network: The reference to the virtual network. This cannot be changed after creation.
        :param pulumi.Input[str] virtual_network_link_name: The name of the virtual network link.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateResolverVirtualNetworkLinkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Describes a virtual network link.

        :param str resource_name: The name of the resource.
        :param PrivateResolverVirtualNetworkLinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateResolverVirtualNetworkLinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dns_forwarding_ruleset_name: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_network: Optional[pulumi.Input[Union['SubResourceArgs', 'SubResourceArgsDict']]] = None,
                 virtual_network_link_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivateResolverVirtualNetworkLinkArgs.__new__(PrivateResolverVirtualNetworkLinkArgs)

            if dns_forwarding_ruleset_name is None and not opts.urn:
                raise TypeError("Missing required property 'dns_forwarding_ruleset_name'")
            __props__.__dict__["dns_forwarding_ruleset_name"] = dns_forwarding_ruleset_name
            __props__.__dict__["metadata"] = metadata
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["virtual_network"] = virtual_network
            __props__.__dict__["virtual_network_link_name"] = virtual_network_link_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:PrivateResolverVirtualNetworkLink"), pulumi.Alias(type_="azure-native:network/v20220701:PrivateResolverVirtualNetworkLink")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateResolverVirtualNetworkLink, __self__).__init__(
            'azure-native:network/v20200401preview:PrivateResolverVirtualNetworkLink',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateResolverVirtualNetworkLink':
        """
        Get an existing PrivateResolverVirtualNetworkLink resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrivateResolverVirtualNetworkLinkArgs.__new__(PrivateResolverVirtualNetworkLinkArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_network"] = None
        return PrivateResolverVirtualNetworkLink(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        ETag of the virtual network link.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Metadata attached to the virtual network link.
        """
        return pulumi.get(self, "metadata")

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
        The current provisioning state of the virtual network link. This is a read-only property and any attempt to set this value will be ignored.
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

    @property
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        The reference to the virtual network. This cannot be changed after creation.
        """
        return pulumi.get(self, "virtual_network")

