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
    'SecretAuthInfoResponse',
    'SecretStoreResponse',
    'ServicePrincipalCertificateAuthInfoResponse',
    'ServicePrincipalSecretAuthInfoResponse',
    'SourceConfigurationResponse',
    'SystemAssignedIdentityAuthInfoResponse',
    'SystemDataResponse',
    'UserAssignedIdentityAuthInfoResponse',
    'VNetSolutionResponse',
]

@pulumi.output_type
class SecretAuthInfoResponse(dict):
    """
    The authentication info when authType is secret
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "authType":
            suggest = "auth_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SecretAuthInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SecretAuthInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SecretAuthInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 auth_type: str,
                 name: Optional[str] = None,
                 secret: Optional[str] = None):
        """
        The authentication info when authType is secret
        :param str auth_type: The authentication type.
               Expected value is 'secret'.
        :param str name: Username or account name for secret auth.
        :param str secret: Password or account key for secret auth.
        """
        pulumi.set(__self__, "auth_type", 'secret')
        if name is not None:
            pulumi.set(__self__, "name", name)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> str:
        """
        The authentication type.
        Expected value is 'secret'.
        """
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Username or account name for secret auth.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def secret(self) -> Optional[str]:
        """
        Password or account key for secret auth.
        """
        return pulumi.get(self, "secret")


@pulumi.output_type
class SecretStoreResponse(dict):
    """
    An option to store secret value in secure place
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyVaultId":
            suggest = "key_vault_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SecretStoreResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SecretStoreResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SecretStoreResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 key_vault_id: Optional[str] = None):
        """
        An option to store secret value in secure place
        :param str key_vault_id: The key vault id to store secret
        """
        if key_vault_id is not None:
            pulumi.set(__self__, "key_vault_id", key_vault_id)

    @property
    @pulumi.getter(name="keyVaultId")
    def key_vault_id(self) -> Optional[str]:
        """
        The key vault id to store secret
        """
        return pulumi.get(self, "key_vault_id")


@pulumi.output_type
class ServicePrincipalCertificateAuthInfoResponse(dict):
    """
    The authentication info when authType is servicePrincipal certificate
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "authType":
            suggest = "auth_type"
        elif key == "clientId":
            suggest = "client_id"
        elif key == "principalId":
            suggest = "principal_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServicePrincipalCertificateAuthInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServicePrincipalCertificateAuthInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServicePrincipalCertificateAuthInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 auth_type: str,
                 certificate: str,
                 client_id: str,
                 principal_id: str):
        """
        The authentication info when authType is servicePrincipal certificate
        :param str auth_type: The authentication type.
               Expected value is 'servicePrincipalCertificate'.
        :param str certificate: ServicePrincipal certificate for servicePrincipal auth.
        :param str client_id: Application clientId for servicePrincipal auth.
        :param str principal_id: Principal Id for servicePrincipal auth.
        """
        pulumi.set(__self__, "auth_type", 'servicePrincipalCertificate')
        pulumi.set(__self__, "certificate", certificate)
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "principal_id", principal_id)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> str:
        """
        The authentication type.
        Expected value is 'servicePrincipalCertificate'.
        """
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter
    def certificate(self) -> str:
        """
        ServicePrincipal certificate for servicePrincipal auth.
        """
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        Application clientId for servicePrincipal auth.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        Principal Id for servicePrincipal auth.
        """
        return pulumi.get(self, "principal_id")


@pulumi.output_type
class ServicePrincipalSecretAuthInfoResponse(dict):
    """
    The authentication info when authType is servicePrincipal secret
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "authType":
            suggest = "auth_type"
        elif key == "clientId":
            suggest = "client_id"
        elif key == "principalId":
            suggest = "principal_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServicePrincipalSecretAuthInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServicePrincipalSecretAuthInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServicePrincipalSecretAuthInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 auth_type: str,
                 client_id: str,
                 principal_id: str,
                 secret: str):
        """
        The authentication info when authType is servicePrincipal secret
        :param str auth_type: The authentication type.
               Expected value is 'servicePrincipalSecret'.
        :param str client_id: ServicePrincipal application clientId for servicePrincipal auth.
        :param str principal_id: Principal Id for servicePrincipal auth.
        :param str secret: Secret for servicePrincipal auth.
        """
        pulumi.set(__self__, "auth_type", 'servicePrincipalSecret')
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> str:
        """
        The authentication type.
        Expected value is 'servicePrincipalSecret'.
        """
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        ServicePrincipal application clientId for servicePrincipal auth.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        Principal Id for servicePrincipal auth.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter
    def secret(self) -> str:
        """
        Secret for servicePrincipal auth.
        """
        return pulumi.get(self, "secret")


@pulumi.output_type
class SourceConfigurationResponse(dict):
    """
    A configuration item for source resource
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 value: Optional[str] = None):
        """
        A configuration item for source resource
        :param str name: The name of setting.
        :param str value: The value of setting
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of setting.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The value of setting
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class SystemAssignedIdentityAuthInfoResponse(dict):
    """
    The authentication info when authType is systemAssignedIdentity
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "authType":
            suggest = "auth_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemAssignedIdentityAuthInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemAssignedIdentityAuthInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemAssignedIdentityAuthInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 auth_type: str):
        """
        The authentication info when authType is systemAssignedIdentity
        :param str auth_type: The authentication type.
               Expected value is 'systemAssignedIdentity'.
        """
        pulumi.set(__self__, "auth_type", 'systemAssignedIdentity')

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> str:
        """
        The authentication type.
        Expected value is 'systemAssignedIdentity'.
        """
        return pulumi.get(self, "auth_type")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


@pulumi.output_type
class UserAssignedIdentityAuthInfoResponse(dict):
    """
    The authentication info when authType is userAssignedIdentity
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "authType":
            suggest = "auth_type"
        elif key == "clientId":
            suggest = "client_id"
        elif key == "subscriptionId":
            suggest = "subscription_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserAssignedIdentityAuthInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserAssignedIdentityAuthInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserAssignedIdentityAuthInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 auth_type: str,
                 client_id: str,
                 subscription_id: str):
        """
        The authentication info when authType is userAssignedIdentity
        :param str auth_type: The authentication type.
               Expected value is 'userAssignedIdentity'.
        :param str client_id: Client Id for userAssignedIdentity.
        :param str subscription_id: Subscription id for userAssignedIdentity.
        """
        pulumi.set(__self__, "auth_type", 'userAssignedIdentity')
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "subscription_id", subscription_id)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> str:
        """
        The authentication type.
        Expected value is 'userAssignedIdentity'.
        """
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        Client Id for userAssignedIdentity.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        """
        Subscription id for userAssignedIdentity.
        """
        return pulumi.get(self, "subscription_id")


@pulumi.output_type
class VNetSolutionResponse(dict):
    """
    The VNet solution for linker
    """
    def __init__(__self__, *,
                 type: Optional[str] = None):
        """
        The VNet solution for linker
        :param str type: Type of VNet solution.
        """
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Type of VNet solution.
        """
        return pulumi.get(self, "type")


