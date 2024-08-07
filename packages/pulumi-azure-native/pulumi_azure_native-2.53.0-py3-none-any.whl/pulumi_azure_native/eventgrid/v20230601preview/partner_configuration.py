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
from ._enums import *
from ._inputs import *

__all__ = ['PartnerConfigurationArgs', 'PartnerConfiguration']

@pulumi.input_type
class PartnerConfigurationArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 partner_authorization: Optional[pulumi.Input['PartnerAuthorizationArgs']] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'PartnerConfigurationProvisioningState']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a PartnerConfiguration resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input['PartnerAuthorizationArgs'] partner_authorization: The details of authorized partners.
        :param pulumi.Input[Union[str, 'PartnerConfigurationProvisioningState']] provisioning_state: Provisioning state of the partner configuration.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if partner_authorization is not None:
            pulumi.set(__self__, "partner_authorization", partner_authorization)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="partnerAuthorization")
    def partner_authorization(self) -> Optional[pulumi.Input['PartnerAuthorizationArgs']]:
        """
        The details of authorized partners.
        """
        return pulumi.get(self, "partner_authorization")

    @partner_authorization.setter
    def partner_authorization(self, value: Optional[pulumi.Input['PartnerAuthorizationArgs']]):
        pulumi.set(self, "partner_authorization", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'PartnerConfigurationProvisioningState']]]:
        """
        Provisioning state of the partner configuration.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'PartnerConfigurationProvisioningState']]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class PartnerConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 partner_authorization: Optional[pulumi.Input[Union['PartnerAuthorizationArgs', 'PartnerAuthorizationArgsDict']]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'PartnerConfigurationProvisioningState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Partner configuration information

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[Union['PartnerAuthorizationArgs', 'PartnerAuthorizationArgsDict']] partner_authorization: The details of authorized partners.
        :param pulumi.Input[Union[str, 'PartnerConfigurationProvisioningState']] provisioning_state: Provisioning state of the partner configuration.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PartnerConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Partner configuration information

        :param str resource_name: The name of the resource.
        :param PartnerConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PartnerConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 partner_authorization: Optional[pulumi.Input[Union['PartnerAuthorizationArgs', 'PartnerAuthorizationArgsDict']]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'PartnerConfigurationProvisioningState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PartnerConfigurationArgs.__new__(PartnerConfigurationArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["partner_authorization"] = partner_authorization
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventgrid:PartnerConfiguration"), pulumi.Alias(type_="azure-native:eventgrid/v20211015preview:PartnerConfiguration"), pulumi.Alias(type_="azure-native:eventgrid/v20220615:PartnerConfiguration"), pulumi.Alias(type_="azure-native:eventgrid/v20231215preview:PartnerConfiguration"), pulumi.Alias(type_="azure-native:eventgrid/v20240601preview:PartnerConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PartnerConfiguration, __self__).__init__(
            'azure-native:eventgrid/v20230601preview:PartnerConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PartnerConfiguration':
        """
        Get an existing PartnerConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PartnerConfigurationArgs.__new__(PartnerConfigurationArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partner_authorization"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return PartnerConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partnerAuthorization")
    def partner_authorization(self) -> pulumi.Output[Optional['outputs.PartnerAuthorizationResponse']]:
        """
        The details of authorized partners.
        """
        return pulumi.get(self, "partner_authorization")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Provisioning state of the partner configuration.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to partner configuration resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

