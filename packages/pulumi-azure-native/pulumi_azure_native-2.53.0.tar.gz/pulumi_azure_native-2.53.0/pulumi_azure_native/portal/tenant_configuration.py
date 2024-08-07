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

__all__ = ['TenantConfigurationArgs', 'TenantConfiguration']

@pulumi.input_type
class TenantConfigurationArgs:
    def __init__(__self__, *,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 enforce_private_markdown_storage: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a TenantConfiguration resource.
        :param pulumi.Input[str] configuration_name: The configuration name. Value must be 'default'
        :param pulumi.Input[bool] enforce_private_markdown_storage: When flag is set to true Markdown tile will require external storage configuration (URI). The inline content configuration will be prohibited.
        """
        if configuration_name is not None:
            pulumi.set(__self__, "configuration_name", configuration_name)
        if enforce_private_markdown_storage is not None:
            pulumi.set(__self__, "enforce_private_markdown_storage", enforce_private_markdown_storage)

    @property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The configuration name. Value must be 'default'
        """
        return pulumi.get(self, "configuration_name")

    @configuration_name.setter
    def configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_name", value)

    @property
    @pulumi.getter(name="enforcePrivateMarkdownStorage")
    def enforce_private_markdown_storage(self) -> Optional[pulumi.Input[bool]]:
        """
        When flag is set to true Markdown tile will require external storage configuration (URI). The inline content configuration will be prohibited.
        """
        return pulumi.get(self, "enforce_private_markdown_storage")

    @enforce_private_markdown_storage.setter
    def enforce_private_markdown_storage(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enforce_private_markdown_storage", value)


class TenantConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 enforce_private_markdown_storage: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Tenant configuration.
        Azure REST API version: 2020-09-01-preview. Prior API version in Azure Native 1.x: 2020-09-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] configuration_name: The configuration name. Value must be 'default'
        :param pulumi.Input[bool] enforce_private_markdown_storage: When flag is set to true Markdown tile will require external storage configuration (URI). The inline content configuration will be prohibited.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TenantConfigurationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Tenant configuration.
        Azure REST API version: 2020-09-01-preview. Prior API version in Azure Native 1.x: 2020-09-01-preview.

        :param str resource_name: The name of the resource.
        :param TenantConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TenantConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 enforce_private_markdown_storage: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TenantConfigurationArgs.__new__(TenantConfigurationArgs)

            __props__.__dict__["configuration_name"] = configuration_name
            __props__.__dict__["enforce_private_markdown_storage"] = enforce_private_markdown_storage
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:portal/v20190101preview:TenantConfiguration"), pulumi.Alias(type_="azure-native:portal/v20200901preview:TenantConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(TenantConfiguration, __self__).__init__(
            'azure-native:portal:TenantConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'TenantConfiguration':
        """
        Get an existing TenantConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TenantConfigurationArgs.__new__(TenantConfigurationArgs)

        __props__.__dict__["enforce_private_markdown_storage"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return TenantConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="enforcePrivateMarkdownStorage")
    def enforce_private_markdown_storage(self) -> pulumi.Output[Optional[bool]]:
        """
        When flag is set to true Markdown tile will require external storage configuration (URI). The inline content configuration will be prohibited.
        """
        return pulumi.get(self, "enforce_private_markdown_storage")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

