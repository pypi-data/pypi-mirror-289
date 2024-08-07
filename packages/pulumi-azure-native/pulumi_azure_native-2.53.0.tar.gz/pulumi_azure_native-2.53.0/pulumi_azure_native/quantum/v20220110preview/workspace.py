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

__all__ = ['WorkspaceArgs', 'Workspace']

@pulumi.input_type
class WorkspaceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 identity: Optional[pulumi.Input['QuantumWorkspaceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 providers: Optional[pulumi.Input[Sequence[pulumi.Input['ProviderArgs']]]] = None,
                 storage_account: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Workspace resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['QuantumWorkspaceIdentityArgs'] identity: Managed Identity information.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Sequence[pulumi.Input['ProviderArgs']]] providers: List of Providers selected for this Workspace
        :param pulumi.Input[str] storage_account: ARM Resource Id of the storage account associated with this workspace.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] workspace_name: The name of the quantum workspace resource.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if providers is not None:
            pulumi.set(__self__, "providers", providers)
        if storage_account is not None:
            pulumi.set(__self__, "storage_account", storage_account)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if workspace_name is not None:
            pulumi.set(__self__, "workspace_name", workspace_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['QuantumWorkspaceIdentityArgs']]:
        """
        Managed Identity information.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['QuantumWorkspaceIdentityArgs']]):
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
    @pulumi.getter
    def providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProviderArgs']]]]:
        """
        List of Providers selected for this Workspace
        """
        return pulumi.get(self, "providers")

    @providers.setter
    def providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProviderArgs']]]]):
        pulumi.set(self, "providers", value)

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> Optional[pulumi.Input[str]]:
        """
        ARM Resource Id of the storage account associated with this workspace.
        """
        return pulumi.get(self, "storage_account")

    @storage_account.setter
    def storage_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account", value)

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
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the quantum workspace resource.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_name", value)


class Workspace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[Union['QuantumWorkspaceIdentityArgs', 'QuantumWorkspaceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 providers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ProviderArgs', 'ProviderArgsDict']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The resource proxy definition object for quantum workspace.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['QuantumWorkspaceIdentityArgs', 'QuantumWorkspaceIdentityArgsDict']] identity: Managed Identity information.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Sequence[pulumi.Input[Union['ProviderArgs', 'ProviderArgsDict']]]] providers: List of Providers selected for this Workspace
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] storage_account: ARM Resource Id of the storage account associated with this workspace.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] workspace_name: The name of the quantum workspace resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The resource proxy definition object for quantum workspace.

        :param str resource_name: The name of the resource.
        :param WorkspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[Union['QuantumWorkspaceIdentityArgs', 'QuantumWorkspaceIdentityArgsDict']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 providers: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ProviderArgs', 'ProviderArgsDict']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["providers"] = providers
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["storage_account"] = storage_account
            __props__.__dict__["tags"] = tags
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["endpoint_uri"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["usable"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:quantum:Workspace"), pulumi.Alias(type_="azure-native:quantum/v20191104preview:Workspace"), pulumi.Alias(type_="azure-native:quantum/v20231113preview:Workspace")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Workspace, __self__).__init__(
            'azure-native:quantum/v20220110preview:Workspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Workspace':
        """
        Get an existing Workspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

        __props__.__dict__["endpoint_uri"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["providers"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["storage_account"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["usable"] = None
        return Workspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="endpointUri")
    def endpoint_uri(self) -> pulumi.Output[str]:
        """
        The URI of the workspace endpoint.
        """
        return pulumi.get(self, "endpoint_uri")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.QuantumWorkspaceResponseIdentity']]:
        """
        Managed Identity information.
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
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def providers(self) -> pulumi.Output[Optional[Sequence['outputs.ProviderResponse']]]:
        """
        List of Providers selected for this Workspace
        """
        return pulumi.get(self, "providers")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning status field
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="storageAccount")
    def storage_account(self) -> pulumi.Output[Optional[str]]:
        """
        ARM Resource Id of the storage account associated with this workspace.
        """
        return pulumi.get(self, "storage_account")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        System metadata
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
    @pulumi.getter
    def usable(self) -> pulumi.Output[str]:
        """
        Whether the current workspace is ready to accept Jobs.
        """
        return pulumi.get(self, "usable")

