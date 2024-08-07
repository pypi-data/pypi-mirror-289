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
    'AzureDevOpsOrganizationProfileArgs',
    'AzureDevOpsOrganizationProfileArgsDict',
    'DevOpsAzureSkuArgs',
    'DevOpsAzureSkuArgsDict',
    'ManagedServiceIdentityArgs',
    'ManagedServiceIdentityArgsDict',
    'NetworkProfileArgs',
    'NetworkProfileArgsDict',
    'OrganizationArgs',
    'OrganizationArgsDict',
    'OsProfileArgs',
    'OsProfileArgsDict',
    'PoolImageArgs',
    'PoolImageArgsDict',
    'SecretsManagementSettingsArgs',
    'SecretsManagementSettingsArgsDict',
    'StatefulArgs',
    'StatefulArgsDict',
    'StatelessAgentProfileArgs',
    'StatelessAgentProfileArgsDict',
    'VmssFabricProfileArgs',
    'VmssFabricProfileArgsDict',
]

MYPY = False

if not MYPY:
    class AzureDevOpsOrganizationProfileArgsDict(TypedDict):
        """
        Azure DevOps organization profile
        """
        kind: pulumi.Input[str]
        """
        Discriminator property for OrganizationProfile.
        Expected value is 'AzureDevOps'.
        """
        organizations: pulumi.Input[Sequence[pulumi.Input['OrganizationArgsDict']]]
        """
        The list of Azure DevOps organizations the pool should be present in.
        """
elif False:
    AzureDevOpsOrganizationProfileArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class AzureDevOpsOrganizationProfileArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 organizations: pulumi.Input[Sequence[pulumi.Input['OrganizationArgs']]]):
        """
        Azure DevOps organization profile
        :param pulumi.Input[str] kind: Discriminator property for OrganizationProfile.
               Expected value is 'AzureDevOps'.
        :param pulumi.Input[Sequence[pulumi.Input['OrganizationArgs']]] organizations: The list of Azure DevOps organizations the pool should be present in.
        """
        pulumi.set(__self__, "kind", 'AzureDevOps')
        pulumi.set(__self__, "organizations", organizations)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Discriminator property for OrganizationProfile.
        Expected value is 'AzureDevOps'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def organizations(self) -> pulumi.Input[Sequence[pulumi.Input['OrganizationArgs']]]:
        """
        The list of Azure DevOps organizations the pool should be present in.
        """
        return pulumi.get(self, "organizations")

    @organizations.setter
    def organizations(self, value: pulumi.Input[Sequence[pulumi.Input['OrganizationArgs']]]):
        pulumi.set(self, "organizations", value)


if not MYPY:
    class DevOpsAzureSkuArgsDict(TypedDict):
        """
        The Azure SKU of the machines in the pool.
        """
        name: pulumi.Input[str]
        """
        The Azure SKU name of the machines in the pool.
        """
        tier: NotRequired[pulumi.Input[str]]
        """
        The Azure SKU tier of the machines in the pool.
        """
elif False:
    DevOpsAzureSkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DevOpsAzureSkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 tier: Optional[pulumi.Input[str]] = None):
        """
        The Azure SKU of the machines in the pool.
        :param pulumi.Input[str] name: The Azure SKU name of the machines in the pool.
        :param pulumi.Input[str] tier: The Azure SKU tier of the machines in the pool.
        """
        pulumi.set(__self__, "name", name)
        if tier is None:
            tier = 'Standard'
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The Azure SKU name of the machines in the pool.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure SKU tier of the machines in the pool.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tier", value)


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
    class NetworkProfileArgsDict(TypedDict):
        """
        The network profile of the machines in the pool.
        """
        subnet_id: pulumi.Input[str]
        """
        The subnet id on which to put all machines created in the pool.
        """
elif False:
    NetworkProfileArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class NetworkProfileArgs:
    def __init__(__self__, *,
                 subnet_id: pulumi.Input[str]):
        """
        The network profile of the machines in the pool.
        :param pulumi.Input[str] subnet_id: The subnet id on which to put all machines created in the pool.
        """
        pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        """
        The subnet id on which to put all machines created in the pool.
        """
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)


if not MYPY:
    class OrganizationArgsDict(TypedDict):
        """
        Defines an Azure DevOps organization.
        """
        url: pulumi.Input[str]
        """
        The Azure DevOps organization URL in which the pool should be created.
        """
        parallelism: NotRequired[pulumi.Input[int]]
        """
        How many machines can be created at maximum in this organization out of the maximumConcurrency of the pool.
        """
        projects: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        Optional list of projects in which the pool should be created.
        """
elif False:
    OrganizationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class OrganizationArgs:
    def __init__(__self__, *,
                 url: pulumi.Input[str],
                 parallelism: Optional[pulumi.Input[int]] = None,
                 projects: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Defines an Azure DevOps organization.
        :param pulumi.Input[str] url: The Azure DevOps organization URL in which the pool should be created.
        :param pulumi.Input[int] parallelism: How many machines can be created at maximum in this organization out of the maximumConcurrency of the pool.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] projects: Optional list of projects in which the pool should be created.
        """
        pulumi.set(__self__, "url", url)
        if parallelism is not None:
            pulumi.set(__self__, "parallelism", parallelism)
        if projects is not None:
            pulumi.set(__self__, "projects", projects)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        The Azure DevOps organization URL in which the pool should be created.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def parallelism(self) -> Optional[pulumi.Input[int]]:
        """
        How many machines can be created at maximum in this organization out of the maximumConcurrency of the pool.
        """
        return pulumi.get(self, "parallelism")

    @parallelism.setter
    def parallelism(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "parallelism", value)

    @property
    @pulumi.getter
    def projects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Optional list of projects in which the pool should be created.
        """
        return pulumi.get(self, "projects")

    @projects.setter
    def projects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "projects", value)


if not MYPY:
    class OsProfileArgsDict(TypedDict):
        """
        The OS profile of the machines in the pool.
        """
        secrets_management_settings: pulumi.Input['SecretsManagementSettingsArgsDict']
        """
        The secret management settings of the machines in the pool.
        """
elif False:
    OsProfileArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class OsProfileArgs:
    def __init__(__self__, *,
                 secrets_management_settings: pulumi.Input['SecretsManagementSettingsArgs']):
        """
        The OS profile of the machines in the pool.
        :param pulumi.Input['SecretsManagementSettingsArgs'] secrets_management_settings: The secret management settings of the machines in the pool.
        """
        pulumi.set(__self__, "secrets_management_settings", secrets_management_settings)

    @property
    @pulumi.getter(name="secretsManagementSettings")
    def secrets_management_settings(self) -> pulumi.Input['SecretsManagementSettingsArgs']:
        """
        The secret management settings of the machines in the pool.
        """
        return pulumi.get(self, "secrets_management_settings")

    @secrets_management_settings.setter
    def secrets_management_settings(self, value: pulumi.Input['SecretsManagementSettingsArgs']):
        pulumi.set(self, "secrets_management_settings", value)


if not MYPY:
    class PoolImageArgsDict(TypedDict):
        """
        The VM image of the machines in the pool.
        """
        resource_id: pulumi.Input[str]
        """
        The resource id of the image.
        """
        aliases: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        List of aliases to reference the image by.
        """
        buffer: NotRequired[pulumi.Input[str]]
        """
        The percentage of the buffer to be allocated to this image.
        """
elif False:
    PoolImageArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PoolImageArgs:
    def __init__(__self__, *,
                 resource_id: pulumi.Input[str],
                 aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 buffer: Optional[pulumi.Input[str]] = None):
        """
        The VM image of the machines in the pool.
        :param pulumi.Input[str] resource_id: The resource id of the image.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] aliases: List of aliases to reference the image by.
        :param pulumi.Input[str] buffer: The percentage of the buffer to be allocated to this image.
        """
        pulumi.set(__self__, "resource_id", resource_id)
        if aliases is not None:
            pulumi.set(__self__, "aliases", aliases)
        if buffer is None:
            buffer = '*'
        if buffer is not None:
            pulumi.set(__self__, "buffer", buffer)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        The resource id of the image.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter
    def aliases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of aliases to reference the image by.
        """
        return pulumi.get(self, "aliases")

    @aliases.setter
    def aliases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "aliases", value)

    @property
    @pulumi.getter
    def buffer(self) -> Optional[pulumi.Input[str]]:
        """
        The percentage of the buffer to be allocated to this image.
        """
        return pulumi.get(self, "buffer")

    @buffer.setter
    def buffer(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "buffer", value)


if not MYPY:
    class SecretsManagementSettingsArgsDict(TypedDict):
        """
        The secret management settings of the machines in the pool.
        """
        key_exportable: pulumi.Input[bool]
        """
        Defines if the key of the certificates should be exportable.
        """
        observed_certificates: pulumi.Input[Sequence[pulumi.Input[str]]]
        """
        The list of certificates to install on all machines in the pool.
        """
        certificate_store_location: NotRequired[pulumi.Input[str]]
        """
        Where to store certificates on the machine.
        """
elif False:
    SecretsManagementSettingsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SecretsManagementSettingsArgs:
    def __init__(__self__, *,
                 key_exportable: pulumi.Input[bool],
                 observed_certificates: pulumi.Input[Sequence[pulumi.Input[str]]],
                 certificate_store_location: Optional[pulumi.Input[str]] = None):
        """
        The secret management settings of the machines in the pool.
        :param pulumi.Input[bool] key_exportable: Defines if the key of the certificates should be exportable.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] observed_certificates: The list of certificates to install on all machines in the pool.
        :param pulumi.Input[str] certificate_store_location: Where to store certificates on the machine.
        """
        pulumi.set(__self__, "key_exportable", key_exportable)
        pulumi.set(__self__, "observed_certificates", observed_certificates)
        if certificate_store_location is not None:
            pulumi.set(__self__, "certificate_store_location", certificate_store_location)

    @property
    @pulumi.getter(name="keyExportable")
    def key_exportable(self) -> pulumi.Input[bool]:
        """
        Defines if the key of the certificates should be exportable.
        """
        return pulumi.get(self, "key_exportable")

    @key_exportable.setter
    def key_exportable(self, value: pulumi.Input[bool]):
        pulumi.set(self, "key_exportable", value)

    @property
    @pulumi.getter(name="observedCertificates")
    def observed_certificates(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of certificates to install on all machines in the pool.
        """
        return pulumi.get(self, "observed_certificates")

    @observed_certificates.setter
    def observed_certificates(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "observed_certificates", value)

    @property
    @pulumi.getter(name="certificateStoreLocation")
    def certificate_store_location(self) -> Optional[pulumi.Input[str]]:
        """
        Where to store certificates on the machine.
        """
        return pulumi.get(self, "certificate_store_location")

    @certificate_store_location.setter
    def certificate_store_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_store_location", value)


if not MYPY:
    class StatefulArgsDict(TypedDict):
        """
        Stateful profile meaning that the machines will be returned to the pool after running a job.
        """
        kind: pulumi.Input[str]
        """
        Discriminator property for AgentProfile.
        Expected value is 'Stateful'.
        """
        max_agent_lifetime: pulumi.Input[str]
        """
        How long should stateful machines be kept around. The maximum is one week.
        """
        resource_predictions: NotRequired[Any]
        """
        Defines pool buffer.
        """
elif False:
    StatefulArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class StatefulArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 max_agent_lifetime: pulumi.Input[str],
                 resource_predictions: Optional[Any] = None):
        """
        Stateful profile meaning that the machines will be returned to the pool after running a job.
        :param pulumi.Input[str] kind: Discriminator property for AgentProfile.
               Expected value is 'Stateful'.
        :param pulumi.Input[str] max_agent_lifetime: How long should stateful machines be kept around. The maximum is one week.
        :param Any resource_predictions: Defines pool buffer.
        """
        pulumi.set(__self__, "kind", 'Stateful')
        pulumi.set(__self__, "max_agent_lifetime", max_agent_lifetime)
        if resource_predictions is not None:
            pulumi.set(__self__, "resource_predictions", resource_predictions)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Discriminator property for AgentProfile.
        Expected value is 'Stateful'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="maxAgentLifetime")
    def max_agent_lifetime(self) -> pulumi.Input[str]:
        """
        How long should stateful machines be kept around. The maximum is one week.
        """
        return pulumi.get(self, "max_agent_lifetime")

    @max_agent_lifetime.setter
    def max_agent_lifetime(self, value: pulumi.Input[str]):
        pulumi.set(self, "max_agent_lifetime", value)

    @property
    @pulumi.getter(name="resourcePredictions")
    def resource_predictions(self) -> Optional[Any]:
        """
        Defines pool buffer.
        """
        return pulumi.get(self, "resource_predictions")

    @resource_predictions.setter
    def resource_predictions(self, value: Optional[Any]):
        pulumi.set(self, "resource_predictions", value)


if not MYPY:
    class StatelessAgentProfileArgsDict(TypedDict):
        """
        Stateless profile meaning that the machines will be cleaned up after running a job.
        """
        kind: pulumi.Input[str]
        """
        Discriminator property for AgentProfile.
        Expected value is 'Stateless'.
        """
        resource_predictions: NotRequired[Any]
        """
        Defines pool buffer.
        """
elif False:
    StatelessAgentProfileArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class StatelessAgentProfileArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 resource_predictions: Optional[Any] = None):
        """
        Stateless profile meaning that the machines will be cleaned up after running a job.
        :param pulumi.Input[str] kind: Discriminator property for AgentProfile.
               Expected value is 'Stateless'.
        :param Any resource_predictions: Defines pool buffer.
        """
        pulumi.set(__self__, "kind", 'Stateless')
        if resource_predictions is not None:
            pulumi.set(__self__, "resource_predictions", resource_predictions)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Discriminator property for AgentProfile.
        Expected value is 'Stateless'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="resourcePredictions")
    def resource_predictions(self) -> Optional[Any]:
        """
        Defines pool buffer.
        """
        return pulumi.get(self, "resource_predictions")

    @resource_predictions.setter
    def resource_predictions(self, value: Optional[Any]):
        pulumi.set(self, "resource_predictions", value)


if not MYPY:
    class VmssFabricProfileArgsDict(TypedDict):
        """
        The agents will run on Virtual Machine Scale Sets.
        """
        images: pulumi.Input[Sequence[pulumi.Input['PoolImageArgsDict']]]
        """
        The VM images of the machines in the pool.
        """
        kind: pulumi.Input[str]
        """
        Discriminator property for FabricProfile.
        Expected value is 'Vmss'.
        """
        sku: pulumi.Input['DevOpsAzureSkuArgsDict']
        """
        The Azure SKU of the machines in the pool.
        """
        network_profile: NotRequired[pulumi.Input['NetworkProfileArgsDict']]
        """
        The network profile of the machines in the pool.
        """
        os_profile: NotRequired[pulumi.Input['OsProfileArgsDict']]
        """
        The OS profile of the machines in the pool.
        """
elif False:
    VmssFabricProfileArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class VmssFabricProfileArgs:
    def __init__(__self__, *,
                 images: pulumi.Input[Sequence[pulumi.Input['PoolImageArgs']]],
                 kind: pulumi.Input[str],
                 sku: pulumi.Input['DevOpsAzureSkuArgs'],
                 network_profile: Optional[pulumi.Input['NetworkProfileArgs']] = None,
                 os_profile: Optional[pulumi.Input['OsProfileArgs']] = None):
        """
        The agents will run on Virtual Machine Scale Sets.
        :param pulumi.Input[Sequence[pulumi.Input['PoolImageArgs']]] images: The VM images of the machines in the pool.
        :param pulumi.Input[str] kind: Discriminator property for FabricProfile.
               Expected value is 'Vmss'.
        :param pulumi.Input['DevOpsAzureSkuArgs'] sku: The Azure SKU of the machines in the pool.
        :param pulumi.Input['NetworkProfileArgs'] network_profile: The network profile of the machines in the pool.
        :param pulumi.Input['OsProfileArgs'] os_profile: The OS profile of the machines in the pool.
        """
        pulumi.set(__self__, "images", images)
        pulumi.set(__self__, "kind", 'Vmss')
        pulumi.set(__self__, "sku", sku)
        if network_profile is not None:
            pulumi.set(__self__, "network_profile", network_profile)
        if os_profile is not None:
            pulumi.set(__self__, "os_profile", os_profile)

    @property
    @pulumi.getter
    def images(self) -> pulumi.Input[Sequence[pulumi.Input['PoolImageArgs']]]:
        """
        The VM images of the machines in the pool.
        """
        return pulumi.get(self, "images")

    @images.setter
    def images(self, value: pulumi.Input[Sequence[pulumi.Input['PoolImageArgs']]]):
        pulumi.set(self, "images", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Discriminator property for FabricProfile.
        Expected value is 'Vmss'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input['DevOpsAzureSkuArgs']:
        """
        The Azure SKU of the machines in the pool.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input['DevOpsAzureSkuArgs']):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input['NetworkProfileArgs']]:
        """
        The network profile of the machines in the pool.
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input['NetworkProfileArgs']]):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input['OsProfileArgs']]:
        """
        The OS profile of the machines in the pool.
        """
        return pulumi.get(self, "os_profile")

    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input['OsProfileArgs']]):
        pulumi.set(self, "os_profile", value)


