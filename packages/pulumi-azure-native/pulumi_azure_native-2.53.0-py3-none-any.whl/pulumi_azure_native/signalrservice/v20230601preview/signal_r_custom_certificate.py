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

__all__ = ['SignalRCustomCertificateArgs', 'SignalRCustomCertificate']

@pulumi.input_type
class SignalRCustomCertificateArgs:
    def __init__(__self__, *,
                 key_vault_base_uri: pulumi.Input[str],
                 key_vault_secret_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 key_vault_secret_version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SignalRCustomCertificate resource.
        :param pulumi.Input[str] key_vault_base_uri: Base uri of the KeyVault that stores certificate.
        :param pulumi.Input[str] key_vault_secret_name: Certificate secret name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name: The name of the resource.
        :param pulumi.Input[str] certificate_name: Custom certificate name
        :param pulumi.Input[str] key_vault_secret_version: Certificate secret version.
        """
        pulumi.set(__self__, "key_vault_base_uri", key_vault_base_uri)
        pulumi.set(__self__, "key_vault_secret_name", key_vault_secret_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if certificate_name is not None:
            pulumi.set(__self__, "certificate_name", certificate_name)
        if key_vault_secret_version is not None:
            pulumi.set(__self__, "key_vault_secret_version", key_vault_secret_version)

    @property
    @pulumi.getter(name="keyVaultBaseUri")
    def key_vault_base_uri(self) -> pulumi.Input[str]:
        """
        Base uri of the KeyVault that stores certificate.
        """
        return pulumi.get(self, "key_vault_base_uri")

    @key_vault_base_uri.setter
    def key_vault_base_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_vault_base_uri", value)

    @property
    @pulumi.getter(name="keyVaultSecretName")
    def key_vault_secret_name(self) -> pulumi.Input[str]:
        """
        Certificate secret name.
        """
        return pulumi.get(self, "key_vault_secret_name")

    @key_vault_secret_name.setter
    def key_vault_secret_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_vault_secret_name", value)

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
        The name of the resource.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="certificateName")
    def certificate_name(self) -> Optional[pulumi.Input[str]]:
        """
        Custom certificate name
        """
        return pulumi.get(self, "certificate_name")

    @certificate_name.setter
    def certificate_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_name", value)

    @property
    @pulumi.getter(name="keyVaultSecretVersion")
    def key_vault_secret_version(self) -> Optional[pulumi.Input[str]]:
        """
        Certificate secret version.
        """
        return pulumi.get(self, "key_vault_secret_version")

    @key_vault_secret_version.setter
    def key_vault_secret_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_vault_secret_version", value)


class SignalRCustomCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 key_vault_base_uri: Optional[pulumi.Input[str]] = None,
                 key_vault_secret_name: Optional[pulumi.Input[str]] = None,
                 key_vault_secret_version: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A custom certificate.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_name: Custom certificate name
        :param pulumi.Input[str] key_vault_base_uri: Base uri of the KeyVault that stores certificate.
        :param pulumi.Input[str] key_vault_secret_name: Certificate secret name.
        :param pulumi.Input[str] key_vault_secret_version: Certificate secret version.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_name_: The name of the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SignalRCustomCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A custom certificate.

        :param str resource_name: The name of the resource.
        :param SignalRCustomCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SignalRCustomCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_name: Optional[pulumi.Input[str]] = None,
                 key_vault_base_uri: Optional[pulumi.Input[str]] = None,
                 key_vault_secret_name: Optional[pulumi.Input[str]] = None,
                 key_vault_secret_version: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SignalRCustomCertificateArgs.__new__(SignalRCustomCertificateArgs)

            __props__.__dict__["certificate_name"] = certificate_name
            if key_vault_base_uri is None and not opts.urn:
                raise TypeError("Missing required property 'key_vault_base_uri'")
            __props__.__dict__["key_vault_base_uri"] = key_vault_base_uri
            if key_vault_secret_name is None and not opts.urn:
                raise TypeError("Missing required property 'key_vault_secret_name'")
            __props__.__dict__["key_vault_secret_name"] = key_vault_secret_name
            __props__.__dict__["key_vault_secret_version"] = key_vault_secret_version
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:signalrservice:SignalRCustomCertificate"), pulumi.Alias(type_="azure-native:signalrservice/v20220201:SignalRCustomCertificate"), pulumi.Alias(type_="azure-native:signalrservice/v20220801preview:SignalRCustomCertificate"), pulumi.Alias(type_="azure-native:signalrservice/v20230201:SignalRCustomCertificate"), pulumi.Alias(type_="azure-native:signalrservice/v20230301preview:SignalRCustomCertificate"), pulumi.Alias(type_="azure-native:signalrservice/v20230801preview:SignalRCustomCertificate"), pulumi.Alias(type_="azure-native:signalrservice/v20240101preview:SignalRCustomCertificate"), pulumi.Alias(type_="azure-native:signalrservice/v20240301:SignalRCustomCertificate"), pulumi.Alias(type_="azure-native:signalrservice/v20240401preview:SignalRCustomCertificate")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SignalRCustomCertificate, __self__).__init__(
            'azure-native:signalrservice/v20230601preview:SignalRCustomCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SignalRCustomCertificate':
        """
        Get an existing SignalRCustomCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SignalRCustomCertificateArgs.__new__(SignalRCustomCertificateArgs)

        __props__.__dict__["key_vault_base_uri"] = None
        __props__.__dict__["key_vault_secret_name"] = None
        __props__.__dict__["key_vault_secret_version"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return SignalRCustomCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="keyVaultBaseUri")
    def key_vault_base_uri(self) -> pulumi.Output[str]:
        """
        Base uri of the KeyVault that stores certificate.
        """
        return pulumi.get(self, "key_vault_base_uri")

    @property
    @pulumi.getter(name="keyVaultSecretName")
    def key_vault_secret_name(self) -> pulumi.Output[str]:
        """
        Certificate secret name.
        """
        return pulumi.get(self, "key_vault_secret_name")

    @property
    @pulumi.getter(name="keyVaultSecretVersion")
    def key_vault_secret_version(self) -> pulumi.Output[Optional[str]]:
        """
        Certificate secret version.
        """
        return pulumi.get(self, "key_vault_secret_version")

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
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

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

