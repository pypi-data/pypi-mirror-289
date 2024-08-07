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
    'EncryptionPropertiesIdentityArgs',
    'EncryptionPropertiesIdentityArgsDict',
    'EncryptionPropertiesArgs',
    'EncryptionPropertiesArgsDict',
    'ManagedServiceIdentityArgs',
    'ManagedServiceIdentityArgsDict',
]

MYPY = False

if not MYPY:
    class EncryptionPropertiesIdentityArgsDict(TypedDict):
        """
        All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        """
        resource_id: NotRequired[pulumi.Input[str]]
        """
        User assigned identity to use for accessing key encryption key Url. Ex: /subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId.
        """
        type: NotRequired[pulumi.Input[Union[str, 'Type']]]
        """
        Managed identity type to use for accessing encryption key Url.
        """
elif False:
    EncryptionPropertiesIdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class EncryptionPropertiesIdentityArgs:
    def __init__(__self__, *,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[Union[str, 'Type']]] = None):
        """
        All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        :param pulumi.Input[str] resource_id: User assigned identity to use for accessing key encryption key Url. Ex: /subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId.
        :param pulumi.Input[Union[str, 'Type']] type: Managed identity type to use for accessing encryption key Url.
        """
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        User assigned identity to use for accessing key encryption key Url. Ex: /subscriptions/fa5fc227-a624-475e-b696-cdd604c735bc/resourceGroups/<resource group>/providers/Microsoft.ManagedIdentity/userAssignedIdentities/myId.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'Type']]]:
        """
        Managed identity type to use for accessing encryption key Url.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'Type']]]):
        pulumi.set(self, "type", value)


if not MYPY:
    class EncryptionPropertiesArgsDict(TypedDict):
        """
        Key and identity details for Customer Managed Key encryption of load test resource.
        """
        identity: NotRequired[pulumi.Input['EncryptionPropertiesIdentityArgsDict']]
        """
        All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        """
        key_url: NotRequired[pulumi.Input[str]]
        """
        key encryption key Url, versioned. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek.
        """
elif False:
    EncryptionPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class EncryptionPropertiesArgs:
    def __init__(__self__, *,
                 identity: Optional[pulumi.Input['EncryptionPropertiesIdentityArgs']] = None,
                 key_url: Optional[pulumi.Input[str]] = None):
        """
        Key and identity details for Customer Managed Key encryption of load test resource.
        :param pulumi.Input['EncryptionPropertiesIdentityArgs'] identity: All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        :param pulumi.Input[str] key_url: key encryption key Url, versioned. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek.
        """
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if key_url is not None:
            pulumi.set(__self__, "key_url", key_url)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['EncryptionPropertiesIdentityArgs']]:
        """
        All identity configuration for Customer-managed key settings defining which identity should be used to auth to Key Vault.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['EncryptionPropertiesIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="keyUrl")
    def key_url(self) -> Optional[pulumi.Input[str]]:
        """
        key encryption key Url, versioned. Ex: https://contosovault.vault.azure.net/keys/contosokek/562a4bb76b524a1493a6afe8e536ee78 or https://contosovault.vault.azure.net/keys/contosokek.
        """
        return pulumi.get(self, "key_url")

    @key_url.setter
    def key_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_url", value)


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


