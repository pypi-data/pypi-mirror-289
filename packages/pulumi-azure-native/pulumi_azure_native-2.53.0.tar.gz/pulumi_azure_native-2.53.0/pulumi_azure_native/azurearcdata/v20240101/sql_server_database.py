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

__all__ = ['SqlServerDatabaseArgs', 'SqlServerDatabase']

@pulumi.input_type
class SqlServerDatabaseArgs:
    def __init__(__self__, *,
                 properties: pulumi.Input['SqlServerDatabaseResourcePropertiesArgs'],
                 resource_group_name: pulumi.Input[str],
                 sql_server_instance_name: pulumi.Input[str],
                 database_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SqlServerDatabase resource.
        :param pulumi.Input['SqlServerDatabaseResourcePropertiesArgs'] properties: Properties of Arc Sql Server database
        :param pulumi.Input[str] resource_group_name: The name of the Azure resource group
        :param pulumi.Input[str] sql_server_instance_name: Name of SQL Server Instance
        :param pulumi.Input[str] database_name: Name of the database
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sql_server_instance_name", sql_server_instance_name)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input['SqlServerDatabaseResourcePropertiesArgs']:
        """
        Properties of Arc Sql Server database
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input['SqlServerDatabaseResourcePropertiesArgs']):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Azure resource group
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sqlServerInstanceName")
    def sql_server_instance_name(self) -> pulumi.Input[str]:
        """
        Name of SQL Server Instance
        """
        return pulumi.get(self, "sql_server_instance_name")

    @sql_server_instance_name.setter
    def sql_server_instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sql_server_instance_name", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the database
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class SqlServerDatabase(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['SqlServerDatabaseResourcePropertiesArgs', 'SqlServerDatabaseResourcePropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_server_instance_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Arc Sql Server database

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_name: Name of the database
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union['SqlServerDatabaseResourcePropertiesArgs', 'SqlServerDatabaseResourcePropertiesArgsDict']] properties: Properties of Arc Sql Server database
        :param pulumi.Input[str] resource_group_name: The name of the Azure resource group
        :param pulumi.Input[str] sql_server_instance_name: Name of SQL Server Instance
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlServerDatabaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Arc Sql Server database

        :param str resource_name: The name of the resource.
        :param SqlServerDatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlServerDatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['SqlServerDatabaseResourcePropertiesArgs', 'SqlServerDatabaseResourcePropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_server_instance_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlServerDatabaseArgs.__new__(SqlServerDatabaseArgs)

            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["location"] = location
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sql_server_instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'sql_server_instance_name'")
            __props__.__dict__["sql_server_instance_name"] = sql_server_instance_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurearcdata:SqlServerDatabase"), pulumi.Alias(type_="azure-native:azurearcdata/v20220615preview:SqlServerDatabase"), pulumi.Alias(type_="azure-native:azurearcdata/v20230115preview:SqlServerDatabase")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SqlServerDatabase, __self__).__init__(
            'azure-native:azurearcdata/v20240101:SqlServerDatabase',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SqlServerDatabase':
        """
        Get an existing SqlServerDatabase resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SqlServerDatabaseArgs.__new__(SqlServerDatabaseArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return SqlServerDatabase(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.SqlServerDatabaseResourcePropertiesResponse']:
        """
        Properties of Arc Sql Server database
        """
        return pulumi.get(self, "properties")

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

