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

__all__ = ['SqlServerArgs', 'SqlServer']

@pulumi.input_type
class SqlServerArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 sql_server_registration_name: pulumi.Input[str],
                 cores: Optional[pulumi.Input[int]] = None,
                 edition: Optional[pulumi.Input[str]] = None,
                 property_bag: Optional[pulumi.Input[str]] = None,
                 registration_id: Optional[pulumi.Input[str]] = None,
                 sql_server_name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SqlServer resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] sql_server_registration_name: Name of the SQL Server registration.
        :param pulumi.Input[int] cores: Cores of the Sql Server.
        :param pulumi.Input[str] edition: Sql Server Edition.
        :param pulumi.Input[str] property_bag: Sql Server Json Property Bag.
        :param pulumi.Input[str] registration_id: ID for Parent Sql Server Registration.
        :param pulumi.Input[str] sql_server_name: Name of the SQL Server.
        :param pulumi.Input[str] version: Version of the Sql Server.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sql_server_registration_name", sql_server_registration_name)
        if cores is not None:
            pulumi.set(__self__, "cores", cores)
        if edition is not None:
            pulumi.set(__self__, "edition", edition)
        if property_bag is not None:
            pulumi.set(__self__, "property_bag", property_bag)
        if registration_id is not None:
            pulumi.set(__self__, "registration_id", registration_id)
        if sql_server_name is not None:
            pulumi.set(__self__, "sql_server_name", sql_server_name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sqlServerRegistrationName")
    def sql_server_registration_name(self) -> pulumi.Input[str]:
        """
        Name of the SQL Server registration.
        """
        return pulumi.get(self, "sql_server_registration_name")

    @sql_server_registration_name.setter
    def sql_server_registration_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sql_server_registration_name", value)

    @property
    @pulumi.getter
    def cores(self) -> Optional[pulumi.Input[int]]:
        """
        Cores of the Sql Server.
        """
        return pulumi.get(self, "cores")

    @cores.setter
    def cores(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "cores", value)

    @property
    @pulumi.getter
    def edition(self) -> Optional[pulumi.Input[str]]:
        """
        Sql Server Edition.
        """
        return pulumi.get(self, "edition")

    @edition.setter
    def edition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "edition", value)

    @property
    @pulumi.getter(name="propertyBag")
    def property_bag(self) -> Optional[pulumi.Input[str]]:
        """
        Sql Server Json Property Bag.
        """
        return pulumi.get(self, "property_bag")

    @property_bag.setter
    def property_bag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "property_bag", value)

    @property
    @pulumi.getter(name="registrationID")
    def registration_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID for Parent Sql Server Registration.
        """
        return pulumi.get(self, "registration_id")

    @registration_id.setter
    def registration_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "registration_id", value)

    @property
    @pulumi.getter(name="sqlServerName")
    def sql_server_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the SQL Server.
        """
        return pulumi.get(self, "sql_server_name")

    @sql_server_name.setter
    def sql_server_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_server_name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Version of the Sql Server.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class SqlServer(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cores: Optional[pulumi.Input[int]] = None,
                 edition: Optional[pulumi.Input[str]] = None,
                 property_bag: Optional[pulumi.Input[str]] = None,
                 registration_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_server_name: Optional[pulumi.Input[str]] = None,
                 sql_server_registration_name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A SQL server.
        Azure REST API version: 2019-07-24-preview. Prior API version in Azure Native 1.x: 2019-07-24-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] cores: Cores of the Sql Server.
        :param pulumi.Input[str] edition: Sql Server Edition.
        :param pulumi.Input[str] property_bag: Sql Server Json Property Bag.
        :param pulumi.Input[str] registration_id: ID for Parent Sql Server Registration.
        :param pulumi.Input[str] resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] sql_server_name: Name of the SQL Server.
        :param pulumi.Input[str] sql_server_registration_name: Name of the SQL Server registration.
        :param pulumi.Input[str] version: Version of the Sql Server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A SQL server.
        Azure REST API version: 2019-07-24-preview. Prior API version in Azure Native 1.x: 2019-07-24-preview.

        :param str resource_name: The name of the resource.
        :param SqlServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cores: Optional[pulumi.Input[int]] = None,
                 edition: Optional[pulumi.Input[str]] = None,
                 property_bag: Optional[pulumi.Input[str]] = None,
                 registration_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_server_name: Optional[pulumi.Input[str]] = None,
                 sql_server_registration_name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlServerArgs.__new__(SqlServerArgs)

            __props__.__dict__["cores"] = cores
            __props__.__dict__["edition"] = edition
            __props__.__dict__["property_bag"] = property_bag
            __props__.__dict__["registration_id"] = registration_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sql_server_name"] = sql_server_name
            if sql_server_registration_name is None and not opts.urn:
                raise TypeError("Missing required property 'sql_server_registration_name'")
            __props__.__dict__["sql_server_registration_name"] = sql_server_registration_name
            __props__.__dict__["version"] = version
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azuredata/v20170301preview:SqlServer"), pulumi.Alias(type_="azure-native:azuredata/v20190724preview:SqlServer")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SqlServer, __self__).__init__(
            'azure-native:azuredata:SqlServer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SqlServer':
        """
        Get an existing SqlServer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SqlServerArgs.__new__(SqlServerArgs)

        __props__.__dict__["cores"] = None
        __props__.__dict__["edition"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["property_bag"] = None
        __props__.__dict__["registration_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return SqlServer(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cores(self) -> pulumi.Output[Optional[int]]:
        """
        Cores of the Sql Server.
        """
        return pulumi.get(self, "cores")

    @property
    @pulumi.getter
    def edition(self) -> pulumi.Output[Optional[str]]:
        """
        Sql Server Edition.
        """
        return pulumi.get(self, "edition")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="propertyBag")
    def property_bag(self) -> pulumi.Output[Optional[str]]:
        """
        Sql Server Json Property Bag.
        """
        return pulumi.get(self, "property_bag")

    @property
    @pulumi.getter(name="registrationID")
    def registration_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID for Parent Sql Server Registration.
        """
        return pulumi.get(self, "registration_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        Version of the Sql Server.
        """
        return pulumi.get(self, "version")

