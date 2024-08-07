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

__all__ = ['CatalogArgs', 'Catalog']

@pulumi.input_type
class CatalogArgs:
    def __init__(__self__, *,
                 dev_center_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 ado_git: Optional[pulumi.Input['GitCatalogArgs']] = None,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 git_hub: Optional[pulumi.Input['GitCatalogArgs']] = None):
        """
        The set of arguments for constructing a Catalog resource.
        :param pulumi.Input[str] dev_center_name: The name of the devcenter.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['GitCatalogArgs'] ado_git: Properties for an Azure DevOps catalog type.
        :param pulumi.Input[str] catalog_name: The name of the Catalog.
        :param pulumi.Input['GitCatalogArgs'] git_hub: Properties for a GitHub catalog type.
        """
        pulumi.set(__self__, "dev_center_name", dev_center_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if ado_git is not None:
            pulumi.set(__self__, "ado_git", ado_git)
        if catalog_name is not None:
            pulumi.set(__self__, "catalog_name", catalog_name)
        if git_hub is not None:
            pulumi.set(__self__, "git_hub", git_hub)

    @property
    @pulumi.getter(name="devCenterName")
    def dev_center_name(self) -> pulumi.Input[str]:
        """
        The name of the devcenter.
        """
        return pulumi.get(self, "dev_center_name")

    @dev_center_name.setter
    def dev_center_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "dev_center_name", value)

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
    @pulumi.getter(name="adoGit")
    def ado_git(self) -> Optional[pulumi.Input['GitCatalogArgs']]:
        """
        Properties for an Azure DevOps catalog type.
        """
        return pulumi.get(self, "ado_git")

    @ado_git.setter
    def ado_git(self, value: Optional[pulumi.Input['GitCatalogArgs']]):
        pulumi.set(self, "ado_git", value)

    @property
    @pulumi.getter(name="catalogName")
    def catalog_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Catalog.
        """
        return pulumi.get(self, "catalog_name")

    @catalog_name.setter
    def catalog_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_name", value)

    @property
    @pulumi.getter(name="gitHub")
    def git_hub(self) -> Optional[pulumi.Input['GitCatalogArgs']]:
        """
        Properties for a GitHub catalog type.
        """
        return pulumi.get(self, "git_hub")

    @git_hub.setter
    def git_hub(self, value: Optional[pulumi.Input['GitCatalogArgs']]):
        pulumi.set(self, "git_hub", value)


class Catalog(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ado_git: Optional[pulumi.Input[Union['GitCatalogArgs', 'GitCatalogArgsDict']]] = None,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 dev_center_name: Optional[pulumi.Input[str]] = None,
                 git_hub: Optional[pulumi.Input[Union['GitCatalogArgs', 'GitCatalogArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a catalog.
        Azure REST API version: 2023-04-01. Prior API version in Azure Native 1.x: 2022-09-01-preview.

        Other available API versions: 2023-08-01-preview, 2023-10-01-preview, 2024-02-01, 2024-05-01-preview, 2024-06-01-preview, 2024-07-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['GitCatalogArgs', 'GitCatalogArgsDict']] ado_git: Properties for an Azure DevOps catalog type.
        :param pulumi.Input[str] catalog_name: The name of the Catalog.
        :param pulumi.Input[str] dev_center_name: The name of the devcenter.
        :param pulumi.Input[Union['GitCatalogArgs', 'GitCatalogArgsDict']] git_hub: Properties for a GitHub catalog type.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CatalogArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a catalog.
        Azure REST API version: 2023-04-01. Prior API version in Azure Native 1.x: 2022-09-01-preview.

        Other available API versions: 2023-08-01-preview, 2023-10-01-preview, 2024-02-01, 2024-05-01-preview, 2024-06-01-preview, 2024-07-01-preview.

        :param str resource_name: The name of the resource.
        :param CatalogArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CatalogArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ado_git: Optional[pulumi.Input[Union['GitCatalogArgs', 'GitCatalogArgsDict']]] = None,
                 catalog_name: Optional[pulumi.Input[str]] = None,
                 dev_center_name: Optional[pulumi.Input[str]] = None,
                 git_hub: Optional[pulumi.Input[Union['GitCatalogArgs', 'GitCatalogArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CatalogArgs.__new__(CatalogArgs)

            __props__.__dict__["ado_git"] = ado_git
            __props__.__dict__["catalog_name"] = catalog_name
            if dev_center_name is None and not opts.urn:
                raise TypeError("Missing required property 'dev_center_name'")
            __props__.__dict__["dev_center_name"] = dev_center_name
            __props__.__dict__["git_hub"] = git_hub
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["last_sync_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["sync_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devcenter/v20220801preview:Catalog"), pulumi.Alias(type_="azure-native:devcenter/v20220901preview:Catalog"), pulumi.Alias(type_="azure-native:devcenter/v20221012preview:Catalog"), pulumi.Alias(type_="azure-native:devcenter/v20221111preview:Catalog"), pulumi.Alias(type_="azure-native:devcenter/v20230101preview:Catalog"), pulumi.Alias(type_="azure-native:devcenter/v20230401:Catalog"), pulumi.Alias(type_="azure-native:devcenter/v20230801preview:Catalog"), pulumi.Alias(type_="azure-native:devcenter/v20231001preview:Catalog"), pulumi.Alias(type_="azure-native:devcenter/v20240201:Catalog"), pulumi.Alias(type_="azure-native:devcenter/v20240501preview:Catalog"), pulumi.Alias(type_="azure-native:devcenter/v20240601preview:Catalog"), pulumi.Alias(type_="azure-native:devcenter/v20240701preview:Catalog")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Catalog, __self__).__init__(
            'azure-native:devcenter:Catalog',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Catalog':
        """
        Get an existing Catalog resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CatalogArgs.__new__(CatalogArgs)

        __props__.__dict__["ado_git"] = None
        __props__.__dict__["git_hub"] = None
        __props__.__dict__["last_sync_time"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["sync_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Catalog(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adoGit")
    def ado_git(self) -> pulumi.Output[Optional['outputs.GitCatalogResponse']]:
        """
        Properties for an Azure DevOps catalog type.
        """
        return pulumi.get(self, "ado_git")

    @property
    @pulumi.getter(name="gitHub")
    def git_hub(self) -> pulumi.Output[Optional['outputs.GitCatalogResponse']]:
        """
        Properties for a GitHub catalog type.
        """
        return pulumi.get(self, "git_hub")

    @property
    @pulumi.getter(name="lastSyncTime")
    def last_sync_time(self) -> pulumi.Output[str]:
        """
        When the catalog was last synced.
        """
        return pulumi.get(self, "last_sync_time")

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
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="syncState")
    def sync_state(self) -> pulumi.Output[str]:
        """
        The synchronization state of the catalog.
        """
        return pulumi.get(self, "sync_state")

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

