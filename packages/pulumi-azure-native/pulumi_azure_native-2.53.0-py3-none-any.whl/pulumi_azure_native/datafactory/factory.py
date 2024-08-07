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

__all__ = ['FactoryArgs', 'Factory']

@pulumi.input_type
class FactoryArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 encryption: Optional[pulumi.Input['EncryptionConfigurationArgs']] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 global_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input['GlobalParameterSpecificationArgs']]]] = None,
                 identity: Optional[pulumi.Input['FactoryIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 purview_configuration: Optional[pulumi.Input['PurviewConfigurationArgs']] = None,
                 repo_configuration: Optional[pulumi.Input[Union['FactoryGitHubConfigurationArgs', 'FactoryVSTSConfigurationArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Factory resource.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input['EncryptionConfigurationArgs'] encryption: Properties to enable Customer Managed Key for the factory.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input[Mapping[str, pulumi.Input['GlobalParameterSpecificationArgs']]] global_parameters: List of parameters for factory.
        :param pulumi.Input['FactoryIdentityArgs'] identity: Managed service identity of the factory.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: Whether or not public network access is allowed for the data factory.
        :param pulumi.Input['PurviewConfigurationArgs'] purview_configuration: Purview information of the factory.
        :param pulumi.Input[Union['FactoryGitHubConfigurationArgs', 'FactoryVSTSConfigurationArgs']] repo_configuration: Git repo information of the factory.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)
        if factory_name is not None:
            pulumi.set(__self__, "factory_name", factory_name)
        if global_parameters is not None:
            pulumi.set(__self__, "global_parameters", global_parameters)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if purview_configuration is not None:
            pulumi.set(__self__, "purview_configuration", purview_configuration)
        if repo_configuration is not None:
            pulumi.set(__self__, "repo_configuration", repo_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input['EncryptionConfigurationArgs']]:
        """
        Properties to enable Customer Managed Key for the factory.
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input['EncryptionConfigurationArgs']]):
        pulumi.set(self, "encryption", value)

    @property
    @pulumi.getter(name="factoryName")
    def factory_name(self) -> Optional[pulumi.Input[str]]:
        """
        The factory name.
        """
        return pulumi.get(self, "factory_name")

    @factory_name.setter
    def factory_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "factory_name", value)

    @property
    @pulumi.getter(name="globalParameters")
    def global_parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['GlobalParameterSpecificationArgs']]]]:
        """
        List of parameters for factory.
        """
        return pulumi.get(self, "global_parameters")

    @global_parameters.setter
    def global_parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['GlobalParameterSpecificationArgs']]]]):
        pulumi.set(self, "global_parameters", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['FactoryIdentityArgs']]:
        """
        Managed service identity of the factory.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['FactoryIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        Whether or not public network access is allowed for the data factory.
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter(name="purviewConfiguration")
    def purview_configuration(self) -> Optional[pulumi.Input['PurviewConfigurationArgs']]:
        """
        Purview information of the factory.
        """
        return pulumi.get(self, "purview_configuration")

    @purview_configuration.setter
    def purview_configuration(self, value: Optional[pulumi.Input['PurviewConfigurationArgs']]):
        pulumi.set(self, "purview_configuration", value)

    @property
    @pulumi.getter(name="repoConfiguration")
    def repo_configuration(self) -> Optional[pulumi.Input[Union['FactoryGitHubConfigurationArgs', 'FactoryVSTSConfigurationArgs']]]:
        """
        Git repo information of the factory.
        """
        return pulumi.get(self, "repo_configuration")

    @repo_configuration.setter
    def repo_configuration(self, value: Optional[pulumi.Input[Union['FactoryGitHubConfigurationArgs', 'FactoryVSTSConfigurationArgs']]]):
        pulumi.set(self, "repo_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Factory(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption: Optional[pulumi.Input[Union['EncryptionConfigurationArgs', 'EncryptionConfigurationArgsDict']]] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 global_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['GlobalParameterSpecificationArgs', 'GlobalParameterSpecificationArgsDict']]]]] = None,
                 identity: Optional[pulumi.Input[Union['FactoryIdentityArgs', 'FactoryIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 purview_configuration: Optional[pulumi.Input[Union['PurviewConfigurationArgs', 'PurviewConfigurationArgsDict']]] = None,
                 repo_configuration: Optional[pulumi.Input[Union[Union['FactoryGitHubConfigurationArgs', 'FactoryGitHubConfigurationArgsDict'], Union['FactoryVSTSConfigurationArgs', 'FactoryVSTSConfigurationArgsDict']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Factory resource type.
        Azure REST API version: 2018-06-01. Prior API version in Azure Native 1.x: 2018-06-01.

        Other available API versions: 2017-09-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['EncryptionConfigurationArgs', 'EncryptionConfigurationArgsDict']] encryption: Properties to enable Customer Managed Key for the factory.
        :param pulumi.Input[str] factory_name: The factory name.
        :param pulumi.Input[Mapping[str, pulumi.Input[Union['GlobalParameterSpecificationArgs', 'GlobalParameterSpecificationArgsDict']]]] global_parameters: List of parameters for factory.
        :param pulumi.Input[Union['FactoryIdentityArgs', 'FactoryIdentityArgsDict']] identity: Managed service identity of the factory.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: Whether or not public network access is allowed for the data factory.
        :param pulumi.Input[Union['PurviewConfigurationArgs', 'PurviewConfigurationArgsDict']] purview_configuration: Purview information of the factory.
        :param pulumi.Input[Union[Union['FactoryGitHubConfigurationArgs', 'FactoryGitHubConfigurationArgsDict'], Union['FactoryVSTSConfigurationArgs', 'FactoryVSTSConfigurationArgsDict']]] repo_configuration: Git repo information of the factory.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FactoryArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Factory resource type.
        Azure REST API version: 2018-06-01. Prior API version in Azure Native 1.x: 2018-06-01.

        Other available API versions: 2017-09-01-preview.

        :param str resource_name: The name of the resource.
        :param FactoryArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FactoryArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption: Optional[pulumi.Input[Union['EncryptionConfigurationArgs', 'EncryptionConfigurationArgsDict']]] = None,
                 factory_name: Optional[pulumi.Input[str]] = None,
                 global_parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[Union['GlobalParameterSpecificationArgs', 'GlobalParameterSpecificationArgsDict']]]]] = None,
                 identity: Optional[pulumi.Input[Union['FactoryIdentityArgs', 'FactoryIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 purview_configuration: Optional[pulumi.Input[Union['PurviewConfigurationArgs', 'PurviewConfigurationArgsDict']]] = None,
                 repo_configuration: Optional[pulumi.Input[Union[Union['FactoryGitHubConfigurationArgs', 'FactoryGitHubConfigurationArgsDict'], Union['FactoryVSTSConfigurationArgs', 'FactoryVSTSConfigurationArgsDict']]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FactoryArgs.__new__(FactoryArgs)

            __props__.__dict__["encryption"] = encryption
            __props__.__dict__["factory_name"] = factory_name
            __props__.__dict__["global_parameters"] = global_parameters
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["public_network_access"] = public_network_access
            __props__.__dict__["purview_configuration"] = purview_configuration
            __props__.__dict__["repo_configuration"] = repo_configuration
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["create_time"] = None
            __props__.__dict__["e_tag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:datafactory/v20170901preview:Factory"), pulumi.Alias(type_="azure-native:datafactory/v20180601:Factory")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Factory, __self__).__init__(
            'azure-native:datafactory:Factory',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Factory':
        """
        Get an existing Factory resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FactoryArgs.__new__(FactoryArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["e_tag"] = None
        __props__.__dict__["encryption"] = None
        __props__.__dict__["global_parameters"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["purview_configuration"] = None
        __props__.__dict__["repo_configuration"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return Factory(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Time the factory was created in ISO8601 format.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[str]:
        """
        Etag identifies change in the resource.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def encryption(self) -> pulumi.Output[Optional['outputs.EncryptionConfigurationResponse']]:
        """
        Properties to enable Customer Managed Key for the factory.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="globalParameters")
    def global_parameters(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.GlobalParameterSpecificationResponse']]]:
        """
        List of parameters for factory.
        """
        return pulumi.get(self, "global_parameters")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.FactoryIdentityResponse']]:
        """
        Managed service identity of the factory.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Factory provisioning state, example Succeeded.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        Whether or not public network access is allowed for the data factory.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="purviewConfiguration")
    def purview_configuration(self) -> pulumi.Output[Optional['outputs.PurviewConfigurationResponse']]:
        """
        Purview information of the factory.
        """
        return pulumi.get(self, "purview_configuration")

    @property
    @pulumi.getter(name="repoConfiguration")
    def repo_configuration(self) -> pulumi.Output[Optional[Any]]:
        """
        Git repo information of the factory.
        """
        return pulumi.get(self, "repo_configuration")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Version of the factory.
        """
        return pulumi.get(self, "version")

