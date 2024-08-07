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

__all__ = ['ReplicationvCenterArgs', 'ReplicationvCenter']

@pulumi.input_type
class ReplicationvCenterArgs:
    def __init__(__self__, *,
                 fabric_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 properties: Optional[pulumi.Input['AddVCenterRequestPropertiesArgs']] = None,
                 v_center_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ReplicationvCenter resource.
        :param pulumi.Input[str] fabric_name: Fabric name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the recovery services vault is present.
        :param pulumi.Input[str] resource_name: The name of the recovery services vault.
        :param pulumi.Input['AddVCenterRequestPropertiesArgs'] properties: The properties of an add vCenter request.
        :param pulumi.Input[str] v_center_name: vCenter name.
        """
        pulumi.set(__self__, "fabric_name", fabric_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if v_center_name is not None:
            pulumi.set(__self__, "v_center_name", v_center_name)

    @property
    @pulumi.getter(name="fabricName")
    def fabric_name(self) -> pulumi.Input[str]:
        """
        Fabric name.
        """
        return pulumi.get(self, "fabric_name")

    @fabric_name.setter
    def fabric_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "fabric_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group where the recovery services vault is present.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the recovery services vault.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['AddVCenterRequestPropertiesArgs']]:
        """
        The properties of an add vCenter request.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['AddVCenterRequestPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="vCenterName")
    def v_center_name(self) -> Optional[pulumi.Input[str]]:
        """
        vCenter name.
        """
        return pulumi.get(self, "v_center_name")

    @v_center_name.setter
    def v_center_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "v_center_name", value)


class ReplicationvCenter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fabric_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['AddVCenterRequestPropertiesArgs', 'AddVCenterRequestPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 v_center_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        vCenter definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fabric_name: Fabric name.
        :param pulumi.Input[Union['AddVCenterRequestPropertiesArgs', 'AddVCenterRequestPropertiesArgsDict']] properties: The properties of an add vCenter request.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the recovery services vault is present.
        :param pulumi.Input[str] resource_name_: The name of the recovery services vault.
        :param pulumi.Input[str] v_center_name: vCenter name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReplicationvCenterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        vCenter definition.

        :param str resource_name: The name of the resource.
        :param ReplicationvCenterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReplicationvCenterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fabric_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['AddVCenterRequestPropertiesArgs', 'AddVCenterRequestPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 v_center_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReplicationvCenterArgs.__new__(ReplicationvCenterArgs)

            if fabric_name is None and not opts.urn:
                raise TypeError("Missing required property 'fabric_name'")
            __props__.__dict__["fabric_name"] = fabric_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["v_center_name"] = v_center_name
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:recoveryservices:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20160810:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20180110:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20180710:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20210210:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20210401:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20210601:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20210701:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20210801:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20211001:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20211101:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20211201:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20220101:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20220201:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20220301:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20220401:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20220501:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20220801:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20220910:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20221001:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20230101:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20230201:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20230401:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20230601:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20230801:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20240101:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20240201:ReplicationvCenter"), pulumi.Alias(type_="azure-native:recoveryservices/v20240401:ReplicationvCenter")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ReplicationvCenter, __self__).__init__(
            'azure-native:recoveryservices/v20210301:ReplicationvCenter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReplicationvCenter':
        """
        Get an existing ReplicationvCenter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReplicationvCenterArgs.__new__(ReplicationvCenterArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return ReplicationvCenter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Location
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
    def properties(self) -> pulumi.Output['outputs.VCenterPropertiesResponse']:
        """
        VCenter related data.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource Type
        """
        return pulumi.get(self, "type")

