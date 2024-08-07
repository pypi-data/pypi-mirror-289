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

__all__ = ['L2IsolationDomainArgs', 'L2IsolationDomain']

@pulumi.input_type
class L2IsolationDomainArgs:
    def __init__(__self__, *,
                 network_fabric_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 vlan_id: pulumi.Input[int],
                 annotation: Optional[pulumi.Input[str]] = None,
                 l2_isolation_domain_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a L2IsolationDomain resource.
        :param pulumi.Input[str] network_fabric_id: Network Fabric ARM resource id.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[int] vlan_id: vlanId. Example: 501.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[str] l2_isolation_domain_name: Name of the L2 Isolation Domain
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[int] mtu: maximum transmission unit. Default value is 1500.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "network_fabric_id", network_fabric_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "vlan_id", vlan_id)
        if annotation is not None:
            pulumi.set(__self__, "annotation", annotation)
        if l2_isolation_domain_name is not None:
            pulumi.set(__self__, "l2_isolation_domain_name", l2_isolation_domain_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mtu is not None:
            pulumi.set(__self__, "mtu", mtu)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> pulumi.Input[str]:
        """
        Network Fabric ARM resource id.
        """
        return pulumi.get(self, "network_fabric_id")

    @network_fabric_id.setter
    def network_fabric_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_fabric_id", value)

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
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> pulumi.Input[int]:
        """
        vlanId. Example: 501.
        """
        return pulumi.get(self, "vlan_id")

    @vlan_id.setter
    def vlan_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "vlan_id", value)

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
    @pulumi.getter(name="l2IsolationDomainName")
    def l2_isolation_domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the L2 Isolation Domain
        """
        return pulumi.get(self, "l2_isolation_domain_name")

    @l2_isolation_domain_name.setter
    def l2_isolation_domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "l2_isolation_domain_name", value)

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
    def mtu(self) -> Optional[pulumi.Input[int]]:
        """
        maximum transmission unit. Default value is 1500.
        """
        return pulumi.get(self, "mtu")

    @mtu.setter
    def mtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "mtu", value)

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


class L2IsolationDomain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 l2_isolation_domain_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 network_fabric_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        The L2IsolationDomain resource definition.
        Azure REST API version: 2023-02-01-preview. Prior API version in Azure Native 1.x: 2023-02-01-preview.

        Other available API versions: 2023-06-15.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[str] l2_isolation_domain_name: Name of the L2 Isolation Domain
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[int] mtu: maximum transmission unit. Default value is 1500.
        :param pulumi.Input[str] network_fabric_id: Network Fabric ARM resource id.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[int] vlan_id: vlanId. Example: 501.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: L2IsolationDomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The L2IsolationDomain resource definition.
        Azure REST API version: 2023-02-01-preview. Prior API version in Azure Native 1.x: 2023-02-01-preview.

        Other available API versions: 2023-06-15.

        :param str resource_name: The name of the resource.
        :param L2IsolationDomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(L2IsolationDomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 l2_isolation_domain_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 network_fabric_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vlan_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = L2IsolationDomainArgs.__new__(L2IsolationDomainArgs)

            __props__.__dict__["annotation"] = annotation
            __props__.__dict__["l2_isolation_domain_name"] = l2_isolation_domain_name
            __props__.__dict__["location"] = location
            __props__.__dict__["mtu"] = mtu
            if network_fabric_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_fabric_id'")
            __props__.__dict__["network_fabric_id"] = network_fabric_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            if vlan_id is None and not opts.urn:
                raise TypeError("Missing required property 'vlan_id'")
            __props__.__dict__["vlan_id"] = vlan_id
            __props__.__dict__["administrative_state"] = None
            __props__.__dict__["disabled_on_resources"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:managednetworkfabric/v20230201preview:L2IsolationDomain"), pulumi.Alias(type_="azure-native:managednetworkfabric/v20230615:L2IsolationDomain")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(L2IsolationDomain, __self__).__init__(
            'azure-native:managednetworkfabric:L2IsolationDomain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'L2IsolationDomain':
        """
        Get an existing L2IsolationDomain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = L2IsolationDomainArgs.__new__(L2IsolationDomainArgs)

        __props__.__dict__["administrative_state"] = None
        __props__.__dict__["annotation"] = None
        __props__.__dict__["disabled_on_resources"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mtu"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_fabric_id"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vlan_id"] = None
        return L2IsolationDomain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> pulumi.Output[str]:
        """
        state. Example: Enabled | Disabled. It indicates administrative state of the isolationDomain, whether it is enabled or disabled. If enabled, the configuration is applied on the devices. If disabled, the configuration is removed from the devices
        """
        return pulumi.get(self, "administrative_state")

    @property
    @pulumi.getter
    def annotation(self) -> pulumi.Output[Optional[str]]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter(name="disabledOnResources")
    def disabled_on_resources(self) -> pulumi.Output[Sequence[str]]:
        """
        List of resources the L2 Isolation Domain is disabled on. Can be either entire NetworkFabric or NetworkRack.
        """
        return pulumi.get(self, "disabled_on_resources")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def mtu(self) -> pulumi.Output[Optional[int]]:
        """
        maximum transmission unit. Default value is 1500.
        """
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkFabricId")
    def network_fabric_id(self) -> pulumi.Output[str]:
        """
        Network Fabric ARM resource id.
        """
        return pulumi.get(self, "network_fabric_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets the provisioning state of the resource.
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
    @pulumi.getter(name="vlanId")
    def vlan_id(self) -> pulumi.Output[int]:
        """
        vlanId. Example: 501.
        """
        return pulumi.get(self, "vlan_id")

