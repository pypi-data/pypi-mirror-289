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

__all__ = ['SqlDiscoverySiteDataSourceControllerArgs', 'SqlDiscoverySiteDataSourceController']

@pulumi.input_type
class SqlDiscoverySiteDataSourceControllerArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 site_name: pulumi.Input[str],
                 sql_site_name: pulumi.Input[str],
                 discovery_site_data_source_name: Optional[pulumi.Input[str]] = None,
                 discovery_site_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SqlDiscoverySiteDataSourceController resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] site_name: Site name
        :param pulumi.Input[str] sql_site_name: SQL site name.
        :param pulumi.Input[str] discovery_site_data_source_name: SQL Discovery site data source name.
        :param pulumi.Input[str] discovery_site_id: Gets or sets the discovery site Id.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "site_name", site_name)
        pulumi.set(__self__, "sql_site_name", sql_site_name)
        if discovery_site_data_source_name is not None:
            pulumi.set(__self__, "discovery_site_data_source_name", discovery_site_data_source_name)
        if discovery_site_id is not None:
            pulumi.set(__self__, "discovery_site_id", discovery_site_id)

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
    @pulumi.getter(name="siteName")
    def site_name(self) -> pulumi.Input[str]:
        """
        Site name
        """
        return pulumi.get(self, "site_name")

    @site_name.setter
    def site_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "site_name", value)

    @property
    @pulumi.getter(name="sqlSiteName")
    def sql_site_name(self) -> pulumi.Input[str]:
        """
        SQL site name.
        """
        return pulumi.get(self, "sql_site_name")

    @sql_site_name.setter
    def sql_site_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sql_site_name", value)

    @property
    @pulumi.getter(name="discoverySiteDataSourceName")
    def discovery_site_data_source_name(self) -> Optional[pulumi.Input[str]]:
        """
        SQL Discovery site data source name.
        """
        return pulumi.get(self, "discovery_site_data_source_name")

    @discovery_site_data_source_name.setter
    def discovery_site_data_source_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "discovery_site_data_source_name", value)

    @property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the discovery site Id.
        """
        return pulumi.get(self, "discovery_site_id")

    @discovery_site_id.setter
    def discovery_site_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "discovery_site_id", value)


class SqlDiscoverySiteDataSourceController(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 discovery_site_data_source_name: Optional[pulumi.Input[str]] = None,
                 discovery_site_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 sql_site_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A SQL discovery site data source resource.
        Azure REST API version: 2023-06-06.

        Other available API versions: 2023-10-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] discovery_site_data_source_name: SQL Discovery site data source name.
        :param pulumi.Input[str] discovery_site_id: Gets or sets the discovery site Id.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] site_name: Site name
        :param pulumi.Input[str] sql_site_name: SQL site name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlDiscoverySiteDataSourceControllerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A SQL discovery site data source resource.
        Azure REST API version: 2023-06-06.

        Other available API versions: 2023-10-01-preview.

        :param str resource_name: The name of the resource.
        :param SqlDiscoverySiteDataSourceControllerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlDiscoverySiteDataSourceControllerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 discovery_site_data_source_name: Optional[pulumi.Input[str]] = None,
                 discovery_site_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 sql_site_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlDiscoverySiteDataSourceControllerArgs.__new__(SqlDiscoverySiteDataSourceControllerArgs)

            __props__.__dict__["discovery_site_data_source_name"] = discovery_site_data_source_name
            __props__.__dict__["discovery_site_id"] = discovery_site_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if site_name is None and not opts.urn:
                raise TypeError("Missing required property 'site_name'")
            __props__.__dict__["site_name"] = site_name
            if sql_site_name is None and not opts.urn:
                raise TypeError("Missing required property 'sql_site_name'")
            __props__.__dict__["sql_site_name"] = sql_site_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:offazure/v20230606:SqlDiscoverySiteDataSourceController"), pulumi.Alias(type_="azure-native:offazure/v20231001preview:SqlDiscoverySiteDataSourceController")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SqlDiscoverySiteDataSourceController, __self__).__init__(
            'azure-native:offazure:SqlDiscoverySiteDataSourceController',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SqlDiscoverySiteDataSourceController':
        """
        Get an existing SqlDiscoverySiteDataSourceController resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SqlDiscoverySiteDataSourceControllerArgs.__new__(SqlDiscoverySiteDataSourceControllerArgs)

        __props__.__dict__["discovery_site_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return SqlDiscoverySiteDataSourceController(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="discoverySiteId")
    def discovery_site_id(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the discovery site Id.
        """
        return pulumi.get(self, "discovery_site_id")

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
        provisioning state enum
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

