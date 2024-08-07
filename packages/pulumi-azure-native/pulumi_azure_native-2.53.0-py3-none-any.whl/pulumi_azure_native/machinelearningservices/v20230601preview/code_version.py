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

__all__ = ['CodeVersionInitArgs', 'CodeVersion']

@pulumi.input_type
class CodeVersionInitArgs:
    def __init__(__self__, *,
                 code_version_properties: pulumi.Input['CodeVersionArgs'],
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CodeVersion resource.
        :param pulumi.Input['CodeVersionArgs'] code_version_properties: [Required] Additional attributes of the entity.
        :param pulumi.Input[str] name: Container name. This is case-sensitive.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        :param pulumi.Input[str] version: Version identifier. This is case-sensitive.
        """
        pulumi.set(__self__, "code_version_properties", code_version_properties)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="codeVersionProperties")
    def code_version_properties(self) -> pulumi.Input['CodeVersionArgs']:
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "code_version_properties")

    @code_version_properties.setter
    def code_version_properties(self, value: pulumi.Input['CodeVersionArgs']):
        pulumi.set(self, "code_version_properties", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Container name. This is case-sensitive.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

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
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        Name of Azure Machine Learning workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Version identifier. This is case-sensitive.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class CodeVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 code_version_properties: Optional[pulumi.Input[Union['CodeVersionArgs', 'CodeVersionArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Azure Resource Manager resource envelope.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['CodeVersionArgs', 'CodeVersionArgsDict']] code_version_properties: [Required] Additional attributes of the entity.
        :param pulumi.Input[str] name: Container name. This is case-sensitive.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] version: Version identifier. This is case-sensitive.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CodeVersionInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure Resource Manager resource envelope.

        :param str resource_name: The name of the resource.
        :param CodeVersionInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CodeVersionInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 code_version_properties: Optional[pulumi.Input[Union['CodeVersionArgs', 'CodeVersionArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CodeVersionInitArgs.__new__(CodeVersionInitArgs)

            if code_version_properties is None and not opts.urn:
                raise TypeError("Missing required property 'code_version_properties'")
            __props__.__dict__["code_version_properties"] = code_version_properties
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["version"] = version
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:machinelearningservices:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20210301preview:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20220201preview:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20220501:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20220601preview:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20221001:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20221001preview:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20221201preview:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230201preview:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230401:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230401preview:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230801preview:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20231001:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240101preview:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240401:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240401preview:CodeVersion"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240701preview:CodeVersion")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CodeVersion, __self__).__init__(
            'azure-native:machinelearningservices/v20230601preview:CodeVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CodeVersion':
        """
        Get an existing CodeVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CodeVersionInitArgs.__new__(CodeVersionInitArgs)

        __props__.__dict__["code_version_properties"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return CodeVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="codeVersionProperties")
    def code_version_properties(self) -> pulumi.Output['outputs.CodeVersionResponse']:
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "code_version_properties")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

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

