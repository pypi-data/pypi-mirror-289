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
from ._enums import *

__all__ = ['SyncMemberArgs', 'SyncMember']

@pulumi.input_type
class SyncMemberArgs:
    def __init__(__self__, *,
                 database_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 sync_group_name: pulumi.Input[str],
                 database_type: Optional[pulumi.Input[Union[str, 'SyncMemberDbType']]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 sql_server_database_id: Optional[pulumi.Input[str]] = None,
                 sync_agent_id: Optional[pulumi.Input[str]] = None,
                 sync_direction: Optional[pulumi.Input[Union[str, 'SyncDirection']]] = None,
                 sync_member_azure_database_resource_id: Optional[pulumi.Input[str]] = None,
                 sync_member_name: Optional[pulumi.Input[str]] = None,
                 use_private_link_connection: Optional[pulumi.Input[bool]] = None,
                 user_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SyncMember resource.
        :param pulumi.Input[str] database_name: Database name of the member database in the sync member.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: Server name of the member database in the sync member
        :param pulumi.Input[str] sync_group_name: The name of the sync group on which the sync member is hosted.
        :param pulumi.Input[Union[str, 'SyncMemberDbType']] database_type: Database type of the sync member.
        :param pulumi.Input[str] password: Password of the member database in the sync member.
        :param pulumi.Input[str] sql_server_database_id: SQL Server database id of the sync member.
        :param pulumi.Input[str] sync_agent_id: ARM resource id of the sync agent in the sync member.
        :param pulumi.Input[Union[str, 'SyncDirection']] sync_direction: Sync direction of the sync member.
        :param pulumi.Input[str] sync_member_azure_database_resource_id: ARM resource id of the sync member logical database, for sync members in Azure.
        :param pulumi.Input[str] sync_member_name: The name of the sync member.
        :param pulumi.Input[bool] use_private_link_connection: Whether to use private link connection.
        :param pulumi.Input[str] user_name: User name of the member database in the sync member.
        """
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        pulumi.set(__self__, "sync_group_name", sync_group_name)
        if database_type is not None:
            pulumi.set(__self__, "database_type", database_type)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if sql_server_database_id is not None:
            pulumi.set(__self__, "sql_server_database_id", sql_server_database_id)
        if sync_agent_id is not None:
            pulumi.set(__self__, "sync_agent_id", sync_agent_id)
        if sync_direction is not None:
            pulumi.set(__self__, "sync_direction", sync_direction)
        if sync_member_azure_database_resource_id is not None:
            pulumi.set(__self__, "sync_member_azure_database_resource_id", sync_member_azure_database_resource_id)
        if sync_member_name is not None:
            pulumi.set(__self__, "sync_member_name", sync_member_name)
        if use_private_link_connection is not None:
            pulumi.set(__self__, "use_private_link_connection", use_private_link_connection)
        if user_name is not None:
            pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        Database name of the member database in the sync member.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

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
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        Server name of the member database in the sync member
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="syncGroupName")
    def sync_group_name(self) -> pulumi.Input[str]:
        """
        The name of the sync group on which the sync member is hosted.
        """
        return pulumi.get(self, "sync_group_name")

    @sync_group_name.setter
    def sync_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sync_group_name", value)

    @property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> Optional[pulumi.Input[Union[str, 'SyncMemberDbType']]]:
        """
        Database type of the sync member.
        """
        return pulumi.get(self, "database_type")

    @database_type.setter
    def database_type(self, value: Optional[pulumi.Input[Union[str, 'SyncMemberDbType']]]):
        pulumi.set(self, "database_type", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password of the member database in the sync member.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="sqlServerDatabaseId")
    def sql_server_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        SQL Server database id of the sync member.
        """
        return pulumi.get(self, "sql_server_database_id")

    @sql_server_database_id.setter
    def sql_server_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_server_database_id", value)

    @property
    @pulumi.getter(name="syncAgentId")
    def sync_agent_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM resource id of the sync agent in the sync member.
        """
        return pulumi.get(self, "sync_agent_id")

    @sync_agent_id.setter
    def sync_agent_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_agent_id", value)

    @property
    @pulumi.getter(name="syncDirection")
    def sync_direction(self) -> Optional[pulumi.Input[Union[str, 'SyncDirection']]]:
        """
        Sync direction of the sync member.
        """
        return pulumi.get(self, "sync_direction")

    @sync_direction.setter
    def sync_direction(self, value: Optional[pulumi.Input[Union[str, 'SyncDirection']]]):
        pulumi.set(self, "sync_direction", value)

    @property
    @pulumi.getter(name="syncMemberAzureDatabaseResourceId")
    def sync_member_azure_database_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM resource id of the sync member logical database, for sync members in Azure.
        """
        return pulumi.get(self, "sync_member_azure_database_resource_id")

    @sync_member_azure_database_resource_id.setter
    def sync_member_azure_database_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_member_azure_database_resource_id", value)

    @property
    @pulumi.getter(name="syncMemberName")
    def sync_member_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the sync member.
        """
        return pulumi.get(self, "sync_member_name")

    @sync_member_name.setter
    def sync_member_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_member_name", value)

    @property
    @pulumi.getter(name="usePrivateLinkConnection")
    def use_private_link_connection(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to use private link connection.
        """
        return pulumi.get(self, "use_private_link_connection")

    @use_private_link_connection.setter
    def use_private_link_connection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_private_link_connection", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        """
        User name of the member database in the sync member.
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)


class SyncMember(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 database_type: Optional[pulumi.Input[Union[str, 'SyncMemberDbType']]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sql_server_database_id: Optional[pulumi.Input[str]] = None,
                 sync_agent_id: Optional[pulumi.Input[str]] = None,
                 sync_direction: Optional[pulumi.Input[Union[str, 'SyncDirection']]] = None,
                 sync_group_name: Optional[pulumi.Input[str]] = None,
                 sync_member_azure_database_resource_id: Optional[pulumi.Input[str]] = None,
                 sync_member_name: Optional[pulumi.Input[str]] = None,
                 use_private_link_connection: Optional[pulumi.Input[bool]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        An Azure SQL Database sync member.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_name: Database name of the member database in the sync member.
        :param pulumi.Input[Union[str, 'SyncMemberDbType']] database_type: Database type of the sync member.
        :param pulumi.Input[str] password: Password of the member database in the sync member.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: Server name of the member database in the sync member
        :param pulumi.Input[str] sql_server_database_id: SQL Server database id of the sync member.
        :param pulumi.Input[str] sync_agent_id: ARM resource id of the sync agent in the sync member.
        :param pulumi.Input[Union[str, 'SyncDirection']] sync_direction: Sync direction of the sync member.
        :param pulumi.Input[str] sync_group_name: The name of the sync group on which the sync member is hosted.
        :param pulumi.Input[str] sync_member_azure_database_resource_id: ARM resource id of the sync member logical database, for sync members in Azure.
        :param pulumi.Input[str] sync_member_name: The name of the sync member.
        :param pulumi.Input[bool] use_private_link_connection: Whether to use private link connection.
        :param pulumi.Input[str] user_name: User name of the member database in the sync member.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SyncMemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Azure SQL Database sync member.

        :param str resource_name: The name of the resource.
        :param SyncMemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SyncMemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 database_type: Optional[pulumi.Input[Union[str, 'SyncMemberDbType']]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 sql_server_database_id: Optional[pulumi.Input[str]] = None,
                 sync_agent_id: Optional[pulumi.Input[str]] = None,
                 sync_direction: Optional[pulumi.Input[Union[str, 'SyncDirection']]] = None,
                 sync_group_name: Optional[pulumi.Input[str]] = None,
                 sync_member_azure_database_resource_id: Optional[pulumi.Input[str]] = None,
                 sync_member_name: Optional[pulumi.Input[str]] = None,
                 use_private_link_connection: Optional[pulumi.Input[bool]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SyncMemberArgs.__new__(SyncMemberArgs)

            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["database_type"] = database_type
            __props__.__dict__["password"] = password
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["sql_server_database_id"] = sql_server_database_id
            __props__.__dict__["sync_agent_id"] = sync_agent_id
            __props__.__dict__["sync_direction"] = sync_direction
            if sync_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'sync_group_name'")
            __props__.__dict__["sync_group_name"] = sync_group_name
            __props__.__dict__["sync_member_azure_database_resource_id"] = sync_member_azure_database_resource_id
            __props__.__dict__["sync_member_name"] = sync_member_name
            __props__.__dict__["use_private_link_connection"] = use_private_link_connection
            __props__.__dict__["user_name"] = user_name
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_name"] = None
            __props__.__dict__["sync_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20150501preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20190601preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20200202preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20200801preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20201101preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20210201preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20210501preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20210801preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20211101:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20211101preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20220201preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20220501preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20220801preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20221101preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20230201preview:SyncMember"), pulumi.Alias(type_="azure-native:sql/v20230501preview:SyncMember")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SyncMember, __self__).__init__(
            'azure-native:sql/v20230801preview:SyncMember',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SyncMember':
        """
        Get an existing SyncMember resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SyncMemberArgs.__new__(SyncMemberArgs)

        __props__.__dict__["database_name"] = None
        __props__.__dict__["database_type"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_name"] = None
        __props__.__dict__["server_name"] = None
        __props__.__dict__["sql_server_database_id"] = None
        __props__.__dict__["sync_agent_id"] = None
        __props__.__dict__["sync_direction"] = None
        __props__.__dict__["sync_member_azure_database_resource_id"] = None
        __props__.__dict__["sync_state"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["use_private_link_connection"] = None
        __props__.__dict__["user_name"] = None
        return SyncMember(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[Optional[str]]:
        """
        Database name of the member database in the sync member.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> pulumi.Output[Optional[str]]:
        """
        Database type of the sync member.
        """
        return pulumi.get(self, "database_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointName")
    def private_endpoint_name(self) -> pulumi.Output[str]:
        """
        Private endpoint name of the sync member if use private link connection is enabled, for sync members in Azure.
        """
        return pulumi.get(self, "private_endpoint_name")

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Output[Optional[str]]:
        """
        Server name of the member database in the sync member
        """
        return pulumi.get(self, "server_name")

    @property
    @pulumi.getter(name="sqlServerDatabaseId")
    def sql_server_database_id(self) -> pulumi.Output[Optional[str]]:
        """
        SQL Server database id of the sync member.
        """
        return pulumi.get(self, "sql_server_database_id")

    @property
    @pulumi.getter(name="syncAgentId")
    def sync_agent_id(self) -> pulumi.Output[Optional[str]]:
        """
        ARM resource id of the sync agent in the sync member.
        """
        return pulumi.get(self, "sync_agent_id")

    @property
    @pulumi.getter(name="syncDirection")
    def sync_direction(self) -> pulumi.Output[Optional[str]]:
        """
        Sync direction of the sync member.
        """
        return pulumi.get(self, "sync_direction")

    @property
    @pulumi.getter(name="syncMemberAzureDatabaseResourceId")
    def sync_member_azure_database_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        ARM resource id of the sync member logical database, for sync members in Azure.
        """
        return pulumi.get(self, "sync_member_azure_database_resource_id")

    @property
    @pulumi.getter(name="syncState")
    def sync_state(self) -> pulumi.Output[str]:
        """
        Sync state of the sync member.
        """
        return pulumi.get(self, "sync_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="usePrivateLinkConnection")
    def use_private_link_connection(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to use private link connection.
        """
        return pulumi.get(self, "use_private_link_connection")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[Optional[str]]:
        """
        User name of the member database in the sync member.
        """
        return pulumi.get(self, "user_name")

