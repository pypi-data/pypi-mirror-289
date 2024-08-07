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

__all__ = [
    'BackupArgs',
    'BackupArgsDict',
    'DataEncryptionArgs',
    'DataEncryptionArgsDict',
    'HighAvailabilityArgs',
    'HighAvailabilityArgsDict',
    'IdentityArgs',
    'IdentityArgsDict',
    'MaintenanceWindowArgs',
    'MaintenanceWindowArgsDict',
    'NetworkArgs',
    'NetworkArgsDict',
    'SkuArgs',
    'SkuArgsDict',
    'StorageArgs',
    'StorageArgsDict',
]

MYPY = False

if not MYPY:
    class BackupArgsDict(TypedDict):
        """
        Storage Profile properties of a server
        """
        backup_retention_days: NotRequired[pulumi.Input[int]]
        """
        Backup retention days for the server.
        """
        geo_redundant_backup: NotRequired[pulumi.Input[Union[str, 'EnableStatusEnum']]]
        """
        Whether or not geo redundant backup is enabled.
        """
elif False:
    BackupArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class BackupArgs:
    def __init__(__self__, *,
                 backup_retention_days: Optional[pulumi.Input[int]] = None,
                 geo_redundant_backup: Optional[pulumi.Input[Union[str, 'EnableStatusEnum']]] = None):
        """
        Storage Profile properties of a server
        :param pulumi.Input[int] backup_retention_days: Backup retention days for the server.
        :param pulumi.Input[Union[str, 'EnableStatusEnum']] geo_redundant_backup: Whether or not geo redundant backup is enabled.
        """
        if backup_retention_days is not None:
            pulumi.set(__self__, "backup_retention_days", backup_retention_days)
        if geo_redundant_backup is None:
            geo_redundant_backup = 'Disabled'
        if geo_redundant_backup is not None:
            pulumi.set(__self__, "geo_redundant_backup", geo_redundant_backup)

    @property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> Optional[pulumi.Input[int]]:
        """
        Backup retention days for the server.
        """
        return pulumi.get(self, "backup_retention_days")

    @backup_retention_days.setter
    def backup_retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "backup_retention_days", value)

    @property
    @pulumi.getter(name="geoRedundantBackup")
    def geo_redundant_backup(self) -> Optional[pulumi.Input[Union[str, 'EnableStatusEnum']]]:
        """
        Whether or not geo redundant backup is enabled.
        """
        return pulumi.get(self, "geo_redundant_backup")

    @geo_redundant_backup.setter
    def geo_redundant_backup(self, value: Optional[pulumi.Input[Union[str, 'EnableStatusEnum']]]):
        pulumi.set(self, "geo_redundant_backup", value)


if not MYPY:
    class DataEncryptionArgsDict(TypedDict):
        """
        The date encryption for cmk.
        """
        geo_backup_key_uri: NotRequired[pulumi.Input[str]]
        """
        Geo backup key uri as key vault can't cross region, need cmk in same region as geo backup
        """
        geo_backup_user_assigned_identity_id: NotRequired[pulumi.Input[str]]
        """
        Geo backup user identity resource id as identity can't cross region, need identity in same region as geo backup
        """
        primary_key_uri: NotRequired[pulumi.Input[str]]
        """
        Primary key uri
        """
        primary_user_assigned_identity_id: NotRequired[pulumi.Input[str]]
        """
        Primary user identity resource id
        """
        type: NotRequired[pulumi.Input['DataEncryptionType']]
        """
        The key type, AzureKeyVault for enable cmk, SystemManaged for disable cmk.
        """
elif False:
    DataEncryptionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DataEncryptionArgs:
    def __init__(__self__, *,
                 geo_backup_key_uri: Optional[pulumi.Input[str]] = None,
                 geo_backup_user_assigned_identity_id: Optional[pulumi.Input[str]] = None,
                 primary_key_uri: Optional[pulumi.Input[str]] = None,
                 primary_user_assigned_identity_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input['DataEncryptionType']] = None):
        """
        The date encryption for cmk.
        :param pulumi.Input[str] geo_backup_key_uri: Geo backup key uri as key vault can't cross region, need cmk in same region as geo backup
        :param pulumi.Input[str] geo_backup_user_assigned_identity_id: Geo backup user identity resource id as identity can't cross region, need identity in same region as geo backup
        :param pulumi.Input[str] primary_key_uri: Primary key uri
        :param pulumi.Input[str] primary_user_assigned_identity_id: Primary user identity resource id
        :param pulumi.Input['DataEncryptionType'] type: The key type, AzureKeyVault for enable cmk, SystemManaged for disable cmk.
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
    def geo_backup_key_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Geo backup key uri as key vault can't cross region, need cmk in same region as geo backup
        """
        return pulumi.get(self, "geo_backup_key_uri")

    @geo_backup_key_uri.setter
    def geo_backup_key_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "geo_backup_key_uri", value)

    @property
    @pulumi.getter(name="geoBackupUserAssignedIdentityId")
    def geo_backup_user_assigned_identity_id(self) -> Optional[pulumi.Input[str]]:
        """
        Geo backup user identity resource id as identity can't cross region, need identity in same region as geo backup
        """
        return pulumi.get(self, "geo_backup_user_assigned_identity_id")

    @geo_backup_user_assigned_identity_id.setter
    def geo_backup_user_assigned_identity_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "geo_backup_user_assigned_identity_id", value)

    @property
    @pulumi.getter(name="primaryKeyURI")
    def primary_key_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Primary key uri
        """
        return pulumi.get(self, "primary_key_uri")

    @primary_key_uri.setter
    def primary_key_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary_key_uri", value)

    @property
    @pulumi.getter(name="primaryUserAssignedIdentityId")
    def primary_user_assigned_identity_id(self) -> Optional[pulumi.Input[str]]:
        """
        Primary user identity resource id
        """
        return pulumi.get(self, "primary_user_assigned_identity_id")

    @primary_user_assigned_identity_id.setter
    def primary_user_assigned_identity_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "primary_user_assigned_identity_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['DataEncryptionType']]:
        """
        The key type, AzureKeyVault for enable cmk, SystemManaged for disable cmk.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['DataEncryptionType']]):
        pulumi.set(self, "type", value)


if not MYPY:
    class HighAvailabilityArgsDict(TypedDict):
        """
        Network related properties of a server
        """
        mode: NotRequired[pulumi.Input[Union[str, 'HighAvailabilityMode']]]
        """
        High availability mode for a server.
        """
        standby_availability_zone: NotRequired[pulumi.Input[str]]
        """
        Availability zone of the standby server.
        """
elif False:
    HighAvailabilityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class HighAvailabilityArgs:
    def __init__(__self__, *,
                 mode: Optional[pulumi.Input[Union[str, 'HighAvailabilityMode']]] = None,
                 standby_availability_zone: Optional[pulumi.Input[str]] = None):
        """
        Network related properties of a server
        :param pulumi.Input[Union[str, 'HighAvailabilityMode']] mode: High availability mode for a server.
        :param pulumi.Input[str] standby_availability_zone: Availability zone of the standby server.
        """
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if standby_availability_zone is not None:
            pulumi.set(__self__, "standby_availability_zone", standby_availability_zone)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[Union[str, 'HighAvailabilityMode']]]:
        """
        High availability mode for a server.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[Union[str, 'HighAvailabilityMode']]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter(name="standbyAvailabilityZone")
    def standby_availability_zone(self) -> Optional[pulumi.Input[str]]:
        """
        Availability zone of the standby server.
        """
        return pulumi.get(self, "standby_availability_zone")

    @standby_availability_zone.setter
    def standby_availability_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "standby_availability_zone", value)


if not MYPY:
    class IdentityArgsDict(TypedDict):
        """
        Properties to configure Identity for Bring your Own Keys
        """
        type: NotRequired[pulumi.Input['ManagedServiceIdentityType']]
        """
        Type of managed service identity.
        """
        user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        Metadata of user assigned identity.
        """
elif False:
    IdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input['ManagedServiceIdentityType']] = None,
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Properties to configure Identity for Bring your Own Keys
        :param pulumi.Input['ManagedServiceIdentityType'] type: Type of managed service identity.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: Metadata of user assigned identity.
        """
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['ManagedServiceIdentityType']]:
        """
        Type of managed service identity.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['ManagedServiceIdentityType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Metadata of user assigned identity.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


if not MYPY:
    class MaintenanceWindowArgsDict(TypedDict):
        """
        Maintenance window of a server.
        """
        custom_window: NotRequired[pulumi.Input[str]]
        """
        indicates whether custom window is enabled or disabled
        """
        day_of_week: NotRequired[pulumi.Input[int]]
        """
        day of week for maintenance window
        """
        start_hour: NotRequired[pulumi.Input[int]]
        """
        start hour for maintenance window
        """
        start_minute: NotRequired[pulumi.Input[int]]
        """
        start minute for maintenance window
        """
elif False:
    MaintenanceWindowArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MaintenanceWindowArgs:
    def __init__(__self__, *,
                 custom_window: Optional[pulumi.Input[str]] = None,
                 day_of_week: Optional[pulumi.Input[int]] = None,
                 start_hour: Optional[pulumi.Input[int]] = None,
                 start_minute: Optional[pulumi.Input[int]] = None):
        """
        Maintenance window of a server.
        :param pulumi.Input[str] custom_window: indicates whether custom window is enabled or disabled
        :param pulumi.Input[int] day_of_week: day of week for maintenance window
        :param pulumi.Input[int] start_hour: start hour for maintenance window
        :param pulumi.Input[int] start_minute: start minute for maintenance window
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
    def custom_window(self) -> Optional[pulumi.Input[str]]:
        """
        indicates whether custom window is enabled or disabled
        """
        return pulumi.get(self, "custom_window")

    @custom_window.setter
    def custom_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_window", value)

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[pulumi.Input[int]]:
        """
        day of week for maintenance window
        """
        return pulumi.get(self, "day_of_week")

    @day_of_week.setter
    def day_of_week(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "day_of_week", value)

    @property
    @pulumi.getter(name="startHour")
    def start_hour(self) -> Optional[pulumi.Input[int]]:
        """
        start hour for maintenance window
        """
        return pulumi.get(self, "start_hour")

    @start_hour.setter
    def start_hour(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "start_hour", value)

    @property
    @pulumi.getter(name="startMinute")
    def start_minute(self) -> Optional[pulumi.Input[int]]:
        """
        start minute for maintenance window
        """
        return pulumi.get(self, "start_minute")

    @start_minute.setter
    def start_minute(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "start_minute", value)


if not MYPY:
    class NetworkArgsDict(TypedDict):
        """
        Network related properties of a server
        """
        delegated_subnet_resource_id: NotRequired[pulumi.Input[str]]
        """
        Delegated subnet resource id used to setup vnet for a server.
        """
        private_dns_zone_resource_id: NotRequired[pulumi.Input[str]]
        """
        Private DNS zone resource id.
        """
elif False:
    NetworkArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class NetworkArgs:
    def __init__(__self__, *,
                 delegated_subnet_resource_id: Optional[pulumi.Input[str]] = None,
                 private_dns_zone_resource_id: Optional[pulumi.Input[str]] = None):
        """
        Network related properties of a server
        :param pulumi.Input[str] delegated_subnet_resource_id: Delegated subnet resource id used to setup vnet for a server.
        :param pulumi.Input[str] private_dns_zone_resource_id: Private DNS zone resource id.
        """
        if delegated_subnet_resource_id is not None:
            pulumi.set(__self__, "delegated_subnet_resource_id", delegated_subnet_resource_id)
        if private_dns_zone_resource_id is not None:
            pulumi.set(__self__, "private_dns_zone_resource_id", private_dns_zone_resource_id)

    @property
    @pulumi.getter(name="delegatedSubnetResourceId")
    def delegated_subnet_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Delegated subnet resource id used to setup vnet for a server.
        """
        return pulumi.get(self, "delegated_subnet_resource_id")

    @delegated_subnet_resource_id.setter
    def delegated_subnet_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delegated_subnet_resource_id", value)

    @property
    @pulumi.getter(name="privateDnsZoneResourceId")
    def private_dns_zone_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Private DNS zone resource id.
        """
        return pulumi.get(self, "private_dns_zone_resource_id")

    @private_dns_zone_resource_id.setter
    def private_dns_zone_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_dns_zone_resource_id", value)


if not MYPY:
    class SkuArgsDict(TypedDict):
        """
        Billing information related properties of a server.
        """
        name: pulumi.Input[str]
        """
        The name of the sku, e.g. Standard_D32s_v3.
        """
        tier: pulumi.Input[Union[str, 'SkuTier']]
        """
        The tier of the particular SKU, e.g. GeneralPurpose.
        """
elif False:
    SkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 tier: pulumi.Input[Union[str, 'SkuTier']]):
        """
        Billing information related properties of a server.
        :param pulumi.Input[str] name: The name of the sku, e.g. Standard_D32s_v3.
        :param pulumi.Input[Union[str, 'SkuTier']] tier: The tier of the particular SKU, e.g. GeneralPurpose.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the sku, e.g. Standard_D32s_v3.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Input[Union[str, 'SkuTier']]:
        """
        The tier of the particular SKU, e.g. GeneralPurpose.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: pulumi.Input[Union[str, 'SkuTier']]):
        pulumi.set(self, "tier", value)


if not MYPY:
    class StorageArgsDict(TypedDict):
        """
        Storage Profile properties of a server
        """
        auto_grow: NotRequired[pulumi.Input[Union[str, 'EnableStatusEnum']]]
        """
        Enable Storage Auto Grow or not.
        """
        auto_io_scaling: NotRequired[pulumi.Input[Union[str, 'EnableStatusEnum']]]
        """
        Enable IO Auto Scaling or not.
        """
        iops: NotRequired[pulumi.Input[int]]
        """
        Storage IOPS for a server.
        """
        log_on_disk: NotRequired[pulumi.Input[Union[str, 'EnableStatusEnum']]]
        """
        Enable Log On Disk or not.
        """
        storage_size_gb: NotRequired[pulumi.Input[int]]
        """
        Max storage size allowed for a server.
        """
elif False:
    StorageArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class StorageArgs:
    def __init__(__self__, *,
                 auto_grow: Optional[pulumi.Input[Union[str, 'EnableStatusEnum']]] = None,
                 auto_io_scaling: Optional[pulumi.Input[Union[str, 'EnableStatusEnum']]] = None,
                 iops: Optional[pulumi.Input[int]] = None,
                 log_on_disk: Optional[pulumi.Input[Union[str, 'EnableStatusEnum']]] = None,
                 storage_size_gb: Optional[pulumi.Input[int]] = None):
        """
        Storage Profile properties of a server
        :param pulumi.Input[Union[str, 'EnableStatusEnum']] auto_grow: Enable Storage Auto Grow or not.
        :param pulumi.Input[Union[str, 'EnableStatusEnum']] auto_io_scaling: Enable IO Auto Scaling or not.
        :param pulumi.Input[int] iops: Storage IOPS for a server.
        :param pulumi.Input[Union[str, 'EnableStatusEnum']] log_on_disk: Enable Log On Disk or not.
        :param pulumi.Input[int] storage_size_gb: Max storage size allowed for a server.
        """
        if auto_grow is None:
            auto_grow = 'Disabled'
        if auto_grow is not None:
            pulumi.set(__self__, "auto_grow", auto_grow)
        if auto_io_scaling is None:
            auto_io_scaling = 'Disabled'
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
    @pulumi.getter(name="autoGrow")
    def auto_grow(self) -> Optional[pulumi.Input[Union[str, 'EnableStatusEnum']]]:
        """
        Enable Storage Auto Grow or not.
        """
        return pulumi.get(self, "auto_grow")

    @auto_grow.setter
    def auto_grow(self, value: Optional[pulumi.Input[Union[str, 'EnableStatusEnum']]]):
        pulumi.set(self, "auto_grow", value)

    @property
    @pulumi.getter(name="autoIoScaling")
    def auto_io_scaling(self) -> Optional[pulumi.Input[Union[str, 'EnableStatusEnum']]]:
        """
        Enable IO Auto Scaling or not.
        """
        return pulumi.get(self, "auto_io_scaling")

    @auto_io_scaling.setter
    def auto_io_scaling(self, value: Optional[pulumi.Input[Union[str, 'EnableStatusEnum']]]):
        pulumi.set(self, "auto_io_scaling", value)

    @property
    @pulumi.getter
    def iops(self) -> Optional[pulumi.Input[int]]:
        """
        Storage IOPS for a server.
        """
        return pulumi.get(self, "iops")

    @iops.setter
    def iops(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "iops", value)

    @property
    @pulumi.getter(name="logOnDisk")
    def log_on_disk(self) -> Optional[pulumi.Input[Union[str, 'EnableStatusEnum']]]:
        """
        Enable Log On Disk or not.
        """
        return pulumi.get(self, "log_on_disk")

    @log_on_disk.setter
    def log_on_disk(self, value: Optional[pulumi.Input[Union[str, 'EnableStatusEnum']]]):
        pulumi.set(self, "log_on_disk", value)

    @property
    @pulumi.getter(name="storageSizeGB")
    def storage_size_gb(self) -> Optional[pulumi.Input[int]]:
        """
        Max storage size allowed for a server.
        """
        return pulumi.get(self, "storage_size_gb")

    @storage_size_gb.setter
    def storage_size_gb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "storage_size_gb", value)


