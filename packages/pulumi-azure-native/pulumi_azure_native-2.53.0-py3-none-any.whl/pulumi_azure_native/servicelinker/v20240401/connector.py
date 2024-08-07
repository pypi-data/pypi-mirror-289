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

__all__ = ['ConnectorArgs', 'Connector']

@pulumi.input_type
class ConnectorArgs:
    def __init__(__self__, *,
                 location: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 auth_info: Optional[pulumi.Input[Union['AccessKeyInfoBaseArgs', 'EasyAuthMicrosoftEntraIDAuthInfoArgs', 'SecretAuthInfoArgs', 'ServicePrincipalCertificateAuthInfoArgs', 'ServicePrincipalSecretAuthInfoArgs', 'SystemAssignedIdentityAuthInfoArgs', 'UserAccountAuthInfoArgs', 'UserAssignedIdentityAuthInfoArgs']]] = None,
                 client_type: Optional[pulumi.Input[Union[str, 'ClientType']]] = None,
                 configuration_info: Optional[pulumi.Input['ConfigurationInfoArgs']] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 public_network_solution: Optional[pulumi.Input['PublicNetworkSolutionArgs']] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input['SecretStoreArgs']] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 target_service: Optional[pulumi.Input[Union['AzureResourceArgs', 'ConfluentBootstrapServerArgs', 'ConfluentSchemaRegistryArgs', 'SelfHostedServerArgs']]] = None,
                 v_net_solution: Optional[pulumi.Input['VNetSolutionArgs']] = None):
        """
        The set of arguments for constructing a Connector resource.
        :param pulumi.Input[str] location: The name of Azure region.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union['AccessKeyInfoBaseArgs', 'EasyAuthMicrosoftEntraIDAuthInfoArgs', 'SecretAuthInfoArgs', 'ServicePrincipalCertificateAuthInfoArgs', 'ServicePrincipalSecretAuthInfoArgs', 'SystemAssignedIdentityAuthInfoArgs', 'UserAccountAuthInfoArgs', 'UserAssignedIdentityAuthInfoArgs']] auth_info: The authentication type.
        :param pulumi.Input[Union[str, 'ClientType']] client_type: The application client type
        :param pulumi.Input['ConfigurationInfoArgs'] configuration_info: The connection information consumed by applications, including secrets, connection strings.
        :param pulumi.Input[str] connector_name: The name of resource.
        :param pulumi.Input['PublicNetworkSolutionArgs'] public_network_solution: The network solution.
        :param pulumi.Input[str] scope: connection scope in source service.
        :param pulumi.Input['SecretStoreArgs'] secret_store: An option to store secret value in secure place
        :param pulumi.Input[str] subscription_id: The ID of the target subscription.
        :param pulumi.Input[Union['AzureResourceArgs', 'ConfluentBootstrapServerArgs', 'ConfluentSchemaRegistryArgs', 'SelfHostedServerArgs']] target_service: The target service properties
        :param pulumi.Input['VNetSolutionArgs'] v_net_solution: The VNet solution.
        """
        pulumi.set(__self__, "location", location)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if auth_info is not None:
            pulumi.set(__self__, "auth_info", auth_info)
        if client_type is not None:
            pulumi.set(__self__, "client_type", client_type)
        if configuration_info is not None:
            pulumi.set(__self__, "configuration_info", configuration_info)
        if connector_name is not None:
            pulumi.set(__self__, "connector_name", connector_name)
        if public_network_solution is not None:
            pulumi.set(__self__, "public_network_solution", public_network_solution)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if secret_store is not None:
            pulumi.set(__self__, "secret_store", secret_store)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)
        if target_service is not None:
            pulumi.set(__self__, "target_service", target_service)
        if v_net_solution is not None:
            pulumi.set(__self__, "v_net_solution", v_net_solution)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Input[str]:
        """
        The name of Azure region.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: pulumi.Input[str]):
        pulumi.set(self, "location", value)

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
    @pulumi.getter(name="authInfo")
    def auth_info(self) -> Optional[pulumi.Input[Union['AccessKeyInfoBaseArgs', 'EasyAuthMicrosoftEntraIDAuthInfoArgs', 'SecretAuthInfoArgs', 'ServicePrincipalCertificateAuthInfoArgs', 'ServicePrincipalSecretAuthInfoArgs', 'SystemAssignedIdentityAuthInfoArgs', 'UserAccountAuthInfoArgs', 'UserAssignedIdentityAuthInfoArgs']]]:
        """
        The authentication type.
        """
        return pulumi.get(self, "auth_info")

    @auth_info.setter
    def auth_info(self, value: Optional[pulumi.Input[Union['AccessKeyInfoBaseArgs', 'EasyAuthMicrosoftEntraIDAuthInfoArgs', 'SecretAuthInfoArgs', 'ServicePrincipalCertificateAuthInfoArgs', 'ServicePrincipalSecretAuthInfoArgs', 'SystemAssignedIdentityAuthInfoArgs', 'UserAccountAuthInfoArgs', 'UserAssignedIdentityAuthInfoArgs']]]):
        pulumi.set(self, "auth_info", value)

    @property
    @pulumi.getter(name="clientType")
    def client_type(self) -> Optional[pulumi.Input[Union[str, 'ClientType']]]:
        """
        The application client type
        """
        return pulumi.get(self, "client_type")

    @client_type.setter
    def client_type(self, value: Optional[pulumi.Input[Union[str, 'ClientType']]]):
        pulumi.set(self, "client_type", value)

    @property
    @pulumi.getter(name="configurationInfo")
    def configuration_info(self) -> Optional[pulumi.Input['ConfigurationInfoArgs']]:
        """
        The connection information consumed by applications, including secrets, connection strings.
        """
        return pulumi.get(self, "configuration_info")

    @configuration_info.setter
    def configuration_info(self, value: Optional[pulumi.Input['ConfigurationInfoArgs']]):
        pulumi.set(self, "configuration_info", value)

    @property
    @pulumi.getter(name="connectorName")
    def connector_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of resource.
        """
        return pulumi.get(self, "connector_name")

    @connector_name.setter
    def connector_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connector_name", value)

    @property
    @pulumi.getter(name="publicNetworkSolution")
    def public_network_solution(self) -> Optional[pulumi.Input['PublicNetworkSolutionArgs']]:
        """
        The network solution.
        """
        return pulumi.get(self, "public_network_solution")

    @public_network_solution.setter
    def public_network_solution(self, value: Optional[pulumi.Input['PublicNetworkSolutionArgs']]):
        pulumi.set(self, "public_network_solution", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        connection scope in source service.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> Optional[pulumi.Input['SecretStoreArgs']]:
        """
        An option to store secret value in secure place
        """
        return pulumi.get(self, "secret_store")

    @secret_store.setter
    def secret_store(self, value: Optional[pulumi.Input['SecretStoreArgs']]):
        pulumi.set(self, "secret_store", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the target subscription.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter(name="targetService")
    def target_service(self) -> Optional[pulumi.Input[Union['AzureResourceArgs', 'ConfluentBootstrapServerArgs', 'ConfluentSchemaRegistryArgs', 'SelfHostedServerArgs']]]:
        """
        The target service properties
        """
        return pulumi.get(self, "target_service")

    @target_service.setter
    def target_service(self, value: Optional[pulumi.Input[Union['AzureResourceArgs', 'ConfluentBootstrapServerArgs', 'ConfluentSchemaRegistryArgs', 'SelfHostedServerArgs']]]):
        pulumi.set(self, "target_service", value)

    @property
    @pulumi.getter(name="vNetSolution")
    def v_net_solution(self) -> Optional[pulumi.Input['VNetSolutionArgs']]:
        """
        The VNet solution.
        """
        return pulumi.get(self, "v_net_solution")

    @v_net_solution.setter
    def v_net_solution(self, value: Optional[pulumi.Input['VNetSolutionArgs']]):
        pulumi.set(self, "v_net_solution", value)


class Connector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_info: Optional[pulumi.Input[Union[Union['AccessKeyInfoBaseArgs', 'AccessKeyInfoBaseArgsDict'], Union['EasyAuthMicrosoftEntraIDAuthInfoArgs', 'EasyAuthMicrosoftEntraIDAuthInfoArgsDict'], Union['SecretAuthInfoArgs', 'SecretAuthInfoArgsDict'], Union['ServicePrincipalCertificateAuthInfoArgs', 'ServicePrincipalCertificateAuthInfoArgsDict'], Union['ServicePrincipalSecretAuthInfoArgs', 'ServicePrincipalSecretAuthInfoArgsDict'], Union['SystemAssignedIdentityAuthInfoArgs', 'SystemAssignedIdentityAuthInfoArgsDict'], Union['UserAccountAuthInfoArgs', 'UserAccountAuthInfoArgsDict'], Union['UserAssignedIdentityAuthInfoArgs', 'UserAssignedIdentityAuthInfoArgsDict']]]] = None,
                 client_type: Optional[pulumi.Input[Union[str, 'ClientType']]] = None,
                 configuration_info: Optional[pulumi.Input[Union['ConfigurationInfoArgs', 'ConfigurationInfoArgsDict']]] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_solution: Optional[pulumi.Input[Union['PublicNetworkSolutionArgs', 'PublicNetworkSolutionArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input[Union['SecretStoreArgs', 'SecretStoreArgsDict']]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 target_service: Optional[pulumi.Input[Union[Union['AzureResourceArgs', 'AzureResourceArgsDict'], Union['ConfluentBootstrapServerArgs', 'ConfluentBootstrapServerArgsDict'], Union['ConfluentSchemaRegistryArgs', 'ConfluentSchemaRegistryArgsDict'], Union['SelfHostedServerArgs', 'SelfHostedServerArgsDict']]]] = None,
                 v_net_solution: Optional[pulumi.Input[Union['VNetSolutionArgs', 'VNetSolutionArgsDict']]] = None,
                 __props__=None):
        """
        Linker of source and target resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[Union['AccessKeyInfoBaseArgs', 'AccessKeyInfoBaseArgsDict'], Union['EasyAuthMicrosoftEntraIDAuthInfoArgs', 'EasyAuthMicrosoftEntraIDAuthInfoArgsDict'], Union['SecretAuthInfoArgs', 'SecretAuthInfoArgsDict'], Union['ServicePrincipalCertificateAuthInfoArgs', 'ServicePrincipalCertificateAuthInfoArgsDict'], Union['ServicePrincipalSecretAuthInfoArgs', 'ServicePrincipalSecretAuthInfoArgsDict'], Union['SystemAssignedIdentityAuthInfoArgs', 'SystemAssignedIdentityAuthInfoArgsDict'], Union['UserAccountAuthInfoArgs', 'UserAccountAuthInfoArgsDict'], Union['UserAssignedIdentityAuthInfoArgs', 'UserAssignedIdentityAuthInfoArgsDict']]] auth_info: The authentication type.
        :param pulumi.Input[Union[str, 'ClientType']] client_type: The application client type
        :param pulumi.Input[Union['ConfigurationInfoArgs', 'ConfigurationInfoArgsDict']] configuration_info: The connection information consumed by applications, including secrets, connection strings.
        :param pulumi.Input[str] connector_name: The name of resource.
        :param pulumi.Input[str] location: The name of Azure region.
        :param pulumi.Input[Union['PublicNetworkSolutionArgs', 'PublicNetworkSolutionArgsDict']] public_network_solution: The network solution.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] scope: connection scope in source service.
        :param pulumi.Input[Union['SecretStoreArgs', 'SecretStoreArgsDict']] secret_store: An option to store secret value in secure place
        :param pulumi.Input[str] subscription_id: The ID of the target subscription.
        :param pulumi.Input[Union[Union['AzureResourceArgs', 'AzureResourceArgsDict'], Union['ConfluentBootstrapServerArgs', 'ConfluentBootstrapServerArgsDict'], Union['ConfluentSchemaRegistryArgs', 'ConfluentSchemaRegistryArgsDict'], Union['SelfHostedServerArgs', 'SelfHostedServerArgsDict']]] target_service: The target service properties
        :param pulumi.Input[Union['VNetSolutionArgs', 'VNetSolutionArgsDict']] v_net_solution: The VNet solution.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConnectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Linker of source and target resource

        :param str resource_name: The name of the resource.
        :param ConnectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConnectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_info: Optional[pulumi.Input[Union[Union['AccessKeyInfoBaseArgs', 'AccessKeyInfoBaseArgsDict'], Union['EasyAuthMicrosoftEntraIDAuthInfoArgs', 'EasyAuthMicrosoftEntraIDAuthInfoArgsDict'], Union['SecretAuthInfoArgs', 'SecretAuthInfoArgsDict'], Union['ServicePrincipalCertificateAuthInfoArgs', 'ServicePrincipalCertificateAuthInfoArgsDict'], Union['ServicePrincipalSecretAuthInfoArgs', 'ServicePrincipalSecretAuthInfoArgsDict'], Union['SystemAssignedIdentityAuthInfoArgs', 'SystemAssignedIdentityAuthInfoArgsDict'], Union['UserAccountAuthInfoArgs', 'UserAccountAuthInfoArgsDict'], Union['UserAssignedIdentityAuthInfoArgs', 'UserAssignedIdentityAuthInfoArgsDict']]]] = None,
                 client_type: Optional[pulumi.Input[Union[str, 'ClientType']]] = None,
                 configuration_info: Optional[pulumi.Input[Union['ConfigurationInfoArgs', 'ConfigurationInfoArgsDict']]] = None,
                 connector_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_solution: Optional[pulumi.Input[Union['PublicNetworkSolutionArgs', 'PublicNetworkSolutionArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 secret_store: Optional[pulumi.Input[Union['SecretStoreArgs', 'SecretStoreArgsDict']]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 target_service: Optional[pulumi.Input[Union[Union['AzureResourceArgs', 'AzureResourceArgsDict'], Union['ConfluentBootstrapServerArgs', 'ConfluentBootstrapServerArgsDict'], Union['ConfluentSchemaRegistryArgs', 'ConfluentSchemaRegistryArgsDict'], Union['SelfHostedServerArgs', 'SelfHostedServerArgsDict']]]] = None,
                 v_net_solution: Optional[pulumi.Input[Union['VNetSolutionArgs', 'VNetSolutionArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConnectorArgs.__new__(ConnectorArgs)

            __props__.__dict__["auth_info"] = auth_info
            __props__.__dict__["client_type"] = client_type
            __props__.__dict__["configuration_info"] = configuration_info
            __props__.__dict__["connector_name"] = connector_name
            if location is None and not opts.urn:
                raise TypeError("Missing required property 'location'")
            __props__.__dict__["location"] = location
            __props__.__dict__["public_network_solution"] = public_network_solution
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scope"] = scope
            __props__.__dict__["secret_store"] = secret_store
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["target_service"] = target_service
            __props__.__dict__["v_net_solution"] = v_net_solution
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:servicelinker:Connector"), pulumi.Alias(type_="azure-native:servicelinker/v20221101preview:Connector"), pulumi.Alias(type_="azure-native:servicelinker/v20230401preview:Connector")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Connector, __self__).__init__(
            'azure-native:servicelinker/v20240401:Connector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Connector':
        """
        Get an existing Connector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConnectorArgs.__new__(ConnectorArgs)

        __props__.__dict__["auth_info"] = None
        __props__.__dict__["client_type"] = None
        __props__.__dict__["configuration_info"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_solution"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["secret_store"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["target_service"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["v_net_solution"] = None
        return Connector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="authInfo")
    def auth_info(self) -> pulumi.Output[Optional[Any]]:
        """
        The authentication type.
        """
        return pulumi.get(self, "auth_info")

    @property
    @pulumi.getter(name="clientType")
    def client_type(self) -> pulumi.Output[Optional[str]]:
        """
        The application client type
        """
        return pulumi.get(self, "client_type")

    @property
    @pulumi.getter(name="configurationInfo")
    def configuration_info(self) -> pulumi.Output[Optional['outputs.ConfigurationInfoResponse']]:
        """
        The connection information consumed by applications, including secrets, connection strings.
        """
        return pulumi.get(self, "configuration_info")

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
        The provisioning state. 
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkSolution")
    def public_network_solution(self) -> pulumi.Output[Optional['outputs.PublicNetworkSolutionResponse']]:
        """
        The network solution.
        """
        return pulumi.get(self, "public_network_solution")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        connection scope in source service.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="secretStore")
    def secret_store(self) -> pulumi.Output[Optional['outputs.SecretStoreResponse']]:
        """
        An option to store secret value in secure place
        """
        return pulumi.get(self, "secret_store")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetService")
    def target_service(self) -> pulumi.Output[Optional[Any]]:
        """
        The target service properties
        """
        return pulumi.get(self, "target_service")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vNetSolution")
    def v_net_solution(self) -> pulumi.Output[Optional['outputs.VNetSolutionResponse']]:
        """
        The VNet solution.
        """
        return pulumi.get(self, "v_net_solution")

