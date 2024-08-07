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
from ._inputs import *

__all__ = ['HyperVCollectorArgs', 'HyperVCollector']

@pulumi.input_type
class HyperVCollectorArgs:
    def __init__(__self__, *,
                 project_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 e_tag: Optional[pulumi.Input[str]] = None,
                 hyper_v_collector_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['CollectorPropertiesArgs']] = None):
        """
        The set of arguments for constructing a HyperVCollector resource.
        :param pulumi.Input[str] project_name: Name of the Azure Migrate project.
        :param pulumi.Input[str] resource_group_name: Name of the Azure Resource Group that project is part of.
        :param pulumi.Input[str] hyper_v_collector_name: Unique name of a Hyper-V collector within a project.
        """
        pulumi.set(__self__, "project_name", project_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)
        if hyper_v_collector_name is not None:
            pulumi.set(__self__, "hyper_v_collector_name", hyper_v_collector_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[str]:
        """
        Name of the Azure Migrate project.
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Azure Resource Group that project is part of.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_tag", value)

    @property
    @pulumi.getter(name="hyperVCollectorName")
    def hyper_v_collector_name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique name of a Hyper-V collector within a project.
        """
        return pulumi.get(self, "hyper_v_collector_name")

    @hyper_v_collector_name.setter
    def hyper_v_collector_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hyper_v_collector_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['CollectorPropertiesArgs']]:
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['CollectorPropertiesArgs']]):
        pulumi.set(self, "properties", value)


class HyperVCollector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 hyper_v_collector_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['CollectorPropertiesArgs', 'CollectorPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Azure REST API version: 2019-10-01. Prior API version in Azure Native 1.x: 2019-10-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hyper_v_collector_name: Unique name of a Hyper-V collector within a project.
        :param pulumi.Input[str] project_name: Name of the Azure Migrate project.
        :param pulumi.Input[str] resource_group_name: Name of the Azure Resource Group that project is part of.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HyperVCollectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure REST API version: 2019-10-01. Prior API version in Azure Native 1.x: 2019-10-01.

        :param str resource_name: The name of the resource.
        :param HyperVCollectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HyperVCollectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 hyper_v_collector_name: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['CollectorPropertiesArgs', 'CollectorPropertiesArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HyperVCollectorArgs.__new__(HyperVCollectorArgs)

            __props__.__dict__["e_tag"] = e_tag
            __props__.__dict__["hyper_v_collector_name"] = hyper_v_collector_name
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__.__dict__["project_name"] = project_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:migrate/v20191001:HyperVCollector"), pulumi.Alias(type_="azure-native:migrate/v20230315:HyperVCollector"), pulumi.Alias(type_="azure-native:migrate/v20230401preview:HyperVCollector")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(HyperVCollector, __self__).__init__(
            'azure-native:migrate:HyperVCollector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'HyperVCollector':
        """
        Get an existing HyperVCollector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HyperVCollectorArgs.__new__(HyperVCollectorArgs)

        __props__.__dict__["e_tag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return HyperVCollector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.CollectorPropertiesResponse']:
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "type")

