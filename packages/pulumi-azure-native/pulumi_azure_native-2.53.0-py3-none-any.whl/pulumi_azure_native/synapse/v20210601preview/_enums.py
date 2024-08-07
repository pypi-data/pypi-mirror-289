# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'BlobStorageEventType',
    'ClusterPrincipalRole',
    'Compression',
    'ConfigurationType',
    'CreateMode',
    'DataConnectionKind',
    'DataFlowComputeType',
    'DatabasePrincipalRole',
    'DefaultPrincipalsModificationKind',
    'EventGridDataFormat',
    'EventHubDataFormat',
    'IntegrationRuntimeEdition',
    'IntegrationRuntimeEntityReferenceType',
    'IntegrationRuntimeLicenseType',
    'IntegrationRuntimeSsisCatalogPricingTier',
    'IntegrationRuntimeType',
    'IotHubDataFormat',
    'Kind',
    'NodeSize',
    'NodeSizeFamily',
    'PrincipalType',
    'ResourceIdentityType',
    'SensitivityLabelRank',
    'SkuName',
    'SkuSize',
    'StorageAccountType',
    'TransparentDataEncryptionStatus',
    'WorkspacePublicNetworkAccess',
]


class BlobStorageEventType(str, Enum):
    """
    The name of blob storage event type to process.
    """
    MICROSOFT_STORAGE_BLOB_CREATED = "Microsoft.Storage.BlobCreated"
    MICROSOFT_STORAGE_BLOB_RENAMED = "Microsoft.Storage.BlobRenamed"


class ClusterPrincipalRole(str, Enum):
    """
    Cluster principal role.
    """
    ALL_DATABASES_ADMIN = "AllDatabasesAdmin"
    ALL_DATABASES_VIEWER = "AllDatabasesViewer"


class Compression(str, Enum):
    """
    The event hub messages compression type
    """
    NONE = "None"
    G_ZIP = "GZip"


class ConfigurationType(str, Enum):
    """
    The type of the spark config properties file.
    """
    FILE = "File"
    ARTIFACT = "Artifact"


class CreateMode(str, Enum):
    """
    Specifies the mode of sql pool creation.

    Default: regular sql pool creation.

    PointInTimeRestore: Creates a sql pool by restoring a point in time backup of an existing sql pool. sourceDatabaseId must be specified as the resource ID of the existing sql pool, and restorePointInTime must be specified.

    Recovery: Creates a sql pool by a geo-replicated backup. sourceDatabaseId  must be specified as the recoverableDatabaseId to restore.

    Restore: Creates a sql pool by restoring a backup of a deleted sql  pool. SourceDatabaseId should be the sql pool's original resource ID. SourceDatabaseId and sourceDatabaseDeletionDate must be specified.
    """
    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    RECOVERY = "Recovery"
    RESTORE = "Restore"


class DataConnectionKind(str, Enum):
    """
    Kind of the endpoint for the data connection
    """
    EVENT_HUB = "EventHub"
    EVENT_GRID = "EventGrid"
    IOT_HUB = "IotHub"


class DataFlowComputeType(str, Enum):
    """
    Compute type of the cluster which will execute data flow job.
    """
    GENERAL = "General"
    MEMORY_OPTIMIZED = "MemoryOptimized"
    COMPUTE_OPTIMIZED = "ComputeOptimized"


class DatabasePrincipalRole(str, Enum):
    """
    Database principal role.
    """
    ADMIN = "Admin"
    INGESTOR = "Ingestor"
    MONITOR = "Monitor"
    USER = "User"
    UNRESTRICTED_VIEWER = "UnrestrictedViewer"
    VIEWER = "Viewer"


class DefaultPrincipalsModificationKind(str, Enum):
    """
    The default principals modification kind
    """
    UNION = "Union"
    REPLACE = "Replace"
    NONE = "None"


class EventGridDataFormat(str, Enum):
    """
    The data format of the message. Optionally the data format can be added to each message.
    """
    MULTIJSON = "MULTIJSON"
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    SCSV = "SCSV"
    SOHSV = "SOHSV"
    PSV = "PSV"
    TXT = "TXT"
    RAW = "RAW"
    SINGLEJSON = "SINGLEJSON"
    AVRO = "AVRO"
    TSVE = "TSVE"
    PARQUET = "PARQUET"
    ORC = "ORC"
    APACHEAVRO = "APACHEAVRO"
    W3_CLOGFILE = "W3CLOGFILE"


class EventHubDataFormat(str, Enum):
    """
    The data format of the message. Optionally the data format can be added to each message.
    """
    MULTIJSON = "MULTIJSON"
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    SCSV = "SCSV"
    SOHSV = "SOHSV"
    PSV = "PSV"
    TXT = "TXT"
    RAW = "RAW"
    SINGLEJSON = "SINGLEJSON"
    AVRO = "AVRO"
    TSVE = "TSVE"
    PARQUET = "PARQUET"
    ORC = "ORC"
    APACHEAVRO = "APACHEAVRO"
    W3_CLOGFILE = "W3CLOGFILE"


class IntegrationRuntimeEdition(str, Enum):
    """
    The edition for the SSIS Integration Runtime
    """
    STANDARD = "Standard"
    ENTERPRISE = "Enterprise"


class IntegrationRuntimeEntityReferenceType(str, Enum):
    """
    The type of this referenced entity.
    """
    INTEGRATION_RUNTIME_REFERENCE = "IntegrationRuntimeReference"
    LINKED_SERVICE_REFERENCE = "LinkedServiceReference"


class IntegrationRuntimeLicenseType(str, Enum):
    """
    License type for bringing your own license scenario.
    """
    BASE_PRICE = "BasePrice"
    LICENSE_INCLUDED = "LicenseIncluded"


class IntegrationRuntimeSsisCatalogPricingTier(str, Enum):
    """
    The pricing tier for the catalog database. The valid values could be found in https://azure.microsoft.com/en-us/pricing/details/sql-database/
    """
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    PREMIUM_RS = "PremiumRS"


class IntegrationRuntimeType(str, Enum):
    """
    Type of integration runtime.
    """
    MANAGED = "Managed"
    SELF_HOSTED = "SelfHosted"


class IotHubDataFormat(str, Enum):
    """
    The data format of the message. Optionally the data format can be added to each message.
    """
    MULTIJSON = "MULTIJSON"
    JSON = "JSON"
    CSV = "CSV"
    TSV = "TSV"
    SCSV = "SCSV"
    SOHSV = "SOHSV"
    PSV = "PSV"
    TXT = "TXT"
    RAW = "RAW"
    SINGLEJSON = "SINGLEJSON"
    AVRO = "AVRO"
    TSVE = "TSVE"
    PARQUET = "PARQUET"
    ORC = "ORC"
    APACHEAVRO = "APACHEAVRO"
    W3_CLOGFILE = "W3CLOGFILE"


class Kind(str, Enum):
    """
    Kind of the database
    """
    READ_WRITE = "ReadWrite"
    READ_ONLY_FOLLOWING = "ReadOnlyFollowing"


class NodeSize(str, Enum):
    """
    The level of compute power that each node in the Big Data pool has.
    """
    NONE = "None"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    X_LARGE = "XLarge"
    XX_LARGE = "XXLarge"
    XXX_LARGE = "XXXLarge"


class NodeSizeFamily(str, Enum):
    """
    The kind of nodes that the Big Data pool provides.
    """
    NONE = "None"
    MEMORY_OPTIMIZED = "MemoryOptimized"
    HARDWARE_ACCELERATED_FPGA = "HardwareAcceleratedFPGA"
    HARDWARE_ACCELERATED_GPU = "HardwareAcceleratedGPU"


class PrincipalType(str, Enum):
    """
    Principal type.
    """
    APP = "App"
    GROUP = "Group"
    USER = "User"


class ResourceIdentityType(str, Enum):
    """
    The type of managed identity for the workspace
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class SensitivityLabelRank(str, Enum):
    NONE = "None"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class SkuName(str, Enum):
    """
    SKU name.
    """
    COMPUTE_OPTIMIZED = "Compute optimized"
    STORAGE_OPTIMIZED = "Storage optimized"


class SkuSize(str, Enum):
    """
    SKU size.
    """
    EXTRA_SMALL = "Extra small"
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


class StorageAccountType(str, Enum):
    """
    The storage account type used to store backups for this sql pool.
    """
    GRS = "GRS"
    LRS = "LRS"


class TransparentDataEncryptionStatus(str, Enum):
    """
    The status of the database transparent data encryption.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class WorkspacePublicNetworkAccess(str, Enum):
    """
    Enable or Disable public network access to workspace
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
