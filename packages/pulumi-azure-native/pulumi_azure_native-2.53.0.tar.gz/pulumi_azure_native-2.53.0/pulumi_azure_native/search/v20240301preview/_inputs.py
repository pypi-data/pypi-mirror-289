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
    'DataPlaneAadOrApiKeyAuthOptionArgs',
    'DataPlaneAadOrApiKeyAuthOptionArgsDict',
    'DataPlaneAuthOptionsArgs',
    'DataPlaneAuthOptionsArgsDict',
    'EncryptionWithCmkArgs',
    'EncryptionWithCmkArgsDict',
    'IdentityArgs',
    'IdentityArgsDict',
    'IpRuleArgs',
    'IpRuleArgsDict',
    'NetworkRuleSetArgs',
    'NetworkRuleSetArgsDict',
    'PrivateEndpointConnectionPropertiesPrivateEndpointArgs',
    'PrivateEndpointConnectionPropertiesPrivateEndpointArgsDict',
    'PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgs',
    'PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgsDict',
    'PrivateEndpointConnectionPropertiesArgs',
    'PrivateEndpointConnectionPropertiesArgsDict',
    'SharedPrivateLinkResourcePropertiesArgs',
    'SharedPrivateLinkResourcePropertiesArgsDict',
    'SkuArgs',
    'SkuArgsDict',
]

MYPY = False

if not MYPY:
    class DataPlaneAadOrApiKeyAuthOptionArgsDict(TypedDict):
        """
        Indicates that either the API key or an access token from a Microsoft Entra ID tenant can be used for authentication.
        """
        aad_auth_failure_mode: NotRequired[pulumi.Input['AadAuthFailureMode']]
        """
        Describes what response the data plane API of a search service would send for requests that failed authentication.
        """
elif False:
    DataPlaneAadOrApiKeyAuthOptionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DataPlaneAadOrApiKeyAuthOptionArgs:
    def __init__(__self__, *,
                 aad_auth_failure_mode: Optional[pulumi.Input['AadAuthFailureMode']] = None):
        """
        Indicates that either the API key or an access token from a Microsoft Entra ID tenant can be used for authentication.
        :param pulumi.Input['AadAuthFailureMode'] aad_auth_failure_mode: Describes what response the data plane API of a search service would send for requests that failed authentication.
        """
        if aad_auth_failure_mode is not None:
            pulumi.set(__self__, "aad_auth_failure_mode", aad_auth_failure_mode)

    @property
    @pulumi.getter(name="aadAuthFailureMode")
    def aad_auth_failure_mode(self) -> Optional[pulumi.Input['AadAuthFailureMode']]:
        """
        Describes what response the data plane API of a search service would send for requests that failed authentication.
        """
        return pulumi.get(self, "aad_auth_failure_mode")

    @aad_auth_failure_mode.setter
    def aad_auth_failure_mode(self, value: Optional[pulumi.Input['AadAuthFailureMode']]):
        pulumi.set(self, "aad_auth_failure_mode", value)


if not MYPY:
    class DataPlaneAuthOptionsArgsDict(TypedDict):
        """
        Defines the options for how the search service authenticates a data plane request. This cannot be set if 'disableLocalAuth' is set to true.
        """
        aad_or_api_key: NotRequired[pulumi.Input['DataPlaneAadOrApiKeyAuthOptionArgsDict']]
        """
        Indicates that either the API key or an access token from a Microsoft Entra ID tenant can be used for authentication.
        """
        api_key_only: NotRequired[Any]
        """
        Indicates that only the API key can be used for authentication.
        """
elif False:
    DataPlaneAuthOptionsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DataPlaneAuthOptionsArgs:
    def __init__(__self__, *,
                 aad_or_api_key: Optional[pulumi.Input['DataPlaneAadOrApiKeyAuthOptionArgs']] = None,
                 api_key_only: Optional[Any] = None):
        """
        Defines the options for how the search service authenticates a data plane request. This cannot be set if 'disableLocalAuth' is set to true.
        :param pulumi.Input['DataPlaneAadOrApiKeyAuthOptionArgs'] aad_or_api_key: Indicates that either the API key or an access token from a Microsoft Entra ID tenant can be used for authentication.
        :param Any api_key_only: Indicates that only the API key can be used for authentication.
        """
        if aad_or_api_key is not None:
            pulumi.set(__self__, "aad_or_api_key", aad_or_api_key)
        if api_key_only is not None:
            pulumi.set(__self__, "api_key_only", api_key_only)

    @property
    @pulumi.getter(name="aadOrApiKey")
    def aad_or_api_key(self) -> Optional[pulumi.Input['DataPlaneAadOrApiKeyAuthOptionArgs']]:
        """
        Indicates that either the API key or an access token from a Microsoft Entra ID tenant can be used for authentication.
        """
        return pulumi.get(self, "aad_or_api_key")

    @aad_or_api_key.setter
    def aad_or_api_key(self, value: Optional[pulumi.Input['DataPlaneAadOrApiKeyAuthOptionArgs']]):
        pulumi.set(self, "aad_or_api_key", value)

    @property
    @pulumi.getter(name="apiKeyOnly")
    def api_key_only(self) -> Optional[Any]:
        """
        Indicates that only the API key can be used for authentication.
        """
        return pulumi.get(self, "api_key_only")

    @api_key_only.setter
    def api_key_only(self, value: Optional[Any]):
        pulumi.set(self, "api_key_only", value)


if not MYPY:
    class EncryptionWithCmkArgsDict(TypedDict):
        """
        Describes a policy that determines how resources within the search service are to be encrypted with customer managed keys.
        """
        enforcement: NotRequired[pulumi.Input['SearchEncryptionWithCmk']]
        """
        Describes how a search service should enforce compliance if it finds objects that aren't encrypted with the customer-managed key.
        """
elif False:
    EncryptionWithCmkArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class EncryptionWithCmkArgs:
    def __init__(__self__, *,
                 enforcement: Optional[pulumi.Input['SearchEncryptionWithCmk']] = None):
        """
        Describes a policy that determines how resources within the search service are to be encrypted with customer managed keys.
        :param pulumi.Input['SearchEncryptionWithCmk'] enforcement: Describes how a search service should enforce compliance if it finds objects that aren't encrypted with the customer-managed key.
        """
        if enforcement is not None:
            pulumi.set(__self__, "enforcement", enforcement)

    @property
    @pulumi.getter
    def enforcement(self) -> Optional[pulumi.Input['SearchEncryptionWithCmk']]:
        """
        Describes how a search service should enforce compliance if it finds objects that aren't encrypted with the customer-managed key.
        """
        return pulumi.get(self, "enforcement")

    @enforcement.setter
    def enforcement(self, value: Optional[pulumi.Input['SearchEncryptionWithCmk']]):
        pulumi.set(self, "enforcement", value)


if not MYPY:
    class IdentityArgsDict(TypedDict):
        """
        Details about the search service identity. A null value indicates that the search service has no identity assigned.
        """
        type: pulumi.Input[Union[str, 'IdentityType']]
        """
        The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes both an identity created by the system and a set of user assigned identities. The type 'None' will remove all identities from the service.
        """
        user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource IDs in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
elif False:
    IdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[Union[str, 'IdentityType']],
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Details about the search service identity. A null value indicates that the search service has no identity assigned.
        :param pulumi.Input[Union[str, 'IdentityType']] type: The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes both an identity created by the system and a set of user assigned identities. The type 'None' will remove all identities from the service.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource IDs in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'IdentityType']]:
        """
        The type of identity used for the resource. The type 'SystemAssigned, UserAssigned' includes both an identity created by the system and a set of user assigned identities. The type 'None' will remove all identities from the service.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'IdentityType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource IDs in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


if not MYPY:
    class IpRuleArgsDict(TypedDict):
        """
        The IP restriction rule of the Azure AI Search service.
        """
        value: NotRequired[pulumi.Input[str]]
        """
        Value corresponding to a single IPv4 address (eg., 123.1.2.3) or an IP range in CIDR format (eg., 123.1.2.3/24) to be allowed.
        """
elif False:
    IpRuleArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class IpRuleArgs:
    def __init__(__self__, *,
                 value: Optional[pulumi.Input[str]] = None):
        """
        The IP restriction rule of the Azure AI Search service.
        :param pulumi.Input[str] value: Value corresponding to a single IPv4 address (eg., 123.1.2.3) or an IP range in CIDR format (eg., 123.1.2.3/24) to be allowed.
        """
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Value corresponding to a single IPv4 address (eg., 123.1.2.3) or an IP range in CIDR format (eg., 123.1.2.3/24) to be allowed.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


if not MYPY:
    class NetworkRuleSetArgsDict(TypedDict):
        """
        Network specific rules that determine how the Azure AI Search service may be reached.
        """
        bypass: NotRequired[pulumi.Input[Union[str, 'SearchBypass']]]
        """
        Possible origins of inbound traffic that can bypass the rules defined in the 'ipRules' section.
        """
        ip_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input['IpRuleArgsDict']]]]
        """
        A list of IP restriction rules that defines the inbound network(s) with allowing access to the search service endpoint. At the meantime, all other public IP networks are blocked by the firewall. These restriction rules are applied only when the 'publicNetworkAccess' of the search service is 'enabled'; otherwise, traffic over public interface is not allowed even with any public IP rules, and private endpoint connections would be the exclusive access method.
        """
elif False:
    NetworkRuleSetArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class NetworkRuleSetArgs:
    def __init__(__self__, *,
                 bypass: Optional[pulumi.Input[Union[str, 'SearchBypass']]] = None,
                 ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input['IpRuleArgs']]]] = None):
        """
        Network specific rules that determine how the Azure AI Search service may be reached.
        :param pulumi.Input[Union[str, 'SearchBypass']] bypass: Possible origins of inbound traffic that can bypass the rules defined in the 'ipRules' section.
        :param pulumi.Input[Sequence[pulumi.Input['IpRuleArgs']]] ip_rules: A list of IP restriction rules that defines the inbound network(s) with allowing access to the search service endpoint. At the meantime, all other public IP networks are blocked by the firewall. These restriction rules are applied only when the 'publicNetworkAccess' of the search service is 'enabled'; otherwise, traffic over public interface is not allowed even with any public IP rules, and private endpoint connections would be the exclusive access method.
        """
        if bypass is not None:
            pulumi.set(__self__, "bypass", bypass)
        if ip_rules is not None:
            pulumi.set(__self__, "ip_rules", ip_rules)

    @property
    @pulumi.getter
    def bypass(self) -> Optional[pulumi.Input[Union[str, 'SearchBypass']]]:
        """
        Possible origins of inbound traffic that can bypass the rules defined in the 'ipRules' section.
        """
        return pulumi.get(self, "bypass")

    @bypass.setter
    def bypass(self, value: Optional[pulumi.Input[Union[str, 'SearchBypass']]]):
        pulumi.set(self, "bypass", value)

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IpRuleArgs']]]]:
        """
        A list of IP restriction rules that defines the inbound network(s) with allowing access to the search service endpoint. At the meantime, all other public IP networks are blocked by the firewall. These restriction rules are applied only when the 'publicNetworkAccess' of the search service is 'enabled'; otherwise, traffic over public interface is not allowed even with any public IP rules, and private endpoint connections would be the exclusive access method.
        """
        return pulumi.get(self, "ip_rules")

    @ip_rules.setter
    def ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IpRuleArgs']]]]):
        pulumi.set(self, "ip_rules", value)


if not MYPY:
    class PrivateEndpointConnectionPropertiesPrivateEndpointArgsDict(TypedDict):
        """
        The private endpoint resource from Microsoft.Network provider.
        """
        id: NotRequired[pulumi.Input[str]]
        """
        The resource ID of the private endpoint resource from Microsoft.Network provider.
        """
elif False:
    PrivateEndpointConnectionPropertiesPrivateEndpointArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateEndpointConnectionPropertiesPrivateEndpointArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        The private endpoint resource from Microsoft.Network provider.
        :param pulumi.Input[str] id: The resource ID of the private endpoint resource from Microsoft.Network provider.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the private endpoint resource from Microsoft.Network provider.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


if not MYPY:
    class PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgsDict(TypedDict):
        """
        Describes the current state of an existing Azure Private Link service connection to the private endpoint.
        """
        actions_required: NotRequired[pulumi.Input[str]]
        """
        A description of any extra actions that may be required.
        """
        description: NotRequired[pulumi.Input[str]]
        """
        The description for the private link service connection state.
        """
        status: NotRequired[pulumi.Input['PrivateLinkServiceConnectionStatus']]
        """
        Status of the the private link service connection. Valid values are Pending, Approved, Rejected, or Disconnected.
        """
elif False:
    PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgs:
    def __init__(__self__, *,
                 actions_required: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['PrivateLinkServiceConnectionStatus']] = None):
        """
        Describes the current state of an existing Azure Private Link service connection to the private endpoint.
        :param pulumi.Input[str] actions_required: A description of any extra actions that may be required.
        :param pulumi.Input[str] description: The description for the private link service connection state.
        :param pulumi.Input['PrivateLinkServiceConnectionStatus'] status: Status of the the private link service connection. Valid values are Pending, Approved, Rejected, or Disconnected.
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
    def actions_required(self) -> Optional[pulumi.Input[str]]:
        """
        A description of any extra actions that may be required.
        """
        return pulumi.get(self, "actions_required")

    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "actions_required", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description for the private link service connection state.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['PrivateLinkServiceConnectionStatus']]:
        """
        Status of the the private link service connection. Valid values are Pending, Approved, Rejected, or Disconnected.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['PrivateLinkServiceConnectionStatus']]):
        pulumi.set(self, "status", value)


if not MYPY:
    class PrivateEndpointConnectionPropertiesArgsDict(TypedDict):
        """
        Describes the properties of an existing private endpoint connection to the search service.
        """
        group_id: NotRequired[pulumi.Input[str]]
        """
        The group ID of the Azure resource for which the private link service is for.
        """
        private_endpoint: NotRequired[pulumi.Input['PrivateEndpointConnectionPropertiesPrivateEndpointArgsDict']]
        """
        The private endpoint resource from Microsoft.Network provider.
        """
        private_link_service_connection_state: NotRequired[pulumi.Input['PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgsDict']]
        """
        Describes the current state of an existing Azure Private Link service connection to the private endpoint.
        """
        provisioning_state: NotRequired[pulumi.Input[Union[str, 'PrivateLinkServiceConnectionProvisioningState']]]
        """
        The provisioning state of the private link service connection. Valid values are Updating, Deleting, Failed, Succeeded, Incomplete, or Canceled.
        """
elif False:
    PrivateEndpointConnectionPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateEndpointConnectionPropertiesArgs:
    def __init__(__self__, *,
                 group_id: Optional[pulumi.Input[str]] = None,
                 private_endpoint: Optional[pulumi.Input['PrivateEndpointConnectionPropertiesPrivateEndpointArgs']] = None,
                 private_link_service_connection_state: Optional[pulumi.Input['PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgs']] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'PrivateLinkServiceConnectionProvisioningState']]] = None):
        """
        Describes the properties of an existing private endpoint connection to the search service.
        :param pulumi.Input[str] group_id: The group ID of the Azure resource for which the private link service is for.
        :param pulumi.Input['PrivateEndpointConnectionPropertiesPrivateEndpointArgs'] private_endpoint: The private endpoint resource from Microsoft.Network provider.
        :param pulumi.Input['PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgs'] private_link_service_connection_state: Describes the current state of an existing Azure Private Link service connection to the private endpoint.
        :param pulumi.Input[Union[str, 'PrivateLinkServiceConnectionProvisioningState']] provisioning_state: The provisioning state of the private link service connection. Valid values are Updating, Deleting, Failed, Succeeded, Incomplete, or Canceled.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_link_service_connection_state is not None:
            pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The group ID of the Azure resource for which the private link service is for.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input['PrivateEndpointConnectionPropertiesPrivateEndpointArgs']]:
        """
        The private endpoint resource from Microsoft.Network provider.
        """
        return pulumi.get(self, "private_endpoint")

    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input['PrivateEndpointConnectionPropertiesPrivateEndpointArgs']]):
        pulumi.set(self, "private_endpoint", value)

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[pulumi.Input['PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgs']]:
        """
        Describes the current state of an existing Azure Private Link service connection to the private endpoint.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: Optional[pulumi.Input['PrivateEndpointConnectionPropertiesPrivateLinkServiceConnectionStateArgs']]):
        pulumi.set(self, "private_link_service_connection_state", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'PrivateLinkServiceConnectionProvisioningState']]]:
        """
        The provisioning state of the private link service connection. Valid values are Updating, Deleting, Failed, Succeeded, Incomplete, or Canceled.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'PrivateLinkServiceConnectionProvisioningState']]]):
        pulumi.set(self, "provisioning_state", value)


if not MYPY:
    class SharedPrivateLinkResourcePropertiesArgsDict(TypedDict):
        """
        Describes the properties of an existing shared private link resource managed by the Azure AI Search service.
        """
        group_id: NotRequired[pulumi.Input[str]]
        """
        The group ID from the provider of resource the shared private link resource is for.
        """
        private_link_resource_id: NotRequired[pulumi.Input[str]]
        """
        The resource ID of the resource the shared private link resource is for.
        """
        provisioning_state: NotRequired[pulumi.Input[Union[str, 'SharedPrivateLinkResourceProvisioningState']]]
        """
        The provisioning state of the shared private link resource. Valid values are Updating, Deleting, Failed, Succeeded or Incomplete.
        """
        request_message: NotRequired[pulumi.Input[str]]
        """
        The message for requesting approval of the shared private link resource.
        """
        resource_region: NotRequired[pulumi.Input[str]]
        """
        Optional. Can be used to specify the Azure Resource Manager location of the resource for which a shared private link is being created. This is only required for those resources whose DNS configuration are regional (such as Azure Kubernetes Service).
        """
        status: NotRequired[pulumi.Input[Union[str, 'SharedPrivateLinkResourceStatus']]]
        """
        Status of the shared private link resource. Valid values are Pending, Approved, Rejected or Disconnected.
        """
elif False:
    SharedPrivateLinkResourcePropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SharedPrivateLinkResourcePropertiesArgs:
    def __init__(__self__, *,
                 group_id: Optional[pulumi.Input[str]] = None,
                 private_link_resource_id: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'SharedPrivateLinkResourceProvisioningState']]] = None,
                 request_message: Optional[pulumi.Input[str]] = None,
                 resource_region: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'SharedPrivateLinkResourceStatus']]] = None):
        """
        Describes the properties of an existing shared private link resource managed by the Azure AI Search service.
        :param pulumi.Input[str] group_id: The group ID from the provider of resource the shared private link resource is for.
        :param pulumi.Input[str] private_link_resource_id: The resource ID of the resource the shared private link resource is for.
        :param pulumi.Input[Union[str, 'SharedPrivateLinkResourceProvisioningState']] provisioning_state: The provisioning state of the shared private link resource. Valid values are Updating, Deleting, Failed, Succeeded or Incomplete.
        :param pulumi.Input[str] request_message: The message for requesting approval of the shared private link resource.
        :param pulumi.Input[str] resource_region: Optional. Can be used to specify the Azure Resource Manager location of the resource for which a shared private link is being created. This is only required for those resources whose DNS configuration are regional (such as Azure Kubernetes Service).
        :param pulumi.Input[Union[str, 'SharedPrivateLinkResourceStatus']] status: Status of the shared private link resource. Valid values are Pending, Approved, Rejected or Disconnected.
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
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The group ID from the provider of resource the shared private link resource is for.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource ID of the resource the shared private link resource is for.
        """
        return pulumi.get(self, "private_link_resource_id")

    @private_link_resource_id.setter
    def private_link_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_resource_id", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'SharedPrivateLinkResourceProvisioningState']]]:
        """
        The provisioning state of the shared private link resource. Valid values are Updating, Deleting, Failed, Succeeded or Incomplete.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'SharedPrivateLinkResourceProvisioningState']]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[pulumi.Input[str]]:
        """
        The message for requesting approval of the shared private link resource.
        """
        return pulumi.get(self, "request_message")

    @request_message.setter
    def request_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_message", value)

    @property
    @pulumi.getter(name="resourceRegion")
    def resource_region(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Can be used to specify the Azure Resource Manager location of the resource for which a shared private link is being created. This is only required for those resources whose DNS configuration are regional (such as Azure Kubernetes Service).
        """
        return pulumi.get(self, "resource_region")

    @resource_region.setter
    def resource_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_region", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'SharedPrivateLinkResourceStatus']]]:
        """
        Status of the shared private link resource. Valid values are Pending, Approved, Rejected or Disconnected.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'SharedPrivateLinkResourceStatus']]]):
        pulumi.set(self, "status", value)


if not MYPY:
    class SkuArgsDict(TypedDict):
        """
        Defines the SKU of a search service, which determines billing rate and capacity limits.
        """
        name: NotRequired[pulumi.Input[Union[str, 'SkuName']]]
        """
        The SKU of the search service. Valid values include: 'free': Shared service. 'basic': Dedicated service with up to 3 replicas. 'standard': Dedicated service with up to 12 partitions and 12 replicas. 'standard2': Similar to standard, but with more capacity per search unit. 'standard3': The largest Standard offering with up to 12 partitions and 12 replicas (or up to 3 partitions with more indexes if you also set the hostingMode property to 'highDensity'). 'storage_optimized_l1': Supports 1TB per partition, up to 12 partitions. 'storage_optimized_l2': Supports 2TB per partition, up to 12 partitions.'
        """
elif False:
    SkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[Union[str, 'SkuName']]] = None):
        """
        Defines the SKU of a search service, which determines billing rate and capacity limits.
        :param pulumi.Input[Union[str, 'SkuName']] name: The SKU of the search service. Valid values include: 'free': Shared service. 'basic': Dedicated service with up to 3 replicas. 'standard': Dedicated service with up to 12 partitions and 12 replicas. 'standard2': Similar to standard, but with more capacity per search unit. 'standard3': The largest Standard offering with up to 12 partitions and 12 replicas (or up to 3 partitions with more indexes if you also set the hostingMode property to 'highDensity'). 'storage_optimized_l1': Supports 1TB per partition, up to 12 partitions. 'storage_optimized_l2': Supports 2TB per partition, up to 12 partitions.'
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[str, 'SkuName']]]:
        """
        The SKU of the search service. Valid values include: 'free': Shared service. 'basic': Dedicated service with up to 3 replicas. 'standard': Dedicated service with up to 12 partitions and 12 replicas. 'standard2': Similar to standard, but with more capacity per search unit. 'standard3': The largest Standard offering with up to 12 partitions and 12 replicas (or up to 3 partitions with more indexes if you also set the hostingMode property to 'highDensity'). 'storage_optimized_l1': Supports 1TB per partition, up to 12 partitions. 'storage_optimized_l2': Supports 2TB per partition, up to 12 partitions.'
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[str, 'SkuName']]]):
        pulumi.set(self, "name", value)


