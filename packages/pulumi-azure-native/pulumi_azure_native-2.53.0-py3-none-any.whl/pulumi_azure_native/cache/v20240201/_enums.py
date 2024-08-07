# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AofFrequency',
    'ClusteringPolicy',
    'CmkIdentityType',
    'EvictionPolicy',
    'ManagedServiceIdentityType',
    'PrivateEndpointServiceConnectionStatus',
    'Protocol',
    'RdbFrequency',
    'SkuName',
    'TlsVersion',
]


class AofFrequency(str, Enum):
    """
    Sets the frequency at which data is written to disk.
    """
    AOF_FREQUENCY_1S = "1s"
    ALWAYS = "always"


class ClusteringPolicy(str, Enum):
    """
    Clustering policy - default is OSSCluster. Specified at create time.
    """
    ENTERPRISE_CLUSTER = "EnterpriseCluster"
    OSS_CLUSTER = "OSSCluster"


class CmkIdentityType(str, Enum):
    """
    Only userAssignedIdentity is supported in this API version; other types may be supported in the future
    """
    SYSTEM_ASSIGNED_IDENTITY = "systemAssignedIdentity"
    USER_ASSIGNED_IDENTITY = "userAssignedIdentity"


class EvictionPolicy(str, Enum):
    """
    Redis eviction policy - default is VolatileLRU
    """
    ALL_KEYS_LFU = "AllKeysLFU"
    ALL_KEYS_LRU = "AllKeysLRU"
    ALL_KEYS_RANDOM = "AllKeysRandom"
    VOLATILE_LRU = "VolatileLRU"
    VOLATILE_LFU = "VolatileLFU"
    VOLATILE_TTL = "VolatileTTL"
    VOLATILE_RANDOM = "VolatileRandom"
    NO_EVICTION = "NoEviction"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"


class PrivateEndpointServiceConnectionStatus(str, Enum):
    """
    Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"


class Protocol(str, Enum):
    """
    Specifies whether redis clients can connect using TLS-encrypted or plaintext redis protocols. Default is TLS-encrypted.
    """
    ENCRYPTED = "Encrypted"
    PLAINTEXT = "Plaintext"


class RdbFrequency(str, Enum):
    """
    Sets the frequency at which a snapshot of the database is created.
    """
    RDB_FREQUENCY_1H = "1h"
    RDB_FREQUENCY_6H = "6h"
    RDB_FREQUENCY_12H = "12h"


class SkuName(str, Enum):
    """
    The type of RedisEnterprise cluster to deploy. Possible values: (Enterprise_E10, EnterpriseFlash_F300 etc.)
    """
    ENTERPRISE_E5 = "Enterprise_E5"
    ENTERPRISE_E10 = "Enterprise_E10"
    ENTERPRISE_E20 = "Enterprise_E20"
    ENTERPRISE_E50 = "Enterprise_E50"
    ENTERPRISE_E100 = "Enterprise_E100"
    ENTERPRISE_FLASH_F300 = "EnterpriseFlash_F300"
    ENTERPRISE_FLASH_F700 = "EnterpriseFlash_F700"
    ENTERPRISE_FLASH_F1500 = "EnterpriseFlash_F1500"


class TlsVersion(str, Enum):
    """
    The minimum TLS version for the cluster to support, e.g. '1.2'
    """
    TLS_VERSION_1_0 = "1.0"
    TLS_VERSION_1_1 = "1.1"
    TLS_VERSION_1_2 = "1.2"
