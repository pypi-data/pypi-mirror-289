# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AccessTier',
    'AccountImmutabilityPolicyState',
    'AccountType',
    'Action',
    'AllowedCopyScope',
    'AllowedMethods',
    'Bypass',
    'DefaultAction',
    'DefaultSharePermission',
    'DirectoryServiceOptions',
    'DnsEndpointType',
    'EnabledProtocols',
    'EncryptionScopeSource',
    'EncryptionScopeState',
    'ExpirationAction',
    'ExtendedLocationTypes',
    'Format',
    'HttpProtocol',
    'IdentityType',
    'IntervalUnit',
    'InventoryRuleType',
    'KeySource',
    'KeyType',
    'Kind',
    'LargeFileSharesState',
    'MinimumTlsVersion',
    'Name',
    'ObjectType',
    'Permissions',
    'PrivateEndpointServiceConnectionStatus',
    'PublicAccess',
    'PublicNetworkAccess',
    'RootSquashType',
    'RoutingChoice',
    'RuleType',
    'Schedule',
    'Services',
    'ShareAccessTier',
    'SignedResource',
    'SignedResourceTypes',
    'SkuName',
    'State',
    'TriggerType',
]


class AccessTier(str, Enum):
    """
    Required for storage accounts where kind = BlobStorage. The access tier is used for billing. The 'Premium' access tier is the default value for premium block blobs storage account type and it cannot be changed for the premium block blobs storage account type.
    """
    HOT = "Hot"
    COOL = "Cool"
    PREMIUM = "Premium"
    COLD = "Cold"


class AccountImmutabilityPolicyState(str, Enum):
    """
    The ImmutabilityPolicy state defines the mode of the policy. Disabled state disables the policy, Unlocked state allows increase and decrease of immutability retention time and also allows toggling allowProtectedAppendWrites property, Locked state only allows the increase of the immutability retention time. A policy can only be created in a Disabled or Unlocked state and can be toggled between the two states. Only a policy in an Unlocked state can transition to a Locked state which cannot be reverted.
    """
    UNLOCKED = "Unlocked"
    LOCKED = "Locked"
    DISABLED = "Disabled"


class AccountType(str, Enum):
    """
    Specifies the Active Directory account type for Azure Storage.
    """
    USER = "User"
    COMPUTER = "Computer"


class Action(str, Enum):
    """
    The action of virtual network rule.
    """
    ALLOW = "Allow"


class AllowedCopyScope(str, Enum):
    """
    Restrict copy to and from Storage Accounts within an AAD tenant or with Private Links to the same VNet.
    """
    PRIVATE_LINK = "PrivateLink"
    AAD = "AAD"


class AllowedMethods(str, Enum):
    DELETE = "DELETE"
    GET = "GET"
    HEAD = "HEAD"
    MERGE = "MERGE"
    POST = "POST"
    OPTIONS = "OPTIONS"
    PUT = "PUT"
    PATCH = "PATCH"
    CONNECT = "CONNECT"
    TRACE = "TRACE"


class Bypass(str, Enum):
    """
    Specifies whether traffic is bypassed for Logging/Metrics/AzureServices. Possible values are any combination of Logging|Metrics|AzureServices (For example, "Logging, Metrics"), or None to bypass none of those traffics.
    """
    NONE = "None"
    LOGGING = "Logging"
    METRICS = "Metrics"
    AZURE_SERVICES = "AzureServices"


class DefaultAction(str, Enum):
    """
    Specifies the default action of allow or deny when no other rules match.
    """
    ALLOW = "Allow"
    DENY = "Deny"


class DefaultSharePermission(str, Enum):
    """
    Default share permission for users using Kerberos authentication if RBAC role is not assigned.
    """
    NONE = "None"
    STORAGE_FILE_DATA_SMB_SHARE_READER = "StorageFileDataSmbShareReader"
    STORAGE_FILE_DATA_SMB_SHARE_CONTRIBUTOR = "StorageFileDataSmbShareContributor"
    STORAGE_FILE_DATA_SMB_SHARE_ELEVATED_CONTRIBUTOR = "StorageFileDataSmbShareElevatedContributor"


class DirectoryServiceOptions(str, Enum):
    """
    Indicates the directory service used. Note that this enum may be extended in the future.
    """
    NONE = "None"
    AADDS = "AADDS"
    AD = "AD"
    AADKERB = "AADKERB"


class DnsEndpointType(str, Enum):
    """
    Allows you to specify the type of endpoint. Set this to AzureDNSZone to create a large number of accounts in a single subscription, which creates accounts in an Azure DNS Zone and the endpoint URL will have an alphanumeric DNS Zone identifier.
    """
    STANDARD = "Standard"
    AZURE_DNS_ZONE = "AzureDnsZone"


class EnabledProtocols(str, Enum):
    """
    The authentication protocol that is used for the file share. Can only be specified when creating a share.
    """
    SMB = "SMB"
    NFS = "NFS"


class EncryptionScopeSource(str, Enum):
    """
    The provider for the encryption scope. Possible values (case-insensitive):  Microsoft.Storage, Microsoft.KeyVault.
    """
    MICROSOFT_STORAGE = "Microsoft.Storage"
    MICROSOFT_KEY_VAULT = "Microsoft.KeyVault"


class EncryptionScopeState(str, Enum):
    """
    The state of the encryption scope. Possible values (case-insensitive):  Enabled, Disabled.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ExpirationAction(str, Enum):
    """
    The SAS Expiration Action defines the action to be performed when sasPolicy.sasExpirationPeriod is violated. The 'Log' action can be used for audit purposes and the 'Block' action can be used to block and deny the usage of SAS tokens that do not adhere to the sas policy expiration period.
    """
    LOG = "Log"
    BLOCK = "Block"


class ExtendedLocationTypes(str, Enum):
    """
    The type of the extended location.
    """
    EDGE_ZONE = "EdgeZone"


class Format(str, Enum):
    """
    This is a required field, it specifies the format for the inventory files.
    """
    CSV = "Csv"
    PARQUET = "Parquet"


class HttpProtocol(str, Enum):
    """
    The protocol permitted for a request made with the account SAS.
    """
    HTTPS_HTTP = "https,http"
    HTTPS = "https"


class IdentityType(str, Enum):
    """
    The identity type.
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class IntervalUnit(str, Enum):
    """
    Run interval unit of task execution. This is a required field when ExecutionTrigger.properties.type is 'OnSchedule'; this property should not be present when ExecutionTrigger.properties.type is 'RunOnce'
    """
    DAYS = "Days"


class InventoryRuleType(str, Enum):
    """
    The valid value is Inventory
    """
    INVENTORY = "Inventory"


class KeySource(str, Enum):
    """
    The encryption keySource (provider). Possible values (case-insensitive):  Microsoft.Storage, Microsoft.Keyvault
    """
    MICROSOFT_STORAGE = "Microsoft.Storage"
    MICROSOFT_KEYVAULT = "Microsoft.Keyvault"


class KeyType(str, Enum):
    """
    Encryption key type to be used for the encryption service. 'Account' key type implies that an account-scoped encryption key will be used. 'Service' key type implies that a default service key is used.
    """
    SERVICE = "Service"
    ACCOUNT = "Account"


class Kind(str, Enum):
    """
    Required. Indicates the type of storage account.
    """
    STORAGE = "Storage"
    STORAGE_V2 = "StorageV2"
    BLOB_STORAGE = "BlobStorage"
    FILE_STORAGE = "FileStorage"
    BLOCK_BLOB_STORAGE = "BlockBlobStorage"


class LargeFileSharesState(str, Enum):
    """
    Allow large file shares if sets to Enabled. It cannot be disabled once it is enabled.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class MinimumTlsVersion(str, Enum):
    """
    Set the minimum TLS version to be permitted on requests to storage. The default interpretation is TLS 1.0 for this property.
    """
    TLS1_0 = "TLS1_0"
    TLS1_1 = "TLS1_1"
    TLS1_2 = "TLS1_2"
    TLS1_3 = "TLS1_3"


class Name(str, Enum):
    """
    Name of the policy. The valid value is AccessTimeTracking. This field is currently read only
    """
    ACCESS_TIME_TRACKING = "AccessTimeTracking"


class ObjectType(str, Enum):
    """
    This is a required field. This field specifies the scope of the inventory created either at the blob or container level.
    """
    BLOB = "Blob"
    CONTAINER = "Container"


class Permissions(str, Enum):
    """
    The signed permissions for the service SAS. Possible values include: Read (r), Write (w), Delete (d), List (l), Add (a), Create (c), Update (u) and Process (p).
    """
    R = "r"
    D = "d"
    W = "w"
    L = "l"
    A = "a"
    C = "c"
    U = "u"
    P = "p"


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class PublicAccess(str, Enum):
    """
    Specifies whether data in the container may be accessed publicly and the level of access.
    """
    CONTAINER = "Container"
    BLOB = "Blob"
    NONE = "None"


class PublicNetworkAccess(str, Enum):
    """
    Allow, disallow, or let Network Security Perimeter configuration to evaluate public network access to Storage Account. Value is optional but if passed in, must be 'Enabled', 'Disabled' or 'SecuredByPerimeter'.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    SECURED_BY_PERIMETER = "SecuredByPerimeter"


class RootSquashType(str, Enum):
    """
    The property is for NFS share only. The default is NoRootSquash.
    """
    NO_ROOT_SQUASH = "NoRootSquash"
    ROOT_SQUASH = "RootSquash"
    ALL_SQUASH = "AllSquash"


class RoutingChoice(str, Enum):
    """
    Routing Choice defines the kind of network routing opted by the user.
    """
    MICROSOFT_ROUTING = "MicrosoftRouting"
    INTERNET_ROUTING = "InternetRouting"


class RuleType(str, Enum):
    """
    The valid value is Lifecycle
    """
    LIFECYCLE = "Lifecycle"


class Schedule(str, Enum):
    """
    This is a required field. This field is used to schedule an inventory formation.
    """
    DAILY = "Daily"
    WEEKLY = "Weekly"


class Services(str, Enum):
    """
    The signed services accessible with the account SAS. Possible values include: Blob (b), Queue (q), Table (t), File (f).
    """
    B = "b"
    Q = "q"
    T = "t"
    F = "f"


class ShareAccessTier(str, Enum):
    """
    Access tier for specific share. GpV2 account can choose between TransactionOptimized (default), Hot, and Cool. FileStorage account can choose Premium.
    """
    TRANSACTION_OPTIMIZED = "TransactionOptimized"
    HOT = "Hot"
    COOL = "Cool"
    PREMIUM = "Premium"


class SignedResource(str, Enum):
    """
    The signed services accessible with the service SAS. Possible values include: Blob (b), Container (c), File (f), Share (s).
    """
    B = "b"
    C = "c"
    F = "f"
    S = "s"


class SignedResourceTypes(str, Enum):
    """
    The signed resource types that are accessible with the account SAS. Service (s): Access to service-level APIs; Container (c): Access to container-level APIs; Object (o): Access to object-level APIs for blobs, queue messages, table entities, and files.
    """
    S = "s"
    C = "c"
    O = "o"


class SkuName(str, Enum):
    """
    The SKU name. Required for account creation; optional for update. Note that in older versions, SKU name was called accountType.
    """
    STANDARD_LRS = "Standard_LRS"
    STANDARD_GRS = "Standard_GRS"
    STANDARD_RAGRS = "Standard_RAGRS"
    STANDARD_ZRS = "Standard_ZRS"
    PREMIUM_LRS = "Premium_LRS"
    PREMIUM_ZRS = "Premium_ZRS"
    STANDARD_GZRS = "Standard_GZRS"
    STANDARD_RAGZRS = "Standard_RAGZRS"


class State(str, Enum):
    """
    Gets the state of virtual network rule.
    """
    PROVISIONING = "Provisioning"
    DEPROVISIONING = "Deprovisioning"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    NETWORK_SOURCE_DELETED = "NetworkSourceDeleted"


class TriggerType(str, Enum):
    """
    The trigger type of the storage task assignment execution
    """
    RUN_ONCE = "RunOnce"
    ON_SCHEDULE = "OnSchedule"
