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
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['PacketCoreControlPlaneArgs', 'PacketCoreControlPlane']

@pulumi.input_type
class PacketCoreControlPlaneArgs:
    def __init__(__self__, *,
                 control_plane_access_interface: pulumi.Input['InterfacePropertiesArgs'],
                 local_diagnostics_access: pulumi.Input['LocalDiagnosticsAccessConfigurationArgs'],
                 platform: pulumi.Input['PlatformConfigurationArgs'],
                 resource_group_name: pulumi.Input[str],
                 sites: pulumi.Input[Sequence[pulumi.Input['SiteResourceIdArgs']]],
                 sku: pulumi.Input[Union[str, 'BillingSku']],
                 core_network_technology: Optional[pulumi.Input[Union[str, 'CoreNetworkType']]] = None,
                 diagnostics_upload: Optional[pulumi.Input['DiagnosticsUploadConfigurationArgs']] = None,
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None,
                 installation: Optional[pulumi.Input['InstallationArgs']] = None,
                 interop_settings: Optional[Any] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 packet_core_control_plane_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 ue_mtu: Optional[pulumi.Input[int]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PacketCoreControlPlane resource.
        :param pulumi.Input['InterfacePropertiesArgs'] control_plane_access_interface: The control plane interface on the access network. For 5G networks, this is the N2 interface. For 4G networks, this is the S1-MME interface.
        :param pulumi.Input['LocalDiagnosticsAccessConfigurationArgs'] local_diagnostics_access: The kubernetes ingress configuration to control access to packet core diagnostics over local APIs.
        :param pulumi.Input['PlatformConfigurationArgs'] platform: The platform where the packet core is deployed.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input['SiteResourceIdArgs']]] sites: Site(s) under which this packet core control plane should be deployed. The sites must be in the same location as the packet core control plane.
        :param pulumi.Input[Union[str, 'BillingSku']] sku: The SKU defining the throughput and SIM allowances for this packet core control plane deployment.
        :param pulumi.Input[Union[str, 'CoreNetworkType']] core_network_technology: The core network technology generation (5G core or EPC / 4G core).
        :param pulumi.Input['DiagnosticsUploadConfigurationArgs'] diagnostics_upload: Configuration for uploading packet core diagnostics
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: The identity used to retrieve the ingress certificate from Azure key vault.
        :param pulumi.Input['InstallationArgs'] installation: The installation state of the packet core control plane resource.
        :param Any interop_settings: Settings to allow interoperability with third party components e.g. RANs and UEs.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] packet_core_control_plane_name: The name of the packet core control plane.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[int] ue_mtu: The MTU (in bytes) signaled to the UE. The same MTU is set on the user plane data links for all data networks. The MTU set on the user plane access link is calculated to be 60 bytes greater than this value to allow for GTP encapsulation.
        :param pulumi.Input[str] version: The desired version of the packet core software.
        """
        pulumi.set(__self__, "control_plane_access_interface", control_plane_access_interface)
        pulumi.set(__self__, "local_diagnostics_access", local_diagnostics_access)
        pulumi.set(__self__, "platform", platform)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sites", sites)
        pulumi.set(__self__, "sku", sku)
        if core_network_technology is not None:
            pulumi.set(__self__, "core_network_technology", core_network_technology)
        if diagnostics_upload is not None:
            pulumi.set(__self__, "diagnostics_upload", diagnostics_upload)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if installation is not None:
            pulumi.set(__self__, "installation", installation)
        if interop_settings is not None:
            pulumi.set(__self__, "interop_settings", interop_settings)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if packet_core_control_plane_name is not None:
            pulumi.set(__self__, "packet_core_control_plane_name", packet_core_control_plane_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if ue_mtu is None:
            ue_mtu = 1440
        if ue_mtu is not None:
            pulumi.set(__self__, "ue_mtu", ue_mtu)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="controlPlaneAccessInterface")
    def control_plane_access_interface(self) -> pulumi.Input['InterfacePropertiesArgs']:
        """
        The control plane interface on the access network. For 5G networks, this is the N2 interface. For 4G networks, this is the S1-MME interface.
        """
        return pulumi.get(self, "control_plane_access_interface")

    @control_plane_access_interface.setter
    def control_plane_access_interface(self, value: pulumi.Input['InterfacePropertiesArgs']):
        pulumi.set(self, "control_plane_access_interface", value)

    @property
    @pulumi.getter(name="localDiagnosticsAccess")
    def local_diagnostics_access(self) -> pulumi.Input['LocalDiagnosticsAccessConfigurationArgs']:
        """
        The kubernetes ingress configuration to control access to packet core diagnostics over local APIs.
        """
        return pulumi.get(self, "local_diagnostics_access")

    @local_diagnostics_access.setter
    def local_diagnostics_access(self, value: pulumi.Input['LocalDiagnosticsAccessConfigurationArgs']):
        pulumi.set(self, "local_diagnostics_access", value)

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Input['PlatformConfigurationArgs']:
        """
        The platform where the packet core is deployed.
        """
        return pulumi.get(self, "platform")

    @platform.setter
    def platform(self, value: pulumi.Input['PlatformConfigurationArgs']):
        pulumi.set(self, "platform", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def sites(self) -> pulumi.Input[Sequence[pulumi.Input['SiteResourceIdArgs']]]:
        """
        Site(s) under which this packet core control plane should be deployed. The sites must be in the same location as the packet core control plane.
        """
        return pulumi.get(self, "sites")

    @sites.setter
    def sites(self, value: pulumi.Input[Sequence[pulumi.Input['SiteResourceIdArgs']]]):
        pulumi.set(self, "sites", value)

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Input[Union[str, 'BillingSku']]:
        """
        The SKU defining the throughput and SIM allowances for this packet core control plane deployment.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: pulumi.Input[Union[str, 'BillingSku']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="coreNetworkTechnology")
    def core_network_technology(self) -> Optional[pulumi.Input[Union[str, 'CoreNetworkType']]]:
        """
        The core network technology generation (5G core or EPC / 4G core).
        """
        return pulumi.get(self, "core_network_technology")

    @core_network_technology.setter
    def core_network_technology(self, value: Optional[pulumi.Input[Union[str, 'CoreNetworkType']]]):
        pulumi.set(self, "core_network_technology", value)

    @property
    @pulumi.getter(name="diagnosticsUpload")
    def diagnostics_upload(self) -> Optional[pulumi.Input['DiagnosticsUploadConfigurationArgs']]:
        """
        Configuration for uploading packet core diagnostics
        """
        return pulumi.get(self, "diagnostics_upload")

    @diagnostics_upload.setter
    def diagnostics_upload(self, value: Optional[pulumi.Input['DiagnosticsUploadConfigurationArgs']]):
        pulumi.set(self, "diagnostics_upload", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        The identity used to retrieve the ingress certificate from Azure key vault.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def installation(self) -> Optional[pulumi.Input['InstallationArgs']]:
        """
        The installation state of the packet core control plane resource.
        """
        return pulumi.get(self, "installation")

    @installation.setter
    def installation(self, value: Optional[pulumi.Input['InstallationArgs']]):
        pulumi.set(self, "installation", value)

    @property
    @pulumi.getter(name="interopSettings")
    def interop_settings(self) -> Optional[Any]:
        """
        Settings to allow interoperability with third party components e.g. RANs and UEs.
        """
        return pulumi.get(self, "interop_settings")

    @interop_settings.setter
    def interop_settings(self, value: Optional[Any]):
        pulumi.set(self, "interop_settings", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="packetCoreControlPlaneName")
    def packet_core_control_plane_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the packet core control plane.
        """
        return pulumi.get(self, "packet_core_control_plane_name")

    @packet_core_control_plane_name.setter
    def packet_core_control_plane_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "packet_core_control_plane_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="ueMtu")
    def ue_mtu(self) -> Optional[pulumi.Input[int]]:
        """
        The MTU (in bytes) signaled to the UE. The same MTU is set on the user plane data links for all data networks. The MTU set on the user plane access link is calculated to be 60 bytes greater than this value to allow for GTP encapsulation.
        """
        return pulumi.get(self, "ue_mtu")

    @ue_mtu.setter
    def ue_mtu(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ue_mtu", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        The desired version of the packet core software.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class PacketCoreControlPlane(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 control_plane_access_interface: Optional[pulumi.Input[Union['InterfacePropertiesArgs', 'InterfacePropertiesArgsDict']]] = None,
                 core_network_technology: Optional[pulumi.Input[Union[str, 'CoreNetworkType']]] = None,
                 diagnostics_upload: Optional[pulumi.Input[Union['DiagnosticsUploadConfigurationArgs', 'DiagnosticsUploadConfigurationArgsDict']]] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 installation: Optional[pulumi.Input[Union['InstallationArgs', 'InstallationArgsDict']]] = None,
                 interop_settings: Optional[Any] = None,
                 local_diagnostics_access: Optional[pulumi.Input[Union['LocalDiagnosticsAccessConfigurationArgs', 'LocalDiagnosticsAccessConfigurationArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 packet_core_control_plane_name: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[Union['PlatformConfigurationArgs', 'PlatformConfigurationArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sites: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SiteResourceIdArgs', 'SiteResourceIdArgsDict']]]]] = None,
                 sku: Optional[pulumi.Input[Union[str, 'BillingSku']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 ue_mtu: Optional[pulumi.Input[int]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Packet core control plane resource.
        Azure REST API version: 2023-06-01. Prior API version in Azure Native 1.x: 2022-04-01-preview.

        Other available API versions: 2022-03-01-preview, 2022-04-01-preview, 2022-11-01, 2023-09-01, 2024-02-01, 2024-04-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['InterfacePropertiesArgs', 'InterfacePropertiesArgsDict']] control_plane_access_interface: The control plane interface on the access network. For 5G networks, this is the N2 interface. For 4G networks, this is the S1-MME interface.
        :param pulumi.Input[Union[str, 'CoreNetworkType']] core_network_technology: The core network technology generation (5G core or EPC / 4G core).
        :param pulumi.Input[Union['DiagnosticsUploadConfigurationArgs', 'DiagnosticsUploadConfigurationArgsDict']] diagnostics_upload: Configuration for uploading packet core diagnostics
        :param pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']] identity: The identity used to retrieve the ingress certificate from Azure key vault.
        :param pulumi.Input[Union['InstallationArgs', 'InstallationArgsDict']] installation: The installation state of the packet core control plane resource.
        :param Any interop_settings: Settings to allow interoperability with third party components e.g. RANs and UEs.
        :param pulumi.Input[Union['LocalDiagnosticsAccessConfigurationArgs', 'LocalDiagnosticsAccessConfigurationArgsDict']] local_diagnostics_access: The kubernetes ingress configuration to control access to packet core diagnostics over local APIs.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] packet_core_control_plane_name: The name of the packet core control plane.
        :param pulumi.Input[Union['PlatformConfigurationArgs', 'PlatformConfigurationArgsDict']] platform: The platform where the packet core is deployed.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[Union['SiteResourceIdArgs', 'SiteResourceIdArgsDict']]]] sites: Site(s) under which this packet core control plane should be deployed. The sites must be in the same location as the packet core control plane.
        :param pulumi.Input[Union[str, 'BillingSku']] sku: The SKU defining the throughput and SIM allowances for this packet core control plane deployment.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[int] ue_mtu: The MTU (in bytes) signaled to the UE. The same MTU is set on the user plane data links for all data networks. The MTU set on the user plane access link is calculated to be 60 bytes greater than this value to allow for GTP encapsulation.
        :param pulumi.Input[str] version: The desired version of the packet core software.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PacketCoreControlPlaneArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Packet core control plane resource.
        Azure REST API version: 2023-06-01. Prior API version in Azure Native 1.x: 2022-04-01-preview.

        Other available API versions: 2022-03-01-preview, 2022-04-01-preview, 2022-11-01, 2023-09-01, 2024-02-01, 2024-04-01.

        :param str resource_name: The name of the resource.
        :param PacketCoreControlPlaneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PacketCoreControlPlaneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 control_plane_access_interface: Optional[pulumi.Input[Union['InterfacePropertiesArgs', 'InterfacePropertiesArgsDict']]] = None,
                 core_network_technology: Optional[pulumi.Input[Union[str, 'CoreNetworkType']]] = None,
                 diagnostics_upload: Optional[pulumi.Input[Union['DiagnosticsUploadConfigurationArgs', 'DiagnosticsUploadConfigurationArgsDict']]] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 installation: Optional[pulumi.Input[Union['InstallationArgs', 'InstallationArgsDict']]] = None,
                 interop_settings: Optional[Any] = None,
                 local_diagnostics_access: Optional[pulumi.Input[Union['LocalDiagnosticsAccessConfigurationArgs', 'LocalDiagnosticsAccessConfigurationArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 packet_core_control_plane_name: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[Union['PlatformConfigurationArgs', 'PlatformConfigurationArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sites: Optional[pulumi.Input[Sequence[pulumi.Input[Union['SiteResourceIdArgs', 'SiteResourceIdArgsDict']]]]] = None,
                 sku: Optional[pulumi.Input[Union[str, 'BillingSku']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 ue_mtu: Optional[pulumi.Input[int]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PacketCoreControlPlaneArgs.__new__(PacketCoreControlPlaneArgs)

            if control_plane_access_interface is None and not opts.urn:
                raise TypeError("Missing required property 'control_plane_access_interface'")
            __props__.__dict__["control_plane_access_interface"] = control_plane_access_interface
            __props__.__dict__["core_network_technology"] = core_network_technology
            __props__.__dict__["diagnostics_upload"] = diagnostics_upload
            __props__.__dict__["identity"] = identity
            __props__.__dict__["installation"] = installation
            __props__.__dict__["interop_settings"] = interop_settings
            if local_diagnostics_access is None and not opts.urn:
                raise TypeError("Missing required property 'local_diagnostics_access'")
            __props__.__dict__["local_diagnostics_access"] = local_diagnostics_access
            __props__.__dict__["location"] = location
            __props__.__dict__["packet_core_control_plane_name"] = packet_core_control_plane_name
            if platform is None and not opts.urn:
                raise TypeError("Missing required property 'platform'")
            __props__.__dict__["platform"] = platform
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sites is None and not opts.urn:
                raise TypeError("Missing required property 'sites'")
            __props__.__dict__["sites"] = sites
            if sku is None and not opts.urn:
                raise TypeError("Missing required property 'sku'")
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            if ue_mtu is None:
                ue_mtu = 1440
            __props__.__dict__["ue_mtu"] = ue_mtu
            __props__.__dict__["version"] = version
            __props__.__dict__["installed_version"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["rollback_version"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:mobilenetwork/v20220301preview:PacketCoreControlPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20220401preview:PacketCoreControlPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20221101:PacketCoreControlPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20230601:PacketCoreControlPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20230901:PacketCoreControlPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20240201:PacketCoreControlPlane"), pulumi.Alias(type_="azure-native:mobilenetwork/v20240401:PacketCoreControlPlane")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PacketCoreControlPlane, __self__).__init__(
            'azure-native:mobilenetwork:PacketCoreControlPlane',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PacketCoreControlPlane':
        """
        Get an existing PacketCoreControlPlane resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PacketCoreControlPlaneArgs.__new__(PacketCoreControlPlaneArgs)

        __props__.__dict__["control_plane_access_interface"] = None
        __props__.__dict__["core_network_technology"] = None
        __props__.__dict__["diagnostics_upload"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["installation"] = None
        __props__.__dict__["installed_version"] = None
        __props__.__dict__["interop_settings"] = None
        __props__.__dict__["local_diagnostics_access"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["platform"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["rollback_version"] = None
        __props__.__dict__["sites"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["ue_mtu"] = None
        __props__.__dict__["version"] = None
        return PacketCoreControlPlane(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="controlPlaneAccessInterface")
    def control_plane_access_interface(self) -> pulumi.Output['outputs.InterfacePropertiesResponse']:
        """
        The control plane interface on the access network. For 5G networks, this is the N2 interface. For 4G networks, this is the S1-MME interface.
        """
        return pulumi.get(self, "control_plane_access_interface")

    @property
    @pulumi.getter(name="coreNetworkTechnology")
    def core_network_technology(self) -> pulumi.Output[Optional[str]]:
        """
        The core network technology generation (5G core or EPC / 4G core).
        """
        return pulumi.get(self, "core_network_technology")

    @property
    @pulumi.getter(name="diagnosticsUpload")
    def diagnostics_upload(self) -> pulumi.Output[Optional['outputs.DiagnosticsUploadConfigurationResponse']]:
        """
        Configuration for uploading packet core diagnostics
        """
        return pulumi.get(self, "diagnostics_upload")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        The identity used to retrieve the ingress certificate from Azure key vault.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def installation(self) -> pulumi.Output[Optional['outputs.InstallationResponse']]:
        """
        The installation state of the packet core control plane resource.
        """
        return pulumi.get(self, "installation")

    @property
    @pulumi.getter(name="installedVersion")
    def installed_version(self) -> pulumi.Output[str]:
        """
        The currently installed version of the packet core software.
        """
        return pulumi.get(self, "installed_version")

    @property
    @pulumi.getter(name="interopSettings")
    def interop_settings(self) -> pulumi.Output[Optional[Any]]:
        """
        Settings to allow interoperability with third party components e.g. RANs and UEs.
        """
        return pulumi.get(self, "interop_settings")

    @property
    @pulumi.getter(name="localDiagnosticsAccess")
    def local_diagnostics_access(self) -> pulumi.Output['outputs.LocalDiagnosticsAccessConfigurationResponse']:
        """
        The kubernetes ingress configuration to control access to packet core diagnostics over local APIs.
        """
        return pulumi.get(self, "local_diagnostics_access")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Output['outputs.PlatformConfigurationResponse']:
        """
        The platform where the packet core is deployed.
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the packet core control plane resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="rollbackVersion")
    def rollback_version(self) -> pulumi.Output[str]:
        """
        The previous version of the packet core software that was deployed. Used when performing the rollback action.
        """
        return pulumi.get(self, "rollback_version")

    @property
    @pulumi.getter
    def sites(self) -> pulumi.Output[Sequence['outputs.SiteResourceIdResponse']]:
        """
        Site(s) under which this packet core control plane should be deployed. The sites must be in the same location as the packet core control plane.
        """
        return pulumi.get(self, "sites")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[str]:
        """
        The SKU defining the throughput and SIM allowances for this packet core control plane deployment.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="ueMtu")
    def ue_mtu(self) -> pulumi.Output[Optional[int]]:
        """
        The MTU (in bytes) signaled to the UE. The same MTU is set on the user plane data links for all data networks. The MTU set on the user plane access link is calculated to be 60 bytes greater than this value to allow for GTP encapsulation.
        """
        return pulumi.get(self, "ue_mtu")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        The desired version of the packet core software.
        """
        return pulumi.get(self, "version")

