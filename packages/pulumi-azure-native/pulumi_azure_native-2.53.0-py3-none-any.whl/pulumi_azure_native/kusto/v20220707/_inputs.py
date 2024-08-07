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
    'AcceptedAudiencesArgs',
    'AcceptedAudiencesArgsDict',
    'AzureSkuArgs',
    'AzureSkuArgsDict',
    'IdentityArgs',
    'IdentityArgsDict',
    'KeyVaultPropertiesArgs',
    'KeyVaultPropertiesArgsDict',
    'OptimizedAutoscaleArgs',
    'OptimizedAutoscaleArgsDict',
    'TrustedExternalTenantArgs',
    'TrustedExternalTenantArgsDict',
    'VirtualNetworkConfigurationArgs',
    'VirtualNetworkConfigurationArgsDict',
]

MYPY = False

if not MYPY:
    class AcceptedAudiencesArgsDict(TypedDict):
        """
        Represents an accepted audience trusted by the cluster.
        """
        value: NotRequired[pulumi.Input[str]]
        """
        GUID or valid URL representing an accepted audience.
        """
elif False:
    AcceptedAudiencesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class AcceptedAudiencesArgs:
    def __init__(__self__, *,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Represents an accepted audience trusted by the cluster.
        :param pulumi.Input[str] value: GUID or valid URL representing an accepted audience.
        """
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        GUID or valid URL representing an accepted audience.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


if not MYPY:
    class AzureSkuArgsDict(TypedDict):
        """
        Azure SKU definition.
        """
        name: pulumi.Input[Union[str, 'AzureSkuName']]
        """
        SKU name.
        """
        tier: pulumi.Input[Union[str, 'AzureSkuTier']]
        """
        SKU tier.
        """
        capacity: NotRequired[pulumi.Input[int]]
        """
        The number of instances of the cluster.
        """
elif False:
    AzureSkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class AzureSkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[Union[str, 'AzureSkuName']],
                 tier: pulumi.Input[Union[str, 'AzureSkuTier']],
                 capacity: Optional[pulumi.Input[int]] = None):
        """
        Azure SKU definition.
        :param pulumi.Input[Union[str, 'AzureSkuName']] name: SKU name.
        :param pulumi.Input[Union[str, 'AzureSkuTier']] tier: SKU tier.
        :param pulumi.Input[int] capacity: The number of instances of the cluster.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "tier", tier)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[str, 'AzureSkuName']]:
        """
        SKU name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[str, 'AzureSkuName']]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> pulumi.Input[Union[str, 'AzureSkuTier']]:
        """
        SKU tier.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: pulumi.Input[Union[str, 'AzureSkuTier']]):
        pulumi.set(self, "tier", value)

    @property
    @pulumi.getter
    def capacity(self) -> Optional[pulumi.Input[int]]:
        """
        The number of instances of the cluster.
        """
        return pulumi.get(self, "capacity")

    @capacity.setter
    def capacity(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "capacity", value)


if not MYPY:
    class IdentityArgsDict(TypedDict):
        """
        Identity for the resource.
        """
        type: pulumi.Input[Union[str, 'IdentityType']]
        """
        The type of managed identity used. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user-assigned identities. The type 'None' will remove all identities.
        """
        user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        The list of user identities associated with the Kusto cluster. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
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
        :param pulumi.Input[Union[str, 'IdentityType']] type: The type of managed identity used. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user-assigned identities. The type 'None' will remove all identities.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: The list of user identities associated with the Kusto cluster. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[Union[str, 'IdentityType']]:
        """
        The type of managed identity used. The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set of user-assigned identities. The type 'None' will remove all identities.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[Union[str, 'IdentityType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of user identities associated with the Kusto cluster. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


if not MYPY:
    class KeyVaultPropertiesArgsDict(TypedDict):
        """
        Properties of the key vault.
        """
        key_name: NotRequired[pulumi.Input[str]]
        """
        The name of the key vault key.
        """
        key_vault_uri: NotRequired[pulumi.Input[str]]
        """
        The Uri of the key vault.
        """
        key_version: NotRequired[pulumi.Input[str]]
        """
        The version of the key vault key.
        """
        user_identity: NotRequired[pulumi.Input[str]]
        """
        The user assigned identity (ARM resource id) that has access to the key.
        """
elif False:
    KeyVaultPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class KeyVaultPropertiesArgs:
    def __init__(__self__, *,
                 key_name: Optional[pulumi.Input[str]] = None,
                 key_vault_uri: Optional[pulumi.Input[str]] = None,
                 key_version: Optional[pulumi.Input[str]] = None,
                 user_identity: Optional[pulumi.Input[str]] = None):
        """
        Properties of the key vault.
        :param pulumi.Input[str] key_name: The name of the key vault key.
        :param pulumi.Input[str] key_vault_uri: The Uri of the key vault.
        :param pulumi.Input[str] key_version: The version of the key vault key.
        :param pulumi.Input[str] user_identity: The user assigned identity (ARM resource id) that has access to the key.
        """
        if key_name is not None:
            pulumi.set(__self__, "key_name", key_name)
        if key_vault_uri is not None:
            pulumi.set(__self__, "key_vault_uri", key_vault_uri)
        if key_version is not None:
            pulumi.set(__self__, "key_version", key_version)
        if user_identity is not None:
            pulumi.set(__self__, "user_identity", user_identity)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the key vault key.
        """
        return pulumi.get(self, "key_name")

    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_name", value)

    @property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> Optional[pulumi.Input[str]]:
        """
        The Uri of the key vault.
        """
        return pulumi.get(self, "key_vault_uri")

    @key_vault_uri.setter
    def key_vault_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_vault_uri", value)

    @property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the key vault key.
        """
        return pulumi.get(self, "key_version")

    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_version", value)

    @property
    @pulumi.getter(name="userIdentity")
    def user_identity(self) -> Optional[pulumi.Input[str]]:
        """
        The user assigned identity (ARM resource id) that has access to the key.
        """
        return pulumi.get(self, "user_identity")

    @user_identity.setter
    def user_identity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_identity", value)


if not MYPY:
    class OptimizedAutoscaleArgsDict(TypedDict):
        """
        A class that contains the optimized auto scale definition.
        """
        is_enabled: pulumi.Input[bool]
        """
        A boolean value that indicate if the optimized autoscale feature is enabled or not.
        """
        maximum: pulumi.Input[int]
        """
        Maximum allowed instances count.
        """
        minimum: pulumi.Input[int]
        """
        Minimum allowed instances count.
        """
        version: pulumi.Input[int]
        """
        The version of the template defined, for instance 1.
        """
elif False:
    OptimizedAutoscaleArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class OptimizedAutoscaleArgs:
    def __init__(__self__, *,
                 is_enabled: pulumi.Input[bool],
                 maximum: pulumi.Input[int],
                 minimum: pulumi.Input[int],
                 version: pulumi.Input[int]):
        """
        A class that contains the optimized auto scale definition.
        :param pulumi.Input[bool] is_enabled: A boolean value that indicate if the optimized autoscale feature is enabled or not.
        :param pulumi.Input[int] maximum: Maximum allowed instances count.
        :param pulumi.Input[int] minimum: Minimum allowed instances count.
        :param pulumi.Input[int] version: The version of the template defined, for instance 1.
        """
        pulumi.set(__self__, "is_enabled", is_enabled)
        pulumi.set(__self__, "maximum", maximum)
        pulumi.set(__self__, "minimum", minimum)
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[bool]:
        """
        A boolean value that indicate if the optimized autoscale feature is enabled or not.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter
    def maximum(self) -> pulumi.Input[int]:
        """
        Maximum allowed instances count.
        """
        return pulumi.get(self, "maximum")

    @maximum.setter
    def maximum(self, value: pulumi.Input[int]):
        pulumi.set(self, "maximum", value)

    @property
    @pulumi.getter
    def minimum(self) -> pulumi.Input[int]:
        """
        Minimum allowed instances count.
        """
        return pulumi.get(self, "minimum")

    @minimum.setter
    def minimum(self, value: pulumi.Input[int]):
        pulumi.set(self, "minimum", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[int]:
        """
        The version of the template defined, for instance 1.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[int]):
        pulumi.set(self, "version", value)


if not MYPY:
    class TrustedExternalTenantArgsDict(TypedDict):
        """
        Represents a tenant ID that is trusted by the cluster.
        """
        value: NotRequired[pulumi.Input[str]]
        """
        GUID representing an external tenant.
        """
elif False:
    TrustedExternalTenantArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class TrustedExternalTenantArgs:
    def __init__(__self__, *,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Represents a tenant ID that is trusted by the cluster.
        :param pulumi.Input[str] value: GUID representing an external tenant.
        """
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        GUID representing an external tenant.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


if not MYPY:
    class VirtualNetworkConfigurationArgsDict(TypedDict):
        """
        A class that contains virtual network definition.
        """
        data_management_public_ip_id: pulumi.Input[str]
        """
        Data management's service public IP address resource id.
        """
        engine_public_ip_id: pulumi.Input[str]
        """
        Engine service's public IP address resource id.
        """
        subnet_id: pulumi.Input[str]
        """
        The subnet resource id.
        """
elif False:
    VirtualNetworkConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class VirtualNetworkConfigurationArgs:
    def __init__(__self__, *,
                 data_management_public_ip_id: pulumi.Input[str],
                 engine_public_ip_id: pulumi.Input[str],
                 subnet_id: pulumi.Input[str]):
        """
        A class that contains virtual network definition.
        :param pulumi.Input[str] data_management_public_ip_id: Data management's service public IP address resource id.
        :param pulumi.Input[str] engine_public_ip_id: Engine service's public IP address resource id.
        :param pulumi.Input[str] subnet_id: The subnet resource id.
        """
        pulumi.set(__self__, "data_management_public_ip_id", data_management_public_ip_id)
        pulumi.set(__self__, "engine_public_ip_id", engine_public_ip_id)
        pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="dataManagementPublicIpId")
    def data_management_public_ip_id(self) -> pulumi.Input[str]:
        """
        Data management's service public IP address resource id.
        """
        return pulumi.get(self, "data_management_public_ip_id")

    @data_management_public_ip_id.setter
    def data_management_public_ip_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_management_public_ip_id", value)

    @property
    @pulumi.getter(name="enginePublicIpId")
    def engine_public_ip_id(self) -> pulumi.Input[str]:
        """
        Engine service's public IP address resource id.
        """
        return pulumi.get(self, "engine_public_ip_id")

    @engine_public_ip_id.setter
    def engine_public_ip_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "engine_public_ip_id", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        The subnet resource id.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)


