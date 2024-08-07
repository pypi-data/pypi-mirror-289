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
    'EncryptionIdentityArgs',
    'EncryptionIdentityArgsDict',
    'EncryptionPropertiesArgs',
    'EncryptionPropertiesArgsDict',
    'IdentityArgs',
    'IdentityArgsDict',
    'KeyVaultPropertiesArgs',
    'KeyVaultPropertiesArgsDict',
    'ManagedByInfoArgs',
    'ManagedByInfoArgsDict',
    'NetworkRuleSetArgs',
    'NetworkRuleSetArgsDict',
    'PrivateLinkServiceConnectionStateArgs',
    'PrivateLinkServiceConnectionStateArgsDict',
    'SkuArgs',
    'SkuArgsDict',
    'SnapshotCreationDataArgs',
    'SnapshotCreationDataArgsDict',
    'SourceCreationDataArgs',
    'SourceCreationDataArgsDict',
    'VirtualNetworkRuleArgs',
    'VirtualNetworkRuleArgsDict',
]

MYPY = False

if not MYPY:
    class EncryptionIdentityArgsDict(TypedDict):
        """
        Encryption identity for the volume group.
        """
        encryption_user_assigned_identity: NotRequired[pulumi.Input[str]]
        """
        Resource identifier of the UserAssigned identity to be associated with server-side encryption on the volume group.
        """
elif False:
    EncryptionIdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class EncryptionIdentityArgs:
    def __init__(__self__, *,
                 encryption_user_assigned_identity: Optional[pulumi.Input[str]] = None):
        """
        Encryption identity for the volume group.
        :param pulumi.Input[str] encryption_user_assigned_identity: Resource identifier of the UserAssigned identity to be associated with server-side encryption on the volume group.
        """
        if encryption_user_assigned_identity is not None:
            pulumi.set(__self__, "encryption_user_assigned_identity", encryption_user_assigned_identity)

    @property
    @pulumi.getter(name="encryptionUserAssignedIdentity")
    def encryption_user_assigned_identity(self) -> Optional[pulumi.Input[str]]:
        """
        Resource identifier of the UserAssigned identity to be associated with server-side encryption on the volume group.
        """
        return pulumi.get(self, "encryption_user_assigned_identity")

    @encryption_user_assigned_identity.setter
    def encryption_user_assigned_identity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_user_assigned_identity", value)


if not MYPY:
    class EncryptionPropertiesArgsDict(TypedDict):
        """
        The encryption settings on the volume group.
        """
        encryption_identity: NotRequired[pulumi.Input['EncryptionIdentityArgsDict']]
        """
        The identity to be used with service-side encryption at rest.
        """
        key_vault_properties: NotRequired[pulumi.Input['KeyVaultPropertiesArgsDict']]
        """
        Properties provided by key vault.
        """
elif False:
    EncryptionPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class EncryptionPropertiesArgs:
    def __init__(__self__, *,
                 encryption_identity: Optional[pulumi.Input['EncryptionIdentityArgs']] = None,
                 key_vault_properties: Optional[pulumi.Input['KeyVaultPropertiesArgs']] = None):
        """
        The encryption settings on the volume group.
        :param pulumi.Input['EncryptionIdentityArgs'] encryption_identity: The identity to be used with service-side encryption at rest.
        :param pulumi.Input['KeyVaultPropertiesArgs'] key_vault_properties: Properties provided by key vault.
        """
        if encryption_identity is not None:
            pulumi.set(__self__, "encryption_identity", encryption_identity)
        if key_vault_properties is not None:
            pulumi.set(__self__, "key_vault_properties", key_vault_properties)

    @property
    @pulumi.getter(name="encryptionIdentity")
    def encryption_identity(self) -> Optional[pulumi.Input['EncryptionIdentityArgs']]:
        """
        The identity to be used with service-side encryption at rest.
        """
        return pulumi.get(self, "encryption_identity")

    @encryption_identity.setter
    def encryption_identity(self, value: Optional[pulumi.Input['EncryptionIdentityArgs']]):
        pulumi.set(self, "encryption_identity", value)

    @property
    @pulumi.getter(name="keyVaultProperties")
    def key_vault_properties(self) -> Optional[pulumi.Input['KeyVaultPropertiesArgs']]:
        """
        Properties provided by key vault.
        """
        return pulumi.get(self, "key_vault_properties")

    @key_vault_properties.setter
    def key_vault_properties(self, value: Optional[pulumi.Input['KeyVaultPropertiesArgs']]):
        pulumi.set(self, "key_vault_properties", value)


if not MYPY:
    class IdentityArgsDict(TypedDict):
        """
        Identity for the resource.
        """
        type: pulumi.Input[Union[str, 'IdentityType']]
        """
        The identity type.
        """
        user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        Gets or sets a list of key value pairs that describe the set of User Assigned identities that will be used with this volume group. The key is the ARM resource identifier of the identity.
        """
elif False:
    IdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[Union[str, 'IdentityType']],
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Identity for the resource.
        :param pulumi.Input[Union[str, 'IdentityType']] type: The identity type.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: Gets or sets a list of key value pairs that describe the set of User Assigned identities that will be used with this volume group. The key is the ARM resource identifier of the identity.
        """
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'IdentityType']]:
        """
        The identity type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'IdentityType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Gets or sets a list of key value pairs that describe the set of User Assigned identities that will be used with this volume group. The key is the ARM resource identifier of the identity.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


if not MYPY:
    class KeyVaultPropertiesArgsDict(TypedDict):
        """
        Properties of key vault.
        """
        key_name: NotRequired[pulumi.Input[str]]
        """
        The name of KeyVault key.
        """
        key_vault_uri: NotRequired[pulumi.Input[str]]
        """
        The Uri of KeyVault.
        """
        key_version: NotRequired[pulumi.Input[str]]
        """
        The version of KeyVault key.
        """
elif False:
    KeyVaultPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(__self__, *,
                 key_name: Optional[pulumi.Input[str]] = None,
                 key_vault_uri: Optional[pulumi.Input[str]] = None,
                 key_version: Optional[pulumi.Input[str]] = None):
        """
        Properties of key vault.
        :param pulumi.Input[str] key_name: The name of KeyVault key.
        :param pulumi.Input[str] key_vault_uri: The Uri of KeyVault.
        :param pulumi.Input[str] key_version: The version of KeyVault key.
        """
        if key_name is not None:
            pulumi.set(__self__, "key_name", key_name)
        if key_vault_uri is not None:
            pulumi.set(__self__, "key_vault_uri", key_vault_uri)
        if key_version is not None:
            pulumi.set(__self__, "key_version", key_version)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of KeyVault key.
        """
        return pulumi.get(self, "key_name")

    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_name", value)

    @property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The Uri of KeyVault.
        """
        return pulumi.get(self, "key_vault_uri")

    @key_vault_uri.setter
    def key_vault_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_vault_uri", value)

    @property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of KeyVault key.
        """
        return pulumi.get(self, "key_version")

    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_version", value)


if not MYPY:
    class ManagedByInfoArgsDict(TypedDict):
        """
        Parent resource information.
        """
        resource_id: NotRequired[pulumi.Input[str]]
        """
        Resource ID of the resource managing the volume, this is a restricted field and can only be set for internal use.
        """
elif False:
    ManagedByInfoArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ManagedByInfoArgs:
    def __init__(__self__, *,
                 resource_id: Optional[pulumi.Input[str]] = None):
        """
        Parent resource information.
        :param pulumi.Input[str] resource_id: Resource ID of the resource managing the volume, this is a restricted field and can only be set for internal use.
        """
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID of the resource managing the volume, this is a restricted field and can only be set for internal use.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)


if not MYPY:
    class NetworkRuleSetArgsDict(TypedDict):
        """
        A set of rules governing the network accessibility.
        """
        virtual_network_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgsDict']]]]
        """
        The list of virtual network rules.
        """
elif False:
    NetworkRuleSetArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class NetworkRuleSetArgs:
    def __init__(__self__, *,
                 virtual_network_rules: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgs']]]] = None):
        """
        A set of rules governing the network accessibility.
        :param pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgs']]] virtual_network_rules: The list of virtual network rules.
        """
        if virtual_network_rules is not None:
            pulumi.set(__self__, "virtual_network_rules", virtual_network_rules)

    @property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgs']]]]:
        """
        The list of virtual network rules.
        """
        return pulumi.get(self, "virtual_network_rules")

    @virtual_network_rules.setter
    def virtual_network_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VirtualNetworkRuleArgs']]]]):
        pulumi.set(self, "virtual_network_rules", value)


if not MYPY:
    class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
        """
        Response for Private Link Service Connection state
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
        Response for Private Link Service Connection state
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
    class SkuArgsDict(TypedDict):
        """
        The SKU name. Required for account creation; optional for update.
        """
        name: pulumi.Input[Union[str, 'SkuName']]
        """
        The sku name.
        """
        tier: NotRequired[pulumi.Input[Union[str, 'SkuTier']]]
        """
        The sku tier.
        """
elif False:
    SkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[Union[str, 'SkuName']],
                 tier: Optional[pulumi.Input[Union[str, 'SkuTier']]] = None):
        """
        The SKU name. Required for account creation; optional for update.
        :param pulumi.Input[Union[str, 'SkuName']] name: The sku name.
        :param pulumi.Input[Union[str, 'SkuTier']] tier: The sku tier.
        """
        pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[str, 'SkuName']]:
        """
        The sku name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[str, 'SkuName']]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[Union[str, 'SkuTier']]]:
        """
        The sku tier.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[Union[str, 'SkuTier']]]):
        pulumi.set(self, "tier", value)


if not MYPY:
    class SnapshotCreationDataArgsDict(TypedDict):
        """
        Data used when creating a volume snapshot.
        """
        source_id: pulumi.Input[str]
        """
        Fully qualified resource ID of the volume. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}/volumegroups/{volumeGroupName}/volumes/{volumeName}"
        """
elif False:
    SnapshotCreationDataArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SnapshotCreationDataArgs:
    def __init__(__self__, *,
                 source_id: pulumi.Input[str]):
        """
        Data used when creating a volume snapshot.
        :param pulumi.Input[str] source_id: Fully qualified resource ID of the volume. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}/volumegroups/{volumeGroupName}/volumes/{volumeName}"
        """
        pulumi.set(__self__, "source_id", source_id)

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Input[str]:
        """
        Fully qualified resource ID of the volume. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ElasticSan/elasticSans/{elasticSanName}/volumegroups/{volumeGroupName}/volumes/{volumeName}"
        """
        return pulumi.get(self, "source_id")

    @source_id.setter
    def source_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_id", value)


if not MYPY:
    class SourceCreationDataArgsDict(TypedDict):
        """
        Data source used when creating the volume.
        """
        create_source: NotRequired[pulumi.Input[Union[str, 'VolumeCreateOption']]]
        """
        This enumerates the possible sources of a volume creation.
        """
        source_id: NotRequired[pulumi.Input[str]]
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
elif False:
    SourceCreationDataArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SourceCreationDataArgs:
    def __init__(__self__, *,
                 create_source: Optional[pulumi.Input[Union[str, 'VolumeCreateOption']]] = None,
                 source_id: Optional[pulumi.Input[str]] = None):
        """
        Data source used when creating the volume.
        :param pulumi.Input[Union[str, 'VolumeCreateOption']] create_source: This enumerates the possible sources of a volume creation.
        :param pulumi.Input[str] source_id: Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        if create_source is not None:
            pulumi.set(__self__, "create_source", create_source)
        if source_id is not None:
            pulumi.set(__self__, "source_id", source_id)

    @property
    @pulumi.getter(name="createSource")
    def create_source(self) -> Optional[pulumi.Input[Union[str, 'VolumeCreateOption']]]:
        """
        This enumerates the possible sources of a volume creation.
        """
        return pulumi.get(self, "create_source")

    @create_source.setter
    def create_source(self, value: Optional[pulumi.Input[Union[str, 'VolumeCreateOption']]]):
        pulumi.set(self, "create_source", value)

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> Optional[pulumi.Input[str]]:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "source_id")

    @source_id.setter
    def source_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_id", value)


if not MYPY:
    class VirtualNetworkRuleArgsDict(TypedDict):
        """
        Virtual Network rule.
        """
        virtual_network_resource_id: pulumi.Input[str]
        """
        Resource ID of a subnet, for example: /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}.
        """
        action: NotRequired[pulumi.Input[Union[str, 'Action']]]
        """
        The action of virtual network rule.
        """
elif False:
    VirtualNetworkRuleArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class VirtualNetworkRuleArgs:
    def __init__(__self__, *,
                 virtual_network_resource_id: pulumi.Input[str],
                 action: Optional[pulumi.Input[Union[str, 'Action']]] = None):
        """
        Virtual Network rule.
        :param pulumi.Input[str] virtual_network_resource_id: Resource ID of a subnet, for example: /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}.
        :param pulumi.Input[Union[str, 'Action']] action: The action of virtual network rule.
        """
        pulumi.set(__self__, "virtual_network_resource_id", virtual_network_resource_id)
        if action is None:
            action = 'Allow'
        if action is not None:
            pulumi.set(__self__, "action", action)

    @property
    @pulumi.getter(name="virtualNetworkResourceId")
    def virtual_network_resource_id(self) -> pulumi.Input[str]:
        """
        Resource ID of a subnet, for example: /subscriptions/{subscriptionId}/resourceGroups/{groupName}/providers/Microsoft.Network/virtualNetworks/{vnetName}/subnets/{subnetName}.
        """
        return pulumi.get(self, "virtual_network_resource_id")

    @virtual_network_resource_id.setter
    def virtual_network_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_network_resource_id", value)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[Union[str, 'Action']]]:
        """
        The action of virtual network rule.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[Union[str, 'Action']]]):
        pulumi.set(self, "action", value)


