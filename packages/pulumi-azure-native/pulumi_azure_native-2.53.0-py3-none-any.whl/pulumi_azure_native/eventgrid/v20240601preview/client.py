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

__all__ = ['ClientArgs', 'Client']

@pulumi.input_type
class ClientArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 attributes: Optional[Any] = None,
                 authentication_name: Optional[pulumi.Input[str]] = None,
                 client_certificate_authentication: Optional[pulumi.Input['ClientCertificateAuthenticationArgs']] = None,
                 client_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'ClientState']]] = None):
        """
        The set of arguments for constructing a Client resource.
        :param pulumi.Input[str] namespace_name: Name of the namespace.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param Any attributes: Attributes for the client. Supported values are int, bool, string, string[].
               Example:
               "attributes": { "room": "345", "floor": 12, "deviceTypes": ["Fan", "Light"] }
        :param pulumi.Input[str] authentication_name: The name presented by the client for authentication. The default value is the name of the resource.
        :param pulumi.Input['ClientCertificateAuthenticationArgs'] client_certificate_authentication: The client certificate authentication information.
        :param pulumi.Input[str] client_name: The client name.
        :param pulumi.Input[str] description: Description for the Client resource.
        :param pulumi.Input[Union[str, 'ClientState']] state: Indicates if the client is enabled or not. Default value is Enabled.
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
        if authentication_name is not None:
            pulumi.set(__self__, "authentication_name", authentication_name)
        if client_certificate_authentication is not None:
            pulumi.set(__self__, "client_certificate_authentication", client_certificate_authentication)
        if client_name is not None:
            pulumi.set(__self__, "client_name", client_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if state is None:
            state = 'Enabled'
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        Name of the namespace.
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def attributes(self) -> Optional[Any]:
        """
        Attributes for the client. Supported values are int, bool, string, string[].
        Example:
        "attributes": { "room": "345", "floor": 12, "deviceTypes": ["Fan", "Light"] }
        """
        return pulumi.get(self, "attributes")

    @attributes.setter
    def attributes(self, value: Optional[Any]):
        pulumi.set(self, "attributes", value)

    @property
    @pulumi.getter(name="authenticationName")
    def authentication_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name presented by the client for authentication. The default value is the name of the resource.
        """
        return pulumi.get(self, "authentication_name")

    @authentication_name.setter
    def authentication_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_name", value)

    @property
    @pulumi.getter(name="clientCertificateAuthentication")
    def client_certificate_authentication(self) -> Optional[pulumi.Input['ClientCertificateAuthenticationArgs']]:
        """
        The client certificate authentication information.
        """
        return pulumi.get(self, "client_certificate_authentication")

    @client_certificate_authentication.setter
    def client_certificate_authentication(self, value: Optional[pulumi.Input['ClientCertificateAuthenticationArgs']]):
        pulumi.set(self, "client_certificate_authentication", value)

    @property
    @pulumi.getter(name="clientName")
    def client_name(self) -> Optional[pulumi.Input[str]]:
        """
        The client name.
        """
        return pulumi.get(self, "client_name")

    @client_name.setter
    def client_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description for the Client resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'ClientState']]]:
        """
        Indicates if the client is enabled or not. Default value is Enabled.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'ClientState']]]):
        pulumi.set(self, "state", value)


class Client(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attributes: Optional[Any] = None,
                 authentication_name: Optional[pulumi.Input[str]] = None,
                 client_certificate_authentication: Optional[pulumi.Input[Union['ClientCertificateAuthenticationArgs', 'ClientCertificateAuthenticationArgsDict']]] = None,
                 client_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'ClientState']]] = None,
                 __props__=None):
        """
        The Client resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any attributes: Attributes for the client. Supported values are int, bool, string, string[].
               Example:
               "attributes": { "room": "345", "floor": 12, "deviceTypes": ["Fan", "Light"] }
        :param pulumi.Input[str] authentication_name: The name presented by the client for authentication. The default value is the name of the resource.
        :param pulumi.Input[Union['ClientCertificateAuthenticationArgs', 'ClientCertificateAuthenticationArgsDict']] client_certificate_authentication: The client certificate authentication information.
        :param pulumi.Input[str] client_name: The client name.
        :param pulumi.Input[str] description: Description for the Client resource.
        :param pulumi.Input[str] namespace_name: Name of the namespace.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[Union[str, 'ClientState']] state: Indicates if the client is enabled or not. Default value is Enabled.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClientArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Client resource.

        :param str resource_name: The name of the resource.
        :param ClientArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClientArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attributes: Optional[Any] = None,
                 authentication_name: Optional[pulumi.Input[str]] = None,
                 client_certificate_authentication: Optional[pulumi.Input[Union['ClientCertificateAuthenticationArgs', 'ClientCertificateAuthenticationArgsDict']]] = None,
                 client_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'ClientState']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClientArgs.__new__(ClientArgs)

            __props__.__dict__["attributes"] = attributes
            __props__.__dict__["authentication_name"] = authentication_name
            __props__.__dict__["client_certificate_authentication"] = client_certificate_authentication
            __props__.__dict__["client_name"] = client_name
            __props__.__dict__["description"] = description
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if state is None:
                state = 'Enabled'
            __props__.__dict__["state"] = state
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventgrid:Client"), pulumi.Alias(type_="azure-native:eventgrid/v20230601preview:Client"), pulumi.Alias(type_="azure-native:eventgrid/v20231215preview:Client")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Client, __self__).__init__(
            'azure-native:eventgrid/v20240601preview:Client',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Client':
        """
        Get an existing Client resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClientArgs.__new__(ClientArgs)

        __props__.__dict__["attributes"] = None
        __props__.__dict__["authentication_name"] = None
        __props__.__dict__["client_certificate_authentication"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Client(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def attributes(self) -> pulumi.Output[Optional[Any]]:
        """
        Attributes for the client. Supported values are int, bool, string, string[].
        Example:
        "attributes": { "room": "345", "floor": 12, "deviceTypes": ["Fan", "Light"] }
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="authenticationName")
    def authentication_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name presented by the client for authentication. The default value is the name of the resource.
        """
        return pulumi.get(self, "authentication_name")

    @property
    @pulumi.getter(name="clientCertificateAuthentication")
    def client_certificate_authentication(self) -> pulumi.Output[Optional['outputs.ClientCertificateAuthenticationResponse']]:
        """
        The client certificate authentication information.
        """
        return pulumi.get(self, "client_certificate_authentication")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description for the Client resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the Client resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates if the client is enabled or not. Default value is Enabled.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to the Client resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

