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

__all__ = [
    'GetBackendResult',
    'AwaitableGetBackendResult',
    'get_backend',
    'get_backend_output',
]

@pulumi.output_type
class GetBackendResult:
    """
    Backend details.
    """
    def __init__(__self__, circuit_breaker=None, credentials=None, description=None, id=None, name=None, pool=None, properties=None, protocol=None, proxy=None, resource_id=None, title=None, tls=None, type=None, url=None):
        if circuit_breaker and not isinstance(circuit_breaker, dict):
            raise TypeError("Expected argument 'circuit_breaker' to be a dict")
        pulumi.set(__self__, "circuit_breaker", circuit_breaker)
        if credentials and not isinstance(credentials, dict):
            raise TypeError("Expected argument 'credentials' to be a dict")
        pulumi.set(__self__, "credentials", credentials)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pool and not isinstance(pool, dict):
            raise TypeError("Expected argument 'pool' to be a dict")
        pulumi.set(__self__, "pool", pool)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if proxy and not isinstance(proxy, dict):
            raise TypeError("Expected argument 'proxy' to be a dict")
        pulumi.set(__self__, "proxy", proxy)
        if resource_id and not isinstance(resource_id, str):
            raise TypeError("Expected argument 'resource_id' to be a str")
        pulumi.set(__self__, "resource_id", resource_id)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if tls and not isinstance(tls, dict):
            raise TypeError("Expected argument 'tls' to be a dict")
        pulumi.set(__self__, "tls", tls)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="circuitBreaker")
    def circuit_breaker(self) -> Optional['outputs.BackendCircuitBreakerResponse']:
        """
        Backend Circuit Breaker Configuration
        """
        return pulumi.get(self, "circuit_breaker")

    @property
    @pulumi.getter
    def credentials(self) -> Optional['outputs.BackendCredentialsContractResponse']:
        """
        Backend Credentials Contract Properties
        """
        return pulumi.get(self, "credentials")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Backend Description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def pool(self) -> Optional['outputs.BackendBaseParametersResponsePool']:
        return pulumi.get(self, "pool")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.BackendPropertiesResponse':
        """
        Backend Properties contract
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        Backend communication protocol.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def proxy(self) -> Optional['outputs.BackendProxyContractResponse']:
        """
        Backend gateway Contract Properties
        """
        return pulumi.get(self, "proxy")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        """
        Management Uri of the Resource in External System. This URL can be the Arm Resource Id of Logic Apps, Function Apps or API Apps.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter
    def title(self) -> Optional[str]:
        """
        Backend Title.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def tls(self) -> Optional['outputs.BackendTlsPropertiesResponse']:
        """
        Backend TLS Properties
        """
        return pulumi.get(self, "tls")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def url(self) -> str:
        """
        Runtime Url of the Backend.
        """
        return pulumi.get(self, "url")


class AwaitableGetBackendResult(GetBackendResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBackendResult(
            circuit_breaker=self.circuit_breaker,
            credentials=self.credentials,
            description=self.description,
            id=self.id,
            name=self.name,
            pool=self.pool,
            properties=self.properties,
            protocol=self.protocol,
            proxy=self.proxy,
            resource_id=self.resource_id,
            title=self.title,
            tls=self.tls,
            type=self.type,
            url=self.url)


def get_backend(backend_id: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                service_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBackendResult:
    """
    Gets the details of the backend specified by its identifier.


    :param str backend_id: Identifier of the Backend entity. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['backendId'] = backend_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20230501preview:getBackend', __args__, opts=opts, typ=GetBackendResult).value

    return AwaitableGetBackendResult(
        circuit_breaker=pulumi.get(__ret__, 'circuit_breaker'),
        credentials=pulumi.get(__ret__, 'credentials'),
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        pool=pulumi.get(__ret__, 'pool'),
        properties=pulumi.get(__ret__, 'properties'),
        protocol=pulumi.get(__ret__, 'protocol'),
        proxy=pulumi.get(__ret__, 'proxy'),
        resource_id=pulumi.get(__ret__, 'resource_id'),
        title=pulumi.get(__ret__, 'title'),
        tls=pulumi.get(__ret__, 'tls'),
        type=pulumi.get(__ret__, 'type'),
        url=pulumi.get(__ret__, 'url'))


@_utilities.lift_output_func(get_backend)
def get_backend_output(backend_id: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       service_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBackendResult]:
    """
    Gets the details of the backend specified by its identifier.


    :param str backend_id: Identifier of the Backend entity. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
