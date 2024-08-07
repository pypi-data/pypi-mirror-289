# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AnalyticalStorageSchemaType',
    'AuthenticationMethod',
    'AutoReplicate',
    'AzureConnectionType',
    'BackupPolicyMigrationStatus',
    'BackupPolicyType',
    'BackupStorageRedundancy',
    'ClusterType',
    'CompositePathSortOrder',
    'ConflictResolutionMode',
    'ConnectorOffer',
    'ContinuousTier',
    'CreateMode',
    'DataType',
    'DatabaseAccountKind',
    'DatabaseAccountOfferType',
    'DefaultConsistencyLevel',
    'DefaultPriorityLevel',
    'EnableFullTextQuery',
    'IndexKind',
    'IndexingMode',
    'ManagedCassandraProvisioningState',
    'ManagedCassandraResourceIdentityType',
    'MinimalTlsVersion',
    'MongoRoleDefinitionType',
    'NetworkAclBypass',
    'NodeKind',
    'PartitionKind',
    'PublicNetworkAccess',
    'ResourceIdentityType',
    'RestoreMode',
    'RoleDefinitionType',
    'ScheduledEventStrategy',
    'ServerVersion',
    'ServiceSize',
    'ServiceType',
    'SpatialType',
    'TriggerOperation',
    'TriggerType',
]


class AnalyticalStorageSchemaType(str, Enum):
    """
    Describes the types of schema for analytical storage.
    """
    WELL_DEFINED = "WellDefined"
    FULL_FIDELITY = "FullFidelity"


class AuthenticationMethod(str, Enum):
    """
    Which authentication method Cassandra should use to authenticate clients. 'None' turns off authentication, so should not be used except in emergencies. 'Cassandra' is the default password based authentication. The default is 'Cassandra'.
    """
    NONE = "None"
    CASSANDRA = "Cassandra"
    LDAP = "Ldap"


class AutoReplicate(str, Enum):
    """
    The form of AutoReplicate that is being used by this cluster.
    """
    NONE = "None"
    SYSTEM_KEYSPACES = "SystemKeyspaces"
    ALL_KEYSPACES = "AllKeyspaces"


class AzureConnectionType(str, Enum):
    """
    How to connect to the azure services needed for running the cluster
    """
    NONE = "None"
    VPN = "VPN"


class BackupPolicyMigrationStatus(str, Enum):
    """
    Describes the status of migration between backup policy types.
    """
    INVALID = "Invalid"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    FAILED = "Failed"


class BackupPolicyType(str, Enum):
    """
    Describes the mode of backups.
    """
    PERIODIC = "Periodic"
    CONTINUOUS = "Continuous"


class BackupStorageRedundancy(str, Enum):
    """
    Enum to indicate type of backup residency
    """
    GEO = "Geo"
    LOCAL = "Local"
    ZONE = "Zone"


class ClusterType(str, Enum):
    """
    Type of the cluster. If set to Production, some operations might not be permitted on cluster.
    """
    PRODUCTION = "Production"
    NON_PRODUCTION = "NonProduction"


class CompositePathSortOrder(str, Enum):
    """
    Sort order for composite paths.
    """
    ASCENDING = "ascending"
    DESCENDING = "descending"


class ConflictResolutionMode(str, Enum):
    """
    Indicates the conflict resolution mode.
    """
    LAST_WRITER_WINS = "LastWriterWins"
    CUSTOM = "Custom"


class ConnectorOffer(str, Enum):
    """
    The cassandra connector offer type for the Cosmos DB database C* account.
    """
    SMALL = "Small"


class ContinuousTier(str, Enum):
    """
    Enum to indicate type of Continuos backup mode
    """
    CONTINUOUS7_DAYS = "Continuous7Days"
    CONTINUOUS30_DAYS = "Continuous30Days"


class CreateMode(str, Enum):
    """
    Enum to indicate the mode of resource creation.
    """
    DEFAULT = "Default"
    RESTORE = "Restore"


class DataType(str, Enum):
    """
    The datatype for which the indexing behavior is applied to.
    """
    STRING = "String"
    NUMBER = "Number"
    POINT = "Point"
    POLYGON = "Polygon"
    LINE_STRING = "LineString"
    MULTI_POLYGON = "MultiPolygon"


class DatabaseAccountKind(str, Enum):
    """
    Indicates the type of database account. This can only be set at database account creation.
    """
    GLOBAL_DOCUMENT_DB = "GlobalDocumentDB"
    MONGO_DB = "MongoDB"
    PARSE = "Parse"


class DatabaseAccountOfferType(str, Enum):
    """
    The offer type for the database
    """
    STANDARD = "Standard"


class DefaultConsistencyLevel(str, Enum):
    """
    The default consistency level and configuration settings of the Cosmos DB account.
    """
    EVENTUAL = "Eventual"
    SESSION = "Session"
    BOUNDED_STALENESS = "BoundedStaleness"
    STRONG = "Strong"
    CONSISTENT_PREFIX = "ConsistentPrefix"


class DefaultPriorityLevel(str, Enum):
    """
    Enum to indicate default Priority Level of request for Priority Based Execution.
    """
    HIGH = "High"
    LOW = "Low"


class EnableFullTextQuery(str, Enum):
    """
    Describe the level of detail with which queries are to be logged.
    """
    NONE = "None"
    TRUE = "True"
    FALSE = "False"


class IndexKind(str, Enum):
    """
    Indicates the type of index.
    """
    HASH = "Hash"
    RANGE = "Range"
    SPATIAL = "Spatial"


class IndexingMode(str, Enum):
    """
    Indicates the indexing mode.
    """
    CONSISTENT = "consistent"
    LAZY = "lazy"
    NONE = "none"


class ManagedCassandraProvisioningState(str, Enum):
    """
    The status of the resource at the time the operation was called.
    """
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"


class ManagedCassandraResourceIdentityType(str, Enum):
    """
    The type of the resource.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    NONE = "None"


class MinimalTlsVersion(str, Enum):
    """
    Indicates the minimum allowed Tls version. The default is Tls 1.0, except for Cassandra and Mongo API's, which only work with Tls 1.2.
    """
    TLS = "Tls"
    TLS11 = "Tls11"
    TLS12 = "Tls12"


class MongoRoleDefinitionType(str, Enum):
    """
    Indicates whether the Role Definition was built-in or user created.
    """
    BUILT_IN_ROLE = "BuiltInRole"
    CUSTOM_ROLE = "CustomRole"


class NetworkAclBypass(str, Enum):
    """
    Indicates what services are allowed to bypass firewall checks.
    """
    NONE = "None"
    AZURE_SERVICES = "AzureServices"


class NodeKind(str, Enum):
    """
    The node type deployed in the node group.
    """
    SHARD = "Shard"


class PartitionKind(str, Enum):
    """
    Indicates the kind of algorithm used for partitioning. For MultiHash, multiple partition keys (upto three maximum) are supported for container create
    """
    HASH = "Hash"
    RANGE = "Range"
    MULTI_HASH = "MultiHash"


class PublicNetworkAccess(str, Enum):
    """
    Whether requests from Public Network are allowed
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    SECURED_BY_PERIMETER = "SecuredByPerimeter"


class ResourceIdentityType(str, Enum):
    """
    The type of identity used for the resource. The type 'SystemAssigned,UserAssigned' includes both an implicitly created identity and a set of user assigned identities. The type 'None' will remove any identities from the service.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"
    NONE = "None"


class RestoreMode(str, Enum):
    """
    Describes the mode of the restore.
    """
    POINT_IN_TIME = "PointInTime"


class RoleDefinitionType(str, Enum):
    """
    Indicates whether the Role Definition was built-in or user created.
    """
    BUILT_IN_ROLE = "BuiltInRole"
    CUSTOM_ROLE = "CustomRole"


class ScheduledEventStrategy(str, Enum):
    """
    How the nodes in the cluster react to scheduled events
    """
    IGNORE = "Ignore"
    STOP_ANY = "StopAny"
    STOP_BY_RACK = "StopByRack"


class ServerVersion(str, Enum):
    """
    Describes the ServerVersion of an a MongoDB account.
    """
    SERVER_VERSION_3_2 = "3.2"
    SERVER_VERSION_3_6 = "3.6"
    SERVER_VERSION_4_0 = "4.0"
    SERVER_VERSION_4_2 = "4.2"


class ServiceSize(str, Enum):
    """
    Instance type for the service.
    """
    COSMOS_D4S = "Cosmos.D4s"
    COSMOS_D8S = "Cosmos.D8s"
    COSMOS_D16S = "Cosmos.D16s"


class ServiceType(str, Enum):
    """
    ServiceType for the service.
    """
    SQL_DEDICATED_GATEWAY = "SqlDedicatedGateway"
    DATA_TRANSFER = "DataTransfer"
    GRAPH_API_COMPUTE = "GraphAPICompute"
    MATERIALIZED_VIEWS_BUILDER = "MaterializedViewsBuilder"


class SpatialType(str, Enum):
    """
    Indicates the spatial type of index.
    """
    POINT = "Point"
    LINE_STRING = "LineString"
    POLYGON = "Polygon"
    MULTI_POLYGON = "MultiPolygon"


class TriggerOperation(str, Enum):
    """
    The operation the trigger is associated with
    """
    ALL = "All"
    CREATE = "Create"
    UPDATE = "Update"
    DELETE = "Delete"
    REPLACE = "Replace"


class TriggerType(str, Enum):
    """
    Type of the Trigger
    """
    PRE = "Pre"
    POST = "Post"
