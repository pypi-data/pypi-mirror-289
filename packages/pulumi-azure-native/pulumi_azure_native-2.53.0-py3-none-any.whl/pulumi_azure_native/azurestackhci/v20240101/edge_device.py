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

__all__ = ['EdgeDeviceArgs', 'EdgeDevice']

@pulumi.input_type
class EdgeDeviceArgs:
    def __init__(__self__, *,
                 resource_uri: pulumi.Input[str],
                 device_configuration: Optional[pulumi.Input['DeviceConfigurationArgs']] = None,
                 edge_device_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EdgeDevice resource.
        :param pulumi.Input[str] resource_uri: The fully qualified Azure Resource manager identifier of the resource.
        :param pulumi.Input['DeviceConfigurationArgs'] device_configuration: Device Configuration
        :param pulumi.Input[str] edge_device_name: Name of Device
        """
        pulumi.set(__self__, "resource_uri", resource_uri)
        if device_configuration is not None:
            pulumi.set(__self__, "device_configuration", device_configuration)
        if edge_device_name is not None:
            pulumi.set(__self__, "edge_device_name", edge_device_name)

    @property
    @pulumi.getter(name="resourceUri")
    def resource_uri(self) -> pulumi.Input[str]:
        """
        The fully qualified Azure Resource manager identifier of the resource.
        """
        return pulumi.get(self, "resource_uri")

    @resource_uri.setter
    def resource_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_uri", value)

    @property
    @pulumi.getter(name="deviceConfiguration")
    def device_configuration(self) -> Optional[pulumi.Input['DeviceConfigurationArgs']]:
        """
        Device Configuration
        """
        return pulumi.get(self, "device_configuration")

    @device_configuration.setter
    def device_configuration(self, value: Optional[pulumi.Input['DeviceConfigurationArgs']]):
        pulumi.set(self, "device_configuration", value)

    @property
    @pulumi.getter(name="edgeDeviceName")
    def edge_device_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of Device
        """
        return pulumi.get(self, "edge_device_name")

    @edge_device_name.setter
    def edge_device_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "edge_device_name", value)


class EdgeDevice(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device_configuration: Optional[pulumi.Input[Union['DeviceConfigurationArgs', 'DeviceConfigurationArgsDict']]] = None,
                 edge_device_name: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Edge device resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['DeviceConfigurationArgs', 'DeviceConfigurationArgsDict']] device_configuration: Device Configuration
        :param pulumi.Input[str] edge_device_name: Name of Device
        :param pulumi.Input[str] resource_uri: The fully qualified Azure Resource manager identifier of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EdgeDeviceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Edge device resource

        :param str resource_name: The name of the resource.
        :param EdgeDeviceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EdgeDeviceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 device_configuration: Optional[pulumi.Input[Union['DeviceConfigurationArgs', 'DeviceConfigurationArgsDict']]] = None,
                 edge_device_name: Optional[pulumi.Input[str]] = None,
                 resource_uri: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EdgeDeviceArgs.__new__(EdgeDeviceArgs)

            __props__.__dict__["device_configuration"] = device_configuration
            __props__.__dict__["edge_device_name"] = edge_device_name
            if resource_uri is None and not opts.urn:
                raise TypeError("Missing required property 'resource_uri'")
            __props__.__dict__["resource_uri"] = resource_uri
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestackhci:EdgeDevice"), pulumi.Alias(type_="azure-native:azurestackhci/v20230801preview:EdgeDevice"), pulumi.Alias(type_="azure-native:azurestackhci/v20231101preview:EdgeDevice"), pulumi.Alias(type_="azure-native:azurestackhci/v20240215preview:EdgeDevice"), pulumi.Alias(type_="azure-native:azurestackhci/v20240401:EdgeDevice")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(EdgeDevice, __self__).__init__(
            'azure-native:azurestackhci/v20240101:EdgeDevice',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EdgeDevice':
        """
        Get an existing EdgeDevice resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EdgeDeviceArgs.__new__(EdgeDeviceArgs)

        __props__.__dict__["device_configuration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return EdgeDevice(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deviceConfiguration")
    def device_configuration(self) -> pulumi.Output[Optional['outputs.DeviceConfigurationResponse']]:
        """
        Device Configuration
        """
        return pulumi.get(self, "device_configuration")

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
        Provisioning state of edgeDevice resource
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
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

