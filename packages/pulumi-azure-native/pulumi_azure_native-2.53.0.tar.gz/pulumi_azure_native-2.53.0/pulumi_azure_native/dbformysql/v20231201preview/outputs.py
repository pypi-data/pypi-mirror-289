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

__all__ = [
    'BackupResponse',
    'DataEncryptionResponse',
    'HighAvailabilityResponse',
    'ImportSourcePropertiesResponse',
    'MaintenanceWindowResponse',
    'MySQLServerIdentityResponse',
    'MySQLServerSkuResponse',
    'NetworkResponse',
    'PrivateEndpointConnectionResponse',
    'PrivateEndpointResponse',
    'PrivateLinkServiceConnectionStateResponse',
    'StorageResponse',
    'SystemDataResponse',
    'UserAssignedIdentityResponse',
]

@pulumi.output_type
class BackupResponse(dict):
    """
    Storage Profile properties of a server
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "earliestRestoreDate":
            suggest = "earliest_restore_date"
        elif key == "backupIntervalHours":
            suggest = "backup_interval_hours"
        elif key == "backupRetentionDays":
            suggest = "backup_retention_days"
        elif key == "geoRedundantBackup":
            suggest = "geo_redundant_backup"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BackupResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BackupResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BackupResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 earliest_restore_date: str,
                 backup_interval_hours: Optional[int] = None,
                 backup_retention_days: Optional[int] = None,
                 geo_redundant_backup: Optional[str] = None):
        """
        Storage Profile properties of a server
        :param str earliest_restore_date: Earliest restore point creation time (ISO8601 format)
        :param int backup_interval_hours: Backup interval hours for the server.
        :param int backup_retention_days: Backup retention days for the server.
        :param str geo_redundant_backup: Whether or not geo redundant backup is enabled.
        """
        pulumi.set(__self__, "earliest_restore_date", earliest_restore_date)
        if backup_interval_hours is not None:
            pulumi.set(__self__, "backup_interval_hours", backup_interval_hours)
        if backup_retention_days is not None:
            pulumi.set(__self__, "backup_retention_days", backup_retention_days)
        if geo_redundant_backup is None:
            geo_redundant_backup = 'Disabled'
        if geo_redundant_backup is not None:
            pulumi.set(__self__, "geo_redundant_backup", geo_redundant_backup)

    @property
    @pulumi.getter(name="earliestRestoreDate")
    def earliest_restore_date(self) -> str:
        """
        Earliest restore point creation time (ISO8601 format)
        """
        return pulumi.get(self, "earliest_restore_date")

    @property
    @pulumi.getter(name="backupIntervalHours")
    def backup_interval_hours(self) -> Optional[int]:
        """
        Backup interval hours for the server.
        """
        return pulumi.get(self, "backup_interval_hours")

    @property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> Optional[int]:
        """
        Backup retention days for the server.
        """
        return pulumi.get(self, "backup_retention_days")

    @property
    @pulumi.getter(name="geoRedundantBackup")
    def geo_redundant_backup(self) -> Optional[str]:
        """
        Whether or not geo redundant backup is enabled.
        """
        return pulumi.get(self, "geo_redundant_backup")


@pulumi.output_type
class DataEncryptionResponse(dict):
    """
    The date encryption for cmk.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "geoBackupKeyURI":
            suggest = "geo_backup_key_uri"
        elif key == "geoBackupUserAssignedIdentityId":
            suggest = "geo_backup_user_assigned_identity_id"
        elif key == "primaryKeyURI":
            suggest = "primary_key_uri"
        elif key == "primaryUserAssignedIdentityId":
            suggest = "primary_user_assigned_identity_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DataEncryptionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DataEncryptionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DataEncryptionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 geo_backup_key_uri: Optional[str] = None,
                 geo_backup_user_assigned_identity_id: Optional[str] = None,
                 primary_key_uri: Optional[str] = None,
                 primary_user_assigned_identity_id: Optional[str] = None,
                 type: Optional[str] = None):
        """
        The date encryption for cmk.
        :param str geo_backup_key_uri: Geo backup key uri as key vault can't cross region, need cmk in same region as geo backup
        :param str geo_backup_user_assigned_identity_id: Geo backup user identity resource id as identity can't cross region, need identity in same region as geo backup
        :param str primary_key_uri: Primary key uri
        :param str primary_user_assigned_identity_id: Primary user identity resource id
        :param str type: The key type, AzureKeyVault for enable cmk, SystemManaged for disable cmk.
        """
        if geo_backup_key_uri is not None:
            pulumi.set(__self__, "geo_backup_key_uri", geo_backup_key_uri)
        if geo_backup_user_assigned_identity_id is not None:
            pulumi.set(__self__, "geo_backup_user_assigned_identity_id", geo_backup_user_assigned_identity_id)
        if primary_key_uri is not None:
            pulumi.set(__self__, "primary_key_uri", primary_key_uri)
        if primary_user_assigned_identity_id is not None:
            pulumi.set(__self__, "primary_user_assigned_identity_id", primary_user_assigned_identity_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="geoBackupKeyURI")
    def geo_backup_key_uri(self) -> Optional[str]:
        """
        Geo backup key uri as key vault can't cross region, need cmk in same region as geo backup
        """
        return pulumi.get(self, "geo_backup_key_uri")

    @property
    @pulumi.getter(name="geoBackupUserAssignedIdentityId")
    def geo_backup_user_assigned_identity_id(self) -> Optional[str]:
        """
        Geo backup user identity resource id as identity can't cross region, need identity in same region as geo backup
        """
        return pulumi.get(self, "geo_backup_user_assigned_identity_id")

    @property
    @pulumi.getter(name="primaryKeyURI")
    def primary_key_uri(self) -> Optional[str]:
        """
        Primary key uri
        """
        return pulumi.get(self, "primary_key_uri")

    @property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(self) -> Optional[str]:
        """
        Primary user identity resource id
        """
        return pulumi.get(self, "primary_user_assigned_identity_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The key type, AzureKeyVault for enable cmk, SystemManaged for disable cmk.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class HighAvailabilityResponse(dict):
    """
    High availability properties of a server
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "standbyAvailabilityZone":
            suggest = "standby_availability_zone"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HighAvailabilityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HighAvailabilityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HighAvailabilityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 state: str,
                 mode: Optional[str] = None,
                 standby_availability_zone: Optional[str] = None):
        """
        High availability properties of a server
        :param str state: The state of server high availability.
        :param str mode: High availability mode for a server.
        :param str standby_availability_zone: Availability zone of the standby server.
        """
        pulumi.set(__self__, "state", state)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if standby_availability_zone is not None:
            pulumi.set(__self__, "standby_availability_zone", standby_availability_zone)

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of server high availability.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def mode(self) -> Optional[str]:
        """
        High availability mode for a server.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter(name="standbyAvailabilityZone")
    def standby_availability_zone(self) -> Optional[str]:
        """
        Availability zone of the standby server.
        """
        return pulumi.get(self, "standby_availability_zone")


@pulumi.output_type
class ImportSourcePropertiesResponse(dict):
    """
    Import source related properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dataDirPath":
            suggest = "data_dir_path"
        elif key == "storageType":
            suggest = "storage_type"
        elif key == "storageUrl":
            suggest = "storage_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ImportSourcePropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ImportSourcePropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ImportSourcePropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 data_dir_path: Optional[str] = None,
                 storage_type: Optional[str] = None,
                 storage_url: Optional[str] = None):
        """
        Import source related properties.
        :param str data_dir_path: Relative path of data directory in storage.
        :param str storage_type: Storage type of import source.
        :param str storage_url: Uri of the import source storage.
        """
        if data_dir_path is not None:
            pulumi.set(__self__, "data_dir_path", data_dir_path)
        if storage_type is not None:
            pulumi.set(__self__, "storage_type", storage_type)
        if storage_url is not None:
            pulumi.set(__self__, "storage_url", storage_url)

    @property
    @pulumi.getter(name="dataDirPath")
    def data_dir_path(self) -> Optional[str]:
        """
        Relative path of data directory in storage.
        """
        return pulumi.get(self, "data_dir_path")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[str]:
        """
        Storage type of import source.
        """
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter(name="storageUrl")
    def storage_url(self) -> Optional[str]:
        """
        Uri of the import source storage.
        """
        return pulumi.get(self, "storage_url")


@pulumi.output_type
class MaintenanceWindowResponse(dict):
    """
    Maintenance window of a server.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "customWindow":
            suggest = "custom_window"
        elif key == "dayOfWeek":
            suggest = "day_of_week"
        elif key == "startHour":
            suggest = "start_hour"
        elif key == "startMinute":
            suggest = "start_minute"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MaintenanceWindowResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MaintenanceWindowResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MaintenanceWindowResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 custom_window: Optional[str] = None,
                 day_of_week: Optional[int] = None,
                 start_hour: Optional[int] = None,
                 start_minute: Optional[int] = None):
        """
        Maintenance window of a server.
        :param str custom_window: indicates whether custom window is enabled or disabled
        :param int day_of_week: day of week for maintenance window
        :param int start_hour: start hour for maintenance window
        :param int start_minute: start minute for maintenance window
        """
        if custom_window is not None:
            pulumi.set(__self__, "custom_window", custom_window)
        if day_of_week is not None:
            pulumi.set(__self__, "day_of_week", day_of_week)
        if start_hour is not None:
            pulumi.set(__self__, "start_hour", start_hour)
        if start_minute is not None:
            pulumi.set(__self__, "start_minute", start_minute)

    @property
    @pulumi.getter(name="customWindow")
    def custom_window(self) -> Optional[str]:
        """
        indicates whether custom window is enabled or disabled
        """
        return pulumi.get(self, "custom_window")

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[int]:
        """
        day of week for maintenance window
        """
        return pulumi.get(self, "day_of_week")

    @property
    @pulumi.getter(name="startHour")
    def start_hour(self) -> Optional[int]:
        """
        start hour for maintenance window
        """
        return pulumi.get(self, "start_hour")

    @property
    @pulumi.getter(name="startMinute")
    def start_minute(self) -> Optional[int]:
        """
        start minute for maintenance window
        """
        return pulumi.get(self, "start_minute")


@pulumi.output_type
class MySQLServerIdentityResponse(dict):
    """
    Properties to configure Identity for Bring your Own Keys
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"
        elif key == "userAssignedIdentities":
            suggest = "user_assigned_identities"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MySQLServerIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MySQLServerIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MySQLServerIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None,
                 user_assigned_identities: Optional[Mapping[str, Sequence['outputs.UserAssignedIdentityResponse']]] = None):
        """
        Properties to configure Identity for Bring your Own Keys
        :param str principal_id: ObjectId from the KeyVault
        :param str tenant_id: TenantId from the KeyVault
        :param str type: Type of managed service identity.
        :param Mapping[str, Sequence['UserAssignedIdentityResponse']] user_assigned_identities: Metadata of user assigned identity.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        ObjectId from the KeyVault
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        TenantId from the KeyVault
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Type of managed service identity.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, Sequence['outputs.UserAssignedIdentityResponse']]]:
        """
        Metadata of user assigned identity.
        """
        return pulumi.get(self, "user_assigned_identities")


@pulumi.output_type
class MySQLServerSkuResponse(dict):
    """
    Billing information related properties of a server.
    """
    def __init__(__self__, *,
                 name: str,
                 tier: str):
        """
        Billing information related properties of a server.
        :param str name: The name of the sku, e.g. Standard_D32s_v3.
        :param str tier: The tier of the particular SKU, e.g. GeneralPurpose.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the sku, e.g. Standard_D32s_v3.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tier(self) -> str:
        """
        The tier of the particular SKU, e.g. GeneralPurpose.
        """
        return pulumi.get(self, "tier")


@pulumi.output_type
class NetworkResponse(dict):
    """
    Network related properties of a server
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "delegatedSubnetResourceId":
            suggest = "delegated_subnet_resource_id"
        elif key == "privateDnsZoneResourceId":
            suggest = "private_dns_zone_resource_id"
        elif key == "publicNetworkAccess":
            suggest = "public_network_access"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NetworkResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NetworkResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NetworkResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 delegated_subnet_resource_id: Optional[str] = None,
                 private_dns_zone_resource_id: Optional[str] = None,
                 public_network_access: Optional[str] = None):
        """
        Network related properties of a server
        :param str delegated_subnet_resource_id: Delegated subnet resource id used to setup vnet for a server.
        :param str private_dns_zone_resource_id: Private DNS zone resource id.
        :param str public_network_access: Whether or not public network access is allowed for this server. Value is 'Disabled' when server has VNet integration.
        """
        if delegated_subnet_resource_id is not None:
            pulumi.set(__self__, "delegated_subnet_resource_id", delegated_subnet_resource_id)
        if private_dns_zone_resource_id is not None:
            pulumi.set(__self__, "private_dns_zone_resource_id", private_dns_zone_resource_id)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)

    @property
    @pulumi.getter(name="delegatedSubnetResourceId")
    def delegated_subnet_resource_id(self) -> Optional[str]:
        """
        Delegated subnet resource id used to setup vnet for a server.
        """
        return pulumi.get(self, "delegated_subnet_resource_id")

    @property
    @pulumi.getter(name="privateDnsZoneResourceId")
    def private_dns_zone_resource_id(self) -> Optional[str]:
        """
        Private DNS zone resource id.
        """
        return pulumi.get(self, "private_dns_zone_resource_id")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Whether or not public network access is allowed for this server. Value is 'Disabled' when server has VNet integration.
        """
        return pulumi.get(self, "public_network_access")


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    """
    The private endpoint connection resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "groupIds":
            suggest = "group_ids"
        elif key == "privateLinkServiceConnectionState":
            suggest = "private_link_service_connection_state"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "systemData":
            suggest = "system_data"
        elif key == "privateEndpoint":
            suggest = "private_endpoint"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateEndpointConnectionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 group_ids: Sequence[str],
                 id: str,
                 name: str,
                 private_link_service_connection_state: 'outputs.PrivateLinkServiceConnectionStateResponse',
                 provisioning_state: str,
                 system_data: 'outputs.SystemDataResponse',
                 type: str,
                 private_endpoint: Optional['outputs.PrivateEndpointResponse'] = None):
        """
        The private endpoint connection resource.
        :param Sequence[str] group_ids: The group ids for the private endpoint resource.
        :param str id: Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        :param str name: The name of the resource
        :param 'PrivateLinkServiceConnectionStateResponse' private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        :param str provisioning_state: The provisioning state of the private endpoint connection resource.
        :param 'SystemDataResponse' system_data: Azure Resource Manager metadata containing createdBy and modifiedBy information.
        :param str type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        :param 'PrivateEndpointResponse' private_endpoint: The private endpoint resource.
        """
        pulumi.set(__self__, "group_ids", group_ids)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "system_data", system_data)
        pulumi.set(__self__, "type", type)
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)

    @property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Sequence[str]:
        """
        The group ids for the private endpoint resource.
        """
        return pulumi.get(self, "group_ids")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> 'outputs.PrivateLinkServiceConnectionStateResponse':
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the private endpoint connection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional['outputs.PrivateEndpointResponse']:
        """
        The private endpoint resource.
        """
        return pulumi.get(self, "private_endpoint")


@pulumi.output_type
class PrivateEndpointResponse(dict):
    """
    The private endpoint resource.
    """
    def __init__(__self__, *,
                 id: str):
        """
        The private endpoint resource.
        :param str id: The ARM identifier for private endpoint.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ARM identifier for private endpoint.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    """
    A collection of information about the state of the connection between service consumer and provider.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionsRequired":
            suggest = "actions_required"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateLinkServiceConnectionStateResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 actions_required: Optional[str] = None,
                 description: Optional[str] = None,
                 status: Optional[str] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param str actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param str description: The reason for approval/rejection of the connection.
        :param str status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[str]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class StorageResponse(dict):
    """
    Storage Profile properties of a server
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "storageSku":
            suggest = "storage_sku"
        elif key == "autoGrow":
            suggest = "auto_grow"
        elif key == "autoIoScaling":
            suggest = "auto_io_scaling"
        elif key == "logOnDisk":
            suggest = "log_on_disk"
        elif key == "storageSizeGB":
            suggest = "storage_size_gb"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StorageResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StorageResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StorageResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 storage_sku: str,
                 auto_grow: Optional[str] = None,
                 auto_io_scaling: Optional[str] = None,
                 iops: Optional[int] = None,
                 log_on_disk: Optional[str] = None,
                 storage_size_gb: Optional[int] = None):
        """
        Storage Profile properties of a server
        :param str storage_sku: The sku name of the server storage.
        :param str auto_grow: Enable Storage Auto Grow or not.
        :param str auto_io_scaling: Enable IO Auto Scaling or not.
        :param int iops: Storage IOPS for a server.
        :param str log_on_disk: Enable Log On Disk or not.
        :param int storage_size_gb: Max storage size allowed for a server.
        """
        pulumi.set(__self__, "storage_sku", storage_sku)
        if auto_grow is None:
            auto_grow = 'Disabled'
        if auto_grow is not None:
            pulumi.set(__self__, "auto_grow", auto_grow)
        if auto_io_scaling is None:
            auto_io_scaling = 'Enabled'
        if auto_io_scaling is not None:
            pulumi.set(__self__, "auto_io_scaling", auto_io_scaling)
        if iops is not None:
            pulumi.set(__self__, "iops", iops)
        if log_on_disk is None:
            log_on_disk = 'Disabled'
        if log_on_disk is not None:
            pulumi.set(__self__, "log_on_disk", log_on_disk)
        if storage_size_gb is not None:
            pulumi.set(__self__, "storage_size_gb", storage_size_gb)

    @property
    @pulumi.getter(name="storageSku")
    def storage_sku(self) -> str:
        """
        The sku name of the server storage.
        """
        return pulumi.get(self, "storage_sku")

    @property
    @pulumi.getter(name="autoGrow")
    def auto_grow(self) -> Optional[str]:
        """
        Enable Storage Auto Grow or not.
        """
        return pulumi.get(self, "auto_grow")

    @property
    @pulumi.getter(name="autoIoScaling")
    def auto_io_scaling(self) -> Optional[str]:
        """
        Enable IO Auto Scaling or not.
        """
        return pulumi.get(self, "auto_io_scaling")

    @property
    @pulumi.getter
    def iops(self) -> Optional[int]:
        """
        Storage IOPS for a server.
        """
        return pulumi.get(self, "iops")

    @property
    @pulumi.getter(name="logOnDisk")
    def log_on_disk(self) -> Optional[str]:
        """
        Enable Log On Disk or not.
        """
        return pulumi.get(self, "log_on_disk")

    @property
    @pulumi.getter(name="storageSizeGB")
    def storage_size_gb(self) -> Optional[int]:
        """
        Max storage size allowed for a server.
        """
        return pulumi.get(self, "storage_size_gb")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    """
    Metadata of user assigned identity.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientId":
            suggest = "client_id"
        elif key == "principalId":
            suggest = "principal_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserAssignedIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserAssignedIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserAssignedIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_id: str,
                 principal_id: str):
        """
        Metadata of user assigned identity.
        :param str client_id: Client Id of user assigned identity
        :param str principal_id: Principal Id of user assigned identity
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "principal_id", principal_id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        Client Id of user assigned identity
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        Principal Id of user assigned identity
        """
        return pulumi.get(self, "principal_id")


