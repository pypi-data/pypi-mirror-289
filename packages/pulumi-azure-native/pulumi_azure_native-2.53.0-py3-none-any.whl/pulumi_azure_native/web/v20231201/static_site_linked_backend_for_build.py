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

__all__ = ['StaticSiteLinkedBackendForBuildArgs', 'StaticSiteLinkedBackendForBuild']

@pulumi.input_type
class StaticSiteLinkedBackendForBuildArgs:
    def __init__(__self__, *,
                 environment_name: pulumi.Input[str],
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 backend_resource_id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 linked_backend_name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StaticSiteLinkedBackendForBuild resource.
        :param pulumi.Input[str] environment_name: The stage site identifier
        :param pulumi.Input[str] name: Name of the static site
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        :param pulumi.Input[str] backend_resource_id: The resource id of the backend linked to the static site
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] linked_backend_name: Name of the backend to link to the static site
        :param pulumi.Input[str] region: The region of the backend linked to the static site
        """
        pulumi.set(__self__, "environment_name", environment_name)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if backend_resource_id is not None:
            pulumi.set(__self__, "backend_resource_id", backend_resource_id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if linked_backend_name is not None:
            pulumi.set(__self__, "linked_backend_name", linked_backend_name)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[str]:
        """
        The stage site identifier
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the static site
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group to which the resource belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="backendResourceId")
    def backend_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id of the backend linked to the static site
        """
        return pulumi.get(self, "backend_resource_id")

    @backend_resource_id.setter
    def backend_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backend_resource_id", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="linkedBackendName")
    def linked_backend_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the backend to link to the static site
        """
        return pulumi.get(self, "linked_backend_name")

    @linked_backend_name.setter
    def linked_backend_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "linked_backend_name", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region of the backend linked to the static site
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


class StaticSiteLinkedBackendForBuild(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_resource_id: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 linked_backend_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Static Site Linked Backend ARM resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backend_resource_id: The resource id of the backend linked to the static site
        :param pulumi.Input[str] environment_name: The stage site identifier
        :param pulumi.Input[str] kind: Kind of resource.
        :param pulumi.Input[str] linked_backend_name: Name of the backend to link to the static site
        :param pulumi.Input[str] name: Name of the static site
        :param pulumi.Input[str] region: The region of the backend linked to the static site
        :param pulumi.Input[str] resource_group_name: Name of the resource group to which the resource belongs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StaticSiteLinkedBackendForBuildArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Static Site Linked Backend ARM resource.

        :param str resource_name: The name of the resource.
        :param StaticSiteLinkedBackendForBuildArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StaticSiteLinkedBackendForBuildArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backend_resource_id: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 linked_backend_name: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StaticSiteLinkedBackendForBuildArgs.__new__(StaticSiteLinkedBackendForBuildArgs)

            __props__.__dict__["backend_resource_id"] = backend_resource_id
            if environment_name is None and not opts.urn:
                raise TypeError("Missing required property 'environment_name'")
            __props__.__dict__["environment_name"] = environment_name
            __props__.__dict__["kind"] = kind
            __props__.__dict__["linked_backend_name"] = linked_backend_name
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["region"] = region
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["created_on"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:StaticSiteLinkedBackendForBuild"), pulumi.Alias(type_="azure-native:web/v20220301:StaticSiteLinkedBackendForBuild"), pulumi.Alias(type_="azure-native:web/v20220901:StaticSiteLinkedBackendForBuild"), pulumi.Alias(type_="azure-native:web/v20230101:StaticSiteLinkedBackendForBuild")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StaticSiteLinkedBackendForBuild, __self__).__init__(
            'azure-native:web/v20231201:StaticSiteLinkedBackendForBuild',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StaticSiteLinkedBackendForBuild':
        """
        Get an existing StaticSiteLinkedBackendForBuild resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StaticSiteLinkedBackendForBuildArgs.__new__(StaticSiteLinkedBackendForBuildArgs)

        __props__.__dict__["backend_resource_id"] = None
        __props__.__dict__["created_on"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["type"] = None
        return StaticSiteLinkedBackendForBuild(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backendResourceId")
    def backend_resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        The resource id of the backend linked to the static site
        """
        return pulumi.get(self, "backend_resource_id")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> pulumi.Output[str]:
        """
        The date and time on which the backend was linked to the static site.
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the linking process.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        The region of the backend linked to the static site
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

