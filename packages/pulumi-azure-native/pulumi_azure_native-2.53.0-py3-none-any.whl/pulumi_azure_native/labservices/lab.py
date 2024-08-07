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

__all__ = ['LabArgs', 'Lab']

@pulumi.input_type
class LabArgs:
    def __init__(__self__, *,
                 auto_shutdown_profile: pulumi.Input['AutoShutdownProfileArgs'],
                 connection_profile: pulumi.Input['ConnectionProfileArgs'],
                 resource_group_name: pulumi.Input[str],
                 security_profile: pulumi.Input['SecurityProfileArgs'],
                 virtual_machine_profile: pulumi.Input['VirtualMachineProfileArgs'],
                 description: Optional[pulumi.Input[str]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 lab_plan_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input['LabNetworkProfileArgs']] = None,
                 roster_profile: Optional[pulumi.Input['RosterProfileArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 title: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Lab resource.
        :param pulumi.Input['AutoShutdownProfileArgs'] auto_shutdown_profile: The resource auto shutdown configuration for the lab. This controls whether actions are taken on resources that are sitting idle.
        :param pulumi.Input['ConnectionProfileArgs'] connection_profile: The connection profile for the lab. This controls settings such as web access to lab resources or whether RDP or SSH ports are open.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['SecurityProfileArgs'] security_profile: The lab security profile.
        :param pulumi.Input['VirtualMachineProfileArgs'] virtual_machine_profile: The profile used for creating lab virtual machines.
        :param pulumi.Input[str] description: The description of the lab.
        :param pulumi.Input[str] lab_name: The name of the lab that uniquely identifies it within containing lab plan. Used in resource URIs.
        :param pulumi.Input[str] lab_plan_id: The ID of the lab plan. Used during resource creation to provide defaults and acts as a permission container when creating a lab via labs.azure.com. Setting a labPlanId on an existing lab provides organization..
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['LabNetworkProfileArgs'] network_profile: The network profile for the lab, typically applied via a lab plan. This profile cannot be modified once a lab has been created.
        :param pulumi.Input['RosterProfileArgs'] roster_profile: The lab user list management profile.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] title: The title of the lab.
        """
        pulumi.set(__self__, "auto_shutdown_profile", auto_shutdown_profile)
        pulumi.set(__self__, "connection_profile", connection_profile)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "security_profile", security_profile)
        pulumi.set(__self__, "virtual_machine_profile", virtual_machine_profile)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if lab_name is not None:
            pulumi.set(__self__, "lab_name", lab_name)
        if lab_plan_id is not None:
            pulumi.set(__self__, "lab_plan_id", lab_plan_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_profile is not None:
            pulumi.set(__self__, "network_profile", network_profile)
        if roster_profile is not None:
            pulumi.set(__self__, "roster_profile", roster_profile)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter(name="autoShutdownProfile")
    def auto_shutdown_profile(self) -> pulumi.Input['AutoShutdownProfileArgs']:
        """
        The resource auto shutdown configuration for the lab. This controls whether actions are taken on resources that are sitting idle.
        """
        return pulumi.get(self, "auto_shutdown_profile")

    @auto_shutdown_profile.setter
    def auto_shutdown_profile(self, value: pulumi.Input['AutoShutdownProfileArgs']):
        pulumi.set(self, "auto_shutdown_profile", value)

    @property
    @pulumi.getter(name="connectionProfile")
    def connection_profile(self) -> pulumi.Input['ConnectionProfileArgs']:
        """
        The connection profile for the lab. This controls settings such as web access to lab resources or whether RDP or SSH ports are open.
        """
        return pulumi.get(self, "connection_profile")

    @connection_profile.setter
    def connection_profile(self, value: pulumi.Input['ConnectionProfileArgs']):
        pulumi.set(self, "connection_profile", value)

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
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> pulumi.Input['SecurityProfileArgs']:
        """
        The lab security profile.
        """
        return pulumi.get(self, "security_profile")

    @security_profile.setter
    def security_profile(self, value: pulumi.Input['SecurityProfileArgs']):
        pulumi.set(self, "security_profile", value)

    @property
    @pulumi.getter(name="virtualMachineProfile")
    def virtual_machine_profile(self) -> pulumi.Input['VirtualMachineProfileArgs']:
        """
        The profile used for creating lab virtual machines.
        """
        return pulumi.get(self, "virtual_machine_profile")

    @virtual_machine_profile.setter
    def virtual_machine_profile(self, value: pulumi.Input['VirtualMachineProfileArgs']):
        pulumi.set(self, "virtual_machine_profile", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the lab.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="labName")
    def lab_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the lab that uniquely identifies it within containing lab plan. Used in resource URIs.
        """
        return pulumi.get(self, "lab_name")

    @lab_name.setter
    def lab_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lab_name", value)

    @property
    @pulumi.getter(name="labPlanId")
    def lab_plan_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the lab plan. Used during resource creation to provide defaults and acts as a permission container when creating a lab via labs.azure.com. Setting a labPlanId on an existing lab provides organization..
        """
        return pulumi.get(self, "lab_plan_id")

    @lab_plan_id.setter
    def lab_plan_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lab_plan_id", value)

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
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> Optional[pulumi.Input['LabNetworkProfileArgs']]:
        """
        The network profile for the lab, typically applied via a lab plan. This profile cannot be modified once a lab has been created.
        """
        return pulumi.get(self, "network_profile")

    @network_profile.setter
    def network_profile(self, value: Optional[pulumi.Input['LabNetworkProfileArgs']]):
        pulumi.set(self, "network_profile", value)

    @property
    @pulumi.getter(name="rosterProfile")
    def roster_profile(self) -> Optional[pulumi.Input['RosterProfileArgs']]:
        """
        The lab user list management profile.
        """
        return pulumi.get(self, "roster_profile")

    @roster_profile.setter
    def roster_profile(self, value: Optional[pulumi.Input['RosterProfileArgs']]):
        pulumi.set(self, "roster_profile", value)

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
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the lab.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)


class Lab(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_shutdown_profile: Optional[pulumi.Input[Union['AutoShutdownProfileArgs', 'AutoShutdownProfileArgsDict']]] = None,
                 connection_profile: Optional[pulumi.Input[Union['ConnectionProfileArgs', 'ConnectionProfileArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 lab_plan_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[Union['LabNetworkProfileArgs', 'LabNetworkProfileArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 roster_profile: Optional[pulumi.Input[Union['RosterProfileArgs', 'RosterProfileArgsDict']]] = None,
                 security_profile: Optional[pulumi.Input[Union['SecurityProfileArgs', 'SecurityProfileArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 virtual_machine_profile: Optional[pulumi.Input[Union['VirtualMachineProfileArgs', 'VirtualMachineProfileArgsDict']]] = None,
                 __props__=None):
        """
        The lab resource.
        Azure REST API version: 2022-08-01. Prior API version in Azure Native 1.x: 2018-10-15.

        Other available API versions: 2018-10-15, 2023-06-07.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['AutoShutdownProfileArgs', 'AutoShutdownProfileArgsDict']] auto_shutdown_profile: The resource auto shutdown configuration for the lab. This controls whether actions are taken on resources that are sitting idle.
        :param pulumi.Input[Union['ConnectionProfileArgs', 'ConnectionProfileArgsDict']] connection_profile: The connection profile for the lab. This controls settings such as web access to lab resources or whether RDP or SSH ports are open.
        :param pulumi.Input[str] description: The description of the lab.
        :param pulumi.Input[str] lab_name: The name of the lab that uniquely identifies it within containing lab plan. Used in resource URIs.
        :param pulumi.Input[str] lab_plan_id: The ID of the lab plan. Used during resource creation to provide defaults and acts as a permission container when creating a lab via labs.azure.com. Setting a labPlanId on an existing lab provides organization..
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union['LabNetworkProfileArgs', 'LabNetworkProfileArgsDict']] network_profile: The network profile for the lab, typically applied via a lab plan. This profile cannot be modified once a lab has been created.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union['RosterProfileArgs', 'RosterProfileArgsDict']] roster_profile: The lab user list management profile.
        :param pulumi.Input[Union['SecurityProfileArgs', 'SecurityProfileArgsDict']] security_profile: The lab security profile.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] title: The title of the lab.
        :param pulumi.Input[Union['VirtualMachineProfileArgs', 'VirtualMachineProfileArgsDict']] virtual_machine_profile: The profile used for creating lab virtual machines.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LabArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The lab resource.
        Azure REST API version: 2022-08-01. Prior API version in Azure Native 1.x: 2018-10-15.

        Other available API versions: 2018-10-15, 2023-06-07.

        :param str resource_name: The name of the resource.
        :param LabArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LabArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_shutdown_profile: Optional[pulumi.Input[Union['AutoShutdownProfileArgs', 'AutoShutdownProfileArgsDict']]] = None,
                 connection_profile: Optional[pulumi.Input[Union['ConnectionProfileArgs', 'ConnectionProfileArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 lab_plan_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile: Optional[pulumi.Input[Union['LabNetworkProfileArgs', 'LabNetworkProfileArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 roster_profile: Optional[pulumi.Input[Union['RosterProfileArgs', 'RosterProfileArgsDict']]] = None,
                 security_profile: Optional[pulumi.Input[Union['SecurityProfileArgs', 'SecurityProfileArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 virtual_machine_profile: Optional[pulumi.Input[Union['VirtualMachineProfileArgs', 'VirtualMachineProfileArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LabArgs.__new__(LabArgs)

            if auto_shutdown_profile is None and not opts.urn:
                raise TypeError("Missing required property 'auto_shutdown_profile'")
            __props__.__dict__["auto_shutdown_profile"] = auto_shutdown_profile
            if connection_profile is None and not opts.urn:
                raise TypeError("Missing required property 'connection_profile'")
            __props__.__dict__["connection_profile"] = connection_profile
            __props__.__dict__["description"] = description
            __props__.__dict__["lab_name"] = lab_name
            __props__.__dict__["lab_plan_id"] = lab_plan_id
            __props__.__dict__["location"] = location
            __props__.__dict__["network_profile"] = network_profile
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["roster_profile"] = roster_profile
            if security_profile is None and not opts.urn:
                raise TypeError("Missing required property 'security_profile'")
            __props__.__dict__["security_profile"] = security_profile
            __props__.__dict__["tags"] = tags
            __props__.__dict__["title"] = title
            if virtual_machine_profile is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_machine_profile'")
            __props__.__dict__["virtual_machine_profile"] = virtual_machine_profile
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:labservices/v20211001preview:Lab"), pulumi.Alias(type_="azure-native:labservices/v20211115preview:Lab"), pulumi.Alias(type_="azure-native:labservices/v20220801:Lab"), pulumi.Alias(type_="azure-native:labservices/v20230607:Lab")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Lab, __self__).__init__(
            'azure-native:labservices:Lab',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Lab':
        """
        Get an existing Lab resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LabArgs.__new__(LabArgs)

        __props__.__dict__["auto_shutdown_profile"] = None
        __props__.__dict__["connection_profile"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["lab_plan_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_profile"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["roster_profile"] = None
        __props__.__dict__["security_profile"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_machine_profile"] = None
        return Lab(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoShutdownProfile")
    def auto_shutdown_profile(self) -> pulumi.Output['outputs.AutoShutdownProfileResponse']:
        """
        The resource auto shutdown configuration for the lab. This controls whether actions are taken on resources that are sitting idle.
        """
        return pulumi.get(self, "auto_shutdown_profile")

    @property
    @pulumi.getter(name="connectionProfile")
    def connection_profile(self) -> pulumi.Output['outputs.ConnectionProfileResponse']:
        """
        The connection profile for the lab. This controls settings such as web access to lab resources or whether RDP or SSH ports are open.
        """
        return pulumi.get(self, "connection_profile")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the lab.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="labPlanId")
    def lab_plan_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the lab plan. Used during resource creation to provide defaults and acts as a permission container when creating a lab via labs.azure.com. Setting a labPlanId on an existing lab provides organization..
        """
        return pulumi.get(self, "lab_plan_id")

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
    @pulumi.getter(name="networkProfile")
    def network_profile(self) -> pulumi.Output[Optional['outputs.LabNetworkProfileResponse']]:
        """
        The network profile for the lab, typically applied via a lab plan. This profile cannot be modified once a lab has been created.
        """
        return pulumi.get(self, "network_profile")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Current provisioning state of the lab.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="rosterProfile")
    def roster_profile(self) -> pulumi.Output[Optional['outputs.RosterProfileResponse']]:
        """
        The lab user list management profile.
        """
        return pulumi.get(self, "roster_profile")

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> pulumi.Output['outputs.SecurityProfileResponse']:
        """
        The lab security profile.
        """
        return pulumi.get(self, "security_profile")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The lab state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the lab.
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
    def title(self) -> pulumi.Output[Optional[str]]:
        """
        The title of the lab.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualMachineProfile")
    def virtual_machine_profile(self) -> pulumi.Output['outputs.VirtualMachineProfileResponse']:
        """
        The profile used for creating lab virtual machines.
        """
        return pulumi.get(self, "virtual_machine_profile")

