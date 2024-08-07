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
    'GetNetworkVirtualApplianceResult',
    'AwaitableGetNetworkVirtualApplianceResult',
    'get_network_virtual_appliance',
    'get_network_virtual_appliance_output',
]

@pulumi.output_type
class GetNetworkVirtualApplianceResult:
    """
    NetworkVirtualAppliance Resource.
    """
    def __init__(__self__, additional_nics=None, address_prefix=None, boot_strap_configuration_blobs=None, cloud_init_configuration=None, cloud_init_configuration_blobs=None, delegation=None, deployment_type=None, etag=None, id=None, identity=None, inbound_security_rules=None, internet_ingress_public_ips=None, location=None, name=None, network_profile=None, nva_sku=None, partner_managed_resource=None, provisioning_state=None, ssh_public_key=None, tags=None, type=None, virtual_appliance_asn=None, virtual_appliance_connections=None, virtual_appliance_nics=None, virtual_appliance_sites=None, virtual_hub=None):
        if additional_nics and not isinstance(additional_nics, list):
            raise TypeError("Expected argument 'additional_nics' to be a list")
        pulumi.set(__self__, "additional_nics", additional_nics)
        if address_prefix and not isinstance(address_prefix, str):
            raise TypeError("Expected argument 'address_prefix' to be a str")
        pulumi.set(__self__, "address_prefix", address_prefix)
        if boot_strap_configuration_blobs and not isinstance(boot_strap_configuration_blobs, list):
            raise TypeError("Expected argument 'boot_strap_configuration_blobs' to be a list")
        pulumi.set(__self__, "boot_strap_configuration_blobs", boot_strap_configuration_blobs)
        if cloud_init_configuration and not isinstance(cloud_init_configuration, str):
            raise TypeError("Expected argument 'cloud_init_configuration' to be a str")
        pulumi.set(__self__, "cloud_init_configuration", cloud_init_configuration)
        if cloud_init_configuration_blobs and not isinstance(cloud_init_configuration_blobs, list):
            raise TypeError("Expected argument 'cloud_init_configuration_blobs' to be a list")
        pulumi.set(__self__, "cloud_init_configuration_blobs", cloud_init_configuration_blobs)
        if delegation and not isinstance(delegation, dict):
            raise TypeError("Expected argument 'delegation' to be a dict")
        pulumi.set(__self__, "delegation", delegation)
        if deployment_type and not isinstance(deployment_type, str):
            raise TypeError("Expected argument 'deployment_type' to be a str")
        pulumi.set(__self__, "deployment_type", deployment_type)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if inbound_security_rules and not isinstance(inbound_security_rules, list):
            raise TypeError("Expected argument 'inbound_security_rules' to be a list")
        pulumi.set(__self__, "inbound_security_rules", inbound_security_rules)
        if internet_ingress_public_ips and not isinstance(internet_ingress_public_ips, list):
            raise TypeError("Expected argument 'internet_ingress_public_ips' to be a list")
        pulumi.set(__self__, "internet_ingress_public_ips", internet_ingress_public_ips)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_profile and not isinstance(network_profile, dict):
            raise TypeError("Expected argument 'network_profile' to be a dict")
        pulumi.set(__self__, "network_profile", network_profile)
        if nva_sku and not isinstance(nva_sku, dict):
            raise TypeError("Expected argument 'nva_sku' to be a dict")
        pulumi.set(__self__, "nva_sku", nva_sku)
        if partner_managed_resource and not isinstance(partner_managed_resource, dict):
            raise TypeError("Expected argument 'partner_managed_resource' to be a dict")
        pulumi.set(__self__, "partner_managed_resource", partner_managed_resource)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if ssh_public_key and not isinstance(ssh_public_key, str):
            raise TypeError("Expected argument 'ssh_public_key' to be a str")
        pulumi.set(__self__, "ssh_public_key", ssh_public_key)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_appliance_asn and not isinstance(virtual_appliance_asn, float):
            raise TypeError("Expected argument 'virtual_appliance_asn' to be a float")
        pulumi.set(__self__, "virtual_appliance_asn", virtual_appliance_asn)
        if virtual_appliance_connections and not isinstance(virtual_appliance_connections, list):
            raise TypeError("Expected argument 'virtual_appliance_connections' to be a list")
        pulumi.set(__self__, "virtual_appliance_connections", virtual_appliance_connections)
        if virtual_appliance_nics and not isinstance(virtual_appliance_nics, list):
            raise TypeError("Expected argument 'virtual_appliance_nics' to be a list")
        pulumi.set(__self__, "virtual_appliance_nics", virtual_appliance_nics)
        if virtual_appliance_sites and not isinstance(virtual_appliance_sites, list):
            raise TypeError("Expected argument 'virtual_appliance_sites' to be a list")
        pulumi.set(__self__, "virtual_appliance_sites", virtual_appliance_sites)
        if virtual_hub and not isinstance(virtual_hub, dict):
            raise TypeError("Expected argument 'virtual_hub' to be a dict")
        pulumi.set(__self__, "virtual_hub", virtual_hub)

    @property
    @pulumi.getter(name="additionalNics")
    def additional_nics(self) -> Optional[Sequence['outputs.VirtualApplianceAdditionalNicPropertiesResponse']]:
        """
        Details required for Additional Network Interface.
        """
        return pulumi.get(self, "additional_nics")

    @property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> str:
        """
        Address Prefix.
        """
        return pulumi.get(self, "address_prefix")

    @property
    @pulumi.getter(name="bootStrapConfigurationBlobs")
    def boot_strap_configuration_blobs(self) -> Optional[Sequence[str]]:
        """
        BootStrapConfigurationBlobs storage URLs.
        """
        return pulumi.get(self, "boot_strap_configuration_blobs")

    @property
    @pulumi.getter(name="cloudInitConfiguration")
    def cloud_init_configuration(self) -> Optional[str]:
        """
        CloudInitConfiguration string in plain text.
        """
        return pulumi.get(self, "cloud_init_configuration")

    @property
    @pulumi.getter(name="cloudInitConfigurationBlobs")
    def cloud_init_configuration_blobs(self) -> Optional[Sequence[str]]:
        """
        CloudInitConfigurationBlob storage URLs.
        """
        return pulumi.get(self, "cloud_init_configuration_blobs")

    @property
    @pulumi.getter
    def delegation(self) -> Optional['outputs.DelegationPropertiesResponse']:
        """
        The delegation for the Virtual Appliance
        """
        return pulumi.get(self, "delegation")

    @property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> str:
        """
        The deployment type. PartnerManaged for the SaaS NVA
        """
        return pulumi.get(self, "deployment_type")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedServiceIdentityResponse']:
        """
        The service principal that has read access to cloud-init and config blob.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="inboundSecurityRules")
    def inbound_security_rules(self) -> Sequence['outputs.SubResourceResponse']:
        """
        List of references to InboundSecurityRules.
        """
        return pulumi.get(self, "inbound_security_rules")

    @property
    @pulumi.getter(name="internetIngressPublicIps")
    def internet_ingress_public_ips(self) -> Optional[Sequence['outputs.InternetIngressPublicIpsPropertiesResponse']]:
        """
        List of Resource Uri of Public IPs for Internet Ingress Scenario.
        """
        return pulumi.get(self, "internet_ingress_public_ips")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional['outputs.NetworkVirtualAppliancePropertiesFormatResponseNetworkProfile']:
        """
        Network Profile containing configurations for Public and Private NIC.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="nvaSku")
    def nva_sku(self) -> Optional['outputs.VirtualApplianceSkuPropertiesResponse']:
        """
        Network Virtual Appliance SKU.
        """
        return pulumi.get(self, "nva_sku")

    @property
    @pulumi.getter(name="partnerManagedResource")
    def partner_managed_resource(self) -> Optional['outputs.PartnerManagedResourcePropertiesResponse']:
        """
        The delegation for the Virtual Appliance
        """
        return pulumi.get(self, "partner_managed_resource")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> Optional[str]:
        """
        Public key for SSH login.
        """
        return pulumi.get(self, "ssh_public_key")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualApplianceAsn")
    def virtual_appliance_asn(self) -> Optional[float]:
        """
        VirtualAppliance ASN. Microsoft private, public and IANA reserved ASN are not supported.
        """
        return pulumi.get(self, "virtual_appliance_asn")

    @property
    @pulumi.getter(name="virtualApplianceConnections")
    def virtual_appliance_connections(self) -> Sequence['outputs.SubResourceResponse']:
        """
        List of references to VirtualApplianceConnections.
        """
        return pulumi.get(self, "virtual_appliance_connections")

    @property
    @pulumi.getter(name="virtualApplianceNics")
    def virtual_appliance_nics(self) -> Sequence['outputs.VirtualApplianceNicPropertiesResponse']:
        """
        List of Virtual Appliance Network Interfaces.
        """
        return pulumi.get(self, "virtual_appliance_nics")

    @property
    @pulumi.getter(name="virtualApplianceSites")
    def virtual_appliance_sites(self) -> Sequence['outputs.SubResourceResponse']:
        """
        List of references to VirtualApplianceSite.
        """
        return pulumi.get(self, "virtual_appliance_sites")

    @property
    @pulumi.getter(name="virtualHub")
    def virtual_hub(self) -> Optional['outputs.SubResourceResponse']:
        """
        The Virtual Hub where Network Virtual Appliance is being deployed.
        """
        return pulumi.get(self, "virtual_hub")


class AwaitableGetNetworkVirtualApplianceResult(GetNetworkVirtualApplianceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkVirtualApplianceResult(
            additional_nics=self.additional_nics,
            address_prefix=self.address_prefix,
            boot_strap_configuration_blobs=self.boot_strap_configuration_blobs,
            cloud_init_configuration=self.cloud_init_configuration,
            cloud_init_configuration_blobs=self.cloud_init_configuration_blobs,
            delegation=self.delegation,
            deployment_type=self.deployment_type,
            etag=self.etag,
            id=self.id,
            identity=self.identity,
            inbound_security_rules=self.inbound_security_rules,
            internet_ingress_public_ips=self.internet_ingress_public_ips,
            location=self.location,
            name=self.name,
            network_profile=self.network_profile,
            nva_sku=self.nva_sku,
            partner_managed_resource=self.partner_managed_resource,
            provisioning_state=self.provisioning_state,
            ssh_public_key=self.ssh_public_key,
            tags=self.tags,
            type=self.type,
            virtual_appliance_asn=self.virtual_appliance_asn,
            virtual_appliance_connections=self.virtual_appliance_connections,
            virtual_appliance_nics=self.virtual_appliance_nics,
            virtual_appliance_sites=self.virtual_appliance_sites,
            virtual_hub=self.virtual_hub)


def get_network_virtual_appliance(expand: Optional[str] = None,
                                  network_virtual_appliance_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkVirtualApplianceResult:
    """
    Gets the specified Network Virtual Appliance.


    :param str expand: Expands referenced resources.
    :param str network_virtual_appliance_name: The name of Network Virtual Appliance.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['networkVirtualApplianceName'] = network_virtual_appliance_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20231101:getNetworkVirtualAppliance', __args__, opts=opts, typ=GetNetworkVirtualApplianceResult).value

    return AwaitableGetNetworkVirtualApplianceResult(
        additional_nics=pulumi.get(__ret__, 'additional_nics'),
        address_prefix=pulumi.get(__ret__, 'address_prefix'),
        boot_strap_configuration_blobs=pulumi.get(__ret__, 'boot_strap_configuration_blobs'),
        cloud_init_configuration=pulumi.get(__ret__, 'cloud_init_configuration'),
        cloud_init_configuration_blobs=pulumi.get(__ret__, 'cloud_init_configuration_blobs'),
        delegation=pulumi.get(__ret__, 'delegation'),
        deployment_type=pulumi.get(__ret__, 'deployment_type'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        inbound_security_rules=pulumi.get(__ret__, 'inbound_security_rules'),
        internet_ingress_public_ips=pulumi.get(__ret__, 'internet_ingress_public_ips'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_profile=pulumi.get(__ret__, 'network_profile'),
        nva_sku=pulumi.get(__ret__, 'nva_sku'),
        partner_managed_resource=pulumi.get(__ret__, 'partner_managed_resource'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        ssh_public_key=pulumi.get(__ret__, 'ssh_public_key'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        virtual_appliance_asn=pulumi.get(__ret__, 'virtual_appliance_asn'),
        virtual_appliance_connections=pulumi.get(__ret__, 'virtual_appliance_connections'),
        virtual_appliance_nics=pulumi.get(__ret__, 'virtual_appliance_nics'),
        virtual_appliance_sites=pulumi.get(__ret__, 'virtual_appliance_sites'),
        virtual_hub=pulumi.get(__ret__, 'virtual_hub'))


@_utilities.lift_output_func(get_network_virtual_appliance)
def get_network_virtual_appliance_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                                         network_virtual_appliance_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkVirtualApplianceResult]:
    """
    Gets the specified Network Virtual Appliance.


    :param str expand: Expands referenced resources.
    :param str network_virtual_appliance_name: The name of Network Virtual Appliance.
    :param str resource_group_name: The name of the resource group.
    """
    ...
