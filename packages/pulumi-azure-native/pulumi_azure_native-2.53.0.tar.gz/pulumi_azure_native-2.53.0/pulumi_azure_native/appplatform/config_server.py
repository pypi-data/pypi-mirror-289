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

__all__ = ['ConfigServerArgs', 'ConfigServer']

@pulumi.input_type
class ConfigServerArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 properties: Optional[pulumi.Input['ConfigServerPropertiesArgs']] = None):
        """
        The set of arguments for constructing a ConfigServer resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] service_name: The name of the Service resource.
        :param pulumi.Input['ConfigServerPropertiesArgs'] properties: Properties of the Config Server resource
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

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
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['ConfigServerPropertiesArgs']]:
        """
        Properties of the Config Server resource
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['ConfigServerPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class ConfigServer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 properties: Optional[pulumi.Input[Union['ConfigServerPropertiesArgs', 'ConfigServerPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Config Server resource
        Azure REST API version: 2023-05-01-preview. Prior API version in Azure Native 1.x: 2020-07-01.

        Other available API versions: 2023-07-01-preview, 2023-09-01-preview, 2023-11-01-preview, 2023-12-01, 2024-01-01-preview, 2024-05-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['ConfigServerPropertiesArgs', 'ConfigServerPropertiesArgsDict']] properties: Properties of the Config Server resource
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] service_name: The name of the Service resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Config Server resource
        Azure REST API version: 2023-05-01-preview. Prior API version in Azure Native 1.x: 2020-07-01.

        Other available API versions: 2023-07-01-preview, 2023-09-01-preview, 2023-11-01-preview, 2023-12-01, 2024-01-01-preview, 2024-05-01-preview.

        :param str resource_name: The name of the resource.
        :param ConfigServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 properties: Optional[pulumi.Input[Union['ConfigServerPropertiesArgs', 'ConfigServerPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigServerArgs.__new__(ConfigServerArgs)

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
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:appplatform/v20200701:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20201101preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20210601preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20210901preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20220101preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20220301preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20220401:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20220501preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20220901preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20221101preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20221201:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20230101preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20230301preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20230501preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20230701preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20230901preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20231101preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20231201:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20240101preview:ConfigServer"), pulumi.Alias(type_="azure-native:appplatform/v20240501preview:ConfigServer")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ConfigServer, __self__).__init__(
            'azure-native:appplatform:ConfigServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ConfigServer':
        """
        Get an existing ConfigServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConfigServerArgs.__new__(ConfigServerArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ConfigServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.ConfigServerPropertiesResponse']:
        """
        Properties of the Config Server resource
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

