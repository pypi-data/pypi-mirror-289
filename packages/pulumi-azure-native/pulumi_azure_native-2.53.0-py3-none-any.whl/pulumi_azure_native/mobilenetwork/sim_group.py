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

__all__ = ['SimGroupArgs', 'SimGroup']

@pulumi.input_type
class SimGroupArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 encryption_key: Optional[pulumi.Input['KeyVaultKeyArgs']] = None,
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mobile_network: Optional[pulumi.Input['MobileNetworkResourceIdArgs']] = None,
                 sim_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SimGroup resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['KeyVaultKeyArgs'] encryption_key: A key to encrypt the SIM data that belongs to this SIM group.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: The identity used to retrieve the encryption key from Azure key vault.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['MobileNetworkResourceIdArgs'] mobile_network: Mobile network that this SIM group belongs to. The mobile network must be in the same location as the SIM group.
        :param pulumi.Input[str] sim_group_name: The name of the SIM Group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if encryption_key is not None:
            pulumi.set(__self__, "encryption_key", encryption_key)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mobile_network is not None:
            pulumi.set(__self__, "mobile_network", mobile_network)
        if sim_group_name is not None:
            pulumi.set(__self__, "sim_group_name", sim_group_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[pulumi.Input['KeyVaultKeyArgs']]:
        """
        A key to encrypt the SIM data that belongs to this SIM group.
        """
        return pulumi.get(self, "encryption_key")

    @encryption_key.setter
    def encryption_key(self, value: Optional[pulumi.Input['KeyVaultKeyArgs']]):
        pulumi.set(self, "encryption_key", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        The identity used to retrieve the encryption key from Azure key vault.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

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
    @pulumi.getter(name="mobileNetwork")
    def mobile_network(self) -> Optional[pulumi.Input['MobileNetworkResourceIdArgs']]:
        """
        Mobile network that this SIM group belongs to. The mobile network must be in the same location as the SIM group.
        """
        return pulumi.get(self, "mobile_network")

    @mobile_network.setter
    def mobile_network(self, value: Optional[pulumi.Input['MobileNetworkResourceIdArgs']]):
        pulumi.set(self, "mobile_network", value)

    @property
    @pulumi.getter(name="simGroupName")
    def sim_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the SIM Group.
        """
        return pulumi.get(self, "sim_group_name")

    @sim_group_name.setter
    def sim_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sim_group_name", value)

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


class SimGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption_key: Optional[pulumi.Input[Union['KeyVaultKeyArgs', 'KeyVaultKeyArgsDict']]] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mobile_network: Optional[pulumi.Input[Union['MobileNetworkResourceIdArgs', 'MobileNetworkResourceIdArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sim_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        SIM group resource.
        Azure REST API version: 2023-06-01. Prior API version in Azure Native 1.x: 2022-04-01-preview.

        Other available API versions: 2022-04-01-preview, 2022-11-01, 2023-09-01, 2024-02-01, 2024-04-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['KeyVaultKeyArgs', 'KeyVaultKeyArgsDict']] encryption_key: A key to encrypt the SIM data that belongs to this SIM group.
        :param pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']] identity: The identity used to retrieve the encryption key from Azure key vault.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union['MobileNetworkResourceIdArgs', 'MobileNetworkResourceIdArgsDict']] mobile_network: Mobile network that this SIM group belongs to. The mobile network must be in the same location as the SIM group.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sim_group_name: The name of the SIM Group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SimGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        SIM group resource.
        Azure REST API version: 2023-06-01. Prior API version in Azure Native 1.x: 2022-04-01-preview.

        Other available API versions: 2022-04-01-preview, 2022-11-01, 2023-09-01, 2024-02-01, 2024-04-01.

        :param str resource_name: The name of the resource.
        :param SimGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SimGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 encryption_key: Optional[pulumi.Input[Union['KeyVaultKeyArgs', 'KeyVaultKeyArgsDict']]] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mobile_network: Optional[pulumi.Input[Union['MobileNetworkResourceIdArgs', 'MobileNetworkResourceIdArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sim_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SimGroupArgs.__new__(SimGroupArgs)

            __props__.__dict__["encryption_key"] = encryption_key
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["mobile_network"] = mobile_network
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sim_group_name"] = sim_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:mobilenetwork/v20220401preview:SimGroup"), pulumi.Alias(type_="azure-native:mobilenetwork/v20221101:SimGroup"), pulumi.Alias(type_="azure-native:mobilenetwork/v20230601:SimGroup"), pulumi.Alias(type_="azure-native:mobilenetwork/v20230901:SimGroup"), pulumi.Alias(type_="azure-native:mobilenetwork/v20240201:SimGroup"), pulumi.Alias(type_="azure-native:mobilenetwork/v20240401:SimGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SimGroup, __self__).__init__(
            'azure-native:mobilenetwork:SimGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SimGroup':
        """
        Get an existing SimGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SimGroupArgs.__new__(SimGroupArgs)

        __props__.__dict__["encryption_key"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mobile_network"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return SimGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> pulumi.Output[Optional['outputs.KeyVaultKeyResponse']]:
        """
        A key to encrypt the SIM data that belongs to this SIM group.
        """
        return pulumi.get(self, "encryption_key")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        The identity used to retrieve the encryption key from Azure key vault.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mobileNetwork")
    def mobile_network(self) -> pulumi.Output[Optional['outputs.MobileNetworkResourceIdResponse']]:
        """
        Mobile network that this SIM group belongs to. The mobile network must be in the same location as the SIM group.
        """
        return pulumi.get(self, "mobile_network")

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
        The provisioning state of the SIM group resource.
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
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

