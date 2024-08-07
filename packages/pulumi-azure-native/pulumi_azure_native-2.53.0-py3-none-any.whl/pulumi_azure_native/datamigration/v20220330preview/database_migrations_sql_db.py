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

__all__ = ['DatabaseMigrationsSqlDbArgs', 'DatabaseMigrationsSqlDb']

@pulumi.input_type
class DatabaseMigrationsSqlDbArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 sql_db_instance_name: pulumi.Input[str],
                 properties: Optional[pulumi.Input['DatabaseMigrationPropertiesSqlDbArgs']] = None,
                 target_db_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DatabaseMigrationsSqlDb resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input['DatabaseMigrationPropertiesSqlDbArgs'] properties: Database Migration Resource properties for SQL database.
        :param pulumi.Input[str] target_db_name: The name of the target database.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sql_db_instance_name", sql_db_instance_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if target_db_name is not None:
            pulumi.set(__self__, "target_db_name", target_db_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sqlDbInstanceName")
    def sql_db_instance_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "sql_db_instance_name")

    @sql_db_instance_name.setter
    def sql_db_instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sql_db_instance_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['DatabaseMigrationPropertiesSqlDbArgs']]:
        """
        Database Migration Resource properties for SQL database.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['DatabaseMigrationPropertiesSqlDbArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="targetDbName")
    def target_db_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the target database.
        """
        return pulumi.get(self, "target_db_name")

    @target_db_name.setter
    def target_db_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_db_name", value)


class DatabaseMigrationsSqlDb(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 properties: Optional[pulumi.Input[Union['DatabaseMigrationPropertiesSqlDbArgs', 'DatabaseMigrationPropertiesSqlDbArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_db_instance_name: Optional[pulumi.Input[str]] = None,
                 target_db_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Database Migration Resource for SQL Database.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['DatabaseMigrationPropertiesSqlDbArgs', 'DatabaseMigrationPropertiesSqlDbArgsDict']] properties: Database Migration Resource properties for SQL database.
        :param pulumi.Input[str] resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] target_db_name: The name of the target database.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatabaseMigrationsSqlDbArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Database Migration Resource for SQL Database.

        :param str resource_name: The name of the resource.
        :param DatabaseMigrationsSqlDbArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatabaseMigrationsSqlDbArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 properties: Optional[pulumi.Input[Union['DatabaseMigrationPropertiesSqlDbArgs', 'DatabaseMigrationPropertiesSqlDbArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_db_instance_name: Optional[pulumi.Input[str]] = None,
                 target_db_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatabaseMigrationsSqlDbArgs.__new__(DatabaseMigrationsSqlDbArgs)

            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sql_db_instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'sql_db_instance_name'")
            __props__.__dict__["sql_db_instance_name"] = sql_db_instance_name
            __props__.__dict__["target_db_name"] = target_db_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datamigration:DatabaseMigrationsSqlDb"), pulumi.Alias(type_="azure-native:datamigration/v20230715preview:DatabaseMigrationsSqlDb")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DatabaseMigrationsSqlDb, __self__).__init__(
            'azure-native:datamigration/v20220330preview:DatabaseMigrationsSqlDb',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DatabaseMigrationsSqlDb':
        """
        Get an existing DatabaseMigrationsSqlDb resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatabaseMigrationsSqlDbArgs.__new__(DatabaseMigrationsSqlDbArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return DatabaseMigrationsSqlDb(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.DatabaseMigrationPropertiesSqlDbResponse']:
        """
        Database Migration Resource properties for SQL database.
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
        return pulumi.get(self, "type")

