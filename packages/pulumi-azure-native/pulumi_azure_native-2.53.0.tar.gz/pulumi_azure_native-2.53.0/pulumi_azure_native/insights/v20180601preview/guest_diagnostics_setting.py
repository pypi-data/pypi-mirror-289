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

__all__ = ['GuestDiagnosticsSettingArgs', 'GuestDiagnosticsSetting']

@pulumi.input_type
class GuestDiagnosticsSettingArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 data_sources: Optional[pulumi.Input[Sequence[pulumi.Input['DataSourceArgs']]]] = None,
                 diagnostic_settings_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 proxy_setting: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a GuestDiagnosticsSetting resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['DataSourceArgs']]] data_sources: the array of data source object which are configured to collect and send data
        :param pulumi.Input[str] diagnostic_settings_name: The name of the diagnostic setting.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] os_type: Operating system type for the configuration
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if data_sources is not None:
            pulumi.set(__self__, "data_sources", data_sources)
        if diagnostic_settings_name is not None:
            pulumi.set(__self__, "diagnostic_settings_name", diagnostic_settings_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if os_type is not None:
            pulumi.set(__self__, "os_type", os_type)
        if proxy_setting is not None:
            pulumi.set(__self__, "proxy_setting", proxy_setting)
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
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DataSourceArgs']]]]:
        """
        the array of data source object which are configured to collect and send data
        """
        return pulumi.get(self, "data_sources")

    @data_sources.setter
    def data_sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DataSourceArgs']]]]):
        pulumi.set(self, "data_sources", value)

    @property
    @pulumi.getter(name="diagnosticSettingsName")
    def diagnostic_settings_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the diagnostic setting.
        """
        return pulumi.get(self, "diagnostic_settings_name")

    @diagnostic_settings_name.setter
    def diagnostic_settings_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "diagnostic_settings_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[str]]:
        """
        Operating system type for the configuration
        """
        return pulumi.get(self, "os_type")

    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_type", value)

    @property
    @pulumi.getter(name="proxySetting")
    def proxy_setting(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "proxy_setting")

    @proxy_setting.setter
    def proxy_setting(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proxy_setting", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class GuestDiagnosticsSetting(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DataSourceArgs', 'DataSourceArgsDict']]]]] = None,
                 diagnostic_settings_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 proxy_setting: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Virtual machine guest diagnostics settings resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['DataSourceArgs', 'DataSourceArgsDict']]]] data_sources: the array of data source object which are configured to collect and send data
        :param pulumi.Input[str] diagnostic_settings_name: The name of the diagnostic setting.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] os_type: Operating system type for the configuration
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GuestDiagnosticsSettingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Virtual machine guest diagnostics settings resource.

        :param str resource_name: The name of the resource.
        :param GuestDiagnosticsSettingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GuestDiagnosticsSettingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_sources: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DataSourceArgs', 'DataSourceArgsDict']]]]] = None,
                 diagnostic_settings_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 proxy_setting: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GuestDiagnosticsSettingArgs.__new__(GuestDiagnosticsSettingArgs)

            __props__.__dict__["data_sources"] = data_sources
            __props__.__dict__["diagnostic_settings_name"] = diagnostic_settings_name
            __props__.__dict__["location"] = location
            __props__.__dict__["os_type"] = os_type
            __props__.__dict__["proxy_setting"] = proxy_setting
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights/v20180601preview:guestDiagnosticsSetting"), pulumi.Alias(type_="azure-native:insights:GuestDiagnosticsSetting"), pulumi.Alias(type_="azure-native:insights:guestDiagnosticsSetting")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GuestDiagnosticsSetting, __self__).__init__(
            'azure-native:insights/v20180601preview:GuestDiagnosticsSetting',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GuestDiagnosticsSetting':
        """
        Get an existing GuestDiagnosticsSetting resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GuestDiagnosticsSettingArgs.__new__(GuestDiagnosticsSettingArgs)

        __props__.__dict__["data_sources"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["os_type"] = None
        __props__.__dict__["proxy_setting"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return GuestDiagnosticsSetting(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataSources")
    def data_sources(self) -> pulumi.Output[Optional[Sequence['outputs.DataSourceResponse']]]:
        """
        the array of data source object which are configured to collect and send data
        """
        return pulumi.get(self, "data_sources")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> pulumi.Output[Optional[str]]:
        """
        Operating system type for the configuration
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="proxySetting")
    def proxy_setting(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "proxy_setting")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

