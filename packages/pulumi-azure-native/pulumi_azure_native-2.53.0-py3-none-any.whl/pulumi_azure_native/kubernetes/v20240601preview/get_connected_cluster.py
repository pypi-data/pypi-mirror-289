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
    'GetConnectedClusterResult',
    'AwaitableGetConnectedClusterResult',
    'get_connected_cluster',
    'get_connected_cluster_output',
]

@pulumi.output_type
class GetConnectedClusterResult:
    """
    Represents a connected cluster.
    """
    def __init__(__self__, aad_profile=None, agent_public_key_certificate=None, agent_version=None, arc_agent_profile=None, azure_hybrid_benefit=None, connectivity_status=None, distribution=None, distribution_version=None, id=None, identity=None, infrastructure=None, kind=None, kubernetes_version=None, last_connectivity_time=None, location=None, managed_identity_certificate_expiration_time=None, miscellaneous_properties=None, name=None, offering=None, oidc_issuer_profile=None, private_link_scope_resource_id=None, private_link_state=None, provisioning_state=None, security_profile=None, system_data=None, tags=None, total_core_count=None, total_node_count=None, type=None):
        if aad_profile and not isinstance(aad_profile, dict):
            raise TypeError("Expected argument 'aad_profile' to be a dict")
        pulumi.set(__self__, "aad_profile", aad_profile)
        if agent_public_key_certificate and not isinstance(agent_public_key_certificate, str):
            raise TypeError("Expected argument 'agent_public_key_certificate' to be a str")
        pulumi.set(__self__, "agent_public_key_certificate", agent_public_key_certificate)
        if agent_version and not isinstance(agent_version, str):
            raise TypeError("Expected argument 'agent_version' to be a str")
        pulumi.set(__self__, "agent_version", agent_version)
        if arc_agent_profile and not isinstance(arc_agent_profile, dict):
            raise TypeError("Expected argument 'arc_agent_profile' to be a dict")
        pulumi.set(__self__, "arc_agent_profile", arc_agent_profile)
        if azure_hybrid_benefit and not isinstance(azure_hybrid_benefit, str):
            raise TypeError("Expected argument 'azure_hybrid_benefit' to be a str")
        pulumi.set(__self__, "azure_hybrid_benefit", azure_hybrid_benefit)
        if connectivity_status and not isinstance(connectivity_status, str):
            raise TypeError("Expected argument 'connectivity_status' to be a str")
        pulumi.set(__self__, "connectivity_status", connectivity_status)
        if distribution and not isinstance(distribution, str):
            raise TypeError("Expected argument 'distribution' to be a str")
        pulumi.set(__self__, "distribution", distribution)
        if distribution_version and not isinstance(distribution_version, str):
            raise TypeError("Expected argument 'distribution_version' to be a str")
        pulumi.set(__self__, "distribution_version", distribution_version)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if infrastructure and not isinstance(infrastructure, str):
            raise TypeError("Expected argument 'infrastructure' to be a str")
        pulumi.set(__self__, "infrastructure", infrastructure)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if kubernetes_version and not isinstance(kubernetes_version, str):
            raise TypeError("Expected argument 'kubernetes_version' to be a str")
        pulumi.set(__self__, "kubernetes_version", kubernetes_version)
        if last_connectivity_time and not isinstance(last_connectivity_time, str):
            raise TypeError("Expected argument 'last_connectivity_time' to be a str")
        pulumi.set(__self__, "last_connectivity_time", last_connectivity_time)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_identity_certificate_expiration_time and not isinstance(managed_identity_certificate_expiration_time, str):
            raise TypeError("Expected argument 'managed_identity_certificate_expiration_time' to be a str")
        pulumi.set(__self__, "managed_identity_certificate_expiration_time", managed_identity_certificate_expiration_time)
        if miscellaneous_properties and not isinstance(miscellaneous_properties, dict):
            raise TypeError("Expected argument 'miscellaneous_properties' to be a dict")
        pulumi.set(__self__, "miscellaneous_properties", miscellaneous_properties)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if offering and not isinstance(offering, str):
            raise TypeError("Expected argument 'offering' to be a str")
        pulumi.set(__self__, "offering", offering)
        if oidc_issuer_profile and not isinstance(oidc_issuer_profile, dict):
            raise TypeError("Expected argument 'oidc_issuer_profile' to be a dict")
        pulumi.set(__self__, "oidc_issuer_profile", oidc_issuer_profile)
        if private_link_scope_resource_id and not isinstance(private_link_scope_resource_id, str):
            raise TypeError("Expected argument 'private_link_scope_resource_id' to be a str")
        pulumi.set(__self__, "private_link_scope_resource_id", private_link_scope_resource_id)
        if private_link_state and not isinstance(private_link_state, str):
            raise TypeError("Expected argument 'private_link_state' to be a str")
        pulumi.set(__self__, "private_link_state", private_link_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if security_profile and not isinstance(security_profile, dict):
            raise TypeError("Expected argument 'security_profile' to be a dict")
        pulumi.set(__self__, "security_profile", security_profile)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if total_core_count and not isinstance(total_core_count, int):
            raise TypeError("Expected argument 'total_core_count' to be a int")
        pulumi.set(__self__, "total_core_count", total_core_count)
        if total_node_count and not isinstance(total_node_count, int):
            raise TypeError("Expected argument 'total_node_count' to be a int")
        pulumi.set(__self__, "total_node_count", total_node_count)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="aadProfile")
    def aad_profile(self) -> Optional['outputs.AadProfileResponse']:
        """
        AAD profile for the connected cluster.
        """
        return pulumi.get(self, "aad_profile")

    @property
    @pulumi.getter(name="agentPublicKeyCertificate")
    def agent_public_key_certificate(self) -> str:
        """
        Base64 encoded public certificate used by the agent to do the initial handshake to the backend services in Azure.
        """
        return pulumi.get(self, "agent_public_key_certificate")

    @property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> str:
        """
        Version of the agent running on the connected cluster resource
        """
        return pulumi.get(self, "agent_version")

    @property
    @pulumi.getter(name="arcAgentProfile")
    def arc_agent_profile(self) -> Optional['outputs.ArcAgentProfileResponse']:
        """
        Arc agentry configuration for the provisioned cluster.
        """
        return pulumi.get(self, "arc_agent_profile")

    @property
    @pulumi.getter(name="azureHybridBenefit")
    def azure_hybrid_benefit(self) -> Optional[str]:
        """
        Indicates whether Azure Hybrid Benefit is opted in
        """
        return pulumi.get(self, "azure_hybrid_benefit")

    @property
    @pulumi.getter(name="connectivityStatus")
    def connectivity_status(self) -> str:
        """
        Represents the connectivity status of the connected cluster.
        """
        return pulumi.get(self, "connectivity_status")

    @property
    @pulumi.getter
    def distribution(self) -> Optional[str]:
        """
        The Kubernetes distribution running on this connected cluster.
        """
        return pulumi.get(self, "distribution")

    @property
    @pulumi.getter(name="distributionVersion")
    def distribution_version(self) -> Optional[str]:
        """
        The Kubernetes distribution version on this connected cluster.
        """
        return pulumi.get(self, "distribution_version")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> 'outputs.ConnectedClusterIdentityResponse':
        """
        The identity of the connected cluster.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def infrastructure(self) -> Optional[str]:
        """
        The infrastructure on which the Kubernetes cluster represented by this connected cluster is running on.
        """
        return pulumi.get(self, "infrastructure")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The kind of connected cluster.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="kubernetesVersion")
    def kubernetes_version(self) -> str:
        """
        The Kubernetes version of the connected cluster resource
        """
        return pulumi.get(self, "kubernetes_version")

    @property
    @pulumi.getter(name="lastConnectivityTime")
    def last_connectivity_time(self) -> str:
        """
        Time representing the last instance when heart beat was received from the cluster
        """
        return pulumi.get(self, "last_connectivity_time")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedIdentityCertificateExpirationTime")
    def managed_identity_certificate_expiration_time(self) -> str:
        """
        Expiration time of the managed identity certificate
        """
        return pulumi.get(self, "managed_identity_certificate_expiration_time")

    @property
    @pulumi.getter(name="miscellaneousProperties")
    def miscellaneous_properties(self) -> Mapping[str, str]:
        """
        More properties related to the Connected Cluster
        """
        return pulumi.get(self, "miscellaneous_properties")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def offering(self) -> str:
        """
        Connected cluster offering
        """
        return pulumi.get(self, "offering")

    @property
    @pulumi.getter(name="oidcIssuerProfile")
    def oidc_issuer_profile(self) -> Optional['outputs.OidcIssuerProfileResponse']:
        """
        Open ID Connect (OIDC) Issuer Profile for the connected cluster.
        """
        return pulumi.get(self, "oidc_issuer_profile")

    @property
    @pulumi.getter(name="privateLinkScopeResourceId")
    def private_link_scope_resource_id(self) -> Optional[str]:
        """
        This is populated only if privateLinkState is enabled. The resource id of the private link scope this connected cluster is assigned to, if any.
        """
        return pulumi.get(self, "private_link_scope_resource_id")

    @property
    @pulumi.getter(name="privateLinkState")
    def private_link_state(self) -> Optional[str]:
        """
        Property which describes the state of private link on a connected cluster resource.
        """
        return pulumi.get(self, "private_link_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        Provisioning state of the connected cluster resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional['outputs.SecurityProfileResponse']:
        """
        Security profile for the connected cluster.
        """
        return pulumi.get(self, "security_profile")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="totalCoreCount")
    def total_core_count(self) -> int:
        """
        Number of CPU cores present in the connected cluster resource
        """
        return pulumi.get(self, "total_core_count")

    @property
    @pulumi.getter(name="totalNodeCount")
    def total_node_count(self) -> int:
        """
        Number of nodes present in the connected cluster resource
        """
        return pulumi.get(self, "total_node_count")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetConnectedClusterResult(GetConnectedClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectedClusterResult(
            aad_profile=self.aad_profile,
            agent_public_key_certificate=self.agent_public_key_certificate,
            agent_version=self.agent_version,
            arc_agent_profile=self.arc_agent_profile,
            azure_hybrid_benefit=self.azure_hybrid_benefit,
            connectivity_status=self.connectivity_status,
            distribution=self.distribution,
            distribution_version=self.distribution_version,
            id=self.id,
            identity=self.identity,
            infrastructure=self.infrastructure,
            kind=self.kind,
            kubernetes_version=self.kubernetes_version,
            last_connectivity_time=self.last_connectivity_time,
            location=self.location,
            managed_identity_certificate_expiration_time=self.managed_identity_certificate_expiration_time,
            miscellaneous_properties=self.miscellaneous_properties,
            name=self.name,
            offering=self.offering,
            oidc_issuer_profile=self.oidc_issuer_profile,
            private_link_scope_resource_id=self.private_link_scope_resource_id,
            private_link_state=self.private_link_state,
            provisioning_state=self.provisioning_state,
            security_profile=self.security_profile,
            system_data=self.system_data,
            tags=self.tags,
            total_core_count=self.total_core_count,
            total_node_count=self.total_node_count,
            type=self.type)


def get_connected_cluster(cluster_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectedClusterResult:
    """
    Returns the properties of the specified connected cluster, including name, identity, properties, and additional cluster details.


    :param str cluster_name: The name of the Kubernetes cluster on which get is called.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:kubernetes/v20240601preview:getConnectedCluster', __args__, opts=opts, typ=GetConnectedClusterResult).value

    return AwaitableGetConnectedClusterResult(
        aad_profile=pulumi.get(__ret__, 'aad_profile'),
        agent_public_key_certificate=pulumi.get(__ret__, 'agent_public_key_certificate'),
        agent_version=pulumi.get(__ret__, 'agent_version'),
        arc_agent_profile=pulumi.get(__ret__, 'arc_agent_profile'),
        azure_hybrid_benefit=pulumi.get(__ret__, 'azure_hybrid_benefit'),
        connectivity_status=pulumi.get(__ret__, 'connectivity_status'),
        distribution=pulumi.get(__ret__, 'distribution'),
        distribution_version=pulumi.get(__ret__, 'distribution_version'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        infrastructure=pulumi.get(__ret__, 'infrastructure'),
        kind=pulumi.get(__ret__, 'kind'),
        kubernetes_version=pulumi.get(__ret__, 'kubernetes_version'),
        last_connectivity_time=pulumi.get(__ret__, 'last_connectivity_time'),
        location=pulumi.get(__ret__, 'location'),
        managed_identity_certificate_expiration_time=pulumi.get(__ret__, 'managed_identity_certificate_expiration_time'),
        miscellaneous_properties=pulumi.get(__ret__, 'miscellaneous_properties'),
        name=pulumi.get(__ret__, 'name'),
        offering=pulumi.get(__ret__, 'offering'),
        oidc_issuer_profile=pulumi.get(__ret__, 'oidc_issuer_profile'),
        private_link_scope_resource_id=pulumi.get(__ret__, 'private_link_scope_resource_id'),
        private_link_state=pulumi.get(__ret__, 'private_link_state'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        security_profile=pulumi.get(__ret__, 'security_profile'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        total_core_count=pulumi.get(__ret__, 'total_core_count'),
        total_node_count=pulumi.get(__ret__, 'total_node_count'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_connected_cluster)
def get_connected_cluster_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConnectedClusterResult]:
    """
    Returns the properties of the specified connected cluster, including name, identity, properties, and additional cluster details.


    :param str cluster_name: The name of the Kubernetes cluster on which get is called.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
