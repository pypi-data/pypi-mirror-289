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

__all__ = ['CommitmentPlanAssociationArgs', 'CommitmentPlanAssociation']

@pulumi.input_type
class CommitmentPlanAssociationArgs:
    def __init__(__self__, *,
                 commitment_plan_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 commitment_plan_association_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CommitmentPlanAssociation resource.
        :param pulumi.Input[str] commitment_plan_name: The name of the commitmentPlan associated with the Cognitive Services Account
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] account_id: The Azure resource id of the account.
        :param pulumi.Input[str] commitment_plan_association_name: The name of the commitment plan association with the Cognitive Services Account
        """
        pulumi.set(__self__, "commitment_plan_name", commitment_plan_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if commitment_plan_association_name is not None:
            pulumi.set(__self__, "commitment_plan_association_name", commitment_plan_association_name)

    @property
    @pulumi.getter(name="commitmentPlanName")
    def commitment_plan_name(self) -> pulumi.Input[str]:
        """
        The name of the commitmentPlan associated with the Cognitive Services Account
        """
        return pulumi.get(self, "commitment_plan_name")

    @commitment_plan_name.setter
    def commitment_plan_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "commitment_plan_name", value)

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
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Azure resource id of the account.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="commitmentPlanAssociationName")
    def commitment_plan_association_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the commitment plan association with the Cognitive Services Account
        """
        return pulumi.get(self, "commitment_plan_association_name")

    @commitment_plan_association_name.setter
    def commitment_plan_association_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "commitment_plan_association_name", value)


class CommitmentPlanAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 commitment_plan_association_name: Optional[pulumi.Input[str]] = None,
                 commitment_plan_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The commitment plan association.
        Azure REST API version: 2023-05-01.

        Other available API versions: 2023-10-01-preview, 2024-04-01-preview, 2024-06-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The Azure resource id of the account.
        :param pulumi.Input[str] commitment_plan_association_name: The name of the commitment plan association with the Cognitive Services Account
        :param pulumi.Input[str] commitment_plan_name: The name of the commitmentPlan associated with the Cognitive Services Account
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CommitmentPlanAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The commitment plan association.
        Azure REST API version: 2023-05-01.

        Other available API versions: 2023-10-01-preview, 2024-04-01-preview, 2024-06-01-preview.

        :param str resource_name: The name of the resource.
        :param CommitmentPlanAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CommitmentPlanAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 commitment_plan_association_name: Optional[pulumi.Input[str]] = None,
                 commitment_plan_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CommitmentPlanAssociationArgs.__new__(CommitmentPlanAssociationArgs)

            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["commitment_plan_association_name"] = commitment_plan_association_name
            if commitment_plan_name is None and not opts.urn:
                raise TypeError("Missing required property 'commitment_plan_name'")
            __props__.__dict__["commitment_plan_name"] = commitment_plan_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cognitiveservices/v20221201:CommitmentPlanAssociation"), pulumi.Alias(type_="azure-native:cognitiveservices/v20230501:CommitmentPlanAssociation"), pulumi.Alias(type_="azure-native:cognitiveservices/v20231001preview:CommitmentPlanAssociation"), pulumi.Alias(type_="azure-native:cognitiveservices/v20240401preview:CommitmentPlanAssociation"), pulumi.Alias(type_="azure-native:cognitiveservices/v20240601preview:CommitmentPlanAssociation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CommitmentPlanAssociation, __self__).__init__(
            'azure-native:cognitiveservices:CommitmentPlanAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CommitmentPlanAssociation':
        """
        Get an existing CommitmentPlanAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CommitmentPlanAssociationArgs.__new__(CommitmentPlanAssociationArgs)

        __props__.__dict__["account_id"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return CommitmentPlanAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[str]]:
        """
        The Azure resource id of the account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Resource Etag.
        """
        return pulumi.get(self, "etag")

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
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

