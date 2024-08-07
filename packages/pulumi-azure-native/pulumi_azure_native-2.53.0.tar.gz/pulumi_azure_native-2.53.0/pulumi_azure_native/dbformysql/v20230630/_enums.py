# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AdministratorType',
    'ConfigurationSource',
    'CreateMode',
    'DataEncryptionType',
    'EnableStatusEnum',
    'HighAvailabilityMode',
    'ImportSourceStorageType',
    'ManagedServiceIdentityType',
    'PrivateEndpointServiceConnectionStatus',
    'ReplicationRole',
    'ServerSkuTier',
    'ServerVersion',
]


class AdministratorType(str, Enum):
    """
    Type of the sever administrator.
    """
    ACTIVE_DIRECTORY = "ActiveDirectory"


class ConfigurationSource(str, Enum):
    """
    Source of the configuration.
    """
    SYSTEM_DEFAULT = "system-default"
    USER_OVERRIDE = "user-override"


class CreateMode(str, Enum):
    """
    The mode to create a new MySQL server.
    """
    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    REPLICA = "Replica"
    GEO_RESTORE = "GeoRestore"


class DataEncryptionType(str, Enum):
    """
    The key type, AzureKeyVault for enable cmk, SystemManaged for disable cmk.
    """
    AZURE_KEY_VAULT = "AzureKeyVault"
    SYSTEM_MANAGED = "SystemManaged"


class EnableStatusEnum(str, Enum):
    """
    Enable Log On Disk or not.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class HighAvailabilityMode(str, Enum):
    """
    High availability mode for a server.
    """
    DISABLED = "Disabled"
    ZONE_REDUNDANT = "ZoneRedundant"
    SAME_ZONE = "SameZone"


class ImportSourceStorageType(str, Enum):
    """
    Storage type of import source.
    """
    AZURE_BLOB = "AzureBlob"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity.
    """
    USER_ASSIGNED = "UserAssigned"


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class ReplicationRole(str, Enum):
    """
    The replication role.
    """
    NONE = "None"
    SOURCE = "Source"
    REPLICA = "Replica"


class ServerSkuTier(str, Enum):
    """
    The tier of the particular SKU, e.g. GeneralPurpose.
    """
    BURSTABLE = "Burstable"
    GENERAL_PURPOSE = "GeneralPurpose"
    MEMORY_OPTIMIZED = "MemoryOptimized"


class ServerVersion(str, Enum):
    """
    Server version.
    """
    SERVER_VERSION_5_7 = "5.7"
    SERVER_VERSION_8_0_21 = "8.0.21"
