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

__all__ = ['SyncSetArgs', 'SyncSet']

@pulumi.input_type
class SyncSetArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 child_resource_name: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SyncSet resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name: The name of the OpenShift cluster resource.
        :param pulumi.Input[str] child_resource_name: The name of the SyncSet resource.
        :param pulumi.Input[str] resources: Resources represents the SyncSets configuration.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if child_resource_name is not None:
            pulumi.set(__self__, "child_resource_name", child_resource_name)
        if resources is not None:
            pulumi.set(__self__, "resources", resources)

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
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the OpenShift cluster resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="childResourceName")
    def child_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the SyncSet resource.
        """
        return pulumi.get(self, "child_resource_name")

    @child_resource_name.setter
    def child_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "child_resource_name", value)

    @property
    @pulumi.getter
    def resources(self) -> Optional[pulumi.Input[str]]:
        """
        Resources represents the SyncSets configuration.
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resources", value)


class SyncSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 child_resource_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        SyncSet represents a SyncSet for an Azure Red Hat OpenShift Cluster.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] child_resource_name: The name of the SyncSet resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the OpenShift cluster resource.
        :param pulumi.Input[str] resources: Resources represents the SyncSets configuration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SyncSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        SyncSet represents a SyncSet for an Azure Red Hat OpenShift Cluster.

        :param str resource_name: The name of the resource.
        :param SyncSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SyncSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 child_resource_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 resources: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SyncSetArgs.__new__(SyncSetArgs)

            __props__.__dict__["child_resource_name"] = child_resource_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["resources"] = resources
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:redhatopenshift:SyncSet"), pulumi.Alias(type_="azure-native:redhatopenshift/v20220904:SyncSet"), pulumi.Alias(type_="azure-native:redhatopenshift/v20230701preview:SyncSet"), pulumi.Alias(type_="azure-native:redhatopenshift/v20230904:SyncSet"), pulumi.Alias(type_="azure-native:redhatopenshift/v20231122:SyncSet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SyncSet, __self__).__init__(
            'azure-native:redhatopenshift/v20230401:SyncSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SyncSet':
        """
        Get an existing SyncSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SyncSetArgs.__new__(SyncSetArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["resources"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return SyncSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Output[Optional[str]]:
        """
        Resources represents the SyncSets configuration.
        """
        return pulumi.get(self, "resources")

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

