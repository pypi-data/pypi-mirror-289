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
    'IdentityArgs',
    'IdentityArgsDict',
    'MaintenanceWindowArgs',
    'MaintenanceWindowArgsDict',
    'ServerPropertiesDelegatedSubnetArgumentsArgs',
    'ServerPropertiesDelegatedSubnetArgumentsArgsDict',
    'ServerPropertiesPrivateDnsZoneArgumentsArgs',
    'ServerPropertiesPrivateDnsZoneArgumentsArgsDict',
    'SkuArgs',
    'SkuArgsDict',
    'StorageProfileArgs',
    'StorageProfileArgsDict',
]

MYPY = False

if not MYPY:
    class IdentityArgsDict(TypedDict):
        """
        Identity for the resource.
        """
        type: NotRequired[pulumi.Input['ResourceIdentityType']]
        """
        The identity type.
        """
elif False:
    IdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input['ResourceIdentityType']] = None):
        """
        Identity for the resource.
        :param pulumi.Input['ResourceIdentityType'] type: The identity type.
        """
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['ResourceIdentityType']]:
        """
        The identity type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['ResourceIdentityType']]):
        pulumi.set(self, "type", value)


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
    class ServerPropertiesDelegatedSubnetArgumentsArgsDict(TypedDict):
        subnet_arm_resource_id: NotRequired[pulumi.Input[str]]
        """
        delegated subnet arm resource id.
        """
elif False:
    ServerPropertiesDelegatedSubnetArgumentsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerPropertiesDelegatedSubnetArgumentsArgs:
    def __init__(__self__, *,
                 subnet_arm_resource_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] subnet_arm_resource_id: delegated subnet arm resource id.
        """
        if subnet_arm_resource_id is not None:
            pulumi.set(__self__, "subnet_arm_resource_id", subnet_arm_resource_id)

    @property
    @pulumi.getter(name="subnetArmResourceId")
    def subnet_arm_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        delegated subnet arm resource id.
        """
        return pulumi.get(self, "subnet_arm_resource_id")

    @subnet_arm_resource_id.setter
    def subnet_arm_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subnet_arm_resource_id", value)


if not MYPY:
    class ServerPropertiesPrivateDnsZoneArgumentsArgsDict(TypedDict):
        private_dns_zone_arm_resource_id: NotRequired[pulumi.Input[str]]
        """
        private dns zone arm resource id.
        """
elif False:
    ServerPropertiesPrivateDnsZoneArgumentsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerPropertiesPrivateDnsZoneArgumentsArgs:
    def __init__(__self__, *,
                 private_dns_zone_arm_resource_id: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] private_dns_zone_arm_resource_id: private dns zone arm resource id.
        """
        if private_dns_zone_arm_resource_id is not None:
            pulumi.set(__self__, "private_dns_zone_arm_resource_id", private_dns_zone_arm_resource_id)

    @property
    @pulumi.getter(name="privateDnsZoneArmResourceId")
    def private_dns_zone_arm_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        private dns zone arm resource id.
        """
        return pulumi.get(self, "private_dns_zone_arm_resource_id")

    @private_dns_zone_arm_resource_id.setter
    def private_dns_zone_arm_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_dns_zone_arm_resource_id", value)


if not MYPY:
    class SkuArgsDict(TypedDict):
        """
        Sku information related properties of a server.
        """
        name: pulumi.Input[str]
        """
        The name of the sku, typically, tier + family + cores, e.g. Standard_D4s_v3.
        """
        tier: pulumi.Input[Union[str, 'SkuTier']]
        """
        The tier of the particular SKU, e.g. Burstable.
        """
elif False:
    SkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 tier: pulumi.Input[Union[str, 'SkuTier']]):
        """
        Sku information related properties of a server.
        :param pulumi.Input[str] name: The name of the sku, typically, tier + family + cores, e.g. Standard_D4s_v3.
        :param pulumi.Input[Union[str, 'SkuTier']] tier: The tier of the particular SKU, e.g. Burstable.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the sku, typically, tier + family + cores, e.g. Standard_D4s_v3.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Input[Union[str, 'SkuTier']]:
        """
        The tier of the particular SKU, e.g. Burstable.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: pulumi.Input[Union[str, 'SkuTier']]):
        pulumi.set(self, "tier", value)


if not MYPY:
    class StorageProfileArgsDict(TypedDict):
        """
        Storage Profile properties of a server
        """
        backup_retention_days: NotRequired[pulumi.Input[int]]
        """
        Backup retention days for the server.
        """
        geo_redundant_backup: NotRequired[pulumi.Input[Union[str, 'GeoRedundantBackupEnum']]]
        """
        A value indicating whether Geo-Redundant backup is enabled on the server.
        """
        storage_mb: NotRequired[pulumi.Input[int]]
        """
        Max storage allowed for a server.
        """
elif False:
    StorageProfileArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class StorageProfileArgs:
    def __init__(__self__, *,
                 backup_retention_days: Optional[pulumi.Input[int]] = None,
                 geo_redundant_backup: Optional[pulumi.Input[Union[str, 'GeoRedundantBackupEnum']]] = None,
                 storage_mb: Optional[pulumi.Input[int]] = None):
        """
        Storage Profile properties of a server
        :param pulumi.Input[int] backup_retention_days: Backup retention days for the server.
        :param pulumi.Input[Union[str, 'GeoRedundantBackupEnum']] geo_redundant_backup: A value indicating whether Geo-Redundant backup is enabled on the server.
        :param pulumi.Input[int] storage_mb: Max storage allowed for a server.
        """
        if backup_retention_days is not None:
            pulumi.set(__self__, "backup_retention_days", backup_retention_days)
        if geo_redundant_backup is not None:
            pulumi.set(__self__, "geo_redundant_backup", geo_redundant_backup)
        if storage_mb is not None:
            pulumi.set(__self__, "storage_mb", storage_mb)

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
    def geo_redundant_backup(self) -> Optional[pulumi.Input[Union[str, 'GeoRedundantBackupEnum']]]:
        """
        A value indicating whether Geo-Redundant backup is enabled on the server.
        """
        return pulumi.get(self, "geo_redundant_backup")

    @geo_redundant_backup.setter
    def geo_redundant_backup(self, value: Optional[pulumi.Input[Union[str, 'GeoRedundantBackupEnum']]]):
        pulumi.set(self, "geo_redundant_backup", value)

    @property
    @pulumi.getter(name="storageMB")
    def storage_mb(self) -> Optional[pulumi.Input[int]]:
        """
        Max storage allowed for a server.
        """
        return pulumi.get(self, "storage_mb")

    @storage_mb.setter
    def storage_mb(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "storage_mb", value)


