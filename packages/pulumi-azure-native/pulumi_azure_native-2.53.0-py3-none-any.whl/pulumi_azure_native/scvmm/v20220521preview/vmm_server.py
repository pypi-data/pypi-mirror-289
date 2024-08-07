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

__all__ = ['VmmServerArgs', 'VmmServer']

@pulumi.input_type
class VmmServerArgs:
    def __init__(__self__, *,
                 extended_location: pulumi.Input['ExtendedLocationArgs'],
                 fqdn: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 credentials: Optional[pulumi.Input['VMMServerPropertiesCredentialsArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vmm_server_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VmmServer resource.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location.
        :param pulumi.Input[str] fqdn: Fqdn is the hostname/ip of the vmmServer.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['VMMServerPropertiesCredentialsArgs'] credentials: Credentials to connect to VMMServer.
        :param pulumi.Input[str] location: Gets or sets the location.
        :param pulumi.Input[int] port: Port is the port on which the vmmServer is listening.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] vmm_server_name: Name of the VMMServer.
        """
        pulumi.set(__self__, "extended_location", extended_location)
        pulumi.set(__self__, "fqdn", fqdn)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vmm_server_name is not None:
            pulumi.set(__self__, "vmm_server_name", vmm_server_name)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input['ExtendedLocationArgs']:
        """
        The extended location.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: pulumi.Input['ExtendedLocationArgs']):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Input[str]:
        """
        Fqdn is the hostname/ip of the vmmServer.
        """
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: pulumi.Input[str]):
        pulumi.set(self, "fqdn", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def credentials(self) -> Optional[pulumi.Input['VMMServerPropertiesCredentialsArgs']]:
        """
        Credentials to connect to VMMServer.
        """
        return pulumi.get(self, "credentials")

    @credentials.setter
    def credentials(self, value: Optional[pulumi.Input['VMMServerPropertiesCredentialsArgs']]):
        pulumi.set(self, "credentials", value)

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
        Port is the port on which the vmmServer is listening.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vmmServerName")
    def vmm_server_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the VMMServer.
        """
        return pulumi.get(self, "vmm_server_name")

    @vmm_server_name.setter
    def vmm_server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vmm_server_name", value)


class VmmServer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials: Optional[pulumi.Input[Union['VMMServerPropertiesCredentialsArgs', 'VMMServerPropertiesCredentialsArgsDict']]] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vmm_server_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The VmmServers resource definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['VMMServerPropertiesCredentialsArgs', 'VMMServerPropertiesCredentialsArgsDict']] credentials: Credentials to connect to VMMServer.
        :param pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']] extended_location: The extended location.
        :param pulumi.Input[str] fqdn: Fqdn is the hostname/ip of the vmmServer.
        :param pulumi.Input[str] location: Gets or sets the location.
        :param pulumi.Input[int] port: Port is the port on which the vmmServer is listening.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] vmm_server_name: Name of the VMMServer.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VmmServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The VmmServers resource definition.

        :param str resource_name: The name of the resource.
        :param VmmServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VmmServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 credentials: Optional[pulumi.Input[Union['VMMServerPropertiesCredentialsArgs', 'VMMServerPropertiesCredentialsArgsDict']]] = None,
                 extended_location: Optional[pulumi.Input[Union['ExtendedLocationArgs', 'ExtendedLocationArgsDict']]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vmm_server_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VmmServerArgs.__new__(VmmServerArgs)

            __props__.__dict__["credentials"] = credentials
            if extended_location is None and not opts.urn:
                raise TypeError("Missing required property 'extended_location'")
            __props__.__dict__["extended_location"] = extended_location
            if fqdn is None and not opts.urn:
                raise TypeError("Missing required property 'fqdn'")
            __props__.__dict__["fqdn"] = fqdn
            __props__.__dict__["location"] = location
            __props__.__dict__["port"] = port
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vmm_server_name"] = vmm_server_name
            __props__.__dict__["connection_status"] = None
            __props__.__dict__["error_message"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["uuid"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:scvmm:VmmServer"), pulumi.Alias(type_="azure-native:scvmm/v20200605preview:VmmServer"), pulumi.Alias(type_="azure-native:scvmm/v20230401preview:VmmServer"), pulumi.Alias(type_="azure-native:scvmm/v20231007:VmmServer"), pulumi.Alias(type_="azure-native:scvmm/v20240601:VmmServer")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VmmServer, __self__).__init__(
            'azure-native:scvmm/v20220521preview:VmmServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VmmServer':
        """
        Get an existing VmmServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VmmServerArgs.__new__(VmmServerArgs)

        __props__.__dict__["connection_status"] = None
        __props__.__dict__["credentials"] = None
        __props__.__dict__["error_message"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["fqdn"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["port"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["uuid"] = None
        __props__.__dict__["version"] = None
        return VmmServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> pulumi.Output[str]:
        """
        Gets or sets the connection status to the vmmServer.
        """
        return pulumi.get(self, "connection_status")

    @property
    @pulumi.getter
    def credentials(self) -> pulumi.Output[Optional['outputs.VMMServerPropertiesResponseCredentials']]:
        """
        Credentials to connect to VMMServer.
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> pulumi.Output[str]:
        """
        Gets or sets any error message if connection to vmmServer is having any issue.
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output['outputs.ExtendedLocationResponse']:
        """
        The extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[str]:
        """
        Fqdn is the hostname/ip of the vmmServer.
        """
        return pulumi.get(self, "fqdn")

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
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[Optional[int]]:
        """
        Port is the port on which the vmmServer is listening.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Gets or sets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

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
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource Type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        Unique ID of vmmServer.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Version is the version of the vmmSever.
        """
        return pulumi.get(self, "version")

