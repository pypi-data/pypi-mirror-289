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

__all__ = ['StaticSiteDatabaseConnectionArgs', 'StaticSiteDatabaseConnection']

@pulumi.input_type
class StaticSiteDatabaseConnectionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 region: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 resource_id: pulumi.Input[str],
                 connection_identity: Optional[pulumi.Input[str]] = None,
                 connection_string: Optional[pulumi.Input[str]] = None,
                 database_connection_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StaticSiteDatabaseConnection resource.
        :param pulumi.Input[str] name: Name of the static site
        :param pulumi.Input[str] region: The region of the database resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] resource_id: The resource id of the database.
        :param pulumi.Input[str] connection_identity: If present, the identity is used in conjunction with connection string to connect to the database. Use of the system-assigned managed identity is indicated with the string 'SystemAssigned', while use of a user-assigned managed identity is indicated with the resource id of the managed identity resource.
        :param pulumi.Input[str] connection_string: The connection string to use to connect to the database.
        :param pulumi.Input[str] database_connection_name: Name of the database connection.
        :param pulumi.Input[str] kind: Kind of resource.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "region", region)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_id", resource_id)
        if connection_identity is not None:
            pulumi.set(__self__, "connection_identity", connection_identity)
        if connection_string is not None:
            pulumi.set(__self__, "connection_string", connection_string)
        if database_connection_name is not None:
            pulumi.set(__self__, "database_connection_name", database_connection_name)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the static site
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        The region of the database resource.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        The resource id of the database.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="connectionIdentity")
    def connection_identity(self) -> Optional[pulumi.Input[str]]:
        """
        If present, the identity is used in conjunction with connection string to connect to the database. Use of the system-assigned managed identity is indicated with the string 'SystemAssigned', while use of a user-assigned managed identity is indicated with the resource id of the managed identity resource.
        """
        return pulumi.get(self, "connection_identity")

    @connection_identity.setter
    def connection_identity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_identity", value)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        The connection string to use to connect to the database.
        """
        return pulumi.get(self, "connection_string")

    @connection_string.setter
    def connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_string", value)

    @property
    @pulumi.getter(name="databaseConnectionName")
    def database_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the database connection.
        """
        return pulumi.get(self, "database_connection_name")

    @database_connection_name.setter
    def database_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_connection_name", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)


class StaticSiteDatabaseConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_identity: Optional[pulumi.Input[str]] = None,
                 connection_string: Optional[pulumi.Input[str]] = None,
                 database_connection_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Static Site Database Connection resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] connection_identity: If present, the identity is used in conjunction with connection string to connect to the database. Use of the system-assigned managed identity is indicated with the string 'SystemAssigned', while use of a user-assigned managed identity is indicated with the resource id of the managed identity resource.
        :param pulumi.Input[str] connection_string: The connection string to use to connect to the database.
        :param pulumi.Input[str] database_connection_name: Name of the database connection.
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] name: Name of the static site
        :param pulumi.Input[str] region: The region of the database resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] resource_id: The resource id of the database.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StaticSiteDatabaseConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Static Site Database Connection resource.

        :param str resource_name: The name of the resource.
        :param StaticSiteDatabaseConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StaticSiteDatabaseConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 connection_identity: Optional[pulumi.Input[str]] = None,
                 connection_string: Optional[pulumi.Input[str]] = None,
                 database_connection_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StaticSiteDatabaseConnectionArgs.__new__(StaticSiteDatabaseConnectionArgs)

            __props__.__dict__["connection_identity"] = connection_identity
            __props__.__dict__["connection_string"] = connection_string
            __props__.__dict__["database_connection_name"] = database_connection_name
            __props__.__dict__["kind"] = kind
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["configuration_files"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:StaticSiteDatabaseConnection"), pulumi.Alias(type_="azure-native:web/v20230101:StaticSiteDatabaseConnection"), pulumi.Alias(type_="azure-native:web/v20231201:StaticSiteDatabaseConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StaticSiteDatabaseConnection, __self__).__init__(
            'azure-native:web/v20220901:StaticSiteDatabaseConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StaticSiteDatabaseConnection':
        """
        Get an existing StaticSiteDatabaseConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StaticSiteDatabaseConnectionArgs.__new__(StaticSiteDatabaseConnectionArgs)

        __props__.__dict__["configuration_files"] = None
        __props__.__dict__["connection_identity"] = None
        __props__.__dict__["connection_string"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["type"] = None
        return StaticSiteDatabaseConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="configurationFiles")
    def configuration_files(self) -> pulumi.Output[Sequence['outputs.StaticSiteDatabaseConnectionConfigurationFileOverviewResponse']]:
        """
        A list of configuration files associated with this database connection.
        """
        return pulumi.get(self, "configuration_files")

    @property
    @pulumi.getter(name="connectionIdentity")
    def connection_identity(self) -> pulumi.Output[Optional[str]]:
        """
        If present, the identity is used in conjunction with connection string to connect to the database. Use of the system-assigned managed identity is indicated with the string 'SystemAssigned', while use of a user-assigned managed identity is indicated with the resource id of the managed identity resource.
        """
        return pulumi.get(self, "connection_identity")

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> pulumi.Output[Optional[str]]:
        """
        The connection string to use to connect to the database.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region of the database resource.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        The resource id of the database.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

