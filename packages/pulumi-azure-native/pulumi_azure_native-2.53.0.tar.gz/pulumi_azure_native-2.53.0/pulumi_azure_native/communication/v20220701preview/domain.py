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
from ._enums import *

__all__ = ['DomainArgs', 'Domain']

@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *,
                 domain_management: pulumi.Input[Union[str, 'DomainManagement']],
                 email_service_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 domain_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_engagement_tracking: Optional[pulumi.Input[Union[str, 'UserEngagementTracking']]] = None,
                 valid_sender_usernames: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Domain resource.
        :param pulumi.Input[Union[str, 'DomainManagement']] domain_management: Describes how a Domains resource is being managed.
        :param pulumi.Input[str] email_service_name: The name of the EmailService resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] domain_name: The name of the Domains resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'UserEngagementTracking']] user_engagement_tracking: Describes whether user engagement tracking is enabled or disabled.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] valid_sender_usernames: Collection of valid sender usernames. This is a key-value pair where key=username and value=display name.
        """
        pulumi.set(__self__, "domain_management", domain_management)
        pulumi.set(__self__, "email_service_name", email_service_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if user_engagement_tracking is not None:
            pulumi.set(__self__, "user_engagement_tracking", user_engagement_tracking)
        if valid_sender_usernames is not None:
            pulumi.set(__self__, "valid_sender_usernames", valid_sender_usernames)

    @property
    @pulumi.getter(name="domainManagement")
    def domain_management(self) -> pulumi.Input[Union[str, 'DomainManagement']]:
        """
        Describes how a Domains resource is being managed.
        """
        return pulumi.get(self, "domain_management")

    @domain_management.setter
    def domain_management(self, value: pulumi.Input[Union[str, 'DomainManagement']]):
        pulumi.set(self, "domain_management", value)

    @property
    @pulumi.getter(name="emailServiceName")
    def email_service_name(self) -> pulumi.Input[str]:
        """
        The name of the EmailService resource.
        """
        return pulumi.get(self, "email_service_name")

    @email_service_name.setter
    def email_service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "email_service_name", value)

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
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Domains resource.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="userEngagementTracking")
    def user_engagement_tracking(self) -> Optional[pulumi.Input[Union[str, 'UserEngagementTracking']]]:
        """
        Describes whether user engagement tracking is enabled or disabled.
        """
        return pulumi.get(self, "user_engagement_tracking")

    @user_engagement_tracking.setter
    def user_engagement_tracking(self, value: Optional[pulumi.Input[Union[str, 'UserEngagementTracking']]]):
        pulumi.set(self, "user_engagement_tracking", value)

    @property
    @pulumi.getter(name="validSenderUsernames")
    def valid_sender_usernames(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Collection of valid sender usernames. This is a key-value pair where key=username and value=display name.
        """
        return pulumi.get(self, "valid_sender_usernames")

    @valid_sender_usernames.setter
    def valid_sender_usernames(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "valid_sender_usernames", value)


class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_management: Optional[pulumi.Input[Union[str, 'DomainManagement']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 email_service_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_engagement_tracking: Optional[pulumi.Input[Union[str, 'UserEngagementTracking']]] = None,
                 valid_sender_usernames: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A class representing a Domains resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'DomainManagement']] domain_management: Describes how a Domains resource is being managed.
        :param pulumi.Input[str] domain_name: The name of the Domains resource.
        :param pulumi.Input[str] email_service_name: The name of the EmailService resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Union[str, 'UserEngagementTracking']] user_engagement_tracking: Describes whether user engagement tracking is enabled or disabled.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] valid_sender_usernames: Collection of valid sender usernames. This is a key-value pair where key=username and value=display name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A class representing a Domains resource.

        :param str resource_name: The name of the resource.
        :param DomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_management: Optional[pulumi.Input[Union[str, 'DomainManagement']]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 email_service_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_engagement_tracking: Optional[pulumi.Input[Union[str, 'UserEngagementTracking']]] = None,
                 valid_sender_usernames: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainArgs.__new__(DomainArgs)

            if domain_management is None and not opts.urn:
                raise TypeError("Missing required property 'domain_management'")
            __props__.__dict__["domain_management"] = domain_management
            __props__.__dict__["domain_name"] = domain_name
            if email_service_name is None and not opts.urn:
                raise TypeError("Missing required property 'email_service_name'")
            __props__.__dict__["email_service_name"] = email_service_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["user_engagement_tracking"] = user_engagement_tracking
            __props__.__dict__["valid_sender_usernames"] = valid_sender_usernames
            __props__.__dict__["data_location"] = None
            __props__.__dict__["from_sender_domain"] = None
            __props__.__dict__["mail_from_sender_domain"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["verification_records"] = None
            __props__.__dict__["verification_states"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:communication:Domain"), pulumi.Alias(type_="azure-native:communication/v20211001preview:Domain"), pulumi.Alias(type_="azure-native:communication/v20230301preview:Domain"), pulumi.Alias(type_="azure-native:communication/v20230331:Domain"), pulumi.Alias(type_="azure-native:communication/v20230401:Domain"), pulumi.Alias(type_="azure-native:communication/v20230401preview:Domain"), pulumi.Alias(type_="azure-native:communication/v20230601preview:Domain")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Domain, __self__).__init__(
            'azure-native:communication/v20220701preview:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DomainArgs.__new__(DomainArgs)

        __props__.__dict__["data_location"] = None
        __props__.__dict__["domain_management"] = None
        __props__.__dict__["from_sender_domain"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mail_from_sender_domain"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_engagement_tracking"] = None
        __props__.__dict__["valid_sender_usernames"] = None
        __props__.__dict__["verification_records"] = None
        __props__.__dict__["verification_states"] = None
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dataLocation")
    def data_location(self) -> pulumi.Output[str]:
        """
        The location where the Domains resource data is stored at rest.
        """
        return pulumi.get(self, "data_location")

    @property
    @pulumi.getter(name="domainManagement")
    def domain_management(self) -> pulumi.Output[str]:
        """
        Describes how a Domains resource is being managed.
        """
        return pulumi.get(self, "domain_management")

    @property
    @pulumi.getter(name="fromSenderDomain")
    def from_sender_domain(self) -> pulumi.Output[str]:
        """
        P2 sender domain that is displayed to the email recipients [RFC 5322].
        """
        return pulumi.get(self, "from_sender_domain")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mailFromSenderDomain")
    def mail_from_sender_domain(self) -> pulumi.Output[str]:
        """
        P1 sender domain that is present on the email envelope [RFC 5321].
        """
        return pulumi.get(self, "mail_from_sender_domain")

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

    @property
    @pulumi.getter(name="userEngagementTracking")
    def user_engagement_tracking(self) -> pulumi.Output[Optional[str]]:
        """
        Describes whether user engagement tracking is enabled or disabled.
        """
        return pulumi.get(self, "user_engagement_tracking")

    @property
    @pulumi.getter(name="validSenderUsernames")
    def valid_sender_usernames(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Collection of valid sender usernames. This is a key-value pair where key=username and value=display name.
        """
        return pulumi.get(self, "valid_sender_usernames")

    @property
    @pulumi.getter(name="verificationRecords")
    def verification_records(self) -> pulumi.Output['outputs.DomainPropertiesResponseVerificationRecords']:
        """
        List of DnsRecord
        """
        return pulumi.get(self, "verification_records")

    @property
    @pulumi.getter(name="verificationStates")
    def verification_states(self) -> pulumi.Output['outputs.DomainPropertiesResponseVerificationStates']:
        """
        List of VerificationStatusRecord
        """
        return pulumi.get(self, "verification_states")

