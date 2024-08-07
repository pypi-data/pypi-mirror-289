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
from ._enums import *

__all__ = ['SqlPoolTransparentDataEncryptionArgs', 'SqlPoolTransparentDataEncryption']

@pulumi.input_type
class SqlPoolTransparentDataEncryptionArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 sql_pool_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 status: Optional[pulumi.Input[Union[str, 'TransparentDataEncryptionStatus']]] = None,
                 transparent_data_encryption_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SqlPoolTransparentDataEncryption resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sql_pool_name: SQL pool name
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[Union[str, 'TransparentDataEncryptionStatus']] status: The status of the database transparent data encryption.
        :param pulumi.Input[str] transparent_data_encryption_name: The name of the transparent data encryption configuration.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "sql_pool_name", sql_pool_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if transparent_data_encryption_name is not None:
            pulumi.set(__self__, "transparent_data_encryption_name", transparent_data_encryption_name)

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
    @pulumi.getter(name="sqlPoolName")
    def sql_pool_name(self) -> pulumi.Input[str]:
        """
        SQL pool name
        """
        return pulumi.get(self, "sql_pool_name")

    @sql_pool_name.setter
    def sql_pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sql_pool_name", value)

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
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'TransparentDataEncryptionStatus']]]:
        """
        The status of the database transparent data encryption.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'TransparentDataEncryptionStatus']]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="transparentDataEncryptionName")
    def transparent_data_encryption_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the transparent data encryption configuration.
        """
        return pulumi.get(self, "transparent_data_encryption_name")

    @transparent_data_encryption_name.setter
    def transparent_data_encryption_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "transparent_data_encryption_name", value)


class SqlPoolTransparentDataEncryption(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_pool_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'TransparentDataEncryptionStatus']]] = None,
                 transparent_data_encryption_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a Sql pool transparent data encryption configuration.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] sql_pool_name: SQL pool name
        :param pulumi.Input[Union[str, 'TransparentDataEncryptionStatus']] status: The status of the database transparent data encryption.
        :param pulumi.Input[str] transparent_data_encryption_name: The name of the transparent data encryption configuration.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlPoolTransparentDataEncryptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a Sql pool transparent data encryption configuration.

        :param str resource_name: The name of the resource.
        :param SqlPoolTransparentDataEncryptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlPoolTransparentDataEncryptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sql_pool_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'TransparentDataEncryptionStatus']]] = None,
                 transparent_data_encryption_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlPoolTransparentDataEncryptionArgs.__new__(SqlPoolTransparentDataEncryptionArgs)

            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if sql_pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'sql_pool_name'")
            __props__.__dict__["sql_pool_name"] = sql_pool_name
            __props__.__dict__["status"] = status
            __props__.__dict__["transparent_data_encryption_name"] = transparent_data_encryption_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:synapse:SqlPoolTransparentDataEncryption"), pulumi.Alias(type_="azure-native:synapse/v20190601preview:SqlPoolTransparentDataEncryption"), pulumi.Alias(type_="azure-native:synapse/v20201201:SqlPoolTransparentDataEncryption"), pulumi.Alias(type_="azure-native:synapse/v20210301:SqlPoolTransparentDataEncryption"), pulumi.Alias(type_="azure-native:synapse/v20210401preview:SqlPoolTransparentDataEncryption"), pulumi.Alias(type_="azure-native:synapse/v20210501:SqlPoolTransparentDataEncryption"), pulumi.Alias(type_="azure-native:synapse/v20210601preview:SqlPoolTransparentDataEncryption")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SqlPoolTransparentDataEncryption, __self__).__init__(
            'azure-native:synapse/v20210601:SqlPoolTransparentDataEncryption',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SqlPoolTransparentDataEncryption':
        """
        Get an existing SqlPoolTransparentDataEncryption resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SqlPoolTransparentDataEncryptionArgs.__new__(SqlPoolTransparentDataEncryptionArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["type"] = None
        return SqlPoolTransparentDataEncryption(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
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
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the database transparent data encryption.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

