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

__all__ = ['ManagedInstanceLongTermRetentionPolicyArgs', 'ManagedInstanceLongTermRetentionPolicy']

@pulumi.input_type
class ManagedInstanceLongTermRetentionPolicyArgs:
    def __init__(__self__, *,
                 database_name: pulumi.Input[str],
                 managed_instance_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 monthly_retention: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 week_of_year: Optional[pulumi.Input[int]] = None,
                 weekly_retention: Optional[pulumi.Input[str]] = None,
                 yearly_retention: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ManagedInstanceLongTermRetentionPolicy resource.
        :param pulumi.Input[str] database_name: The name of the database.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] monthly_retention: The monthly retention policy for an LTR backup in an ISO 8601 format.
        :param pulumi.Input[str] policy_name: The policy name. Should always be Default.
        :param pulumi.Input[int] week_of_year: The week of year to take the yearly backup in an ISO 8601 format.
        :param pulumi.Input[str] weekly_retention: The weekly retention policy for an LTR backup in an ISO 8601 format.
        :param pulumi.Input[str] yearly_retention: The yearly retention policy for an LTR backup in an ISO 8601 format.
        """
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "managed_instance_name", managed_instance_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if monthly_retention is not None:
            pulumi.set(__self__, "monthly_retention", monthly_retention)
        if policy_name is not None:
            pulumi.set(__self__, "policy_name", policy_name)
        if week_of_year is not None:
            pulumi.set(__self__, "week_of_year", week_of_year)
        if weekly_retention is not None:
            pulumi.set(__self__, "weekly_retention", weekly_retention)
        if yearly_retention is not None:
            pulumi.set(__self__, "yearly_retention", yearly_retention)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        The name of the database.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[str]:
        """
        The name of the managed instance.
        """
        return pulumi.get(self, "managed_instance_name")

    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_instance_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="monthlyRetention")
    def monthly_retention(self) -> Optional[pulumi.Input[str]]:
        """
        The monthly retention policy for an LTR backup in an ISO 8601 format.
        """
        return pulumi.get(self, "monthly_retention")

    @monthly_retention.setter
    def monthly_retention(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "monthly_retention", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The policy name. Should always be Default.
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="weekOfYear")
    def week_of_year(self) -> Optional[pulumi.Input[int]]:
        """
        The week of year to take the yearly backup in an ISO 8601 format.
        """
        return pulumi.get(self, "week_of_year")

    @week_of_year.setter
    def week_of_year(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "week_of_year", value)

    @property
    @pulumi.getter(name="weeklyRetention")
    def weekly_retention(self) -> Optional[pulumi.Input[str]]:
        """
        The weekly retention policy for an LTR backup in an ISO 8601 format.
        """
        return pulumi.get(self, "weekly_retention")

    @weekly_retention.setter
    def weekly_retention(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "weekly_retention", value)

    @property
    @pulumi.getter(name="yearlyRetention")
    def yearly_retention(self) -> Optional[pulumi.Input[str]]:
        """
        The yearly retention policy for an LTR backup in an ISO 8601 format.
        """
        return pulumi.get(self, "yearly_retention")

    @yearly_retention.setter
    def yearly_retention(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "yearly_retention", value)


class ManagedInstanceLongTermRetentionPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 monthly_retention: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 week_of_year: Optional[pulumi.Input[int]] = None,
                 weekly_retention: Optional[pulumi.Input[str]] = None,
                 yearly_retention: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A long term retention policy.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] database_name: The name of the database.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] monthly_retention: The monthly retention policy for an LTR backup in an ISO 8601 format.
        :param pulumi.Input[str] policy_name: The policy name. Should always be Default.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[int] week_of_year: The week of year to take the yearly backup in an ISO 8601 format.
        :param pulumi.Input[str] weekly_retention: The weekly retention policy for an LTR backup in an ISO 8601 format.
        :param pulumi.Input[str] yearly_retention: The yearly retention policy for an LTR backup in an ISO 8601 format.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedInstanceLongTermRetentionPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A long term retention policy.

        :param str resource_name: The name of the resource.
        :param ManagedInstanceLongTermRetentionPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedInstanceLongTermRetentionPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 monthly_retention: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 week_of_year: Optional[pulumi.Input[int]] = None,
                 weekly_retention: Optional[pulumi.Input[str]] = None,
                 yearly_retention: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedInstanceLongTermRetentionPolicyArgs.__new__(ManagedInstanceLongTermRetentionPolicyArgs)

            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            if managed_instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'managed_instance_name'")
            __props__.__dict__["managed_instance_name"] = managed_instance_name
            __props__.__dict__["monthly_retention"] = monthly_retention
            __props__.__dict__["policy_name"] = policy_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["week_of_year"] = week_of_year
            __props__.__dict__["weekly_retention"] = weekly_retention
            __props__.__dict__["yearly_retention"] = yearly_retention
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:ManagedInstanceLongTermRetentionPolicy"), pulumi.Alias(type_="azure-native:sql/v20220501preview:ManagedInstanceLongTermRetentionPolicy"), pulumi.Alias(type_="azure-native:sql/v20220801preview:ManagedInstanceLongTermRetentionPolicy"), pulumi.Alias(type_="azure-native:sql/v20230201preview:ManagedInstanceLongTermRetentionPolicy"), pulumi.Alias(type_="azure-native:sql/v20230501preview:ManagedInstanceLongTermRetentionPolicy"), pulumi.Alias(type_="azure-native:sql/v20230801preview:ManagedInstanceLongTermRetentionPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagedInstanceLongTermRetentionPolicy, __self__).__init__(
            'azure-native:sql/v20221101preview:ManagedInstanceLongTermRetentionPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedInstanceLongTermRetentionPolicy':
        """
        Get an existing ManagedInstanceLongTermRetentionPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedInstanceLongTermRetentionPolicyArgs.__new__(ManagedInstanceLongTermRetentionPolicyArgs)

        __props__.__dict__["monthly_retention"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["week_of_year"] = None
        __props__.__dict__["weekly_retention"] = None
        __props__.__dict__["yearly_retention"] = None
        return ManagedInstanceLongTermRetentionPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="monthlyRetention")
    def monthly_retention(self) -> pulumi.Output[Optional[str]]:
        """
        The monthly retention policy for an LTR backup in an ISO 8601 format.
        """
        return pulumi.get(self, "monthly_retention")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="weekOfYear")
    def week_of_year(self) -> pulumi.Output[Optional[int]]:
        """
        The week of year to take the yearly backup in an ISO 8601 format.
        """
        return pulumi.get(self, "week_of_year")

    @property
    @pulumi.getter(name="weeklyRetention")
    def weekly_retention(self) -> pulumi.Output[Optional[str]]:
        """
        The weekly retention policy for an LTR backup in an ISO 8601 format.
        """
        return pulumi.get(self, "weekly_retention")

    @property
    @pulumi.getter(name="yearlyRetention")
    def yearly_retention(self) -> pulumi.Output[Optional[str]]:
        """
        The yearly retention policy for an LTR backup in an ISO 8601 format.
        """
        return pulumi.get(self, "yearly_retention")

