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
from ._enums import *

__all__ = ['SandboxCustomImageArgs', 'SandboxCustomImage']

@pulumi.input_type
class SandboxCustomImageArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 language: pulumi.Input[Union[str, 'Language']],
                 language_version: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 requirements_file_content: Optional[pulumi.Input[str]] = None,
                 sandbox_custom_image_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SandboxCustomImage resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[Union[str, 'Language']] language: The language name, for example Python.
        :param pulumi.Input[str] language_version: The version of the language.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] requirements_file_content: The requirements file content.
        :param pulumi.Input[str] sandbox_custom_image_name: The name of the sandbox custom image.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "language", language)
        pulumi.set(__self__, "language_version", language_version)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if requirements_file_content is not None:
            pulumi.set(__self__, "requirements_file_content", requirements_file_content)
        if sandbox_custom_image_name is not None:
            pulumi.set(__self__, "sandbox_custom_image_name", sandbox_custom_image_name)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the Kusto cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter
    def language(self) -> pulumi.Input[Union[str, 'Language']]:
        """
        The language name, for example Python.
        """
        return pulumi.get(self, "language")

    @language.setter
    def language(self, value: pulumi.Input[Union[str, 'Language']]):
        pulumi.set(self, "language", value)

    @property
    @pulumi.getter(name="languageVersion")
    def language_version(self) -> pulumi.Input[str]:
        """
        The version of the language.
        """
        return pulumi.get(self, "language_version")

    @language_version.setter
    def language_version(self, value: pulumi.Input[str]):
        pulumi.set(self, "language_version", value)

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
    @pulumi.getter(name="requirementsFileContent")
    def requirements_file_content(self) -> Optional[pulumi.Input[str]]:
        """
        The requirements file content.
        """
        return pulumi.get(self, "requirements_file_content")

    @requirements_file_content.setter
    def requirements_file_content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "requirements_file_content", value)

    @property
    @pulumi.getter(name="sandboxCustomImageName")
    def sandbox_custom_image_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the sandbox custom image.
        """
        return pulumi.get(self, "sandbox_custom_image_name")

    @sandbox_custom_image_name.setter
    def sandbox_custom_image_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sandbox_custom_image_name", value)


class SandboxCustomImage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 language: Optional[pulumi.Input[Union[str, 'Language']]] = None,
                 language_version: Optional[pulumi.Input[str]] = None,
                 requirements_file_content: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sandbox_custom_image_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Class representing a Kusto sandbox custom image.
        Azure REST API version: 2023-08-15.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[Union[str, 'Language']] language: The language name, for example Python.
        :param pulumi.Input[str] language_version: The version of the language.
        :param pulumi.Input[str] requirements_file_content: The requirements file content.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sandbox_custom_image_name: The name of the sandbox custom image.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SandboxCustomImageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing a Kusto sandbox custom image.
        Azure REST API version: 2023-08-15.

        :param str resource_name: The name of the resource.
        :param SandboxCustomImageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SandboxCustomImageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 language: Optional[pulumi.Input[Union[str, 'Language']]] = None,
                 language_version: Optional[pulumi.Input[str]] = None,
                 requirements_file_content: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sandbox_custom_image_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SandboxCustomImageArgs.__new__(SandboxCustomImageArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            if language is None and not opts.urn:
                raise TypeError("Missing required property 'language'")
            __props__.__dict__["language"] = language
            if language_version is None and not opts.urn:
                raise TypeError("Missing required property 'language_version'")
            __props__.__dict__["language_version"] = language_version
            __props__.__dict__["requirements_file_content"] = requirements_file_content
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sandbox_custom_image_name"] = sandbox_custom_image_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:kusto/v20230815:SandboxCustomImage")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SandboxCustomImage, __self__).__init__(
            'azure-native:kusto:SandboxCustomImage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SandboxCustomImage':
        """
        Get an existing SandboxCustomImage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SandboxCustomImageArgs.__new__(SandboxCustomImageArgs)

        __props__.__dict__["language"] = None
        __props__.__dict__["language_version"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["requirements_file_content"] = None
        __props__.__dict__["type"] = None
        return SandboxCustomImage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def language(self) -> pulumi.Output[str]:
        """
        The language name, for example Python.
        """
        return pulumi.get(self, "language")

    @property
    @pulumi.getter(name="languageVersion")
    def language_version(self) -> pulumi.Output[str]:
        """
        The version of the language.
        """
        return pulumi.get(self, "language_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="requirementsFileContent")
    def requirements_file_content(self) -> pulumi.Output[Optional[str]]:
        """
        The requirements file content.
        """
        return pulumi.get(self, "requirements_file_content")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

