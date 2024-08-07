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

__all__ = ['ReadWriteDatabaseArgs', 'ReadWriteDatabase']

@pulumi.input_type
class ReadWriteDatabaseArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 kusto_pool_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 database_name: Optional[pulumi.Input[str]] = None,
                 hot_cache_period: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 soft_delete_period: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ReadWriteDatabase resource.
        :param pulumi.Input[str] kind: Kind of the database
               Expected value is 'ReadWrite'.
        :param pulumi.Input[str] kusto_pool_name: The name of the Kusto pool.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] database_name: The name of the database in the Kusto pool.
        :param pulumi.Input[str] hot_cache_period: The time the data should be kept in cache for fast queries in TimeSpan.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] soft_delete_period: The time the data should be kept before it stops being accessible to queries in TimeSpan.
        """
        pulumi.set(__self__, "kind", 'ReadWrite')
        pulumi.set(__self__, "kusto_pool_name", kusto_pool_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if hot_cache_period is not None:
            pulumi.set(__self__, "hot_cache_period", hot_cache_period)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if soft_delete_period is not None:
            pulumi.set(__self__, "soft_delete_period", soft_delete_period)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Kind of the database
        Expected value is 'ReadWrite'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="kustoPoolName")
    def kusto_pool_name(self) -> pulumi.Input[str]:
        """
        The name of the Kusto pool.
        """
        return pulumi.get(self, "kusto_pool_name")

    @kusto_pool_name.setter
    def kusto_pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "kusto_pool_name", value)

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
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the database in the Kusto pool.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="hotCachePeriod")
    def hot_cache_period(self) -> Optional[pulumi.Input[str]]:
        """
        The time the data should be kept in cache for fast queries in TimeSpan.
        """
        return pulumi.get(self, "hot_cache_period")

    @hot_cache_period.setter
    def hot_cache_period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hot_cache_period", value)

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
    @pulumi.getter(name="softDeletePeriod")
    def soft_delete_period(self) -> Optional[pulumi.Input[str]]:
        """
        The time the data should be kept before it stops being accessible to queries in TimeSpan.
        """
        return pulumi.get(self, "soft_delete_period")

    @soft_delete_period.setter
    def soft_delete_period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "soft_delete_period", value)


class ReadWriteDatabase(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 hot_cache_period: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 kusto_pool_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 soft_delete_period: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Class representing a read write database.
        Azure REST API version: 2021-06-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_name: The name of the database in the Kusto pool.
        :param pulumi.Input[str] hot_cache_period: The time the data should be kept in cache for fast queries in TimeSpan.
        :param pulumi.Input[str] kind: Kind of the database
               Expected value is 'ReadWrite'.
        :param pulumi.Input[str] kusto_pool_name: The name of the Kusto pool.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] soft_delete_period: The time the data should be kept before it stops being accessible to queries in TimeSpan.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReadWriteDatabaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing a read write database.
        Azure REST API version: 2021-06-01-preview.

        :param str resource_name: The name of the resource.
        :param ReadWriteDatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReadWriteDatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 hot_cache_period: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 kusto_pool_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 soft_delete_period: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReadWriteDatabaseArgs.__new__(ReadWriteDatabaseArgs)

            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["hot_cache_period"] = hot_cache_period
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'ReadWrite'
            if kusto_pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'kusto_pool_name'")
            __props__.__dict__["kusto_pool_name"] = kusto_pool_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["soft_delete_period"] = soft_delete_period
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["is_followed"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["statistics"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:synapse/v20210401preview:ReadWriteDatabase"), pulumi.Alias(type_="azure-native:synapse/v20210601preview:ReadWriteDatabase")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ReadWriteDatabase, __self__).__init__(
            'azure-native:synapse:ReadWriteDatabase',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReadWriteDatabase':
        """
        Get an existing ReadWriteDatabase resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReadWriteDatabaseArgs.__new__(ReadWriteDatabaseArgs)

        __props__.__dict__["hot_cache_period"] = None
        __props__.__dict__["is_followed"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["soft_delete_period"] = None
        __props__.__dict__["statistics"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ReadWriteDatabase(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="hotCachePeriod")
    def hot_cache_period(self) -> pulumi.Output[Optional[str]]:
        """
        The time the data should be kept in cache for fast queries in TimeSpan.
        """
        return pulumi.get(self, "hot_cache_period")

    @property
    @pulumi.getter(name="isFollowed")
    def is_followed(self) -> pulumi.Output[bool]:
        """
        Indicates whether the database is followed.
        """
        return pulumi.get(self, "is_followed")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of the database
        Expected value is 'ReadWrite'.
        """
        return pulumi.get(self, "kind")

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
    @pulumi.getter(name="softDeletePeriod")
    def soft_delete_period(self) -> pulumi.Output[Optional[str]]:
        """
        The time the data should be kept before it stops being accessible to queries in TimeSpan.
        """
        return pulumi.get(self, "soft_delete_period")

    @property
    @pulumi.getter
    def statistics(self) -> pulumi.Output['outputs.DatabaseStatisticsResponse']:
        """
        The statistics of the database.
        """
        return pulumi.get(self, "statistics")

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

