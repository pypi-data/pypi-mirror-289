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

__all__ = ['NspProfileArgs', 'NspProfile']

@pulumi.input_type
class NspProfileArgs:
    def __init__(__self__, *,
                 network_security_perimeter_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NspProfile resource.
        :param pulumi.Input[str] network_security_perimeter_name: The name of the network security perimeter.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] name: The name of the profile resource that is unique within a perimeter. This name can be used to access the resource.
        :param pulumi.Input[str] profile_name: The name of the NSP profile.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "network_security_perimeter_name", network_security_perimeter_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if profile_name is not None:
            pulumi.set(__self__, "profile_name", profile_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="networkSecurityPerimeterName")
    def network_security_perimeter_name(self) -> pulumi.Input[str]:
        """
        The name of the network security perimeter.
        """
        return pulumi.get(self, "network_security_perimeter_name")

    @network_security_perimeter_name.setter
    def network_security_perimeter_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_security_perimeter_name", value)

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
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the profile resource that is unique within a perimeter. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the NSP profile.
        """
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile_name", value)

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


class NspProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_security_perimeter_name: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The network security perimeter profile resource
        Azure REST API version: 2021-02-01-preview. Prior API version in Azure Native 1.x: 2021-02-01-preview.

        Other available API versions: 2023-07-01-preview, 2023-08-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] name: The name of the profile resource that is unique within a perimeter. This name can be used to access the resource.
        :param pulumi.Input[str] network_security_perimeter_name: The name of the network security perimeter.
        :param pulumi.Input[str] profile_name: The name of the NSP profile.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NspProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The network security perimeter profile resource
        Azure REST API version: 2021-02-01-preview. Prior API version in Azure Native 1.x: 2021-02-01-preview.

        Other available API versions: 2023-07-01-preview, 2023-08-01-preview.

        :param str resource_name: The name of the resource.
        :param NspProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NspProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network_security_perimeter_name: Optional[pulumi.Input[str]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NspProfileArgs.__new__(NspProfileArgs)

            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            if network_security_perimeter_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_security_perimeter_name'")
            __props__.__dict__["network_security_perimeter_name"] = network_security_perimeter_name
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["access_rules_version"] = None
            __props__.__dict__["diagnostic_settings_version"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network/v20210201preview:NspProfile"), pulumi.Alias(type_="azure-native:network/v20230701preview:NspProfile"), pulumi.Alias(type_="azure-native:network/v20230801preview:NspProfile")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NspProfile, __self__).__init__(
            'azure-native:network:NspProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NspProfile':
        """
        Get an existing NspProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NspProfileArgs.__new__(NspProfileArgs)

        __props__.__dict__["access_rules_version"] = None
        __props__.__dict__["diagnostic_settings_version"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return NspProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessRulesVersion")
    def access_rules_version(self) -> pulumi.Output[str]:
        """
        Version number that increases with every update to access rules within the profile.
        """
        return pulumi.get(self, "access_rules_version")

    @property
    @pulumi.getter(name="diagnosticSettingsVersion")
    def diagnostic_settings_version(self) -> pulumi.Output[str]:
        """
        Version number that increases with every update to diagnostic settings within the profile.
        """
        return pulumi.get(self, "diagnostic_settings_version")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

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
        Resource type.
        """
        return pulumi.get(self, "type")

