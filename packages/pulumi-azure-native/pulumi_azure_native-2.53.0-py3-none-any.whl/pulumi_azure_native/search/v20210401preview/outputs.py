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
from ._enums import *

__all__ = [
    'DataPlaneAadOrApiKeyAuthOptionResponse',
    'DataPlaneAuthOptionsResponse',
    'EncryptionWithCmkResponse',
    'IdentityResponse',
    'IpRuleResponse',
    'NetworkRuleSetResponse',
    'PrivateEndpointConnectionPropertiesResponse',
    'PrivateEndpointConnectionPropertiesResponsePrivateEndpoint',
    'PrivateEndpointConnectionPropertiesResponsePrivateLinkServiceConnectionState',
    'PrivateEndpointConnectionResponse',
    'QueryKeyResponse',
    'SharedPrivateLinkResourcePropertiesResponse',
    'SharedPrivateLinkResourceResponse',
    'SkuResponse',
    'UserAssignedManagedIdentityResponse',
]

@pulumi.output_type
class DataPlaneAadOrApiKeyAuthOptionResponse(dict):
    """
    Indicates that either the API key or an access token from Azure Active Directory can be used for authentication.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "aadAuthFailureMode":
            suggest = "aad_auth_failure_mode"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DataPlaneAadOrApiKeyAuthOptionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DataPlaneAadOrApiKeyAuthOptionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DataPlaneAadOrApiKeyAuthOptionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 aad_auth_failure_mode: Optional[str] = None):
        """
        Indicates that either the API key or an access token from Azure Active Directory can be used for authentication.
        :param str aad_auth_failure_mode: Describes what response the data plane API of a Search service would send for requests that failed authentication.
        """
        if aad_auth_failure_mode is not None:
            pulumi.set(__self__, "aad_auth_failure_mode", aad_auth_failure_mode)

    @property
    @pulumi.getter(name="aadAuthFailureMode")
    def aad_auth_failure_mode(self) -> Optional[str]:
        """
        Describes what response the data plane API of a Search service would send for requests that failed authentication.
        """
        return pulumi.get(self, "aad_auth_failure_mode")


@pulumi.output_type
class DataPlaneAuthOptionsResponse(dict):
    """
    Defines the options for how the data plane API of a Search service authenticates requests. This cannot be set if 'disableLocalAuth' is set to true.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "aadOrApiKey":
            suggest = "aad_or_api_key"
        elif key == "apiKeyOnly":
            suggest = "api_key_only"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DataPlaneAuthOptionsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DataPlaneAuthOptionsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DataPlaneAuthOptionsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 aad_or_api_key: Optional['outputs.DataPlaneAadOrApiKeyAuthOptionResponse'] = None,
                 api_key_only: Optional[Any] = None):
        """
        Defines the options for how the data plane API of a Search service authenticates requests. This cannot be set if 'disableLocalAuth' is set to true.
        :param 'DataPlaneAadOrApiKeyAuthOptionResponse' aad_or_api_key: Indicates that either the API key or an access token from Azure Active Directory can be used for authentication.
        :param Any api_key_only: Indicates that only the API key needs to be used for authentication.
        """
        if aad_or_api_key is not None:
            pulumi.set(__self__, "aad_or_api_key", aad_or_api_key)
        if api_key_only is not None:
            pulumi.set(__self__, "api_key_only", api_key_only)

    @property
    @pulumi.getter(name="aadOrApiKey")
    def aad_or_api_key(self) -> Optional['outputs.DataPlaneAadOrApiKeyAuthOptionResponse']:
        """
        Indicates that either the API key or an access token from Azure Active Directory can be used for authentication.
        """
        return pulumi.get(self, "aad_or_api_key")

    @property
    @pulumi.getter(name="apiKeyOnly")
    def api_key_only(self) -> Optional[Any]:
        """
        Indicates that only the API key needs to be used for authentication.
        """
        return pulumi.get(self, "api_key_only")


@pulumi.output_type
class EncryptionWithCmkResponse(dict):
    """
    Describes a policy that determines how resources within the search service are to be encrypted with Customer Managed Keys.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "encryptionComplianceStatus":
            suggest = "encryption_compliance_status"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EncryptionWithCmkResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EncryptionWithCmkResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EncryptionWithCmkResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 encryption_compliance_status: str,
                 enforcement: Optional[str] = None):
        """
        Describes a policy that determines how resources within the search service are to be encrypted with Customer Managed Keys.
        :param str encryption_compliance_status: Describes whether the search service is compliant or not with respect to having non customer encrypted resources. If a service has more than one non customer encrypted resource and 'Enforcement' is 'enabled' then the service will be marked as 'nonCompliant'.
        :param str enforcement: Describes how a search service should enforce having one or more non customer encrypted resources.
        """
        pulumi.set(__self__, "encryption_compliance_status", encryption_compliance_status)
        if enforcement is not None:
            pulumi.set(__self__, "enforcement", enforcement)

    @property
    @pulumi.getter(name="encryptionComplianceStatus")
    def encryption_compliance_status(self) -> str:
        """
        Describes whether the search service is compliant or not with respect to having non customer encrypted resources. If a service has more than one non customer encrypted resource and 'Enforcement' is 'enabled' then the service will be marked as 'nonCompliant'.
        """
        return pulumi.get(self, "encryption_compliance_status")

    @property
    @pulumi.getter
    def enforcement(self) -> Optional[str]:
        """
        Describes how a search service should enforce having one or more non customer encrypted resources.
        """
        return pulumi.get(self, "enforcement")


@pulumi.output_type
class IdentityResponse(dict):
    """
    Details about the search service identity. A null value indicates that the search service has no identity assigned.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"
        elif key == "userAssignedIdentities":
            suggest = "user_assigned_identities"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: str,
                 user_assigned_identities: Optional[Mapping[str, 'outputs.UserAssignedManagedIdentityResponse']] = None):
        """
        Details about the search service identity. A null value indicates that the search service has no identity assigned.
        :param str principal_id: The principal ID of the system-assigned identity of the search service.
        :param str tenant_id: The tenant ID of the system-assigned identity of the search service.
        :param str type: The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes both an identity created by the system and a set of user assigned identities. The type 'None' will remove all identities from the service.
        :param Mapping[str, 'UserAssignedManagedIdentityResponse'] user_assigned_identities: The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of the system-assigned identity of the search service.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of the system-assigned identity of the search service.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes both an identity created by the system and a set of user assigned identities. The type 'None' will remove all identities from the service.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, 'outputs.UserAssignedManagedIdentityResponse']]:
        """
        The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        return pulumi.get(self, "user_assigned_identities")


@pulumi.output_type
class IpRuleResponse(dict):
    """
    The IP restriction rule of the Azure Cognitive Search service.
    """
    def __init__(__self__, *,
                 value: Optional[str] = None):
        """
        The IP restriction rule of the Azure Cognitive Search service.
        :param str value: Value corresponding to a single IPv4 address (eg., 123.1.2.3) or an IP range in CIDR format (eg., 123.1.2.3/24) to be allowed.
        """
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Value corresponding to a single IPv4 address (eg., 123.1.2.3) or an IP range in CIDR format (eg., 123.1.2.3/24) to be allowed.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class NetworkRuleSetResponse(dict):
    """
    Network specific rules that determine how the Azure Cognitive Search service may be reached.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ipRules":
            suggest = "ip_rules"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NetworkRuleSetResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NetworkRuleSetResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NetworkRuleSetResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 bypass: Optional[str] = None,
                 ip_rules: Optional[Sequence['outputs.IpRuleResponse']] = None):
        """
        Network specific rules that determine how the Azure Cognitive Search service may be reached.
        :param str bypass: Possible origins of inbound traffic that can bypass the rules defined in the 'ipRules' section.
        :param Sequence['IpRuleResponse'] ip_rules: A list of IP restriction rules that defines the inbound network(s) with allowing access to the search service endpoint. At the meantime, all other public IP networks are blocked by the firewall. These restriction rules are applied only when the 'publicNetworkAccess' of the search service is 'enabled'; otherwise, traffic over public interface is not allowed even with any public IP rules, and private endpoint connections would be the exclusive access method.
        """
        if bypass is not None:
            pulumi.set(__self__, "bypass", bypass)
        if ip_rules is not None:
            pulumi.set(__self__, "ip_rules", ip_rules)

    @property
    @pulumi.getter
    def bypass(self) -> Optional[str]:
        """
        Possible origins of inbound traffic that can bypass the rules defined in the 'ipRules' section.
        """
        return pulumi.get(self, "bypass")

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[Sequence['outputs.IpRuleResponse']]:
        """
        A list of IP restriction rules that defines the inbound network(s) with allowing access to the search service endpoint. At the meantime, all other public IP networks are blocked by the firewall. These restriction rules are applied only when the 'publicNetworkAccess' of the search service is 'enabled'; otherwise, traffic over public interface is not allowed even with any public IP rules, and private endpoint connections would be the exclusive access method.
        """
        return pulumi.get(self, "ip_rules")


@pulumi.output_type
class PrivateEndpointConnectionPropertiesResponse(dict):
    """
    Describes the properties of an existing Private Endpoint connection to the Azure Cognitive Search service.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "privateEndpoint":
            suggest = "private_endpoint"
        elif key == "privateLinkServiceConnectionState":
            suggest = "private_link_service_connection_state"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateEndpointConnectionPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateEndpointConnectionPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateEndpointConnectionPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 private_endpoint: Optional['outputs.PrivateEndpointConnectionPropertiesResponsePrivateEndpoint'] = None,
                 private_link_service_connection_state: Optional['outputs.PrivateEndpointConnectionPropertiesResponsePrivateLinkServiceConnectionState'] = None):
        """
        Describes the properties of an existing Private Endpoint connection to the Azure Cognitive Search service.
        :param 'PrivateEndpointConnectionPropertiesResponsePrivateEndpoint' private_endpoint: The private endpoint resource from Microsoft.Network provider.
        :param 'PrivateEndpointConnectionPropertiesResponsePrivateLinkServiceConnectionState' private_link_service_connection_state: Describes the current state of an existing Private Link Service connection to the Azure Private Endpoint.
        """
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_link_service_connection_state is not None:
            pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional['outputs.PrivateEndpointConnectionPropertiesResponsePrivateEndpoint']:
        """
        The private endpoint resource from Microsoft.Network provider.
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional['outputs.PrivateEndpointConnectionPropertiesResponsePrivateLinkServiceConnectionState']:
        """
        Describes the current state of an existing Private Link Service connection to the Azure Private Endpoint.
        """
        return pulumi.get(self, "private_link_service_connection_state")


@pulumi.output_type
class PrivateEndpointConnectionPropertiesResponsePrivateEndpoint(dict):
    """
    The private endpoint resource from Microsoft.Network provider.
    """
    def __init__(__self__, *,
                 id: Optional[str] = None):
        """
        The private endpoint resource from Microsoft.Network provider.
        :param str id: The resource id of the private endpoint resource from Microsoft.Network provider.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The resource id of the private endpoint resource from Microsoft.Network provider.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class PrivateEndpointConnectionPropertiesResponsePrivateLinkServiceConnectionState(dict):
    """
    Describes the current state of an existing Private Link Service connection to the Azure Private Endpoint.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionsRequired":
            suggest = "actions_required"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateEndpointConnectionPropertiesResponsePrivateLinkServiceConnectionState. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateEndpointConnectionPropertiesResponsePrivateLinkServiceConnectionState.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateEndpointConnectionPropertiesResponsePrivateLinkServiceConnectionState.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 actions_required: Optional[str] = None,
                 description: Optional[str] = None,
                 status: Optional[str] = None):
        """
        Describes the current state of an existing Private Link Service connection to the Azure Private Endpoint.
        :param str actions_required: A description of any extra actions that may be required.
        :param str description: The description for the private link service connection state.
        :param str status: Status of the the private link service connection. Can be Pending, Approved, Rejected, or Disconnected.
        """
        if actions_required is None:
            actions_required = 'None'
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[str]:
        """
        A description of any extra actions that may be required.
        """
        return pulumi.get(self, "actions_required")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description for the private link service connection state.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Status of the the private link service connection. Can be Pending, Approved, Rejected, or Disconnected.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    """
    Describes an existing Private Endpoint connection to the Azure Cognitive Search service.
    """
    def __init__(__self__, *,
                 id: str,
                 name: str,
                 type: str,
                 properties: Optional['outputs.PrivateEndpointConnectionPropertiesResponse'] = None):
        """
        Describes an existing Private Endpoint connection to the Azure Cognitive Search service.
        :param str id: Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        :param str name: The name of the resource
        :param str type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        :param 'PrivateEndpointConnectionPropertiesResponse' properties: Describes the properties of an existing Private Endpoint connection to the Azure Cognitive Search service.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def properties(self) -> Optional['outputs.PrivateEndpointConnectionPropertiesResponse']:
        """
        Describes the properties of an existing Private Endpoint connection to the Azure Cognitive Search service.
        """
        return pulumi.get(self, "properties")


@pulumi.output_type
class QueryKeyResponse(dict):
    """
    Describes an API key for a given Azure Cognitive Search service that has permissions for query operations only.
    """
    def __init__(__self__, *,
                 key: str,
                 name: str):
        """
        Describes an API key for a given Azure Cognitive Search service that has permissions for query operations only.
        :param str key: The value of the query API key.
        :param str name: The name of the query API key; may be empty.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The value of the query API key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the query API key; may be empty.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class SharedPrivateLinkResourcePropertiesResponse(dict):
    """
    Describes the properties of an existing Shared Private Link Resource managed by the Azure Cognitive Search service.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "groupId":
            suggest = "group_id"
        elif key == "privateLinkResourceId":
            suggest = "private_link_resource_id"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "requestMessage":
            suggest = "request_message"
        elif key == "resourceRegion":
            suggest = "resource_region"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SharedPrivateLinkResourcePropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SharedPrivateLinkResourcePropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SharedPrivateLinkResourcePropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 group_id: Optional[str] = None,
                 private_link_resource_id: Optional[str] = None,
                 provisioning_state: Optional[str] = None,
                 request_message: Optional[str] = None,
                 resource_region: Optional[str] = None,
                 status: Optional[str] = None):
        """
        Describes the properties of an existing Shared Private Link Resource managed by the Azure Cognitive Search service.
        :param str group_id: The group id from the provider of resource the shared private link resource is for.
        :param str private_link_resource_id: The resource id of the resource the shared private link resource is for.
        :param str provisioning_state: The provisioning state of the shared private link resource. Can be Updating, Deleting, Failed, Succeeded, Incomplete or other yet to be documented value.
        :param str request_message: The request message for requesting approval of the shared private link resource.
        :param str resource_region: Optional. Can be used to specify the Azure Resource Manager location of the resource to which a shared private link is to be created. This is only required for those resources whose DNS configuration are regional (such as Azure Kubernetes Service).
        :param str status: Status of the shared private link resource. Can be Pending, Approved, Rejected, Disconnected or other yet to be documented value.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if private_link_resource_id is not None:
            pulumi.set(__self__, "private_link_resource_id", private_link_resource_id)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if request_message is not None:
            pulumi.set(__self__, "request_message", request_message)
        if resource_region is not None:
            pulumi.set(__self__, "resource_region", resource_region)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[str]:
        """
        The group id from the provider of resource the shared private link resource is for.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[str]:
        """
        The resource id of the resource the shared private link resource is for.
        """
        return pulumi.get(self, "private_link_resource_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The provisioning state of the shared private link resource. Can be Updating, Deleting, Failed, Succeeded, Incomplete or other yet to be documented value.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[str]:
        """
        The request message for requesting approval of the shared private link resource.
        """
        return pulumi.get(self, "request_message")

    @property
    @pulumi.getter(name="resourceRegion")
    def resource_region(self) -> Optional[str]:
        """
        Optional. Can be used to specify the Azure Resource Manager location of the resource to which a shared private link is to be created. This is only required for those resources whose DNS configuration are regional (such as Azure Kubernetes Service).
        """
        return pulumi.get(self, "resource_region")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Status of the shared private link resource. Can be Pending, Approved, Rejected, Disconnected or other yet to be documented value.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class SharedPrivateLinkResourceResponse(dict):
    """
    Describes a Shared Private Link Resource managed by the Azure Cognitive Search service.
    """
    def __init__(__self__, *,
                 id: str,
                 name: str,
                 type: str,
                 properties: Optional['outputs.SharedPrivateLinkResourcePropertiesResponse'] = None):
        """
        Describes a Shared Private Link Resource managed by the Azure Cognitive Search service.
        :param str id: Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        :param str name: The name of the resource
        :param str type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        :param 'SharedPrivateLinkResourcePropertiesResponse' properties: Describes the properties of a Shared Private Link Resource managed by the Azure Cognitive Search service.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def properties(self) -> Optional['outputs.SharedPrivateLinkResourcePropertiesResponse']:
        """
        Describes the properties of a Shared Private Link Resource managed by the Azure Cognitive Search service.
        """
        return pulumi.get(self, "properties")


@pulumi.output_type
class SkuResponse(dict):
    """
    Defines the SKU of an Azure Cognitive Search Service, which determines price tier and capacity limits.
    """
    def __init__(__self__, *,
                 name: Optional[str] = None):
        """
        Defines the SKU of an Azure Cognitive Search Service, which determines price tier and capacity limits.
        :param str name: The SKU of the search service. Valid values include: 'free': Shared service. 'basic': Dedicated service with up to 3 replicas. 'standard': Dedicated service with up to 12 partitions and 12 replicas. 'standard2': Similar to standard, but with more capacity per search unit. 'standard3': The largest Standard offering with up to 12 partitions and 12 replicas (or up to 3 partitions with more indexes if you also set the hostingMode property to 'highDensity'). 'storage_optimized_l1': Supports 1TB per partition, up to 12 partitions. 'storage_optimized_l2': Supports 2TB per partition, up to 12 partitions.'
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The SKU of the search service. Valid values include: 'free': Shared service. 'basic': Dedicated service with up to 3 replicas. 'standard': Dedicated service with up to 12 partitions and 12 replicas. 'standard2': Similar to standard, but with more capacity per search unit. 'standard3': The largest Standard offering with up to 12 partitions and 12 replicas (or up to 3 partitions with more indexes if you also set the hostingMode property to 'highDensity'). 'storage_optimized_l1': Supports 1TB per partition, up to 12 partitions. 'storage_optimized_l2': Supports 2TB per partition, up to 12 partitions.'
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class UserAssignedManagedIdentityResponse(dict):
    """
    The details of the user assigned managed identity assigned to the search service.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientId":
            suggest = "client_id"
        elif key == "principalId":
            suggest = "principal_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserAssignedManagedIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserAssignedManagedIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserAssignedManagedIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_id: str,
                 principal_id: str):
        """
        The details of the user assigned managed identity assigned to the search service.
        :param str client_id: The client ID of user assigned identity.
        :param str principal_id: The principal ID of user assigned identity.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "principal_id", principal_id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        The client ID of user assigned identity.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of user assigned identity.
        """
        return pulumi.get(self, "principal_id")


