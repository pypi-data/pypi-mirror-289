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

__all__ = ['ConfigurationArgs', 'Configuration']

@pulumi.input_type
class ConfigurationArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Configuration resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[str] configuration_name: The name of the server configuration.
        :param pulumi.Input[str] source: Source of the configuration.
        :param pulumi.Input[str] value: Value of the configuration.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        if configuration_name is not None:
            pulumi.set(__self__, "configuration_name", configuration_name)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if value is not None:
            pulumi.set(__self__, "value", value)

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
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the server configuration.
        """
        return pulumi.get(self, "configuration_name")

    @configuration_name.setter
    def configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_name", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Source of the configuration.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Value of the configuration.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class Configuration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a Configuration.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] configuration_name: The name of the server configuration.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[str] source: Source of the configuration.
        :param pulumi.Input[str] value: Value of the configuration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a Configuration.

        :param str resource_name: The name of the resource.
        :param ConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConfigurationArgs.__new__(ConfigurationArgs)

            __props__.__dict__["configuration_name"] = configuration_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["source"] = source
            __props__.__dict__["value"] = value
            __props__.__dict__["allowed_values"] = None
            __props__.__dict__["data_type"] = None
            __props__.__dict__["default_value"] = None
            __props__.__dict__["description"] = None
            __props__.__dict__["documentation_link"] = None
            __props__.__dict__["is_config_pending_restart"] = None
            __props__.__dict__["is_dynamic_config"] = None
            __props__.__dict__["is_read_only"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["unit"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:dbforpostgresql:Configuration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20200214preview:Configuration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20200214privatepreview:Configuration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20210410privatepreview:Configuration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20210601:Configuration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20210601preview:Configuration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20210615privatepreview:Configuration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20220120preview:Configuration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20220308preview:Configuration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20230301preview:Configuration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20230601preview:Configuration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20231201preview:Configuration"), pulumi.Alias(type_="azure-native:dbforpostgresql/v20240301preview:Configuration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Configuration, __self__).__init__(
            'azure-native:dbforpostgresql/v20221201:Configuration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Configuration':
        """
        Get an existing Configuration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConfigurationArgs.__new__(ConfigurationArgs)

        __props__.__dict__["allowed_values"] = None
        __props__.__dict__["data_type"] = None
        __props__.__dict__["default_value"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["documentation_link"] = None
        __props__.__dict__["is_config_pending_restart"] = None
        __props__.__dict__["is_dynamic_config"] = None
        __props__.__dict__["is_read_only"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["unit"] = None
        __props__.__dict__["value"] = None
        return Configuration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowedValues")
    def allowed_values(self) -> pulumi.Output[str]:
        """
        Allowed values of the configuration.
        """
        return pulumi.get(self, "allowed_values")

    @property
    @pulumi.getter(name="dataType")
    def data_type(self) -> pulumi.Output[str]:
        """
        Data type of the configuration.
        """
        return pulumi.get(self, "data_type")

    @property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> pulumi.Output[str]:
        """
        Default value of the configuration.
        """
        return pulumi.get(self, "default_value")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Description of the configuration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="documentationLink")
    def documentation_link(self) -> pulumi.Output[str]:
        """
        Configuration documentation link.
        """
        return pulumi.get(self, "documentation_link")

    @property
    @pulumi.getter(name="isConfigPendingRestart")
    def is_config_pending_restart(self) -> pulumi.Output[bool]:
        """
        Configuration is pending restart or not.
        """
        return pulumi.get(self, "is_config_pending_restart")

    @property
    @pulumi.getter(name="isDynamicConfig")
    def is_dynamic_config(self) -> pulumi.Output[bool]:
        """
        Configuration dynamic or static.
        """
        return pulumi.get(self, "is_dynamic_config")

    @property
    @pulumi.getter(name="isReadOnly")
    def is_read_only(self) -> pulumi.Output[bool]:
        """
        Configuration read-only or not.
        """
        return pulumi.get(self, "is_read_only")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[str]]:
        """
        Source of the configuration.
        """
        return pulumi.get(self, "source")

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

    @property
    @pulumi.getter
    def unit(self) -> pulumi.Output[str]:
        """
        Configuration unit.
        """
        return pulumi.get(self, "unit")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional[str]]:
        """
        Value of the configuration.
        """
        return pulumi.get(self, "value")

