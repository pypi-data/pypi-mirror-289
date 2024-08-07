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
    'GetBastionHostResult',
    'AwaitableGetBastionHostResult',
    'get_bastion_host',
    'get_bastion_host_output',
]

@pulumi.output_type
class GetBastionHostResult:
    """
    Bastion Host resource.
    """
    def __init__(__self__, disable_copy_paste=None, dns_name=None, enable_file_copy=None, enable_ip_connect=None, enable_kerberos=None, enable_session_recording=None, enable_shareable_link=None, enable_tunneling=None, etag=None, id=None, ip_configurations=None, location=None, name=None, network_acls=None, provisioning_state=None, scale_units=None, sku=None, tags=None, type=None, virtual_network=None, zones=None):
        if disable_copy_paste and not isinstance(disable_copy_paste, bool):
            raise TypeError("Expected argument 'disable_copy_paste' to be a bool")
        pulumi.set(__self__, "disable_copy_paste", disable_copy_paste)
        if dns_name and not isinstance(dns_name, str):
            raise TypeError("Expected argument 'dns_name' to be a str")
        pulumi.set(__self__, "dns_name", dns_name)
        if enable_file_copy and not isinstance(enable_file_copy, bool):
            raise TypeError("Expected argument 'enable_file_copy' to be a bool")
        pulumi.set(__self__, "enable_file_copy", enable_file_copy)
        if enable_ip_connect and not isinstance(enable_ip_connect, bool):
            raise TypeError("Expected argument 'enable_ip_connect' to be a bool")
        pulumi.set(__self__, "enable_ip_connect", enable_ip_connect)
        if enable_kerberos and not isinstance(enable_kerberos, bool):
            raise TypeError("Expected argument 'enable_kerberos' to be a bool")
        pulumi.set(__self__, "enable_kerberos", enable_kerberos)
        if enable_session_recording and not isinstance(enable_session_recording, bool):
            raise TypeError("Expected argument 'enable_session_recording' to be a bool")
        pulumi.set(__self__, "enable_session_recording", enable_session_recording)
        if enable_shareable_link and not isinstance(enable_shareable_link, bool):
            raise TypeError("Expected argument 'enable_shareable_link' to be a bool")
        pulumi.set(__self__, "enable_shareable_link", enable_shareable_link)
        if enable_tunneling and not isinstance(enable_tunneling, bool):
            raise TypeError("Expected argument 'enable_tunneling' to be a bool")
        pulumi.set(__self__, "enable_tunneling", enable_tunneling)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_configurations and not isinstance(ip_configurations, list):
            raise TypeError("Expected argument 'ip_configurations' to be a list")
        pulumi.set(__self__, "ip_configurations", ip_configurations)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_acls and not isinstance(network_acls, dict):
            raise TypeError("Expected argument 'network_acls' to be a dict")
        pulumi.set(__self__, "network_acls", network_acls)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if scale_units and not isinstance(scale_units, int):
            raise TypeError("Expected argument 'scale_units' to be a int")
        pulumi.set(__self__, "scale_units", scale_units)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_network and not isinstance(virtual_network, dict):
            raise TypeError("Expected argument 'virtual_network' to be a dict")
        pulumi.set(__self__, "virtual_network", virtual_network)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="disableCopyPaste")
    def disable_copy_paste(self) -> Optional[bool]:
        """
        Enable/Disable Copy/Paste feature of the Bastion Host resource.
        """
        return pulumi.get(self, "disable_copy_paste")

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> Optional[str]:
        """
        FQDN for the endpoint on which bastion host is accessible.
        """
        return pulumi.get(self, "dns_name")

    @property
    @pulumi.getter(name="enableFileCopy")
    def enable_file_copy(self) -> Optional[bool]:
        """
        Enable/Disable File Copy feature of the Bastion Host resource.
        """
        return pulumi.get(self, "enable_file_copy")

    @property
    @pulumi.getter(name="enableIpConnect")
    def enable_ip_connect(self) -> Optional[bool]:
        """
        Enable/Disable IP Connect feature of the Bastion Host resource.
        """
        return pulumi.get(self, "enable_ip_connect")

    @property
    @pulumi.getter(name="enableKerberos")
    def enable_kerberos(self) -> Optional[bool]:
        """
        Enable/Disable Kerberos feature of the Bastion Host resource.
        """
        return pulumi.get(self, "enable_kerberos")

    @property
    @pulumi.getter(name="enableSessionRecording")
    def enable_session_recording(self) -> Optional[bool]:
        """
        Enable/Disable Session Recording feature of the Bastion Host resource.
        """
        return pulumi.get(self, "enable_session_recording")

    @property
    @pulumi.getter(name="enableShareableLink")
    def enable_shareable_link(self) -> Optional[bool]:
        """
        Enable/Disable Shareable Link of the Bastion Host resource.
        """
        return pulumi.get(self, "enable_shareable_link")

    @property
    @pulumi.getter(name="enableTunneling")
    def enable_tunneling(self) -> Optional[bool]:
        """
        Enable/Disable Tunneling feature of the Bastion Host resource.
        """
        return pulumi.get(self, "enable_tunneling")

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
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Optional[Sequence['outputs.BastionHostIPConfigurationResponse']]:
        """
        IP configuration of the Bastion Host resource.
        """
        return pulumi.get(self, "ip_configurations")

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
    @pulumi.getter(name="networkAcls")
    def network_acls(self) -> Optional['outputs.BastionHostPropertiesFormatResponseNetworkAcls']:
        return pulumi.get(self, "network_acls")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the bastion host resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="scaleUnits")
    def scale_units(self) -> Optional[int]:
        """
        The scale units for the Bastion Host resource.
        """
        return pulumi.get(self, "scale_units")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The sku of this Bastion Host.
        """
        return pulumi.get(self, "sku")

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
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(self) -> Optional['outputs.SubResourceResponse']:
        """
        Reference to an existing virtual network required for Developer Bastion Host only.
        """
        return pulumi.get(self, "virtual_network")

    @property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[str]]:
        """
        A list of availability zones denoting where the resource needs to come from.
        """
        return pulumi.get(self, "zones")


class AwaitableGetBastionHostResult(GetBastionHostResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBastionHostResult(
            disable_copy_paste=self.disable_copy_paste,
            dns_name=self.dns_name,
            enable_file_copy=self.enable_file_copy,
            enable_ip_connect=self.enable_ip_connect,
            enable_kerberos=self.enable_kerberos,
            enable_session_recording=self.enable_session_recording,
            enable_shareable_link=self.enable_shareable_link,
            enable_tunneling=self.enable_tunneling,
            etag=self.etag,
            id=self.id,
            ip_configurations=self.ip_configurations,
            location=self.location,
            name=self.name,
            network_acls=self.network_acls,
            provisioning_state=self.provisioning_state,
            scale_units=self.scale_units,
            sku=self.sku,
            tags=self.tags,
            type=self.type,
            virtual_network=self.virtual_network,
            zones=self.zones)


def get_bastion_host(bastion_host_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBastionHostResult:
    """
    Gets the specified Bastion Host.


    :param str bastion_host_name: The name of the Bastion Host.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['bastionHostName'] = bastion_host_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20240101:getBastionHost', __args__, opts=opts, typ=GetBastionHostResult).value

    return AwaitableGetBastionHostResult(
        disable_copy_paste=pulumi.get(__ret__, 'disable_copy_paste'),
        dns_name=pulumi.get(__ret__, 'dns_name'),
        enable_file_copy=pulumi.get(__ret__, 'enable_file_copy'),
        enable_ip_connect=pulumi.get(__ret__, 'enable_ip_connect'),
        enable_kerberos=pulumi.get(__ret__, 'enable_kerberos'),
        enable_session_recording=pulumi.get(__ret__, 'enable_session_recording'),
        enable_shareable_link=pulumi.get(__ret__, 'enable_shareable_link'),
        enable_tunneling=pulumi.get(__ret__, 'enable_tunneling'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        ip_configurations=pulumi.get(__ret__, 'ip_configurations'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        network_acls=pulumi.get(__ret__, 'network_acls'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        scale_units=pulumi.get(__ret__, 'scale_units'),
        sku=pulumi.get(__ret__, 'sku'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        virtual_network=pulumi.get(__ret__, 'virtual_network'),
        zones=pulumi.get(__ret__, 'zones'))


@_utilities.lift_output_func(get_bastion_host)
def get_bastion_host_output(bastion_host_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBastionHostResult]:
    """
    Gets the specified Bastion Host.


    :param str bastion_host_name: The name of the Bastion Host.
    :param str resource_group_name: The name of the resource group.
    """
    ...
