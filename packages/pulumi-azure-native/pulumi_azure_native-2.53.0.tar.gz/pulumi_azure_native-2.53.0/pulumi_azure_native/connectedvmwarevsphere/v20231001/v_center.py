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
from ._inputs import *

__all__ = ['VCenterArgs', 'VCenter']

@pulumi.input_type
class VCenterArgs:
    def __init__(__self__, *,
                 fqdn: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 credentials: Optional[pulumi.Input['VICredentialArgs']] = None,
                 extended_location: Optional[pulumi.Input['ExtendedLocationArgs']] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vcenter_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VCenter resource.
        :param pulumi.Input[str] fqdn: Gets or sets the FQDN/IPAddress of the vCenter.
        :param pulumi.Input[str] resource_group_name: The Resource Group Name.
        :param pulumi.Input['VICredentialArgs'] credentials: Username / Password Credentials to connect to vcenter.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: Gets or sets the extended location.
        :param pulumi.Input[str] kind: Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        :param pulumi.Input[str] location: Gets or sets the location.
        :param pulumi.Input[int] port: Gets or sets the port of the vCenter.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the Resource tags.
        :param pulumi.Input[str] vcenter_name: Name of the vCenter.
        """
        pulumi.set(__self__, "fqdn", fqdn)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if extended_location is not None:
            pulumi.set(__self__, "extended_location", extended_location)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vcenter_name is not None:
            pulumi.set(__self__, "vcenter_name", vcenter_name)

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Input[str]:
        """
        Gets or sets the FQDN/IPAddress of the vCenter.
        """
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: pulumi.Input[str]):
        pulumi.set(self, "fqdn", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The Resource Group Name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['VICredentialArgs']]:
        """
        Username / Password Credentials to connect to vcenter.
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['VICredentialArgs']]):
        pulumi.set(self, "credentials", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional[pulumi.Input['ExtendedLocationArgs']]:
        """
        Gets or sets the extended location.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: Optional[pulumi.Input['ExtendedLocationArgs']]):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        Gets or sets the port of the vCenter.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Gets or sets the Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vcenterName")
    def vcenter_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the vCenter.
        """
        return pulumi.get(self, "vcenter_name")

    @vcenter_name.setter
    def vcenter_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vcenter_name", value)


class VCenter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials: Optional[pulumi.Input[Union['VICredentialArgs', 'VICredentialArgsDict']]] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vcenter_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Defines the vCenter.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['VICredentialArgs', 'VICredentialArgsDict']] credentials: Username / Password Credentials to connect to vcenter.
        :param pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']] extended_location: Gets or sets the extended location.
        :param pulumi.Input[str] fqdn: Gets or sets the FQDN/IPAddress of the vCenter.
        :param pulumi.Input[str] kind: Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        :param pulumi.Input[str] location: Gets or sets the location.
        :param pulumi.Input[int] port: Gets or sets the port of the vCenter.
        :param pulumi.Input[str] resource_group_name: The Resource Group Name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the Resource tags.
        :param pulumi.Input[str] vcenter_name: Name of the vCenter.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VCenterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines the vCenter.

        :param str resource_name: The name of the resource.
        :param VCenterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VCenterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials: Optional[pulumi.Input[Union['VICredentialArgs', 'VICredentialArgsDict']]] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vcenter_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VCenterArgs.__new__(VCenterArgs)

            __props__.__dict__["credentials"] = credentials
            __props__.__dict__["extended_location"] = extended_location
            if fqdn is None and not opts.urn:
                raise TypeError("Missing required property 'fqdn'")
            __props__.__dict__["fqdn"] = fqdn
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["port"] = port
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vcenter_name"] = vcenter_name
            __props__.__dict__["connection_status"] = None
            __props__.__dict__["custom_resource_name"] = None
            __props__.__dict__["instance_uuid"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["statuses"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["uuid"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:connectedvmwarevsphere:VCenter"), pulumi.Alias(type_="azure-native:connectedvmwarevsphere/v20201001preview:VCenter"), pulumi.Alias(type_="azure-native:connectedvmwarevsphere/v20220110preview:VCenter"), pulumi.Alias(type_="azure-native:connectedvmwarevsphere/v20220715preview:VCenter"), pulumi.Alias(type_="azure-native:connectedvmwarevsphere/v20230301preview:VCenter"), pulumi.Alias(type_="azure-native:connectedvmwarevsphere/v20231201:VCenter")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VCenter, __self__).__init__(
            'azure-native:connectedvmwarevsphere/v20231001:VCenter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VCenter':
        """
        Get an existing VCenter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VCenterArgs.__new__(VCenterArgs)

        __props__.__dict__["connection_status"] = None
        __props__.__dict__["credentials"] = None
        __props__.__dict__["custom_resource_name"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["fqdn"] = None
        __props__.__dict__["instance_uuid"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["port"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["statuses"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["uuid"] = None
        __props__.__dict__["version"] = None
        return VCenter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> pulumi.Output[str]:
        """
        Gets or sets the connection status to the vCenter.
        """
        return pulumi.get(self, "connection_status")

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional['outputs.VICredentialResponse']]:
        """
        Username / Password Credentials to connect to vcenter.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="customResourceName")
    def custom_resource_name(self) -> pulumi.Output[str]:
        """
        Gets the name of the corresponding resource in Kubernetes.
        """
        return pulumi.get(self, "custom_resource_name")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output[Optional['outputs.ExtendedLocationResponse']]:
        """
        Gets or sets the extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        Gets or sets the FQDN/IPAddress of the vCenter.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="instanceUuid")
    def instance_uuid(self) -> pulumi.Output[str]:
        """
        Gets or sets the instance UUID of the vCenter.
        """
        return pulumi.get(self, "instance_uuid")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Gets or sets the location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets or sets the name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[int]]:
        """
        Gets or sets the port of the vCenter.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Sequence['outputs.ResourceStatusResponse']]:
        """
        The resource status information.
        """
        return pulumi.get(self, "statuses")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Gets or sets the Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Gets or sets the type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        Gets or sets a unique identifier for this resource.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Gets or sets the version of the vCenter.
        """
        return pulumi.get(self, "version")

