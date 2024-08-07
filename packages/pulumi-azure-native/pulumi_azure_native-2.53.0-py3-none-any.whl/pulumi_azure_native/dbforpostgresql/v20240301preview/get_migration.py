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

__all__ = [
    'GetMigrationResult',
    'AwaitableGetMigrationResult',
    'get_migration',
    'get_migration_output',
]

@pulumi.output_type
class GetMigrationResult:
    """
    Represents a migration resource.
    """
    def __init__(__self__, cancel=None, current_status=None, dbs_to_cancel_migration_on=None, dbs_to_migrate=None, dbs_to_trigger_cutover_on=None, id=None, location=None, migrate_roles=None, migration_id=None, migration_instance_resource_id=None, migration_mode=None, migration_option=None, migration_window_end_time_in_utc=None, migration_window_start_time_in_utc=None, name=None, overwrite_dbs_in_target=None, setup_logical_replication_on_source_db_if_needed=None, source_db_server_fully_qualified_domain_name=None, source_db_server_metadata=None, source_db_server_resource_id=None, source_type=None, ssl_mode=None, start_data_migration=None, system_data=None, tags=None, target_db_server_fully_qualified_domain_name=None, target_db_server_metadata=None, target_db_server_resource_id=None, trigger_cutover=None, type=None):
        if cancel and not isinstance(cancel, str):
            raise TypeError("Expected argument 'cancel' to be a str")
        pulumi.set(__self__, "cancel", cancel)
        if current_status and not isinstance(current_status, dict):
            raise TypeError("Expected argument 'current_status' to be a dict")
        pulumi.set(__self__, "current_status", current_status)
        if dbs_to_cancel_migration_on and not isinstance(dbs_to_cancel_migration_on, list):
            raise TypeError("Expected argument 'dbs_to_cancel_migration_on' to be a list")
        pulumi.set(__self__, "dbs_to_cancel_migration_on", dbs_to_cancel_migration_on)
        if dbs_to_migrate and not isinstance(dbs_to_migrate, list):
            raise TypeError("Expected argument 'dbs_to_migrate' to be a list")
        pulumi.set(__self__, "dbs_to_migrate", dbs_to_migrate)
        if dbs_to_trigger_cutover_on and not isinstance(dbs_to_trigger_cutover_on, list):
            raise TypeError("Expected argument 'dbs_to_trigger_cutover_on' to be a list")
        pulumi.set(__self__, "dbs_to_trigger_cutover_on", dbs_to_trigger_cutover_on)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if migrate_roles and not isinstance(migrate_roles, str):
            raise TypeError("Expected argument 'migrate_roles' to be a str")
        pulumi.set(__self__, "migrate_roles", migrate_roles)
        if migration_id and not isinstance(migration_id, str):
            raise TypeError("Expected argument 'migration_id' to be a str")
        pulumi.set(__self__, "migration_id", migration_id)
        if migration_instance_resource_id and not isinstance(migration_instance_resource_id, str):
            raise TypeError("Expected argument 'migration_instance_resource_id' to be a str")
        pulumi.set(__self__, "migration_instance_resource_id", migration_instance_resource_id)
        if migration_mode and not isinstance(migration_mode, str):
            raise TypeError("Expected argument 'migration_mode' to be a str")
        pulumi.set(__self__, "migration_mode", migration_mode)
        if migration_option and not isinstance(migration_option, str):
            raise TypeError("Expected argument 'migration_option' to be a str")
        pulumi.set(__self__, "migration_option", migration_option)
        if migration_window_end_time_in_utc and not isinstance(migration_window_end_time_in_utc, str):
            raise TypeError("Expected argument 'migration_window_end_time_in_utc' to be a str")
        pulumi.set(__self__, "migration_window_end_time_in_utc", migration_window_end_time_in_utc)
        if migration_window_start_time_in_utc and not isinstance(migration_window_start_time_in_utc, str):
            raise TypeError("Expected argument 'migration_window_start_time_in_utc' to be a str")
        pulumi.set(__self__, "migration_window_start_time_in_utc", migration_window_start_time_in_utc)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if overwrite_dbs_in_target and not isinstance(overwrite_dbs_in_target, str):
            raise TypeError("Expected argument 'overwrite_dbs_in_target' to be a str")
        pulumi.set(__self__, "overwrite_dbs_in_target", overwrite_dbs_in_target)
        if setup_logical_replication_on_source_db_if_needed and not isinstance(setup_logical_replication_on_source_db_if_needed, str):
            raise TypeError("Expected argument 'setup_logical_replication_on_source_db_if_needed' to be a str")
        pulumi.set(__self__, "setup_logical_replication_on_source_db_if_needed", setup_logical_replication_on_source_db_if_needed)
        if source_db_server_fully_qualified_domain_name and not isinstance(source_db_server_fully_qualified_domain_name, str):
            raise TypeError("Expected argument 'source_db_server_fully_qualified_domain_name' to be a str")
        pulumi.set(__self__, "source_db_server_fully_qualified_domain_name", source_db_server_fully_qualified_domain_name)
        if source_db_server_metadata and not isinstance(source_db_server_metadata, dict):
            raise TypeError("Expected argument 'source_db_server_metadata' to be a dict")
        pulumi.set(__self__, "source_db_server_metadata", source_db_server_metadata)
        if source_db_server_resource_id and not isinstance(source_db_server_resource_id, str):
            raise TypeError("Expected argument 'source_db_server_resource_id' to be a str")
        pulumi.set(__self__, "source_db_server_resource_id", source_db_server_resource_id)
        if source_type and not isinstance(source_type, str):
            raise TypeError("Expected argument 'source_type' to be a str")
        pulumi.set(__self__, "source_type", source_type)
        if ssl_mode and not isinstance(ssl_mode, str):
            raise TypeError("Expected argument 'ssl_mode' to be a str")
        pulumi.set(__self__, "ssl_mode", ssl_mode)
        if start_data_migration and not isinstance(start_data_migration, str):
            raise TypeError("Expected argument 'start_data_migration' to be a str")
        pulumi.set(__self__, "start_data_migration", start_data_migration)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_db_server_fully_qualified_domain_name and not isinstance(target_db_server_fully_qualified_domain_name, str):
            raise TypeError("Expected argument 'target_db_server_fully_qualified_domain_name' to be a str")
        pulumi.set(__self__, "target_db_server_fully_qualified_domain_name", target_db_server_fully_qualified_domain_name)
        if target_db_server_metadata and not isinstance(target_db_server_metadata, dict):
            raise TypeError("Expected argument 'target_db_server_metadata' to be a dict")
        pulumi.set(__self__, "target_db_server_metadata", target_db_server_metadata)
        if target_db_server_resource_id and not isinstance(target_db_server_resource_id, str):
            raise TypeError("Expected argument 'target_db_server_resource_id' to be a str")
        pulumi.set(__self__, "target_db_server_resource_id", target_db_server_resource_id)
        if trigger_cutover and not isinstance(trigger_cutover, str):
            raise TypeError("Expected argument 'trigger_cutover' to be a str")
        pulumi.set(__self__, "trigger_cutover", trigger_cutover)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def cancel(self) -> Optional[str]:
        """
        To trigger cancel for entire migration we need to send this flag as True
        """
        return pulumi.get(self, "cancel")

    @property
    @pulumi.getter(name="currentStatus")
    def current_status(self) -> 'outputs.MigrationStatusResponse':
        """
        Current status of migration
        """
        return pulumi.get(self, "current_status")

    @property
    @pulumi.getter(name="dbsToCancelMigrationOn")
    def dbs_to_cancel_migration_on(self) -> Optional[Sequence[str]]:
        """
        When you want to trigger cancel for specific databases send cancel flag as True and database names in this array
        """
        return pulumi.get(self, "dbs_to_cancel_migration_on")

    @property
    @pulumi.getter(name="dbsToMigrate")
    def dbs_to_migrate(self) -> Optional[Sequence[str]]:
        """
        Number of databases to migrate
        """
        return pulumi.get(self, "dbs_to_migrate")

    @property
    @pulumi.getter(name="dbsToTriggerCutoverOn")
    def dbs_to_trigger_cutover_on(self) -> Optional[Sequence[str]]:
        """
        When you want to trigger cutover for specific databases send triggerCutover flag as True and database names in this array
        """
        return pulumi.get(self, "dbs_to_trigger_cutover_on")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="migrateRoles")
    def migrate_roles(self) -> Optional[str]:
        """
        To migrate roles and permissions we need to send this flag as True
        """
        return pulumi.get(self, "migrate_roles")

    @property
    @pulumi.getter(name="migrationId")
    def migration_id(self) -> str:
        """
        ID for migration, a GUID.
        """
        return pulumi.get(self, "migration_id")

    @property
    @pulumi.getter(name="migrationInstanceResourceId")
    def migration_instance_resource_id(self) -> Optional[str]:
        """
        ResourceId of the private endpoint migration instance
        """
        return pulumi.get(self, "migration_instance_resource_id")

    @property
    @pulumi.getter(name="migrationMode")
    def migration_mode(self) -> Optional[str]:
        """
        There are two types of migration modes Online and Offline
        """
        return pulumi.get(self, "migration_mode")

    @property
    @pulumi.getter(name="migrationOption")
    def migration_option(self) -> Optional[str]:
        """
        This indicates the supported Migration option for the migration
        """
        return pulumi.get(self, "migration_option")

    @property
    @pulumi.getter(name="migrationWindowEndTimeInUtc")
    def migration_window_end_time_in_utc(self) -> Optional[str]:
        """
        End time in UTC for migration window
        """
        return pulumi.get(self, "migration_window_end_time_in_utc")

    @property
    @pulumi.getter(name="migrationWindowStartTimeInUtc")
    def migration_window_start_time_in_utc(self) -> Optional[str]:
        """
        Start time in UTC for migration window
        """
        return pulumi.get(self, "migration_window_start_time_in_utc")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="overwriteDbsInTarget")
    def overwrite_dbs_in_target(self) -> Optional[str]:
        """
        Indicates whether the databases on the target server can be overwritten, if already present. If set to False, the migration workflow will wait for a confirmation, if it detects that the database already exists.
        """
        return pulumi.get(self, "overwrite_dbs_in_target")

    @property
    @pulumi.getter(name="setupLogicalReplicationOnSourceDbIfNeeded")
    def setup_logical_replication_on_source_db_if_needed(self) -> Optional[str]:
        """
        Indicates whether to setup LogicalReplicationOnSourceDb, if needed
        """
        return pulumi.get(self, "setup_logical_replication_on_source_db_if_needed")

    @property
    @pulumi.getter(name="sourceDbServerFullyQualifiedDomainName")
    def source_db_server_fully_qualified_domain_name(self) -> Optional[str]:
        """
        Source server fully qualified domain name (FQDN) or IP address. It is a optional value, if customer provide it, migration service will always use it for connection
        """
        return pulumi.get(self, "source_db_server_fully_qualified_domain_name")

    @property
    @pulumi.getter(name="sourceDbServerMetadata")
    def source_db_server_metadata(self) -> 'outputs.DbServerMetadataResponse':
        """
        Metadata of the source database server
        """
        return pulumi.get(self, "source_db_server_metadata")

    @property
    @pulumi.getter(name="sourceDbServerResourceId")
    def source_db_server_resource_id(self) -> Optional[str]:
        """
        ResourceId of the source database server in case the sourceType is PostgreSQLSingleServer. For other source types this should be ipaddress:port@username or hostname:port@username
        """
        return pulumi.get(self, "source_db_server_resource_id")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[str]:
        """
        migration source server type : OnPremises, AWS, GCP, AzureVM, PostgreSQLSingleServer, AWS_RDS, AWS_AURORA, AWS_EC2, GCP_CloudSQL, GCP_AlloyDB, GCP_Compute, or EDB
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> Optional[str]:
        """
        SSL modes for migration. Default SSL mode for PostgreSQLSingleServer is VerifyFull and Prefer for other source types
        """
        return pulumi.get(self, "ssl_mode")

    @property
    @pulumi.getter(name="startDataMigration")
    def start_data_migration(self) -> Optional[str]:
        """
        Indicates whether the data migration should start right away
        """
        return pulumi.get(self, "start_data_migration")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetDbServerFullyQualifiedDomainName")
    def target_db_server_fully_qualified_domain_name(self) -> Optional[str]:
        """
        Target server fully qualified domain name (FQDN) or IP address. It is a optional value, if customer provide it, migration service will always use it for connection
        """
        return pulumi.get(self, "target_db_server_fully_qualified_domain_name")

    @property
    @pulumi.getter(name="targetDbServerMetadata")
    def target_db_server_metadata(self) -> 'outputs.DbServerMetadataResponse':
        """
        Metadata of the target database server
        """
        return pulumi.get(self, "target_db_server_metadata")

    @property
    @pulumi.getter(name="targetDbServerResourceId")
    def target_db_server_resource_id(self) -> str:
        """
        ResourceId of the source database server
        """
        return pulumi.get(self, "target_db_server_resource_id")

    @property
    @pulumi.getter(name="triggerCutover")
    def trigger_cutover(self) -> Optional[str]:
        """
        To trigger cutover for entire migration we need to send this flag as True
        """
        return pulumi.get(self, "trigger_cutover")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetMigrationResult(GetMigrationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMigrationResult(
            cancel=self.cancel,
            current_status=self.current_status,
            dbs_to_cancel_migration_on=self.dbs_to_cancel_migration_on,
            dbs_to_migrate=self.dbs_to_migrate,
            dbs_to_trigger_cutover_on=self.dbs_to_trigger_cutover_on,
            id=self.id,
            location=self.location,
            migrate_roles=self.migrate_roles,
            migration_id=self.migration_id,
            migration_instance_resource_id=self.migration_instance_resource_id,
            migration_mode=self.migration_mode,
            migration_option=self.migration_option,
            migration_window_end_time_in_utc=self.migration_window_end_time_in_utc,
            migration_window_start_time_in_utc=self.migration_window_start_time_in_utc,
            name=self.name,
            overwrite_dbs_in_target=self.overwrite_dbs_in_target,
            setup_logical_replication_on_source_db_if_needed=self.setup_logical_replication_on_source_db_if_needed,
            source_db_server_fully_qualified_domain_name=self.source_db_server_fully_qualified_domain_name,
            source_db_server_metadata=self.source_db_server_metadata,
            source_db_server_resource_id=self.source_db_server_resource_id,
            source_type=self.source_type,
            ssl_mode=self.ssl_mode,
            start_data_migration=self.start_data_migration,
            system_data=self.system_data,
            tags=self.tags,
            target_db_server_fully_qualified_domain_name=self.target_db_server_fully_qualified_domain_name,
            target_db_server_metadata=self.target_db_server_metadata,
            target_db_server_resource_id=self.target_db_server_resource_id,
            trigger_cutover=self.trigger_cutover,
            type=self.type)


def get_migration(migration_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  subscription_id: Optional[str] = None,
                  target_db_server_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMigrationResult:
    """
    Gets details of a migration.


    :param str migration_name: The name of the migration.
    :param str resource_group_name: The resource group name of the target database server.
    :param str subscription_id: The subscription ID of the target database server.
    :param str target_db_server_name: The name of the target database server.
    """
    __args__ = dict()
    __args__['migrationName'] = migration_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['subscriptionId'] = subscription_id
    __args__['targetDbServerName'] = target_db_server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:dbforpostgresql/v20240301preview:getMigration', __args__, opts=opts, typ=GetMigrationResult).value

    return AwaitableGetMigrationResult(
        cancel=pulumi.get(__ret__, 'cancel'),
        current_status=pulumi.get(__ret__, 'current_status'),
        dbs_to_cancel_migration_on=pulumi.get(__ret__, 'dbs_to_cancel_migration_on'),
        dbs_to_migrate=pulumi.get(__ret__, 'dbs_to_migrate'),
        dbs_to_trigger_cutover_on=pulumi.get(__ret__, 'dbs_to_trigger_cutover_on'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        migrate_roles=pulumi.get(__ret__, 'migrate_roles'),
        migration_id=pulumi.get(__ret__, 'migration_id'),
        migration_instance_resource_id=pulumi.get(__ret__, 'migration_instance_resource_id'),
        migration_mode=pulumi.get(__ret__, 'migration_mode'),
        migration_option=pulumi.get(__ret__, 'migration_option'),
        migration_window_end_time_in_utc=pulumi.get(__ret__, 'migration_window_end_time_in_utc'),
        migration_window_start_time_in_utc=pulumi.get(__ret__, 'migration_window_start_time_in_utc'),
        name=pulumi.get(__ret__, 'name'),
        overwrite_dbs_in_target=pulumi.get(__ret__, 'overwrite_dbs_in_target'),
        setup_logical_replication_on_source_db_if_needed=pulumi.get(__ret__, 'setup_logical_replication_on_source_db_if_needed'),
        source_db_server_fully_qualified_domain_name=pulumi.get(__ret__, 'source_db_server_fully_qualified_domain_name'),
        source_db_server_metadata=pulumi.get(__ret__, 'source_db_server_metadata'),
        source_db_server_resource_id=pulumi.get(__ret__, 'source_db_server_resource_id'),
        source_type=pulumi.get(__ret__, 'source_type'),
        ssl_mode=pulumi.get(__ret__, 'ssl_mode'),
        start_data_migration=pulumi.get(__ret__, 'start_data_migration'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        target_db_server_fully_qualified_domain_name=pulumi.get(__ret__, 'target_db_server_fully_qualified_domain_name'),
        target_db_server_metadata=pulumi.get(__ret__, 'target_db_server_metadata'),
        target_db_server_resource_id=pulumi.get(__ret__, 'target_db_server_resource_id'),
        trigger_cutover=pulumi.get(__ret__, 'trigger_cutover'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_migration)
def get_migration_output(migration_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         subscription_id: Optional[pulumi.Input[Optional[str]]] = None,
                         target_db_server_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMigrationResult]:
    """
    Gets details of a migration.


    :param str migration_name: The name of the migration.
    :param str resource_group_name: The resource group name of the target database server.
    :param str subscription_id: The subscription ID of the target database server.
    :param str target_db_server_name: The name of the target database server.
    """
    ...
