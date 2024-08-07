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

__all__ = [
    'GetStorageAccountResult',
    'AwaitableGetStorageAccountResult',
    'get_storage_account',
    'get_storage_account_output',
]

@pulumi.output_type
class GetStorageAccountResult:
    """
    The storage account.
    """
    def __init__(__self__, access_tier=None, account_migration_in_progress=None, allow_blob_public_access=None, allow_cross_tenant_replication=None, allow_shared_key_access=None, allowed_copy_scope=None, azure_files_identity_based_authentication=None, blob_restore_status=None, creation_time=None, custom_domain=None, default_to_o_auth_authentication=None, dns_endpoint_type=None, enable_https_traffic_only=None, enable_nfs_v3=None, encryption=None, extended_location=None, failover_in_progress=None, geo_replication_stats=None, id=None, identity=None, immutable_storage_with_versioning=None, is_hns_enabled=None, is_local_user_enabled=None, is_sftp_enabled=None, is_sku_conversion_blocked=None, key_creation_time=None, key_policy=None, kind=None, large_file_shares_state=None, last_geo_failover_time=None, location=None, minimum_tls_version=None, name=None, network_rule_set=None, primary_endpoints=None, primary_location=None, private_endpoint_connections=None, provisioning_state=None, public_network_access=None, routing_preference=None, sas_policy=None, secondary_endpoints=None, secondary_location=None, sku=None, status_of_primary=None, status_of_secondary=None, storage_account_sku_conversion_status=None, tags=None, type=None):
        if access_tier and not isinstance(access_tier, str):
            raise TypeError("Expected argument 'access_tier' to be a str")
        pulumi.set(__self__, "access_tier", access_tier)
        if account_migration_in_progress and not isinstance(account_migration_in_progress, bool):
            raise TypeError("Expected argument 'account_migration_in_progress' to be a bool")
        pulumi.set(__self__, "account_migration_in_progress", account_migration_in_progress)
        if allow_blob_public_access and not isinstance(allow_blob_public_access, bool):
            raise TypeError("Expected argument 'allow_blob_public_access' to be a bool")
        pulumi.set(__self__, "allow_blob_public_access", allow_blob_public_access)
        if allow_cross_tenant_replication and not isinstance(allow_cross_tenant_replication, bool):
            raise TypeError("Expected argument 'allow_cross_tenant_replication' to be a bool")
        pulumi.set(__self__, "allow_cross_tenant_replication", allow_cross_tenant_replication)
        if allow_shared_key_access and not isinstance(allow_shared_key_access, bool):
            raise TypeError("Expected argument 'allow_shared_key_access' to be a bool")
        pulumi.set(__self__, "allow_shared_key_access", allow_shared_key_access)
        if allowed_copy_scope and not isinstance(allowed_copy_scope, str):
            raise TypeError("Expected argument 'allowed_copy_scope' to be a str")
        pulumi.set(__self__, "allowed_copy_scope", allowed_copy_scope)
        if azure_files_identity_based_authentication and not isinstance(azure_files_identity_based_authentication, dict):
            raise TypeError("Expected argument 'azure_files_identity_based_authentication' to be a dict")
        pulumi.set(__self__, "azure_files_identity_based_authentication", azure_files_identity_based_authentication)
        if blob_restore_status and not isinstance(blob_restore_status, dict):
            raise TypeError("Expected argument 'blob_restore_status' to be a dict")
        pulumi.set(__self__, "blob_restore_status", blob_restore_status)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if custom_domain and not isinstance(custom_domain, dict):
            raise TypeError("Expected argument 'custom_domain' to be a dict")
        pulumi.set(__self__, "custom_domain", custom_domain)
        if default_to_o_auth_authentication and not isinstance(default_to_o_auth_authentication, bool):
            raise TypeError("Expected argument 'default_to_o_auth_authentication' to be a bool")
        pulumi.set(__self__, "default_to_o_auth_authentication", default_to_o_auth_authentication)
        if dns_endpoint_type and not isinstance(dns_endpoint_type, str):
            raise TypeError("Expected argument 'dns_endpoint_type' to be a str")
        pulumi.set(__self__, "dns_endpoint_type", dns_endpoint_type)
        if enable_https_traffic_only and not isinstance(enable_https_traffic_only, bool):
            raise TypeError("Expected argument 'enable_https_traffic_only' to be a bool")
        pulumi.set(__self__, "enable_https_traffic_only", enable_https_traffic_only)
        if enable_nfs_v3 and not isinstance(enable_nfs_v3, bool):
            raise TypeError("Expected argument 'enable_nfs_v3' to be a bool")
        pulumi.set(__self__, "enable_nfs_v3", enable_nfs_v3)
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if failover_in_progress and not isinstance(failover_in_progress, bool):
            raise TypeError("Expected argument 'failover_in_progress' to be a bool")
        pulumi.set(__self__, "failover_in_progress", failover_in_progress)
        if geo_replication_stats and not isinstance(geo_replication_stats, dict):
            raise TypeError("Expected argument 'geo_replication_stats' to be a dict")
        pulumi.set(__self__, "geo_replication_stats", geo_replication_stats)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if immutable_storage_with_versioning and not isinstance(immutable_storage_with_versioning, dict):
            raise TypeError("Expected argument 'immutable_storage_with_versioning' to be a dict")
        pulumi.set(__self__, "immutable_storage_with_versioning", immutable_storage_with_versioning)
        if is_hns_enabled and not isinstance(is_hns_enabled, bool):
            raise TypeError("Expected argument 'is_hns_enabled' to be a bool")
        pulumi.set(__self__, "is_hns_enabled", is_hns_enabled)
        if is_local_user_enabled and not isinstance(is_local_user_enabled, bool):
            raise TypeError("Expected argument 'is_local_user_enabled' to be a bool")
        pulumi.set(__self__, "is_local_user_enabled", is_local_user_enabled)
        if is_sftp_enabled and not isinstance(is_sftp_enabled, bool):
            raise TypeError("Expected argument 'is_sftp_enabled' to be a bool")
        pulumi.set(__self__, "is_sftp_enabled", is_sftp_enabled)
        if is_sku_conversion_blocked and not isinstance(is_sku_conversion_blocked, bool):
            raise TypeError("Expected argument 'is_sku_conversion_blocked' to be a bool")
        pulumi.set(__self__, "is_sku_conversion_blocked", is_sku_conversion_blocked)
        if key_creation_time and not isinstance(key_creation_time, dict):
            raise TypeError("Expected argument 'key_creation_time' to be a dict")
        pulumi.set(__self__, "key_creation_time", key_creation_time)
        if key_policy and not isinstance(key_policy, dict):
            raise TypeError("Expected argument 'key_policy' to be a dict")
        pulumi.set(__self__, "key_policy", key_policy)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if large_file_shares_state and not isinstance(large_file_shares_state, str):
            raise TypeError("Expected argument 'large_file_shares_state' to be a str")
        pulumi.set(__self__, "large_file_shares_state", large_file_shares_state)
        if last_geo_failover_time and not isinstance(last_geo_failover_time, str):
            raise TypeError("Expected argument 'last_geo_failover_time' to be a str")
        pulumi.set(__self__, "last_geo_failover_time", last_geo_failover_time)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if minimum_tls_version and not isinstance(minimum_tls_version, str):
            raise TypeError("Expected argument 'minimum_tls_version' to be a str")
        pulumi.set(__self__, "minimum_tls_version", minimum_tls_version)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_rule_set and not isinstance(network_rule_set, dict):
            raise TypeError("Expected argument 'network_rule_set' to be a dict")
        pulumi.set(__self__, "network_rule_set", network_rule_set)
        if primary_endpoints and not isinstance(primary_endpoints, dict):
            raise TypeError("Expected argument 'primary_endpoints' to be a dict")
        pulumi.set(__self__, "primary_endpoints", primary_endpoints)
        if primary_location and not isinstance(primary_location, str):
            raise TypeError("Expected argument 'primary_location' to be a str")
        pulumi.set(__self__, "primary_location", primary_location)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if routing_preference and not isinstance(routing_preference, dict):
            raise TypeError("Expected argument 'routing_preference' to be a dict")
        pulumi.set(__self__, "routing_preference", routing_preference)
        if sas_policy and not isinstance(sas_policy, dict):
            raise TypeError("Expected argument 'sas_policy' to be a dict")
        pulumi.set(__self__, "sas_policy", sas_policy)
        if secondary_endpoints and not isinstance(secondary_endpoints, dict):
            raise TypeError("Expected argument 'secondary_endpoints' to be a dict")
        pulumi.set(__self__, "secondary_endpoints", secondary_endpoints)
        if secondary_location and not isinstance(secondary_location, str):
            raise TypeError("Expected argument 'secondary_location' to be a str")
        pulumi.set(__self__, "secondary_location", secondary_location)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if status_of_primary and not isinstance(status_of_primary, str):
            raise TypeError("Expected argument 'status_of_primary' to be a str")
        pulumi.set(__self__, "status_of_primary", status_of_primary)
        if status_of_secondary and not isinstance(status_of_secondary, str):
            raise TypeError("Expected argument 'status_of_secondary' to be a str")
        pulumi.set(__self__, "status_of_secondary", status_of_secondary)
        if storage_account_sku_conversion_status and not isinstance(storage_account_sku_conversion_status, dict):
            raise TypeError("Expected argument 'storage_account_sku_conversion_status' to be a dict")
        pulumi.set(__self__, "storage_account_sku_conversion_status", storage_account_sku_conversion_status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accessTier")
    def access_tier(self) -> str:
        """
        Required for storage accounts where kind = BlobStorage. The access tier is used for billing. The 'Premium' access tier is the default value for premium block blobs storage account type and it cannot be changed for the premium block blobs storage account type.
        """
        return pulumi.get(self, "access_tier")

    @property
    @pulumi.getter(name="accountMigrationInProgress")
    def account_migration_in_progress(self) -> bool:
        """
        If customer initiated account migration is in progress, the value will be true else it will be null.
        """
        return pulumi.get(self, "account_migration_in_progress")

    @property
    @pulumi.getter(name="allowBlobPublicAccess")
    def allow_blob_public_access(self) -> Optional[bool]:
        """
        Allow or disallow public access to all blobs or containers in the storage account. The default interpretation is false for this property.
        """
        return pulumi.get(self, "allow_blob_public_access")

    @property
    @pulumi.getter(name="allowCrossTenantReplication")
    def allow_cross_tenant_replication(self) -> Optional[bool]:
        """
        Allow or disallow cross AAD tenant object replication. Set this property to true for new or existing accounts only if object replication policies will involve storage accounts in different AAD tenants. The default interpretation is false for new accounts to follow best security practices by default.
        """
        return pulumi.get(self, "allow_cross_tenant_replication")

    @property
    @pulumi.getter(name="allowSharedKeyAccess")
    def allow_shared_key_access(self) -> Optional[bool]:
        """
        Indicates whether the storage account permits requests to be authorized with the account access key via Shared Key. If false, then all requests, including shared access signatures, must be authorized with Azure Active Directory (Azure AD). The default value is null, which is equivalent to true.
        """
        return pulumi.get(self, "allow_shared_key_access")

    @property
    @pulumi.getter(name="allowedCopyScope")
    def allowed_copy_scope(self) -> Optional[str]:
        """
        Restrict copy to and from Storage Accounts within an AAD tenant or with Private Links to the same VNet.
        """
        return pulumi.get(self, "allowed_copy_scope")

    @property
    @pulumi.getter(name="azureFilesIdentityBasedAuthentication")
    def azure_files_identity_based_authentication(self) -> Optional['outputs.AzureFilesIdentityBasedAuthenticationResponse']:
        """
        Provides the identity based authentication settings for Azure Files.
        """
        return pulumi.get(self, "azure_files_identity_based_authentication")

    @property
    @pulumi.getter(name="blobRestoreStatus")
    def blob_restore_status(self) -> 'outputs.BlobRestoreStatusResponse':
        """
        Blob restore status
        """
        return pulumi.get(self, "blob_restore_status")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        Gets the creation date and time of the storage account in UTC.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> 'outputs.CustomDomainResponse':
        """
        Gets the custom domain the user assigned to this storage account.
        """
        return pulumi.get(self, "custom_domain")

    @property
    @pulumi.getter(name="defaultToOAuthAuthentication")
    def default_to_o_auth_authentication(self) -> Optional[bool]:
        """
        A boolean flag which indicates whether the default authentication is OAuth or not. The default interpretation is false for this property.
        """
        return pulumi.get(self, "default_to_o_auth_authentication")

    @property
    @pulumi.getter(name="dnsEndpointType")
    def dns_endpoint_type(self) -> Optional[str]:
        """
        Allows you to specify the type of endpoint. Set this to AzureDNSZone to create a large number of accounts in a single subscription, which creates accounts in an Azure DNS Zone and the endpoint URL will have an alphanumeric DNS Zone identifier.
        """
        return pulumi.get(self, "dns_endpoint_type")

    @property
    @pulumi.getter(name="enableHttpsTrafficOnly")
    def enable_https_traffic_only(self) -> Optional[bool]:
        """
        Allows https traffic only to storage service if sets to true.
        """
        return pulumi.get(self, "enable_https_traffic_only")

    @property
    @pulumi.getter(name="enableNfsV3")
    def enable_nfs_v3(self) -> Optional[bool]:
        """
        NFS 3.0 protocol support enabled if set to true.
        """
        return pulumi.get(self, "enable_nfs_v3")

    @property
    @pulumi.getter
    def encryption(self) -> 'outputs.EncryptionResponse':
        """
        Encryption settings to be used for server-side encryption for the storage account.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        The extendedLocation of the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="failoverInProgress")
    def failover_in_progress(self) -> bool:
        """
        If the failover is in progress, the value will be true, otherwise, it will be null.
        """
        return pulumi.get(self, "failover_in_progress")

    @property
    @pulumi.getter(name="geoReplicationStats")
    def geo_replication_stats(self) -> 'outputs.GeoReplicationStatsResponse':
        """
        Geo Replication Stats
        """
        return pulumi.get(self, "geo_replication_stats")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="immutableStorageWithVersioning")
    def immutable_storage_with_versioning(self) -> Optional['outputs.ImmutableStorageAccountResponse']:
        """
        The property is immutable and can only be set to true at the account creation time. When set to true, it enables object level immutability for all the containers in the account by default.
        """
        return pulumi.get(self, "immutable_storage_with_versioning")

    @property
    @pulumi.getter(name="isHnsEnabled")
    def is_hns_enabled(self) -> Optional[bool]:
        """
        Account HierarchicalNamespace enabled if sets to true.
        """
        return pulumi.get(self, "is_hns_enabled")

    @property
    @pulumi.getter(name="isLocalUserEnabled")
    def is_local_user_enabled(self) -> Optional[bool]:
        """
        Enables local users feature, if set to true
        """
        return pulumi.get(self, "is_local_user_enabled")

    @property
    @pulumi.getter(name="isSftpEnabled")
    def is_sftp_enabled(self) -> Optional[bool]:
        """
        Enables Secure File Transfer Protocol, if set to true
        """
        return pulumi.get(self, "is_sftp_enabled")

    @property
    @pulumi.getter(name="isSkuConversionBlocked")
    def is_sku_conversion_blocked(self) -> bool:
        """
        This property will be set to true or false on an event of ongoing migration. Default value is null.
        """
        return pulumi.get(self, "is_sku_conversion_blocked")

    @property
    @pulumi.getter(name="keyCreationTime")
    def key_creation_time(self) -> 'outputs.KeyCreationTimeResponse':
        """
        Storage account keys creation time.
        """
        return pulumi.get(self, "key_creation_time")

    @property
    @pulumi.getter(name="keyPolicy")
    def key_policy(self) -> 'outputs.KeyPolicyResponse':
        """
        KeyPolicy assigned to the storage account.
        """
        return pulumi.get(self, "key_policy")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Gets the Kind.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="largeFileSharesState")
    def large_file_shares_state(self) -> Optional[str]:
        """
        Allow large file shares if sets to Enabled. It cannot be disabled once it is enabled.
        """
        return pulumi.get(self, "large_file_shares_state")

    @property
    @pulumi.getter(name="lastGeoFailoverTime")
    def last_geo_failover_time(self) -> str:
        """
        Gets the timestamp of the most recent instance of a failover to the secondary location. Only the most recent timestamp is retained. This element is not returned if there has never been a failover instance. Only available if the accountType is Standard_GRS or Standard_RAGRS.
        """
        return pulumi.get(self, "last_geo_failover_time")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> Optional[str]:
        """
        Set the minimum TLS version to be permitted on requests to storage. The default interpretation is TLS 1.0 for this property.
        """
        return pulumi.get(self, "minimum_tls_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkRuleSet")
    def network_rule_set(self) -> 'outputs.NetworkRuleSetResponse':
        """
        Network rule set
        """
        return pulumi.get(self, "network_rule_set")

    @property
    @pulumi.getter(name="primaryEndpoints")
    def primary_endpoints(self) -> 'outputs.EndpointsResponse':
        """
        Gets the URLs that are used to perform a retrieval of a public blob, queue, or table object. Note that Standard_ZRS and Premium_LRS accounts only return the blob endpoint.
        """
        return pulumi.get(self, "primary_endpoints")

    @property
    @pulumi.getter(name="primaryLocation")
    def primary_location(self) -> str:
        """
        Gets the location of the primary data center for the storage account.
        """
        return pulumi.get(self, "primary_location")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        """
        List of private endpoint connection associated with the specified storage account
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets the status of the storage account at the time the operation was called.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Allow, disallow, or let Network Security Perimeter configuration to evaluate public network access to Storage Account.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="routingPreference")
    def routing_preference(self) -> Optional['outputs.RoutingPreferenceResponse']:
        """
        Maintains information about the network routing choice opted by the user for data transfer
        """
        return pulumi.get(self, "routing_preference")

    @property
    @pulumi.getter(name="sasPolicy")
    def sas_policy(self) -> 'outputs.SasPolicyResponse':
        """
        SasPolicy assigned to the storage account.
        """
        return pulumi.get(self, "sas_policy")

    @property
    @pulumi.getter(name="secondaryEndpoints")
    def secondary_endpoints(self) -> 'outputs.EndpointsResponse':
        """
        Gets the URLs that are used to perform a retrieval of a public blob, queue, or table object from the secondary location of the storage account. Only available if the SKU name is Standard_RAGRS.
        """
        return pulumi.get(self, "secondary_endpoints")

    @property
    @pulumi.getter(name="secondaryLocation")
    def secondary_location(self) -> str:
        """
        Gets the location of the geo-replicated secondary for the storage account. Only available if the accountType is Standard_GRS or Standard_RAGRS.
        """
        return pulumi.get(self, "secondary_location")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.SkuResponse':
        """
        Gets the SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="statusOfPrimary")
    def status_of_primary(self) -> str:
        """
        Gets the status indicating whether the primary location of the storage account is available or unavailable.
        """
        return pulumi.get(self, "status_of_primary")

    @property
    @pulumi.getter(name="statusOfSecondary")
    def status_of_secondary(self) -> str:
        """
        Gets the status indicating whether the secondary location of the storage account is available or unavailable. Only available if the SKU name is Standard_GRS or Standard_RAGRS.
        """
        return pulumi.get(self, "status_of_secondary")

    @property
    @pulumi.getter(name="storageAccountSkuConversionStatus")
    def storage_account_sku_conversion_status(self) -> Optional['outputs.StorageAccountSkuConversionStatusResponse']:
        """
        This property is readOnly and is set by server during asynchronous storage account sku conversion operations.
        """
        return pulumi.get(self, "storage_account_sku_conversion_status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetStorageAccountResult(GetStorageAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStorageAccountResult(
            access_tier=self.access_tier,
            account_migration_in_progress=self.account_migration_in_progress,
            allow_blob_public_access=self.allow_blob_public_access,
            allow_cross_tenant_replication=self.allow_cross_tenant_replication,
            allow_shared_key_access=self.allow_shared_key_access,
            allowed_copy_scope=self.allowed_copy_scope,
            azure_files_identity_based_authentication=self.azure_files_identity_based_authentication,
            blob_restore_status=self.blob_restore_status,
            creation_time=self.creation_time,
            custom_domain=self.custom_domain,
            default_to_o_auth_authentication=self.default_to_o_auth_authentication,
            dns_endpoint_type=self.dns_endpoint_type,
            enable_https_traffic_only=self.enable_https_traffic_only,
            enable_nfs_v3=self.enable_nfs_v3,
            encryption=self.encryption,
            extended_location=self.extended_location,
            failover_in_progress=self.failover_in_progress,
            geo_replication_stats=self.geo_replication_stats,
            id=self.id,
            identity=self.identity,
            immutable_storage_with_versioning=self.immutable_storage_with_versioning,
            is_hns_enabled=self.is_hns_enabled,
            is_local_user_enabled=self.is_local_user_enabled,
            is_sftp_enabled=self.is_sftp_enabled,
            is_sku_conversion_blocked=self.is_sku_conversion_blocked,
            key_creation_time=self.key_creation_time,
            key_policy=self.key_policy,
            kind=self.kind,
            large_file_shares_state=self.large_file_shares_state,
            last_geo_failover_time=self.last_geo_failover_time,
            location=self.location,
            minimum_tls_version=self.minimum_tls_version,
            name=self.name,
            network_rule_set=self.network_rule_set,
            primary_endpoints=self.primary_endpoints,
            primary_location=self.primary_location,
            private_endpoint_connections=self.private_endpoint_connections,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            routing_preference=self.routing_preference,
            sas_policy=self.sas_policy,
            secondary_endpoints=self.secondary_endpoints,
            secondary_location=self.secondary_location,
            sku=self.sku,
            status_of_primary=self.status_of_primary,
            status_of_secondary=self.status_of_secondary,
            storage_account_sku_conversion_status=self.storage_account_sku_conversion_status,
            tags=self.tags,
            type=self.type)


def get_storage_account(account_name: Optional[str] = None,
                        expand: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStorageAccountResult:
    """
    Returns the properties for the specified storage account including but not limited to name, SKU name, location, and account status. The ListKeys operation should be used to retrieve storage keys.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str expand: May be used to expand the properties within account's properties. By default, data is not included when fetching properties. Currently we only support geoReplicationStats and blobRestoreStatus.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storage/v20230401:getStorageAccount', __args__, opts=opts, typ=GetStorageAccountResult).value

    return AwaitableGetStorageAccountResult(
        access_tier=pulumi.get(__ret__, 'access_tier'),
        account_migration_in_progress=pulumi.get(__ret__, 'account_migration_in_progress'),
        allow_blob_public_access=pulumi.get(__ret__, 'allow_blob_public_access'),
        allow_cross_tenant_replication=pulumi.get(__ret__, 'allow_cross_tenant_replication'),
        allow_shared_key_access=pulumi.get(__ret__, 'allow_shared_key_access'),
        allowed_copy_scope=pulumi.get(__ret__, 'allowed_copy_scope'),
        azure_files_identity_based_authentication=pulumi.get(__ret__, 'azure_files_identity_based_authentication'),
        blob_restore_status=pulumi.get(__ret__, 'blob_restore_status'),
        creation_time=pulumi.get(__ret__, 'creation_time'),
        custom_domain=pulumi.get(__ret__, 'custom_domain'),
        default_to_o_auth_authentication=pulumi.get(__ret__, 'default_to_o_auth_authentication'),
        dns_endpoint_type=pulumi.get(__ret__, 'dns_endpoint_type'),
        enable_https_traffic_only=pulumi.get(__ret__, 'enable_https_traffic_only'),
        enable_nfs_v3=pulumi.get(__ret__, 'enable_nfs_v3'),
        encryption=pulumi.get(__ret__, 'encryption'),
        extended_location=pulumi.get(__ret__, 'extended_location'),
        failover_in_progress=pulumi.get(__ret__, 'failover_in_progress'),
        geo_replication_stats=pulumi.get(__ret__, 'geo_replication_stats'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        immutable_storage_with_versioning=pulumi.get(__ret__, 'immutable_storage_with_versioning'),
        is_hns_enabled=pulumi.get(__ret__, 'is_hns_enabled'),
        is_local_user_enabled=pulumi.get(__ret__, 'is_local_user_enabled'),
        is_sftp_enabled=pulumi.get(__ret__, 'is_sftp_enabled'),
        is_sku_conversion_blocked=pulumi.get(__ret__, 'is_sku_conversion_blocked'),
        key_creation_time=pulumi.get(__ret__, 'key_creation_time'),
        key_policy=pulumi.get(__ret__, 'key_policy'),
        kind=pulumi.get(__ret__, 'kind'),
        large_file_shares_state=pulumi.get(__ret__, 'large_file_shares_state'),
        last_geo_failover_time=pulumi.get(__ret__, 'last_geo_failover_time'),
        location=pulumi.get(__ret__, 'location'),
        minimum_tls_version=pulumi.get(__ret__, 'minimum_tls_version'),
        name=pulumi.get(__ret__, 'name'),
        network_rule_set=pulumi.get(__ret__, 'network_rule_set'),
        primary_endpoints=pulumi.get(__ret__, 'primary_endpoints'),
        primary_location=pulumi.get(__ret__, 'primary_location'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        routing_preference=pulumi.get(__ret__, 'routing_preference'),
        sas_policy=pulumi.get(__ret__, 'sas_policy'),
        secondary_endpoints=pulumi.get(__ret__, 'secondary_endpoints'),
        secondary_location=pulumi.get(__ret__, 'secondary_location'),
        sku=pulumi.get(__ret__, 'sku'),
        status_of_primary=pulumi.get(__ret__, 'status_of_primary'),
        status_of_secondary=pulumi.get(__ret__, 'status_of_secondary'),
        storage_account_sku_conversion_status=pulumi.get(__ret__, 'storage_account_sku_conversion_status'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_storage_account)
def get_storage_account_output(account_name: Optional[pulumi.Input[str]] = None,
                               expand: Optional[pulumi.Input[Optional[str]]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStorageAccountResult]:
    """
    Returns the properties for the specified storage account including but not limited to name, SKU name, location, and account status. The ListKeys operation should be used to retrieve storage keys.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str expand: May be used to expand the properties within account's properties. By default, data is not included when fetching properties. Currently we only support geoReplicationStats and blobRestoreStatus.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    ...
