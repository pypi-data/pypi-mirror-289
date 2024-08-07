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
    'AADBasedSecurityPrincipalArgs',
    'AADBasedSecurityPrincipalArgsDict',
    'CertBasedSecurityPrincipalArgs',
    'CertBasedSecurityPrincipalArgsDict',
    'CertificateTagsArgs',
    'CertificateTagsArgsDict',
    'DeploymentTypeArgs',
    'DeploymentTypeArgsDict',
    'LedgerPropertiesArgs',
    'LedgerPropertiesArgsDict',
    'ManagedCCFPropertiesArgs',
    'ManagedCCFPropertiesArgsDict',
    'MemberIdentityCertificateArgs',
    'MemberIdentityCertificateArgsDict',
]

MYPY = False

if not MYPY:
    class AADBasedSecurityPrincipalArgsDict(TypedDict):
        """
        AAD based security principal with associated Ledger RoleName
        """
        ledger_role_name: NotRequired[pulumi.Input[Union[str, 'LedgerRoleName']]]
        """
        LedgerRole associated with the Security Principal of Ledger
        """
        principal_id: NotRequired[pulumi.Input[str]]
        """
        UUID/GUID based Principal Id of the Security Principal
        """
        tenant_id: NotRequired[pulumi.Input[str]]
        """
        UUID/GUID based Tenant Id of the Security Principal
        """
elif False:
    AADBasedSecurityPrincipalArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class AADBasedSecurityPrincipalArgs:
    def __init__(__self__, *,
                 ledger_role_name: Optional[pulumi.Input[Union[str, 'LedgerRoleName']]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        AAD based security principal with associated Ledger RoleName
        :param pulumi.Input[Union[str, 'LedgerRoleName']] ledger_role_name: LedgerRole associated with the Security Principal of Ledger
        :param pulumi.Input[str] principal_id: UUID/GUID based Principal Id of the Security Principal
        :param pulumi.Input[str] tenant_id: UUID/GUID based Tenant Id of the Security Principal
        """
        if ledger_role_name is not None:
            pulumi.set(__self__, "ledger_role_name", ledger_role_name)
        if principal_id is not None:
            pulumi.set(__self__, "principal_id", principal_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="ledgerRoleName")
    def ledger_role_name(self) -> Optional[pulumi.Input[Union[str, 'LedgerRoleName']]]:
        """
        LedgerRole associated with the Security Principal of Ledger
        """
        return pulumi.get(self, "ledger_role_name")

    @ledger_role_name.setter
    def ledger_role_name(self, value: Optional[pulumi.Input[Union[str, 'LedgerRoleName']]]):
        pulumi.set(self, "ledger_role_name", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        UUID/GUID based Principal Id of the Security Principal
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        UUID/GUID based Tenant Id of the Security Principal
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


if not MYPY:
    class CertBasedSecurityPrincipalArgsDict(TypedDict):
        """
        Cert based security principal with Ledger RoleName
        """
        cert: NotRequired[pulumi.Input[str]]
        """
        Public key of the user cert (.pem or .cer)
        """
        ledger_role_name: NotRequired[pulumi.Input[Union[str, 'LedgerRoleName']]]
        """
        LedgerRole associated with the Security Principal of Ledger
        """
elif False:
    CertBasedSecurityPrincipalArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CertBasedSecurityPrincipalArgs:
    def __init__(__self__, *,
                 cert: Optional[pulumi.Input[str]] = None,
                 ledger_role_name: Optional[pulumi.Input[Union[str, 'LedgerRoleName']]] = None):
        """
        Cert based security principal with Ledger RoleName
        :param pulumi.Input[str] cert: Public key of the user cert (.pem or .cer)
        :param pulumi.Input[Union[str, 'LedgerRoleName']] ledger_role_name: LedgerRole associated with the Security Principal of Ledger
        """
        if cert is not None:
            pulumi.set(__self__, "cert", cert)
        if ledger_role_name is not None:
            pulumi.set(__self__, "ledger_role_name", ledger_role_name)

    @property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[str]]:
        """
        Public key of the user cert (.pem or .cer)
        """
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter(name="ledgerRoleName")
    def ledger_role_name(self) -> Optional[pulumi.Input[Union[str, 'LedgerRoleName']]]:
        """
        LedgerRole associated with the Security Principal of Ledger
        """
        return pulumi.get(self, "ledger_role_name")

    @ledger_role_name.setter
    def ledger_role_name(self, value: Optional[pulumi.Input[Union[str, 'LedgerRoleName']]]):
        pulumi.set(self, "ledger_role_name", value)


if not MYPY:
    class CertificateTagsArgsDict(TypedDict):
        """
        Tags for Managed CCF Certificates
        """
        tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[str]]]]
        """
        Additional tags for Managed CCF Certificates
        """
elif False:
    CertificateTagsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CertificateTagsArgs:
    def __init__(__self__, *,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Tags for Managed CCF Certificates
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Additional tags for Managed CCF Certificates
        """
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Additional tags for Managed CCF Certificates
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


if not MYPY:
    class DeploymentTypeArgsDict(TypedDict):
        """
        Object representing DeploymentType for Managed CCF.
        """
        app_source_uri: NotRequired[pulumi.Input[str]]
        """
        Source Uri containing ManagedCCF code
        """
        language_runtime: NotRequired[pulumi.Input[Union[str, 'LanguageRuntime']]]
        """
        Unique name for the Managed CCF.
        """
elif False:
    DeploymentTypeArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DeploymentTypeArgs:
    def __init__(__self__, *,
                 app_source_uri: Optional[pulumi.Input[str]] = None,
                 language_runtime: Optional[pulumi.Input[Union[str, 'LanguageRuntime']]] = None):
        """
        Object representing DeploymentType for Managed CCF.
        :param pulumi.Input[str] app_source_uri: Source Uri containing ManagedCCF code
        :param pulumi.Input[Union[str, 'LanguageRuntime']] language_runtime: Unique name for the Managed CCF.
        """
        if app_source_uri is not None:
            pulumi.set(__self__, "app_source_uri", app_source_uri)
        if language_runtime is not None:
            pulumi.set(__self__, "language_runtime", language_runtime)

    @property
    @pulumi.getter(name="appSourceUri")
    def app_source_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Source Uri containing ManagedCCF code
        """
        return pulumi.get(self, "app_source_uri")

    @app_source_uri.setter
    def app_source_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_source_uri", value)

    @property
    @pulumi.getter(name="languageRuntime")
    def language_runtime(self) -> Optional[pulumi.Input[Union[str, 'LanguageRuntime']]]:
        """
        Unique name for the Managed CCF.
        """
        return pulumi.get(self, "language_runtime")

    @language_runtime.setter
    def language_runtime(self, value: Optional[pulumi.Input[Union[str, 'LanguageRuntime']]]):
        pulumi.set(self, "language_runtime", value)


if not MYPY:
    class LedgerPropertiesArgsDict(TypedDict):
        """
        Additional Confidential Ledger properties.
        """
        aad_based_security_principals: NotRequired[pulumi.Input[Sequence[pulumi.Input['AADBasedSecurityPrincipalArgsDict']]]]
        """
        Array of all AAD based Security Principals.
        """
        cert_based_security_principals: NotRequired[pulumi.Input[Sequence[pulumi.Input['CertBasedSecurityPrincipalArgsDict']]]]
        """
        Array of all cert based Security Principals.
        """
        ledger_sku: NotRequired[pulumi.Input[Union[str, 'LedgerSku']]]
        """
        SKU associated with the ledger
        """
        ledger_type: NotRequired[pulumi.Input[Union[str, 'LedgerType']]]
        """
        Type of Confidential Ledger
        """
        running_state: NotRequired[pulumi.Input[Union[str, 'RunningState']]]
        """
        Object representing RunningState for Ledger.
        """
elif False:
    LedgerPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class LedgerPropertiesArgs:
    def __init__(__self__, *,
                 aad_based_security_principals: Optional[pulumi.Input[Sequence[pulumi.Input['AADBasedSecurityPrincipalArgs']]]] = None,
                 cert_based_security_principals: Optional[pulumi.Input[Sequence[pulumi.Input['CertBasedSecurityPrincipalArgs']]]] = None,
                 ledger_sku: Optional[pulumi.Input[Union[str, 'LedgerSku']]] = None,
                 ledger_type: Optional[pulumi.Input[Union[str, 'LedgerType']]] = None,
                 running_state: Optional[pulumi.Input[Union[str, 'RunningState']]] = None):
        """
        Additional Confidential Ledger properties.
        :param pulumi.Input[Sequence[pulumi.Input['AADBasedSecurityPrincipalArgs']]] aad_based_security_principals: Array of all AAD based Security Principals.
        :param pulumi.Input[Sequence[pulumi.Input['CertBasedSecurityPrincipalArgs']]] cert_based_security_principals: Array of all cert based Security Principals.
        :param pulumi.Input[Union[str, 'LedgerSku']] ledger_sku: SKU associated with the ledger
        :param pulumi.Input[Union[str, 'LedgerType']] ledger_type: Type of Confidential Ledger
        :param pulumi.Input[Union[str, 'RunningState']] running_state: Object representing RunningState for Ledger.
        """
        if aad_based_security_principals is not None:
            pulumi.set(__self__, "aad_based_security_principals", aad_based_security_principals)
        if cert_based_security_principals is not None:
            pulumi.set(__self__, "cert_based_security_principals", cert_based_security_principals)
        if ledger_sku is not None:
            pulumi.set(__self__, "ledger_sku", ledger_sku)
        if ledger_type is not None:
            pulumi.set(__self__, "ledger_type", ledger_type)
        if running_state is not None:
            pulumi.set(__self__, "running_state", running_state)

    @property
    @pulumi.getter(name="aadBasedSecurityPrincipals")
    def aad_based_security_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AADBasedSecurityPrincipalArgs']]]]:
        """
        Array of all AAD based Security Principals.
        """
        return pulumi.get(self, "aad_based_security_principals")

    @aad_based_security_principals.setter
    def aad_based_security_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AADBasedSecurityPrincipalArgs']]]]):
        pulumi.set(self, "aad_based_security_principals", value)

    @property
    @pulumi.getter(name="certBasedSecurityPrincipals")
    def cert_based_security_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CertBasedSecurityPrincipalArgs']]]]:
        """
        Array of all cert based Security Principals.
        """
        return pulumi.get(self, "cert_based_security_principals")

    @cert_based_security_principals.setter
    def cert_based_security_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CertBasedSecurityPrincipalArgs']]]]):
        pulumi.set(self, "cert_based_security_principals", value)

    @property
    @pulumi.getter(name="ledgerSku")
    def ledger_sku(self) -> Optional[pulumi.Input[Union[str, 'LedgerSku']]]:
        """
        SKU associated with the ledger
        """
        return pulumi.get(self, "ledger_sku")

    @ledger_sku.setter
    def ledger_sku(self, value: Optional[pulumi.Input[Union[str, 'LedgerSku']]]):
        pulumi.set(self, "ledger_sku", value)

    @property
    @pulumi.getter(name="ledgerType")
    def ledger_type(self) -> Optional[pulumi.Input[Union[str, 'LedgerType']]]:
        """
        Type of Confidential Ledger
        """
        return pulumi.get(self, "ledger_type")

    @ledger_type.setter
    def ledger_type(self, value: Optional[pulumi.Input[Union[str, 'LedgerType']]]):
        pulumi.set(self, "ledger_type", value)

    @property
    @pulumi.getter(name="runningState")
    def running_state(self) -> Optional[pulumi.Input[Union[str, 'RunningState']]]:
        """
        Object representing RunningState for Ledger.
        """
        return pulumi.get(self, "running_state")

    @running_state.setter
    def running_state(self, value: Optional[pulumi.Input[Union[str, 'RunningState']]]):
        pulumi.set(self, "running_state", value)


if not MYPY:
    class ManagedCCFPropertiesArgsDict(TypedDict):
        """
        Additional Managed CCF properties.
        """
        deployment_type: NotRequired[pulumi.Input['DeploymentTypeArgsDict']]
        """
        Deployment Type of Managed CCF
        """
        member_identity_certificates: NotRequired[pulumi.Input[Sequence[pulumi.Input['MemberIdentityCertificateArgsDict']]]]
        """
        List of member identity certificates for  Managed CCF
        """
        node_count: NotRequired[pulumi.Input[int]]
        """
        Number of CCF nodes in the Managed CCF.
        """
        running_state: NotRequired[pulumi.Input[Union[str, 'RunningState']]]
        """
        Object representing RunningState for Managed CCF.
        """
elif False:
    ManagedCCFPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ManagedCCFPropertiesArgs:
    def __init__(__self__, *,
                 deployment_type: Optional[pulumi.Input['DeploymentTypeArgs']] = None,
                 member_identity_certificates: Optional[pulumi.Input[Sequence[pulumi.Input['MemberIdentityCertificateArgs']]]] = None,
                 node_count: Optional[pulumi.Input[int]] = None,
                 running_state: Optional[pulumi.Input[Union[str, 'RunningState']]] = None):
        """
        Additional Managed CCF properties.
        :param pulumi.Input['DeploymentTypeArgs'] deployment_type: Deployment Type of Managed CCF
        :param pulumi.Input[Sequence[pulumi.Input['MemberIdentityCertificateArgs']]] member_identity_certificates: List of member identity certificates for  Managed CCF
        :param pulumi.Input[int] node_count: Number of CCF nodes in the Managed CCF.
        :param pulumi.Input[Union[str, 'RunningState']] running_state: Object representing RunningState for Managed CCF.
        """
        if deployment_type is not None:
            pulumi.set(__self__, "deployment_type", deployment_type)
        if member_identity_certificates is not None:
            pulumi.set(__self__, "member_identity_certificates", member_identity_certificates)
        if node_count is not None:
            pulumi.set(__self__, "node_count", node_count)
        if running_state is not None:
            pulumi.set(__self__, "running_state", running_state)

    @property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> Optional[pulumi.Input['DeploymentTypeArgs']]:
        """
        Deployment Type of Managed CCF
        """
        return pulumi.get(self, "deployment_type")

    @deployment_type.setter
    def deployment_type(self, value: Optional[pulumi.Input['DeploymentTypeArgs']]):
        pulumi.set(self, "deployment_type", value)

    @property
    @pulumi.getter(name="memberIdentityCertificates")
    def member_identity_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MemberIdentityCertificateArgs']]]]:
        """
        List of member identity certificates for  Managed CCF
        """
        return pulumi.get(self, "member_identity_certificates")

    @member_identity_certificates.setter
    def member_identity_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MemberIdentityCertificateArgs']]]]):
        pulumi.set(self, "member_identity_certificates", value)

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[pulumi.Input[int]]:
        """
        Number of CCF nodes in the Managed CCF.
        """
        return pulumi.get(self, "node_count")

    @node_count.setter
    def node_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "node_count", value)

    @property
    @pulumi.getter(name="runningState")
    def running_state(self) -> Optional[pulumi.Input[Union[str, 'RunningState']]]:
        """
        Object representing RunningState for Managed CCF.
        """
        return pulumi.get(self, "running_state")

    @running_state.setter
    def running_state(self, value: Optional[pulumi.Input[Union[str, 'RunningState']]]):
        pulumi.set(self, "running_state", value)


if not MYPY:
    class MemberIdentityCertificateArgsDict(TypedDict):
        """
        Object representing MemberIdentityCertificate for Managed CCF.
        """
        certificate: NotRequired[pulumi.Input[str]]
        """
        Member Identity Certificate
        """
        encryptionkey: NotRequired[pulumi.Input[str]]
        """
        Member Identity Certificate Encryption Key
        """
        tags: NotRequired[pulumi.Input[Sequence[pulumi.Input['CertificateTagsArgsDict']]]]
elif False:
    MemberIdentityCertificateArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MemberIdentityCertificateArgs:
    def __init__(__self__, *,
                 certificate: Optional[pulumi.Input[str]] = None,
                 encryptionkey: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateTagsArgs']]]] = None):
        """
        Object representing MemberIdentityCertificate for Managed CCF.
        :param pulumi.Input[str] certificate: Member Identity Certificate
        :param pulumi.Input[str] encryptionkey: Member Identity Certificate Encryption Key
        """
        if certificate is not None:
            pulumi.set(__self__, "certificate", certificate)
        if encryptionkey is not None:
            pulumi.set(__self__, "encryptionkey", encryptionkey)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[str]]:
        """
        Member Identity Certificate
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter
    def encryptionkey(self) -> Optional[pulumi.Input[str]]:
        """
        Member Identity Certificate Encryption Key
        """
        return pulumi.get(self, "encryptionkey")

    @encryptionkey.setter
    def encryptionkey(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryptionkey", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CertificateTagsArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CertificateTagsArgs']]]]):
        pulumi.set(self, "tags", value)


