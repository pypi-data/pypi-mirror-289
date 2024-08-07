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
from .. import _utilities
from ._enums import *

__all__ = [
    'DiagnosticStoragePropertiesArgs',
    'DiagnosticStoragePropertiesArgsDict',
    'EncryptionArgs',
    'EncryptionArgsDict',
    'GroupConnectivityInformationArgs',
    'GroupConnectivityInformationArgsDict',
    'IotHubSettingsArgs',
    'IotHubSettingsArgsDict',
    'ManagedServiceIdentityArgs',
    'ManagedServiceIdentityArgsDict',
    'PrivateEndpointConnectionArgs',
    'PrivateEndpointConnectionArgsDict',
    'PrivateLinkServiceConnectionStateArgs',
    'PrivateLinkServiceConnectionStateArgsDict',
    'PrivateLinkServiceConnectionArgs',
    'PrivateLinkServiceConnectionArgsDict',
    'PrivateLinkServiceProxyArgs',
    'PrivateLinkServiceProxyArgsDict',
    'RemotePrivateEndpointArgs',
    'RemotePrivateEndpointArgsDict',
]

MYPY = False

if not MYPY:
    class DiagnosticStoragePropertiesArgsDict(TypedDict):
        """
        Customer-initiated diagnostic log collection storage properties
        """
        authentication_type: pulumi.Input[Union[str, 'AuthenticationType']]
        """
        Authentication Type
        """
        resource_id: pulumi.Input[str]
        """
        ResourceId of the diagnostic storage account
        """
        connection_string: NotRequired[pulumi.Input[str]]
        """
        ConnectionString of the diagnostic storage account
        """
elif False:
    DiagnosticStoragePropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DiagnosticStoragePropertiesArgs:
    def __init__(__self__, *,
                 authentication_type: pulumi.Input[Union[str, 'AuthenticationType']],
                 resource_id: pulumi.Input[str],
                 connection_string: Optional[pulumi.Input[str]] = None):
        """
        Customer-initiated diagnostic log collection storage properties
        :param pulumi.Input[Union[str, 'AuthenticationType']] authentication_type: Authentication Type
        :param pulumi.Input[str] resource_id: ResourceId of the diagnostic storage account
        :param pulumi.Input[str] connection_string: ConnectionString of the diagnostic storage account
        """
        pulumi.set(__self__, "authentication_type", authentication_type)
        pulumi.set(__self__, "resource_id", resource_id)
        if connection_string is not None:
            pulumi.set(__self__, "connection_string", connection_string)

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input[Union[str, 'AuthenticationType']]:
        """
        Authentication Type
        """
        return pulumi.get(self, "authentication_type")

    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input[Union[str, 'AuthenticationType']]):
        pulumi.set(self, "authentication_type", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        ResourceId of the diagnostic storage account
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> Optional[pulumi.Input[str]]:
        """
        ConnectionString of the diagnostic storage account
        """
        return pulumi.get(self, "connection_string")

    @connection_string.setter
    def connection_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_string", value)


if not MYPY:
    class EncryptionArgsDict(TypedDict):
        """
        The CMK encryption settings on the Device Update account.
        """
        key_vault_key_uri: NotRequired[pulumi.Input[str]]
        """
        The URI of the key vault
        """
        user_assigned_identity: NotRequired[pulumi.Input[str]]
        """
        The full resourceId of the user assigned identity to be used for key vault access. Identity has to be also assigned to the Account
        """
elif False:
    EncryptionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class EncryptionArgs:
    def __init__(__self__, *,
                 key_vault_key_uri: Optional[pulumi.Input[str]] = None,
                 user_assigned_identity: Optional[pulumi.Input[str]] = None):
        """
        The CMK encryption settings on the Device Update account.
        :param pulumi.Input[str] key_vault_key_uri: The URI of the key vault
        :param pulumi.Input[str] user_assigned_identity: The full resourceId of the user assigned identity to be used for key vault access. Identity has to be also assigned to the Account
        """
        if key_vault_key_uri is not None:
            pulumi.set(__self__, "key_vault_key_uri", key_vault_key_uri)
        if user_assigned_identity is not None:
            pulumi.set(__self__, "user_assigned_identity", user_assigned_identity)

    @property
    @pulumi.getter(name="keyVaultKeyUri")
    def key_vault_key_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of the key vault
        """
        return pulumi.get(self, "key_vault_key_uri")

    @key_vault_key_uri.setter
    def key_vault_key_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_vault_key_uri", value)

    @property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> Optional[pulumi.Input[str]]:
        """
        The full resourceId of the user assigned identity to be used for key vault access. Identity has to be also assigned to the Account
        """
        return pulumi.get(self, "user_assigned_identity")

    @user_assigned_identity.setter
    def user_assigned_identity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_assigned_identity", value)


if not MYPY:
    class GroupConnectivityInformationArgsDict(TypedDict):
        """
        Group connectivity details.
        """
        customer_visible_fqdns: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        List of customer visible FQDNs.
        """
        private_link_service_arm_region: NotRequired[pulumi.Input[str]]
        """
        PrivateLinkService ARM region.
        """
        redirect_map_id: NotRequired[pulumi.Input[str]]
        """
        Redirect map ID.
        """
elif False:
    GroupConnectivityInformationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class GroupConnectivityInformationArgs:
    def __init__(__self__, *,
                 customer_visible_fqdns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 private_link_service_arm_region: Optional[pulumi.Input[str]] = None,
                 redirect_map_id: Optional[pulumi.Input[str]] = None):
        """
        Group connectivity details.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] customer_visible_fqdns: List of customer visible FQDNs.
        :param pulumi.Input[str] private_link_service_arm_region: PrivateLinkService ARM region.
        :param pulumi.Input[str] redirect_map_id: Redirect map ID.
        """
        if customer_visible_fqdns is not None:
            pulumi.set(__self__, "customer_visible_fqdns", customer_visible_fqdns)
        if private_link_service_arm_region is not None:
            pulumi.set(__self__, "private_link_service_arm_region", private_link_service_arm_region)
        if redirect_map_id is not None:
            pulumi.set(__self__, "redirect_map_id", redirect_map_id)

    @property
    @pulumi.getter(name="customerVisibleFqdns")
    def customer_visible_fqdns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of customer visible FQDNs.
        """
        return pulumi.get(self, "customer_visible_fqdns")

    @customer_visible_fqdns.setter
    def customer_visible_fqdns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "customer_visible_fqdns", value)

    @property
    @pulumi.getter(name="privateLinkServiceArmRegion")
    def private_link_service_arm_region(self) -> Optional[pulumi.Input[str]]:
        """
        PrivateLinkService ARM region.
        """
        return pulumi.get(self, "private_link_service_arm_region")

    @private_link_service_arm_region.setter
    def private_link_service_arm_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_service_arm_region", value)

    @property
    @pulumi.getter(name="redirectMapId")
    def redirect_map_id(self) -> Optional[pulumi.Input[str]]:
        """
        Redirect map ID.
        """
        return pulumi.get(self, "redirect_map_id")

    @redirect_map_id.setter
    def redirect_map_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "redirect_map_id", value)


if not MYPY:
    class IotHubSettingsArgsDict(TypedDict):
        """
        Device Update account integration with IoT Hub settings.
        """
        resource_id: pulumi.Input[str]
        """
        IoTHub resource ID
        """
elif False:
    IotHubSettingsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class IotHubSettingsArgs:
    def __init__(__self__, *,
                 resource_id: pulumi.Input[str]):
        """
        Device Update account integration with IoT Hub settings.
        :param pulumi.Input[str] resource_id: IoTHub resource ID
        """
        pulumi.set(__self__, "resource_id", resource_id)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        IoTHub resource ID
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)


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
    class PrivateEndpointConnectionArgsDict(TypedDict):
        """
        The Private Endpoint Connection resource.
        """
        private_link_service_connection_state: pulumi.Input['PrivateLinkServiceConnectionStateArgsDict']
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        Array of group IDs.
        """
elif False:
    PrivateEndpointConnectionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateEndpointConnectionArgs:
    def __init__(__self__, *,
                 private_link_service_connection_state: pulumi.Input['PrivateLinkServiceConnectionStateArgs'],
                 group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The Private Endpoint Connection resource.
        :param pulumi.Input['PrivateLinkServiceConnectionStateArgs'] private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_ids: Array of group IDs.
        """
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        if group_ids is not None:
            pulumi.set(__self__, "group_ids", group_ids)

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Input['PrivateLinkServiceConnectionStateArgs']:
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: pulumi.Input['PrivateLinkServiceConnectionStateArgs']):
        pulumi.set(self, "private_link_service_connection_state", value)

    @property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Array of group IDs.
        """
        return pulumi.get(self, "group_ids")

    @group_ids.setter
    def group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "group_ids", value)


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


if not MYPY:
    class PrivateLinkServiceConnectionArgsDict(TypedDict):
        """
        Private link service connection details.
        """
        group_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        List of group IDs.
        """
        name: NotRequired[pulumi.Input[str]]
        """
        Private link service connection name.
        """
        request_message: NotRequired[pulumi.Input[str]]
        """
        Request message.
        """
elif False:
    PrivateLinkServiceConnectionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateLinkServiceConnectionArgs:
    def __init__(__self__, *,
                 group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 request_message: Optional[pulumi.Input[str]] = None):
        """
        Private link service connection details.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_ids: List of group IDs.
        :param pulumi.Input[str] name: Private link service connection name.
        :param pulumi.Input[str] request_message: Request message.
        """
        if group_ids is not None:
            pulumi.set(__self__, "group_ids", group_ids)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if request_message is not None:
            pulumi.set(__self__, "request_message", request_message)

    @property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of group IDs.
        """
        return pulumi.get(self, "group_ids")

    @group_ids.setter
    def group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "group_ids", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Private link service connection name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[pulumi.Input[str]]:
        """
        Request message.
        """
        return pulumi.get(self, "request_message")

    @request_message.setter
    def request_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_message", value)


if not MYPY:
    class PrivateLinkServiceProxyArgsDict(TypedDict):
        """
        Private link service proxy details.
        """
        group_connectivity_information: NotRequired[pulumi.Input[Sequence[pulumi.Input['GroupConnectivityInformationArgsDict']]]]
        """
        Group connectivity information.
        """
        id: NotRequired[pulumi.Input[str]]
        """
        NRP resource ID.
        """
        remote_private_link_service_connection_state: NotRequired[pulumi.Input['PrivateLinkServiceConnectionStateArgsDict']]
        """
        Remote private link service connection state
        """
elif False:
    PrivateLinkServiceProxyArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrivateLinkServiceProxyArgs:
    def __init__(__self__, *,
                 group_connectivity_information: Optional[pulumi.Input[Sequence[pulumi.Input['GroupConnectivityInformationArgs']]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 remote_private_link_service_connection_state: Optional[pulumi.Input['PrivateLinkServiceConnectionStateArgs']] = None):
        """
        Private link service proxy details.
        :param pulumi.Input[Sequence[pulumi.Input['GroupConnectivityInformationArgs']]] group_connectivity_information: Group connectivity information.
        :param pulumi.Input[str] id: NRP resource ID.
        :param pulumi.Input['PrivateLinkServiceConnectionStateArgs'] remote_private_link_service_connection_state: Remote private link service connection state
        """
        if group_connectivity_information is not None:
            pulumi.set(__self__, "group_connectivity_information", group_connectivity_information)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if remote_private_link_service_connection_state is not None:
            pulumi.set(__self__, "remote_private_link_service_connection_state", remote_private_link_service_connection_state)

    @property
    @pulumi.getter(name="groupConnectivityInformation")
    def group_connectivity_information(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GroupConnectivityInformationArgs']]]]:
        """
        Group connectivity information.
        """
        return pulumi.get(self, "group_connectivity_information")

    @group_connectivity_information.setter
    def group_connectivity_information(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GroupConnectivityInformationArgs']]]]):
        pulumi.set(self, "group_connectivity_information", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        NRP resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="remotePrivateLinkServiceConnectionState")
    def remote_private_link_service_connection_state(self) -> Optional[pulumi.Input['PrivateLinkServiceConnectionStateArgs']]:
        """
        Remote private link service connection state
        """
        return pulumi.get(self, "remote_private_link_service_connection_state")

    @remote_private_link_service_connection_state.setter
    def remote_private_link_service_connection_state(self, value: Optional[pulumi.Input['PrivateLinkServiceConnectionStateArgs']]):
        pulumi.set(self, "remote_private_link_service_connection_state", value)


if not MYPY:
    class RemotePrivateEndpointArgsDict(TypedDict):
        """
        Remote private endpoint details.
        """
        id: NotRequired[pulumi.Input[str]]
        """
        Remote endpoint resource ID.
        """
        immutable_resource_id: NotRequired[pulumi.Input[str]]
        """
        Original resource ID needed by Microsoft.Network.
        """
        immutable_subscription_id: NotRequired[pulumi.Input[str]]
        """
        Original subscription ID needed by Microsoft.Network.
        """
        location: NotRequired[pulumi.Input[str]]
        """
        ARM location of the remote private endpoint.
        """
        manual_private_link_service_connections: NotRequired[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgsDict']]]]
        """
        List of private link service connections that need manual approval.
        """
        private_link_service_connections: NotRequired[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgsDict']]]]
        """
        List of automatically approved private link service connections.
        """
        private_link_service_proxies: NotRequired[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceProxyArgsDict']]]]
        """
        List of private link service proxies.
        """
        vnet_traffic_tag: NotRequired[pulumi.Input[str]]
        """
        Virtual network traffic tag.
        """
elif False:
    RemotePrivateEndpointArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class RemotePrivateEndpointArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None,
                 immutable_resource_id: Optional[pulumi.Input[str]] = None,
                 immutable_subscription_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 manual_private_link_service_connections: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]]] = None,
                 private_link_service_connections: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]]] = None,
                 private_link_service_proxies: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceProxyArgs']]]] = None,
                 vnet_traffic_tag: Optional[pulumi.Input[str]] = None):
        """
        Remote private endpoint details.
        :param pulumi.Input[str] id: Remote endpoint resource ID.
        :param pulumi.Input[str] immutable_resource_id: Original resource ID needed by Microsoft.Network.
        :param pulumi.Input[str] immutable_subscription_id: Original subscription ID needed by Microsoft.Network.
        :param pulumi.Input[str] location: ARM location of the remote private endpoint.
        :param pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]] manual_private_link_service_connections: List of private link service connections that need manual approval.
        :param pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]] private_link_service_connections: List of automatically approved private link service connections.
        :param pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceProxyArgs']]] private_link_service_proxies: List of private link service proxies.
        :param pulumi.Input[str] vnet_traffic_tag: Virtual network traffic tag.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if immutable_resource_id is not None:
            pulumi.set(__self__, "immutable_resource_id", immutable_resource_id)
        if immutable_subscription_id is not None:
            pulumi.set(__self__, "immutable_subscription_id", immutable_subscription_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if manual_private_link_service_connections is not None:
            pulumi.set(__self__, "manual_private_link_service_connections", manual_private_link_service_connections)
        if private_link_service_connections is not None:
            pulumi.set(__self__, "private_link_service_connections", private_link_service_connections)
        if private_link_service_proxies is not None:
            pulumi.set(__self__, "private_link_service_proxies", private_link_service_proxies)
        if vnet_traffic_tag is not None:
            pulumi.set(__self__, "vnet_traffic_tag", vnet_traffic_tag)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Remote endpoint resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="immutableResourceId")
    def immutable_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Original resource ID needed by Microsoft.Network.
        """
        return pulumi.get(self, "immutable_resource_id")

    @immutable_resource_id.setter
    def immutable_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "immutable_resource_id", value)

    @property
    @pulumi.getter(name="immutableSubscriptionId")
    def immutable_subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        Original subscription ID needed by Microsoft.Network.
        """
        return pulumi.get(self, "immutable_subscription_id")

    @immutable_subscription_id.setter
    def immutable_subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "immutable_subscription_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        ARM location of the remote private endpoint.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="manualPrivateLinkServiceConnections")
    def manual_private_link_service_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]]]:
        """
        List of private link service connections that need manual approval.
        """
        return pulumi.get(self, "manual_private_link_service_connections")

    @manual_private_link_service_connections.setter
    def manual_private_link_service_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]]]):
        pulumi.set(self, "manual_private_link_service_connections", value)

    @property
    @pulumi.getter(name="privateLinkServiceConnections")
    def private_link_service_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]]]:
        """
        List of automatically approved private link service connections.
        """
        return pulumi.get(self, "private_link_service_connections")

    @private_link_service_connections.setter
    def private_link_service_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceConnectionArgs']]]]):
        pulumi.set(self, "private_link_service_connections", value)

    @property
    @pulumi.getter(name="privateLinkServiceProxies")
    def private_link_service_proxies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceProxyArgs']]]]:
        """
        List of private link service proxies.
        """
        return pulumi.get(self, "private_link_service_proxies")

    @private_link_service_proxies.setter
    def private_link_service_proxies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateLinkServiceProxyArgs']]]]):
        pulumi.set(self, "private_link_service_proxies", value)

    @property
    @pulumi.getter(name="vnetTrafficTag")
    def vnet_traffic_tag(self) -> Optional[pulumi.Input[str]]:
        """
        Virtual network traffic tag.
        """
        return pulumi.get(self, "vnet_traffic_tag")

    @vnet_traffic_tag.setter
    def vnet_traffic_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vnet_traffic_tag", value)


