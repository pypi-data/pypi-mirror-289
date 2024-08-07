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
from ._enums import *
from ._inputs import *

__all__ = ['BuildpackBindingArgs', 'BuildpackBinding']

@pulumi.input_type
class BuildpackBindingArgs:
    def __init__(__self__, *,
                 build_service_name: pulumi.Input[str],
                 builder_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 buildpack_binding_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['BuildpackBindingPropertiesArgs']] = None):
        """
        The set of arguments for constructing a BuildpackBinding resource.
        :param pulumi.Input[str] build_service_name: The name of the build service resource.
        :param pulumi.Input[str] builder_name: The name of the builder resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] service_name: The name of the Service resource.
        :param pulumi.Input[str] buildpack_binding_name: The name of the Buildpack Binding Name
        :param pulumi.Input['BuildpackBindingPropertiesArgs'] properties: Properties of a buildpack binding
        """
        pulumi.set(__self__, "build_service_name", build_service_name)
        pulumi.set(__self__, "builder_name", builder_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if buildpack_binding_name is not None:
            pulumi.set(__self__, "buildpack_binding_name", buildpack_binding_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="buildServiceName")
    def build_service_name(self) -> pulumi.Input[str]:
        """
        The name of the build service resource.
        """
        return pulumi.get(self, "build_service_name")

    @build_service_name.setter
    def build_service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "build_service_name", value)

    @property
    @pulumi.getter(name="builderName")
    def builder_name(self) -> pulumi.Input[str]:
        """
        The name of the builder resource.
        """
        return pulumi.get(self, "builder_name")

    @builder_name.setter
    def builder_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "builder_name", value)

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
    @pulumi.getter(name="buildpackBindingName")
    def buildpack_binding_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Buildpack Binding Name
        """
        return pulumi.get(self, "buildpack_binding_name")

    @buildpack_binding_name.setter
    def buildpack_binding_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "buildpack_binding_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['BuildpackBindingPropertiesArgs']]:
        """
        Properties of a buildpack binding
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['BuildpackBindingPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class BuildpackBinding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 build_service_name: Optional[pulumi.Input[str]] = None,
                 builder_name: Optional[pulumi.Input[str]] = None,
                 buildpack_binding_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['BuildpackBindingPropertiesArgs', 'BuildpackBindingPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Buildpack Binding Resource object

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] build_service_name: The name of the build service resource.
        :param pulumi.Input[str] builder_name: The name of the builder resource.
        :param pulumi.Input[str] buildpack_binding_name: The name of the Buildpack Binding Name
        :param pulumi.Input[Union['BuildpackBindingPropertiesArgs', 'BuildpackBindingPropertiesArgsDict']] properties: Properties of a buildpack binding
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] service_name: The name of the Service resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BuildpackBindingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Buildpack Binding Resource object

        :param str resource_name: The name of the resource.
        :param BuildpackBindingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BuildpackBindingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 build_service_name: Optional[pulumi.Input[str]] = None,
                 builder_name: Optional[pulumi.Input[str]] = None,
                 buildpack_binding_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['BuildpackBindingPropertiesArgs', 'BuildpackBindingPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BuildpackBindingArgs.__new__(BuildpackBindingArgs)

            if build_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'build_service_name'")
            __props__.__dict__["build_service_name"] = build_service_name
            if builder_name is None and not opts.urn:
                raise TypeError("Missing required property 'builder_name'")
            __props__.__dict__["builder_name"] = builder_name
            __props__.__dict__["buildpack_binding_name"] = buildpack_binding_name
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
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:appplatform:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20220101preview:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20220301preview:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20220401:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20220501preview:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20220901preview:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20221101preview:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20221201:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20230101preview:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20230301preview:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20230501preview:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20230701preview:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20230901preview:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20231201:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20240101preview:BuildpackBinding"), pulumi.Alias(type_="azure-native:appplatform/v20240501preview:BuildpackBinding")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BuildpackBinding, __self__).__init__(
            'azure-native:appplatform/v20231101preview:BuildpackBinding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BuildpackBinding':
        """
        Get an existing BuildpackBinding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BuildpackBindingArgs.__new__(BuildpackBindingArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return BuildpackBinding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.BuildpackBindingPropertiesResponse']:
        """
        Properties of a buildpack binding
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

