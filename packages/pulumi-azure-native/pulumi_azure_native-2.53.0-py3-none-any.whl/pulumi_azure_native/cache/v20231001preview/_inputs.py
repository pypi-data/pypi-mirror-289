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
    'ClusterPropertiesCustomerManagedKeyEncryptionArgs',
    'ClusterPropertiesCustomerManagedKeyEncryptionArgsDict',
    'ClusterPropertiesEncryptionArgs',
    'ClusterPropertiesEncryptionArgsDict',
    'ClusterPropertiesKeyEncryptionKeyIdentityArgs',
    'ClusterPropertiesKeyEncryptionKeyIdentityArgsDict',
    'DatabasePropertiesGeoReplicationArgs',
    'DatabasePropertiesGeoReplicationArgsDict',
    'EnterpriseSkuArgs',
    'EnterpriseSkuArgsDict',
    'LinkedDatabaseArgs',
    'LinkedDatabaseArgsDict',
    'ManagedServiceIdentityArgs',
    'ManagedServiceIdentityArgsDict',
    'ModuleArgs',
    'ModuleArgsDict',
    'PersistenceArgs',
    'PersistenceArgsDict',
    'PrivateLinkServiceConnectionStateArgs',
    'PrivateLinkServiceConnectionStateArgsDict',
]

MYPY = False

if not MYPY:
    class ClusterPropertiesCustomerManagedKeyEncryptionArgsDict(TypedDict):
        """
        All Customer-managed key encryption properties for the resource. Set this to an empty object to use Microsoft-managed key encryption.
        """
        key_encryption_key_identity: NotRequired[pulumi.Input['ClusterPropertiesKeyEncryptionKeyIdentityArgsDict']]
        """
        All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        """
        key_encryption_key_url: NotRequired[pulumi.Input[str]]
        """
        Key encryption key Url, versioned only. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78
        """
elif False:
    ClusterPropertiesCustomerManagedKeyEncryptionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ClusterPropertiesCustomerManagedKeyEncryptionArgs:
    def __init__(__self__, *,
                 key_encryption_key_identity: Optional[pulumi.Input['ClusterPropertiesKeyEncryptionKeyIdentityArgs']] = None,
                 key_encryption_key_url: Optional[pulumi.Input[str]] = None):
        """
        All Customer-managed key encryption properties for the resource. Set this to an empty object to use Microsoft-managed key encryption.
        :param pulumi.Input['ClusterPropertiesKeyEncryptionKeyIdentityArgs'] key_encryption_key_identity: All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        :param pulumi.Input[str] key_encryption_key_url: Key encryption key Url, versioned only. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78
        """
        if key_encryption_key_identity is not None:
            pulumi.set(__self__, "key_encryption_key_identity", key_encryption_key_identity)
        if key_encryption_key_url is not None:
            pulumi.set(__self__, "key_encryption_key_url", key_encryption_key_url)

    @property
    @pulumi.getter(name="keyEncryptionKeyIdentity")
    def key_encryption_key_identity(self) -> Optional[pulumi.Input['ClusterPropertiesKeyEncryptionKeyIdentityArgs']]:
        """
        All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        """
        return pulumi.get(self, "key_encryption_key_identity")

    @key_encryption_key_identity.setter
    def key_encryption_key_identity(self, value: Optional[pulumi.Input['ClusterPropertiesKeyEncryptionKeyIdentityArgs']]):
        pulumi.set(self, "key_encryption_key_identity", value)

    @property
    @pulumi.getter(name="keyEncryptionKeyUrl")
    def key_encryption_key_url(self) -> Optional[pulumi.Input[str]]:
        """
        Key encryption key Url, versioned only. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78
        """
        return pulumi.get(self, "key_encryption_key_url")

    @key_encryption_key_url.setter
    def key_encryption_key_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_encryption_key_url", value)


if not MYPY:
    class ClusterPropertiesEncryptionArgsDict(TypedDict):
        """
        Encryption-at-rest configuration for the cluster.
        """
        customer_managed_key_encryption: NotRequired[pulumi.Input['ClusterPropertiesCustomerManagedKeyEncryptionArgsDict']]
        """
        All Customer-managed key encryption properties for the resource. Set this to an empty object to use Microsoft-managed key encryption.
        """
elif False:
    ClusterPropertiesEncryptionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ClusterPropertiesEncryptionArgs:
    def __init__(__self__, *,
                 customer_managed_key_encryption: Optional[pulumi.Input['ClusterPropertiesCustomerManagedKeyEncryptionArgs']] = None):
        """
        Encryption-at-rest configuration for the cluster.
        :param pulumi.Input['ClusterPropertiesCustomerManagedKeyEncryptionArgs'] customer_managed_key_encryption: All Customer-managed key encryption properties for the resource. Set this to an empty object to use Microsoft-managed key encryption.
        """
        if customer_managed_key_encryption is not None:
            pulumi.set(__self__, "customer_managed_key_encryption", customer_managed_key_encryption)

    @property
    @pulumi.getter(name="customerManagedKeyEncryption")
    def customer_managed_key_encryption(self) -> Optional[pulumi.Input['ClusterPropertiesCustomerManagedKeyEncryptionArgs']]:
        """
        All Customer-managed key encryption properties for the resource. Set this to an empty object to use Microsoft-managed key encryption.
        """
        return pulumi.get(self, "customer_managed_key_encryption")

    @customer_managed_key_encryption.setter
    def customer_managed_key_encryption(self, value: Optional[pulumi.Input['ClusterPropertiesCustomerManagedKeyEncryptionArgs']]):
        pulumi.set(self, "customer_managed_key_encryption", value)


if not MYPY:
    class ClusterPropertiesKeyEncryptionKeyIdentityArgsDict(TypedDict):
        """
        All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        """
        identity_type: NotRequired[pulumi.Input[Union[str, 'CmkIdentityType']]]
        """
        Only userAssignedIdentity is supported in this API version; other types may be supported in the future
        """
        user_assigned_identity_resource_id: NotRequired[pulumi.Input[str]]
        """
        User assigned identity to use for accessing key encryption key Url. Ex: /subscriptions/<sub uuid>/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId.
        """
elif False:
    ClusterPropertiesKeyEncryptionKeyIdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ClusterPropertiesKeyEncryptionKeyIdentityArgs:
    def __init__(__self__, *,
                 identity_type: Optional[pulumi.Input[Union[str, 'CmkIdentityType']]] = None,
                 user_assigned_identity_resource_id: Optional[pulumi.Input[str]] = None):
        """
        All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        :param pulumi.Input[Union[str, 'CmkIdentityType']] identity_type: Only userAssignedIdentity is supported in this API version; other types may be supported in the future
        :param pulumi.Input[str] user_assigned_identity_resource_id: User assigned identity to use for accessing key encryption key Url. Ex: /subscriptions/<sub uuid>/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId.
        """
        if identity_type is not None:
            pulumi.set(__self__, "identity_type", identity_type)
        if user_assigned_identity_resource_id is not None:
            pulumi.set(__self__, "user_assigned_identity_resource_id", user_assigned_identity_resource_id)

    @property
    @pulumi.getter(name="identityType")
    def identity_type(self) -> Optional[pulumi.Input[Union[str, 'CmkIdentityType']]]:
        """
        Only userAssignedIdentity is supported in this API version; other types may be supported in the future
        """
        return pulumi.get(self, "identity_type")

    @identity_type.setter
    def identity_type(self, value: Optional[pulumi.Input[Union[str, 'CmkIdentityType']]]):
        pulumi.set(self, "identity_type", value)

    @property
    @pulumi.getter(name="userAssignedIdentityResourceId")
    def user_assigned_identity_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        User assigned identity to use for accessing key encryption key Url. Ex: /subscriptions/<sub uuid>/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId.
        """
        return pulumi.get(self, "user_assigned_identity_resource_id")

    @user_assigned_identity_resource_id.setter
    def user_assigned_identity_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_assigned_identity_resource_id", value)


if not MYPY:
    class DatabasePropertiesGeoReplicationArgsDict(TypedDict):
        """
        Optional set of properties to configure geo replication for this database.
        """
        group_nickname: NotRequired[pulumi.Input[str]]
        """
        Name for the group of linked database resources
        """
        linked_databases: NotRequired[pulumi.Input[Sequence[pulumi.Input['LinkedDatabaseArgsDict']]]]
        """
        List of database resources to link with this database
        """
elif False:
    DatabasePropertiesGeoReplicationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DatabasePropertiesGeoReplicationArgs:
    def __init__(__self__, *,
                 group_nickname: Optional[pulumi.Input[str]] = None,
                 linked_databases: Optional[pulumi.Input[Sequence[pulumi.Input['LinkedDatabaseArgs']]]] = None):
        """
        Optional set of properties to configure geo replication for this database.
        :param pulumi.Input[str] group_nickname: Name for the group of linked database resources
        :param pulumi.Input[Sequence[pulumi.Input['LinkedDatabaseArgs']]] linked_databases: List of database resources to link with this database
        """
        if group_nickname is not None:
            pulumi.set(__self__, "group_nickname", group_nickname)
        if linked_databases is not None:
            pulumi.set(__self__, "linked_databases", linked_databases)

    @property
    @pulumi.getter(name="groupNickname")
    def group_nickname(self) -> Optional[pulumi.Input[str]]:
        """
        Name for the group of linked database resources
        """
        return pulumi.get(self, "group_nickname")

    @group_nickname.setter
    def group_nickname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_nickname", value)

    @property
    @pulumi.getter(name="linkedDatabases")
    def linked_databases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LinkedDatabaseArgs']]]]:
        """
        List of database resources to link with this database
        """
        return pulumi.get(self, "linked_databases")

    @linked_databases.setter
    def linked_databases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LinkedDatabaseArgs']]]]):
        pulumi.set(self, "linked_databases", value)


if not MYPY:
    class EnterpriseSkuArgsDict(TypedDict):
        """
        SKU parameters supplied to the create RedisEnterprise operation.
        """
        name: pulumi.Input[Union[str, 'SkuName']]
        """
        The type of RedisEnterprise cluster to deploy. Possible values: (Enterprise_E10, EnterpriseFlash_F300 etc.)
        """
        capacity: NotRequired[pulumi.Input[int]]
        """
        The size of the RedisEnterprise cluster. Defaults to 2 or 3 depending on SKU. Valid values are (2, 4, 6, ...) for Enterprise SKUs and (3, 9, 15, ...) for Flash SKUs.
        """
elif False:
    EnterpriseSkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class EnterpriseSkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[Union[str, 'SkuName']],
                 capacity: Optional[pulumi.Input[int]] = None):
        """
        SKU parameters supplied to the create RedisEnterprise operation.
        :param pulumi.Input[Union[str, 'SkuName']] name: The type of RedisEnterprise cluster to deploy. Possible values: (Enterprise_E10, EnterpriseFlash_F300 etc.)
        :param pulumi.Input[int] capacity: The size of the RedisEnterprise cluster. Defaults to 2 or 3 depending on SKU. Valid values are (2, 4, 6, ...) for Enterprise SKUs and (3, 9, 15, ...) for Flash SKUs.
        """
        pulumi.set(__self__, "name", name)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[str, 'SkuName']]:
        """
        The type of RedisEnterprise cluster to deploy. Possible values: (Enterprise_E10, EnterpriseFlash_F300 etc.)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[str, 'SkuName']]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        """
        The size of the RedisEnterprise cluster. Defaults to 2 or 3 depending on SKU. Valid values are (2, 4, 6, ...) for Enterprise SKUs and (3, 9, 15, ...) for Flash SKUs.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)


if not MYPY:
    class LinkedDatabaseArgsDict(TypedDict):
        """
        Specifies details of a linked database resource.
        """
        id: NotRequired[pulumi.Input[str]]
        """
        Resource ID of a database resource to link with this database.
        """
elif False:
    LinkedDatabaseArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class LinkedDatabaseArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        Specifies details of a linked database resource.
        :param pulumi.Input[str] id: Resource ID of a database resource to link with this database.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID of a database resource to link with this database.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


if not MYPY:
    class ManagedServiceIdentityArgsDict(TypedDict):
        """
        Managed service identity (system assigned and/or user assigned identities)
        """
        type: pulumi.Input[Union[str, 'ManagedServiceIdentityType']]
        """
        Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        """
        user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
elif False:
    ManagedServiceIdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[Union[str, 'ManagedServiceIdentityType']],
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Managed service identity (system assigned and/or user assigned identities)
        :param pulumi.Input[Union[str, 'ManagedServiceIdentityType']] type: Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'ManagedServiceIdentityType']]:
        """
        Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'ManagedServiceIdentityType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


if not MYPY:
    class ModuleArgsDict(TypedDict):
        """
        Specifies configuration of a redis module
        """
        name: pulumi.Input[str]
        """
        The name of the module, e.g. 'RedisBloom', 'RediSearch', 'RedisTimeSeries'
        """
        args: NotRequired[pulumi.Input[str]]
        """
        Configuration options for the module, e.g. 'ERROR_RATE 0.01 INITIAL_SIZE 400'.
        """
elif False:
    ModuleArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ModuleArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 args: Optional[pulumi.Input[str]] = None):
        """
        Specifies configuration of a redis module
        :param pulumi.Input[str] name: The name of the module, e.g. 'RedisBloom', 'RediSearch', 'RedisTimeSeries'
        :param pulumi.Input[str] args: Configuration options for the module, e.g. 'ERROR_RATE 0.01 INITIAL_SIZE 400'.
        """
        pulumi.set(__self__, "name", name)
        if args is not None:
            pulumi.set(__self__, "args", args)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the module, e.g. 'RedisBloom', 'RediSearch', 'RedisTimeSeries'
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[str]]:
        """
        Configuration options for the module, e.g. 'ERROR_RATE 0.01 INITIAL_SIZE 400'.
        """
        return pulumi.get(self, "args")

    @args.setter
    def args(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "args", value)


if not MYPY:
    class PersistenceArgsDict(TypedDict):
        """
        Persistence-related configuration for the RedisEnterprise database
        """
        aof_enabled: NotRequired[pulumi.Input[bool]]
        """
        Sets whether AOF is enabled.
        """
        aof_frequency: NotRequired[pulumi.Input[Union[str, 'AofFrequency']]]
        """
        Sets the frequency at which data is written to disk.
        """
        rdb_enabled: NotRequired[pulumi.Input[bool]]
        """
        Sets whether RDB is enabled.
        """
        rdb_frequency: NotRequired[pulumi.Input[Union[str, 'RdbFrequency']]]
        """
        Sets the frequency at which a snapshot of the database is created.
        """
elif False:
    PersistenceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PersistenceArgs:
    def __init__(__self__, *,
                 aof_enabled: Optional[pulumi.Input[bool]] = None,
                 aof_frequency: Optional[pulumi.Input[Union[str, 'AofFrequency']]] = None,
                 rdb_enabled: Optional[pulumi.Input[bool]] = None,
                 rdb_frequency: Optional[pulumi.Input[Union[str, 'RdbFrequency']]] = None):
        """
        Persistence-related configuration for the RedisEnterprise database
        :param pulumi.Input[bool] aof_enabled: Sets whether AOF is enabled.
        :param pulumi.Input[Union[str, 'AofFrequency']] aof_frequency: Sets the frequency at which data is written to disk.
        :param pulumi.Input[bool] rdb_enabled: Sets whether RDB is enabled.
        :param pulumi.Input[Union[str, 'RdbFrequency']] rdb_frequency: Sets the frequency at which a snapshot of the database is created.
        """
        if aof_enabled is not None:
            pulumi.set(__self__, "aof_enabled", aof_enabled)
        if aof_frequency is not None:
            pulumi.set(__self__, "aof_frequency", aof_frequency)
        if rdb_enabled is not None:
            pulumi.set(__self__, "rdb_enabled", rdb_enabled)
        if rdb_frequency is not None:
            pulumi.set(__self__, "rdb_frequency", rdb_frequency)

    @property
    @pulumi.getter(name="aofEnabled")
    def aof_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Sets whether AOF is enabled.
        """
        return pulumi.get(self, "aof_enabled")

    @aof_enabled.setter
    def aof_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "aof_enabled", value)

    @property
    @pulumi.getter(name="aofFrequency")
    def aof_frequency(self) -> Optional[pulumi.Input[Union[str, 'AofFrequency']]]:
        """
        Sets the frequency at which data is written to disk.
        """
        return pulumi.get(self, "aof_frequency")

    @aof_frequency.setter
    def aof_frequency(self, value: Optional[pulumi.Input[Union[str, 'AofFrequency']]]):
        pulumi.set(self, "aof_frequency", value)

    @property
    @pulumi.getter(name="rdbEnabled")
    def rdb_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Sets whether RDB is enabled.
        """
        return pulumi.get(self, "rdb_enabled")

    @rdb_enabled.setter
    def rdb_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "rdb_enabled", value)

    @property
    @pulumi.getter(name="rdbFrequency")
    def rdb_frequency(self) -> Optional[pulumi.Input[Union[str, 'RdbFrequency']]]:
        """
        Sets the frequency at which a snapshot of the database is created.
        """
        return pulumi.get(self, "rdb_frequency")

    @rdb_frequency.setter
    def rdb_frequency(self, value: Optional[pulumi.Input[Union[str, 'RdbFrequency']]]):
        pulumi.set(self, "rdb_frequency", value)


if not MYPY:
    class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        actions_required: NotRequired[pulumi.Input[str]]
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        description: NotRequired[pulumi.Input[str]]
        """
        The reason for approval/rejection of the connection.
        """
        status: NotRequired[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
elif False:
    PrivateLinkServiceConnectionStateArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 actions_required: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[str] actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param pulumi.Input[str] description: The reason for approval/rejection of the connection.
        :param pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']] status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[str]]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "actions_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'PrivateEndpointServiceConnectionStatus']]]):
        pulumi.set(self, "status", value)


