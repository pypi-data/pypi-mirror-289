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
from ._enums import *
from ._inputs import *

__all__ = ['DevOpsConfigurationArgs', 'DevOpsConfiguration']

@pulumi.input_type
class DevOpsConfigurationArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 security_connector_name: pulumi.Input[str],
                 properties: Optional[pulumi.Input['DevOpsConfigurationPropertiesArgs']] = None):
        """
        The set of arguments for constructing a DevOpsConfiguration resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] security_connector_name: The security connector name.
        :param pulumi.Input['DevOpsConfigurationPropertiesArgs'] properties: DevOps Configuration properties.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "security_connector_name", security_connector_name)
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
    @pulumi.getter(name="securityConnectorName")
    def security_connector_name(self) -> pulumi.Input[str]:
        """
        The security connector name.
        """
        return pulumi.get(self, "security_connector_name")

    @security_connector_name.setter
    def security_connector_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "security_connector_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['DevOpsConfigurationPropertiesArgs']]:
        """
        DevOps Configuration properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['DevOpsConfigurationPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class DevOpsConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 properties: Optional[pulumi.Input[Union['DevOpsConfigurationPropertiesArgs', 'DevOpsConfigurationPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_connector_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        DevOps Configuration resource.
        Azure REST API version: 2023-09-01-preview.

        Other available API versions: 2024-04-01, 2024-05-15-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['DevOpsConfigurationPropertiesArgs', 'DevOpsConfigurationPropertiesArgsDict']] properties: DevOps Configuration properties.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] security_connector_name: The security connector name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DevOpsConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        DevOps Configuration resource.
        Azure REST API version: 2023-09-01-preview.

        Other available API versions: 2024-04-01, 2024-05-15-preview.

        :param str resource_name: The name of the resource.
        :param DevOpsConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DevOpsConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 properties: Optional[pulumi.Input[Union['DevOpsConfigurationPropertiesArgs', 'DevOpsConfigurationPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_connector_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DevOpsConfigurationArgs.__new__(DevOpsConfigurationArgs)

            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if security_connector_name is None and not opts.urn:
                raise TypeError("Missing required property 'security_connector_name'")
            __props__.__dict__["security_connector_name"] = security_connector_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:security/v20230901preview:DevOpsConfiguration"), pulumi.Alias(type_="azure-native:security/v20240401:DevOpsConfiguration"), pulumi.Alias(type_="azure-native:security/v20240515preview:DevOpsConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DevOpsConfiguration, __self__).__init__(
            'azure-native:security:DevOpsConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DevOpsConfiguration':
        """
        Get an existing DevOpsConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DevOpsConfigurationArgs.__new__(DevOpsConfigurationArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return DevOpsConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.DevOpsConfigurationPropertiesResponse']:
        """
        DevOps Configuration properties.
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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

