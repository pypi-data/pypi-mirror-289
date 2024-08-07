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

__all__ = ['NetworkDeviceArgs', 'NetworkDevice']

@pulumi.input_type
class NetworkDeviceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 serial_number: pulumi.Input[str],
                 annotation: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_device_name: Optional[pulumi.Input[str]] = None,
                 network_device_sku: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NetworkDevice resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] serial_number: Serial number of the device. Format of serial Number - Make;Model;HardwareRevisionId;SerialNumber.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[str] host_name: The host name of the device.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] network_device_name: Name of the Network Device.
        :param pulumi.Input[str] network_device_sku: Network Device SKU name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "serial_number", serial_number)
        if annotation is not None:
            pulumi.set(__self__, "annotation", annotation)
        if host_name is not None:
            pulumi.set(__self__, "host_name", host_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_device_name is not None:
            pulumi.set(__self__, "network_device_name", network_device_name)
        if network_device_sku is not None:
            pulumi.set(__self__, "network_device_sku", network_device_sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Input[str]:
        """
        Serial number of the device. Format of serial Number - Make;Model;HardwareRevisionId;SerialNumber.
        """
        return pulumi.get(self, "serial_number")

    @serial_number.setter
    def serial_number(self, value: pulumi.Input[str]):
        pulumi.set(self, "serial_number", value)

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
    @pulumi.getter(name="hostName")
    def host_name(self) -> Optional[pulumi.Input[str]]:
        """
        The host name of the device.
        """
        return pulumi.get(self, "host_name")

    @host_name.setter
    def host_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_name", value)

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
    @pulumi.getter(name="networkDeviceName")
    def network_device_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Network Device.
        """
        return pulumi.get(self, "network_device_name")

    @network_device_name.setter
    def network_device_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_device_name", value)

    @property
    @pulumi.getter(name="networkDeviceSku")
    def network_device_sku(self) -> Optional[pulumi.Input[str]]:
        """
        Network Device SKU name.
        """
        return pulumi.get(self, "network_device_sku")

    @network_device_sku.setter
    def network_device_sku(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_device_sku", value)

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


class NetworkDevice(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_device_name: Optional[pulumi.Input[str]] = None,
                 network_device_sku: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The Network Device resource definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] annotation: Switch configuration description.
        :param pulumi.Input[str] host_name: The host name of the device.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] network_device_name: Name of the Network Device.
        :param pulumi.Input[str] network_device_sku: Network Device SKU name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] serial_number: Serial number of the device. Format of serial Number - Make;Model;HardwareRevisionId;SerialNumber.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkDeviceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Network Device resource definition.

        :param str resource_name: The name of the resource.
        :param NetworkDeviceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkDeviceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotation: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_device_name: Optional[pulumi.Input[str]] = None,
                 network_device_sku: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkDeviceArgs.__new__(NetworkDeviceArgs)

            __props__.__dict__["annotation"] = annotation
            __props__.__dict__["host_name"] = host_name
            __props__.__dict__["location"] = location
            __props__.__dict__["network_device_name"] = network_device_name
            __props__.__dict__["network_device_sku"] = network_device_sku
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if serial_number is None and not opts.urn:
                raise TypeError("Missing required property 'serial_number'")
            __props__.__dict__["serial_number"] = serial_number
            __props__.__dict__["tags"] = tags
            __props__.__dict__["administrative_state"] = None
            __props__.__dict__["configuration_state"] = None
            __props__.__dict__["management_ipv4_address"] = None
            __props__.__dict__["management_ipv6_address"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["network_device_role"] = None
            __props__.__dict__["network_rack_id"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:managednetworkfabric:NetworkDevice"), pulumi.Alias(type_="azure-native:managednetworkfabric/v20230201preview:NetworkDevice")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NetworkDevice, __self__).__init__(
            'azure-native:managednetworkfabric/v20230615:NetworkDevice',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkDevice':
        """
        Get an existing NetworkDevice resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkDeviceArgs.__new__(NetworkDeviceArgs)

        __props__.__dict__["administrative_state"] = None
        __props__.__dict__["annotation"] = None
        __props__.__dict__["configuration_state"] = None
        __props__.__dict__["host_name"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["management_ipv4_address"] = None
        __props__.__dict__["management_ipv6_address"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_device_role"] = None
        __props__.__dict__["network_device_sku"] = None
        __props__.__dict__["network_rack_id"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["serial_number"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return NetworkDevice(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> pulumi.Output[str]:
        """
        Administrative state of the resource.
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
    @pulumi.getter(name="configurationState")
    def configuration_state(self) -> pulumi.Output[str]:
        """
        Configuration state of the resource.
        """
        return pulumi.get(self, "configuration_state")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[Optional[str]]:
        """
        The host name of the device.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managementIpv4Address")
    def management_ipv4_address(self) -> pulumi.Output[str]:
        """
        Management IPv4 Address.
        """
        return pulumi.get(self, "management_ipv4_address")

    @property
    @pulumi.getter(name="managementIpv6Address")
    def management_ipv6_address(self) -> pulumi.Output[str]:
        """
        Management IPv6 Address.
        """
        return pulumi.get(self, "management_ipv6_address")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkDeviceRole")
    def network_device_role(self) -> pulumi.Output[str]:
        """
        NetworkDeviceRole is the device role: Example: CE | ToR.
        """
        return pulumi.get(self, "network_device_role")

    @property
    @pulumi.getter(name="networkDeviceSku")
    def network_device_sku(self) -> pulumi.Output[Optional[str]]:
        """
        Network Device SKU name.
        """
        return pulumi.get(self, "network_device_sku")

    @property
    @pulumi.getter(name="networkRackId")
    def network_rack_id(self) -> pulumi.Output[str]:
        """
        Reference to network rack resource id.
        """
        return pulumi.get(self, "network_rack_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Output[str]:
        """
        Serial number of the device. Format of serial Number - Make;Model;HardwareRevisionId;SerialNumber.
        """
        return pulumi.get(self, "serial_number")

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
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Current version of the device as defined in SKU.
        """
        return pulumi.get(self, "version")

