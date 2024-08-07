# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AcquireStorageAccountLock',
    'AlertsState',
    'BackupItemType',
    'BackupManagementType',
    'CreateMode',
    'CrossRegionRestore',
    'CrossSubscriptionRestoreState',
    'DayOfWeek',
    'EnhancedSecurityState',
    'IAASVMPolicyType',
    'IaasVMSnapshotConsistencyType',
    'ImmutabilityState',
    'InfrastructureEncryptionState',
    'LastBackupStatus',
    'MonthOfYear',
    'OperationType',
    'PolicyType',
    'PrivateEndpointConnectionStatus',
    'ProtectableContainerType',
    'ProtectedItemHealthStatus',
    'ProtectedItemState',
    'ProtectionIntentItemType',
    'ProtectionState',
    'ProtectionStatus',
    'ProvisioningState',
    'PublicNetworkAccess',
    'ResourceHealthStatus',
    'ResourceIdentityType',
    'RetentionDurationType',
    'RetentionScheduleFormat',
    'ScheduleRunType',
    'SkuName',
    'SoftDeleteState',
    'StandardTierStorageRedundancy',
    'TieringMode',
    'VaultSubResourceType',
    'WeekOfMonth',
    'WorkloadItemType',
    'WorkloadType',
]


class AcquireStorageAccountLock(str, Enum):
    """
    Whether storage account lock is to be acquired for this container or not.
    """
    ACQUIRE = "Acquire"
    NOT_ACQUIRE = "NotAcquire"


class AlertsState(str, Enum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class BackupItemType(str, Enum):
    """
    Type of backup items associated with this container.
    """
    INVALID = "Invalid"
    VM = "VM"
    FILE_FOLDER = "FileFolder"
    AZURE_SQL_DB = "AzureSqlDb"
    SQLDB = "SQLDB"
    EXCHANGE = "Exchange"
    SHAREPOINT = "Sharepoint"
    V_MWARE_VM = "VMwareVM"
    SYSTEM_STATE = "SystemState"
    CLIENT = "Client"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    SQL_DATA_BASE = "SQLDataBase"
    AZURE_FILE_SHARE = "AzureFileShare"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAPASE_DATABASE = "SAPAseDatabase"
    SAP_HANA_DB_INSTANCE = "SAPHanaDBInstance"


class BackupManagementType(str, Enum):
    """
    Type of backup management for the backed up item.
    """
    INVALID = "Invalid"
    AZURE_IAAS_VM = "AzureIaasVM"
    MAB = "MAB"
    DPM = "DPM"
    AZURE_BACKUP_SERVER = "AzureBackupServer"
    AZURE_SQL = "AzureSql"
    AZURE_STORAGE = "AzureStorage"
    AZURE_WORKLOAD = "AzureWorkload"
    DEFAULT_BACKUP = "DefaultBackup"


class CreateMode(str, Enum):
    """
    Create mode to indicate recovery of existing soft deleted data source or creation of new data source.
    """
    INVALID = "Invalid"
    DEFAULT = "Default"
    RECOVER = "Recover"


class CrossRegionRestore(str, Enum):
    """
    Flag to show if Cross Region Restore is enabled on the Vault or not
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class CrossSubscriptionRestoreState(str, Enum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    PERMANENTLY_DISABLED = "PermanentlyDisabled"


class DayOfWeek(str, Enum):
    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"


class EnhancedSecurityState(str, Enum):
    INVALID = "Invalid"
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    ALWAYS_ON = "AlwaysON"


class IAASVMPolicyType(str, Enum):
    INVALID = "Invalid"
    V1 = "V1"
    V2 = "V2"


class IaasVMSnapshotConsistencyType(str, Enum):
    ONLY_CRASH_CONSISTENT = "OnlyCrashConsistent"


class ImmutabilityState(str, Enum):
    DISABLED = "Disabled"
    UNLOCKED = "Unlocked"
    LOCKED = "Locked"


class InfrastructureEncryptionState(str, Enum):
    """
    Enabling/Disabling the Double Encryption state
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class LastBackupStatus(str, Enum):
    """
    Last backup operation status. Possible values: Healthy, Unhealthy.
    """
    INVALID = "Invalid"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    IR_PENDING = "IRPending"


class MonthOfYear(str, Enum):
    INVALID = "Invalid"
    JANUARY = "January"
    FEBRUARY = "February"
    MARCH = "March"
    APRIL = "April"
    MAY = "May"
    JUNE = "June"
    JULY = "July"
    AUGUST = "August"
    SEPTEMBER = "September"
    OCTOBER = "October"
    NOVEMBER = "November"
    DECEMBER = "December"


class OperationType(str, Enum):
    """
    Re-Do Operation
    """
    INVALID = "Invalid"
    REGISTER = "Register"
    REREGISTER = "Reregister"


class PolicyType(str, Enum):
    """
    Type of backup policy type
    """
    INVALID = "Invalid"
    FULL = "Full"
    DIFFERENTIAL = "Differential"
    LOG = "Log"
    COPY_ONLY_FULL = "CopyOnlyFull"
    INCREMENTAL = "Incremental"
    SNAPSHOT_FULL = "SnapshotFull"
    SNAPSHOT_COPY_ONLY_FULL = "SnapshotCopyOnlyFull"


class PrivateEndpointConnectionStatus(str, Enum):
    """
    Gets or sets the status
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class ProtectableContainerType(str, Enum):
    """
    Type of the container. The value of this property for: 1. Compute Azure VM is Microsoft.Compute/virtualMachines 2.
    Classic Compute Azure VM is Microsoft.ClassicCompute/virtualMachines 3. Windows machines (like MAB, DPM etc) is
    Windows 4. Azure SQL instance is AzureSqlContainer. 5. Storage containers is StorageContainer. 6. Azure workload
    Backup is VMAppContainer
    """
    INVALID = "Invalid"
    UNKNOWN = "Unknown"
    IAAS_VM_CONTAINER = "IaasVMContainer"
    IAAS_VM_SERVICE_CONTAINER = "IaasVMServiceContainer"
    DPM_CONTAINER = "DPMContainer"
    AZURE_BACKUP_SERVER_CONTAINER = "AzureBackupServerContainer"
    MAB_CONTAINER = "MABContainer"
    CLUSTER = "Cluster"
    AZURE_SQL_CONTAINER = "AzureSqlContainer"
    WINDOWS = "Windows"
    V_CENTER = "VCenter"
    VM_APP_CONTAINER = "VMAppContainer"
    SQLAG_WORK_LOAD_CONTAINER = "SQLAGWorkLoadContainer"
    STORAGE_CONTAINER = "StorageContainer"
    GENERIC_CONTAINER = "GenericContainer"
    MICROSOFT_CLASSIC_COMPUTE_VIRTUAL_MACHINES = "Microsoft.ClassicCompute/virtualMachines"
    MICROSOFT_COMPUTE_VIRTUAL_MACHINES = "Microsoft.Compute/virtualMachines"
    AZURE_WORKLOAD_CONTAINER = "AzureWorkloadContainer"


class ProtectedItemHealthStatus(str, Enum):
    """
    Health status of the backup item, evaluated based on last heartbeat received
    """
    INVALID = "Invalid"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    NOT_REACHABLE = "NotReachable"
    IR_PENDING = "IRPending"


class ProtectedItemState(str, Enum):
    """
    Protection state of the backup engine
    """
    INVALID = "Invalid"
    IR_PENDING = "IRPending"
    PROTECTED = "Protected"
    PROTECTION_ERROR = "ProtectionError"
    PROTECTION_STOPPED = "ProtectionStopped"
    PROTECTION_PAUSED = "ProtectionPaused"
    BACKUPS_SUSPENDED = "BackupsSuspended"


class ProtectionIntentItemType(str, Enum):
    """
    backup protectionIntent type.
    """
    INVALID = "Invalid"
    AZURE_RESOURCE_ITEM = "AzureResourceItem"
    RECOVERY_SERVICE_VAULT_ITEM = "RecoveryServiceVaultItem"
    AZURE_WORKLOAD_CONTAINER_AUTO_PROTECTION_INTENT = "AzureWorkloadContainerAutoProtectionIntent"
    AZURE_WORKLOAD_AUTO_PROTECTION_INTENT = "AzureWorkloadAutoProtectionIntent"
    AZURE_WORKLOAD_SQL_AUTO_PROTECTION_INTENT = "AzureWorkloadSQLAutoProtectionIntent"


class ProtectionState(str, Enum):
    """
    Backup state of this backup item.
    """
    INVALID = "Invalid"
    IR_PENDING = "IRPending"
    PROTECTED = "Protected"
    PROTECTION_ERROR = "ProtectionError"
    PROTECTION_STOPPED = "ProtectionStopped"
    PROTECTION_PAUSED = "ProtectionPaused"
    BACKUPS_SUSPENDED = "BackupsSuspended"


class ProtectionStatus(str, Enum):
    """
    Backup state of this backup item.
    """
    INVALID = "Invalid"
    NOT_PROTECTED = "NotProtected"
    PROTECTING = "Protecting"
    PROTECTED = "Protected"
    PROTECTION_FAILED = "ProtectionFailed"


class ProvisioningState(str, Enum):
    """
    Gets or sets provisioning state of the private endpoint connection
    """
    SUCCEEDED = "Succeeded"
    DELETING = "Deleting"
    FAILED = "Failed"
    PENDING = "Pending"


class PublicNetworkAccess(str, Enum):
    """
    property to enable or disable resource provider inbound network traffic from public clients
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ResourceHealthStatus(str, Enum):
    """
    Resource Health Status
    """
    HEALTHY = "Healthy"
    TRANSIENT_DEGRADED = "TransientDegraded"
    PERSISTENT_DEGRADED = "PersistentDegraded"
    TRANSIENT_UNHEALTHY = "TransientUnhealthy"
    PERSISTENT_UNHEALTHY = "PersistentUnhealthy"
    INVALID = "Invalid"


class ResourceIdentityType(str, Enum):
    """
    The type of managed identity used. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user-assigned identities. The type 'None' will remove any identities.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class RetentionDurationType(str, Enum):
    """
    Retention duration type: days/weeks/months/years
    Used only if TieringMode is set to TierAfter
    """
    INVALID = "Invalid"
    DAYS = "Days"
    WEEKS = "Weeks"
    MONTHS = "Months"
    YEARS = "Years"


class RetentionScheduleFormat(str, Enum):
    """
    Retention schedule format for yearly retention policy.
    """
    INVALID = "Invalid"
    DAILY = "Daily"
    WEEKLY = "Weekly"


class ScheduleRunType(str, Enum):
    """
    Frequency of the schedule operation of this policy.
    """
    INVALID = "Invalid"
    DAILY = "Daily"
    WEEKLY = "Weekly"
    HOURLY = "Hourly"


class SkuName(str, Enum):
    """
    Name of SKU is RS0 (Recovery Services 0th version) and the tier is standard tier. They do not have affect on backend storage redundancy or any other vault settings. To manage storage redundancy, use the backupstorageconfig
    """
    STANDARD = "Standard"
    RS0 = "RS0"


class SoftDeleteState(str, Enum):
    INVALID = "Invalid"
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    ALWAYS_ON = "AlwaysON"


class StandardTierStorageRedundancy(str, Enum):
    """
    The storage redundancy setting of a vault
    """
    INVALID = "Invalid"
    LOCALLY_REDUNDANT = "LocallyRedundant"
    GEO_REDUNDANT = "GeoRedundant"
    ZONE_REDUNDANT = "ZoneRedundant"


class TieringMode(str, Enum):
    """
    Tiering Mode to control automatic tiering of recovery points. Supported values are:
    1. TierRecommended: Tier all recovery points recommended to be tiered
    2. TierAfter: Tier all recovery points after a fixed period, as specified in duration + durationType below.
    3. DoNotTier: Do not tier any recovery points
    """
    INVALID = "Invalid"
    TIER_RECOMMENDED = "TierRecommended"
    TIER_AFTER = "TierAfter"
    DO_NOT_TIER = "DoNotTier"


class VaultSubResourceType(str, Enum):
    """
    GroupId for the PrivateEndpointConnection - AzureBackup, AzureBackup_secondary or AzureSiteRecovery
    """
    AZURE_BACKUP = "AzureBackup"
    AZURE_BACKUP_SECONDARY = "AzureBackup_secondary"
    AZURE_SITE_RECOVERY = "AzureSiteRecovery"


class WeekOfMonth(str, Enum):
    FIRST = "First"
    SECOND = "Second"
    THIRD = "Third"
    FOURTH = "Fourth"
    LAST = "Last"
    INVALID = "Invalid"


class WorkloadItemType(str, Enum):
    """
    Workload item type of the item for which intent is to be set
    """
    INVALID = "Invalid"
    SQL_INSTANCE = "SQLInstance"
    SQL_DATA_BASE = "SQLDataBase"
    SAP_HANA_SYSTEM = "SAPHanaSystem"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAPASE_SYSTEM = "SAPAseSystem"
    SAPASE_DATABASE = "SAPAseDatabase"
    SAP_HANA_DB_INSTANCE = "SAPHanaDBInstance"


class WorkloadType(str, Enum):
    """
    Type of workload for the backup management
    """
    INVALID = "Invalid"
    VM = "VM"
    FILE_FOLDER = "FileFolder"
    AZURE_SQL_DB = "AzureSqlDb"
    SQLDB = "SQLDB"
    EXCHANGE = "Exchange"
    SHAREPOINT = "Sharepoint"
    V_MWARE_VM = "VMwareVM"
    SYSTEM_STATE = "SystemState"
    CLIENT = "Client"
    GENERIC_DATA_SOURCE = "GenericDataSource"
    SQL_DATA_BASE = "SQLDataBase"
    AZURE_FILE_SHARE = "AzureFileShare"
    SAP_HANA_DATABASE = "SAPHanaDatabase"
    SAPASE_DATABASE = "SAPAseDatabase"
    SAP_HANA_DB_INSTANCE = "SAPHanaDBInstance"
