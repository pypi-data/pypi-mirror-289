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

__all__ = ['PrivateEndpointConnectionControllerArgs', 'PrivateEndpointConnectionController']

@pulumi.input_type
class PrivateEndpointConnectionControllerArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 site_name: pulumi.Input[str],
                 pe_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input['PrivateLinkServiceConnectionStateArgs']] = None):
        """
        The set of arguments for constructing a PrivateEndpointConnectionController resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] site_name: Site name
        :param pulumi.Input[str] pe_connection_name:  Private link resource name.
        :param pulumi.Input['PrivateLinkServiceConnectionStateArgs'] private_link_service_connection_state: private endpoints connection state
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "site_name", site_name)
        if pe_connection_name is not None:
            pulumi.set(__self__, "pe_connection_name", pe_connection_name)
        if private_link_service_connection_state is not None:
            pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)

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
    @pulumi.getter(name="siteName")
    def site_name(self) -> pulumi.Input[str]:
        """
        Site name
        """
        return pulumi.get(self, "site_name")

    @site_name.setter
    def site_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "site_name", value)

    @property
    @pulumi.getter(name="peConnectionName")
    def pe_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
         Private link resource name.
        """
        return pulumi.get(self, "pe_connection_name")

    @pe_connection_name.setter
    def pe_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pe_connection_name", value)

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[pulumi.Input['PrivateLinkServiceConnectionStateArgs']]:
        """
        private endpoints connection state
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: Optional[pulumi.Input['PrivateLinkServiceConnectionStateArgs']]):
        pulumi.set(self, "private_link_service_connection_state", value)


class PrivateEndpointConnectionController(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pe_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[Union['PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        REST model used to encapsulate Private Link properties for tracked resources.
        Azure REST API version: 2023-06-06.

        Other available API versions: 2023-10-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] pe_connection_name:  Private link resource name.
        :param pulumi.Input[Union['PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict']] private_link_service_connection_state: private endpoints connection state
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] site_name: Site name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateEndpointConnectionControllerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        REST model used to encapsulate Private Link properties for tracked resources.
        Azure REST API version: 2023-06-06.

        Other available API versions: 2023-10-01-preview.

        :param str resource_name: The name of the resource.
        :param PrivateEndpointConnectionControllerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateEndpointConnectionControllerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pe_connection_name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[Union['PrivateLinkServiceConnectionStateArgs', 'PrivateLinkServiceConnectionStateArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PrivateEndpointConnectionControllerArgs.__new__(PrivateEndpointConnectionControllerArgs)

            __props__.__dict__["pe_connection_name"] = pe_connection_name
            __props__.__dict__["private_link_service_connection_state"] = private_link_service_connection_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if site_name is None and not opts.urn:
                raise TypeError("Missing required property 'site_name'")
            __props__.__dict__["site_name"] = site_name
            __props__.__dict__["group_ids"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:offazure/v20200707:PrivateEndpointConnectionController"), pulumi.Alias(type_="azure-native:offazure/v20230606:PrivateEndpointConnectionController"), pulumi.Alias(type_="azure-native:offazure/v20231001preview:PrivateEndpointConnectionController")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateEndpointConnectionController, __self__).__init__(
            'azure-native:offazure:PrivateEndpointConnectionController',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateEndpointConnectionController':
        """
        Get an existing PrivateEndpointConnectionController resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrivateEndpointConnectionControllerArgs.__new__(PrivateEndpointConnectionControllerArgs)

        __props__.__dict__["group_ids"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint"] = None
        __props__.__dict__["private_link_service_connection_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return PrivateEndpointConnectionController(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        array of group ids
        """
        return pulumi.get(self, "group_ids")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> pulumi.Output['outputs.ResourceIdResponse']:
        """
        private endpoints
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Output[Optional['outputs.PrivateLinkServiceConnectionStateResponse']]:
        """
        private endpoints connection state
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        provisioning state enum
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

