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
from ._inputs import *

__all__ = ['PoolArgs', 'Pool']

@pulumi.input_type
class PoolArgs:
    def __init__(__self__, *,
                 agent_profile: pulumi.Input[Union['StatefulArgs', 'StatelessAgentProfileArgs']],
                 dev_center_project_resource_id: pulumi.Input[str],
                 fabric_profile: pulumi.Input['VmssFabricProfileArgs'],
                 maximum_concurrency: pulumi.Input[int],
                 organization_profile: pulumi.Input[Union['AzureDevOpsOrganizationProfileArgs', 'GitHubOrganizationProfileArgs']],
                 resource_group_name: pulumi.Input[str],
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Pool resource.
        :param pulumi.Input[Union['StatefulArgs', 'StatelessAgentProfileArgs']] agent_profile: Defines how the machine will be handled once it executed a job.
        :param pulumi.Input[str] dev_center_project_resource_id: The resource id of the DevCenter Project the pool belongs to.
        :param pulumi.Input['VmssFabricProfileArgs'] fabric_profile: Defines the type of fabric the agent will run on.
        :param pulumi.Input[int] maximum_concurrency: Defines how many resources can there be created at any given time.
        :param pulumi.Input[Union['AzureDevOpsOrganizationProfileArgs', 'GitHubOrganizationProfileArgs']] organization_profile: Defines the organization in which the pool will be used.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: The managed service identities assigned to this resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] pool_name: Name of the pool. It needs to be globally unique.
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The status of the current operation.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "agent_profile", agent_profile)
        pulumi.set(__self__, "dev_center_project_resource_id", dev_center_project_resource_id)
        pulumi.set(__self__, "fabric_profile", fabric_profile)
        pulumi.set(__self__, "maximum_concurrency", maximum_concurrency)
        pulumi.set(__self__, "organization_profile", organization_profile)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if pool_name is not None:
            pulumi.set(__self__, "pool_name", pool_name)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="agentProfile")
    def agent_profile(self) -> pulumi.Input[Union['StatefulArgs', 'StatelessAgentProfileArgs']]:
        """
        Defines how the machine will be handled once it executed a job.
        """
        return pulumi.get(self, "agent_profile")

    @agent_profile.setter
    def agent_profile(self, value: pulumi.Input[Union['StatefulArgs', 'StatelessAgentProfileArgs']]):
        pulumi.set(self, "agent_profile", value)

    @property
    @pulumi.getter(name="devCenterProjectResourceId")
    def dev_center_project_resource_id(self) -> pulumi.Input[str]:
        """
        The resource id of the DevCenter Project the pool belongs to.
        """
        return pulumi.get(self, "dev_center_project_resource_id")

    @dev_center_project_resource_id.setter
    def dev_center_project_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "dev_center_project_resource_id", value)

    @property
    @pulumi.getter(name="fabricProfile")
    def fabric_profile(self) -> pulumi.Input['VmssFabricProfileArgs']:
        """
        Defines the type of fabric the agent will run on.
        """
        return pulumi.get(self, "fabric_profile")

    @fabric_profile.setter
    def fabric_profile(self, value: pulumi.Input['VmssFabricProfileArgs']):
        pulumi.set(self, "fabric_profile", value)

    @property
    @pulumi.getter(name="maximumConcurrency")
    def maximum_concurrency(self) -> pulumi.Input[int]:
        """
        Defines how many resources can there be created at any given time.
        """
        return pulumi.get(self, "maximum_concurrency")

    @maximum_concurrency.setter
    def maximum_concurrency(self, value: pulumi.Input[int]):
        pulumi.set(self, "maximum_concurrency", value)

    @property
    @pulumi.getter(name="organizationProfile")
    def organization_profile(self) -> pulumi.Input[Union['AzureDevOpsOrganizationProfileArgs', 'GitHubOrganizationProfileArgs']]:
        """
        Defines the organization in which the pool will be used.
        """
        return pulumi.get(self, "organization_profile")

    @organization_profile.setter
    def organization_profile(self, value: pulumi.Input[Union['AzureDevOpsOrganizationProfileArgs', 'GitHubOrganizationProfileArgs']]):
        pulumi.set(self, "organization_profile", value)

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
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        The managed service identities assigned to this resource.
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
    @pulumi.getter(name="poolName")
    def pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the pool. It needs to be globally unique.
        """
        return pulumi.get(self, "pool_name")

    @pool_name.setter
    def pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool_name", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'ProvisioningState']]]:
        """
        The status of the current operation.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'ProvisioningState']]]):
        pulumi.set(self, "provisioning_state", value)

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


class Pool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_profile: Optional[pulumi.Input[Union[Union['StatefulArgs', 'StatefulArgsDict'], Union['StatelessAgentProfileArgs', 'StatelessAgentProfileArgsDict']]]] = None,
                 dev_center_project_resource_id: Optional[pulumi.Input[str]] = None,
                 fabric_profile: Optional[pulumi.Input[Union['VmssFabricProfileArgs', 'VmssFabricProfileArgsDict']]] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maximum_concurrency: Optional[pulumi.Input[int]] = None,
                 organization_profile: Optional[pulumi.Input[Union[Union['AzureDevOpsOrganizationProfileArgs', 'AzureDevOpsOrganizationProfileArgsDict'], Union['GitHubOrganizationProfileArgs', 'GitHubOrganizationProfileArgsDict']]]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Concrete tracked resource types can be created by aliasing this type using a specific property type.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[Union['StatefulArgs', 'StatefulArgsDict'], Union['StatelessAgentProfileArgs', 'StatelessAgentProfileArgsDict']]] agent_profile: Defines how the machine will be handled once it executed a job.
        :param pulumi.Input[str] dev_center_project_resource_id: The resource id of the DevCenter Project the pool belongs to.
        :param pulumi.Input[Union['VmssFabricProfileArgs', 'VmssFabricProfileArgsDict']] fabric_profile: Defines the type of fabric the agent will run on.
        :param pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']] identity: The managed service identities assigned to this resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[int] maximum_concurrency: Defines how many resources can there be created at any given time.
        :param pulumi.Input[Union[Union['AzureDevOpsOrganizationProfileArgs', 'AzureDevOpsOrganizationProfileArgsDict'], Union['GitHubOrganizationProfileArgs', 'GitHubOrganizationProfileArgsDict']]] organization_profile: Defines the organization in which the pool will be used.
        :param pulumi.Input[str] pool_name: Name of the pool. It needs to be globally unique.
        :param pulumi.Input[Union[str, 'ProvisioningState']] provisioning_state: The status of the current operation.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Concrete tracked resource types can be created by aliasing this type using a specific property type.

        :param str resource_name: The name of the resource.
        :param PoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_profile: Optional[pulumi.Input[Union[Union['StatefulArgs', 'StatefulArgsDict'], Union['StatelessAgentProfileArgs', 'StatelessAgentProfileArgsDict']]]] = None,
                 dev_center_project_resource_id: Optional[pulumi.Input[str]] = None,
                 fabric_profile: Optional[pulumi.Input[Union['VmssFabricProfileArgs', 'VmssFabricProfileArgsDict']]] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 maximum_concurrency: Optional[pulumi.Input[int]] = None,
                 organization_profile: Optional[pulumi.Input[Union[Union['AzureDevOpsOrganizationProfileArgs', 'AzureDevOpsOrganizationProfileArgsDict'], Union['GitHubOrganizationProfileArgs', 'GitHubOrganizationProfileArgsDict']]]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[Union[str, 'ProvisioningState']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PoolArgs.__new__(PoolArgs)

            if agent_profile is None and not opts.urn:
                raise TypeError("Missing required property 'agent_profile'")
            __props__.__dict__["agent_profile"] = agent_profile
            if dev_center_project_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'dev_center_project_resource_id'")
            __props__.__dict__["dev_center_project_resource_id"] = dev_center_project_resource_id
            if fabric_profile is None and not opts.urn:
                raise TypeError("Missing required property 'fabric_profile'")
            __props__.__dict__["fabric_profile"] = fabric_profile
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            if maximum_concurrency is None and not opts.urn:
                raise TypeError("Missing required property 'maximum_concurrency'")
            __props__.__dict__["maximum_concurrency"] = maximum_concurrency
            if organization_profile is None and not opts.urn:
                raise TypeError("Missing required property 'organization_profile'")
            __props__.__dict__["organization_profile"] = organization_profile
            __props__.__dict__["pool_name"] = pool_name
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devopsinfrastructure:Pool"), pulumi.Alias(type_="azure-native:devopsinfrastructure/v20231030preview:Pool"), pulumi.Alias(type_="azure-native:devopsinfrastructure/v20240326preview:Pool"), pulumi.Alias(type_="azure-native:devopsinfrastructure/v20240404preview:Pool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Pool, __self__).__init__(
            'azure-native:devopsinfrastructure/v20231213preview:Pool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Pool':
        """
        Get an existing Pool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PoolArgs.__new__(PoolArgs)

        __props__.__dict__["agent_profile"] = None
        __props__.__dict__["dev_center_project_resource_id"] = None
        __props__.__dict__["fabric_profile"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["maximum_concurrency"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["organization_profile"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Pool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentProfile")
    def agent_profile(self) -> pulumi.Output[Any]:
        """
        Defines how the machine will be handled once it executed a job.
        """
        return pulumi.get(self, "agent_profile")

    @property
    @pulumi.getter(name="devCenterProjectResourceId")
    def dev_center_project_resource_id(self) -> pulumi.Output[str]:
        """
        The resource id of the DevCenter Project the pool belongs to.
        """
        return pulumi.get(self, "dev_center_project_resource_id")

    @property
    @pulumi.getter(name="fabricProfile")
    def fabric_profile(self) -> pulumi.Output['outputs.VmssFabricProfileResponse']:
        """
        Defines the type of fabric the agent will run on.
        """
        return pulumi.get(self, "fabric_profile")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        The managed service identities assigned to this resource.
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
    @pulumi.getter(name="maximumConcurrency")
    def maximum_concurrency(self) -> pulumi.Output[int]:
        """
        Defines how many resources can there be created at any given time.
        """
        return pulumi.get(self, "maximum_concurrency")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="organizationProfile")
    def organization_profile(self) -> pulumi.Output[Any]:
        """
        Defines the organization in which the pool will be used.
        """
        return pulumi.get(self, "organization_profile")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the current operation.
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

