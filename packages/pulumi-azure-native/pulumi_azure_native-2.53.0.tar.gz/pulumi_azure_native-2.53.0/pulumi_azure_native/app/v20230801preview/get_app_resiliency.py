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
    'GetAppResiliencyResult',
    'AwaitableGetAppResiliencyResult',
    'get_app_resiliency',
    'get_app_resiliency_output',
]

@pulumi.output_type
class GetAppResiliencyResult:
    """
    Configuration to setup App Resiliency
    """
    def __init__(__self__, circuit_breaker_policy=None, http_connection_pool=None, http_retry_policy=None, id=None, name=None, system_data=None, tcp_connection_pool=None, tcp_retry_policy=None, timeout_policy=None, type=None):
        if circuit_breaker_policy and not isinstance(circuit_breaker_policy, dict):
            raise TypeError("Expected argument 'circuit_breaker_policy' to be a dict")
        pulumi.set(__self__, "circuit_breaker_policy", circuit_breaker_policy)
        if http_connection_pool and not isinstance(http_connection_pool, dict):
            raise TypeError("Expected argument 'http_connection_pool' to be a dict")
        pulumi.set(__self__, "http_connection_pool", http_connection_pool)
        if http_retry_policy and not isinstance(http_retry_policy, dict):
            raise TypeError("Expected argument 'http_retry_policy' to be a dict")
        pulumi.set(__self__, "http_retry_policy", http_retry_policy)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tcp_connection_pool and not isinstance(tcp_connection_pool, dict):
            raise TypeError("Expected argument 'tcp_connection_pool' to be a dict")
        pulumi.set(__self__, "tcp_connection_pool", tcp_connection_pool)
        if tcp_retry_policy and not isinstance(tcp_retry_policy, dict):
            raise TypeError("Expected argument 'tcp_retry_policy' to be a dict")
        pulumi.set(__self__, "tcp_retry_policy", tcp_retry_policy)
        if timeout_policy and not isinstance(timeout_policy, dict):
            raise TypeError("Expected argument 'timeout_policy' to be a dict")
        pulumi.set(__self__, "timeout_policy", timeout_policy)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="circuitBreakerPolicy")
    def circuit_breaker_policy(self) -> Optional['outputs.CircuitBreakerPolicyResponse']:
        """
        Policy that defines circuit breaker conditions
        """
        return pulumi.get(self, "circuit_breaker_policy")

    @property
    @pulumi.getter(name="httpConnectionPool")
    def http_connection_pool(self) -> Optional['outputs.HttpConnectionPoolResponse']:
        """
        Defines parameters for http connection pooling
        """
        return pulumi.get(self, "http_connection_pool")

    @property
    @pulumi.getter(name="httpRetryPolicy")
    def http_retry_policy(self) -> Optional['outputs.HttpRetryPolicyResponse']:
        """
        Policy that defines http request retry conditions
        """
        return pulumi.get(self, "http_retry_policy")

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
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tcpConnectionPool")
    def tcp_connection_pool(self) -> Optional['outputs.TcpConnectionPoolResponse']:
        """
        Defines parameters for tcp connection pooling
        """
        return pulumi.get(self, "tcp_connection_pool")

    @property
    @pulumi.getter(name="tcpRetryPolicy")
    def tcp_retry_policy(self) -> Optional['outputs.TcpRetryPolicyResponse']:
        """
        Policy that defines tcp request retry conditions
        """
        return pulumi.get(self, "tcp_retry_policy")

    @property
    @pulumi.getter(name="timeoutPolicy")
    def timeout_policy(self) -> Optional['outputs.TimeoutPolicyResponse']:
        """
        Policy to set request timeouts
        """
        return pulumi.get(self, "timeout_policy")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAppResiliencyResult(GetAppResiliencyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppResiliencyResult(
            circuit_breaker_policy=self.circuit_breaker_policy,
            http_connection_pool=self.http_connection_pool,
            http_retry_policy=self.http_retry_policy,
            id=self.id,
            name=self.name,
            system_data=self.system_data,
            tcp_connection_pool=self.tcp_connection_pool,
            tcp_retry_policy=self.tcp_retry_policy,
            timeout_policy=self.timeout_policy,
            type=self.type)


def get_app_resiliency(app_name: Optional[str] = None,
                       name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppResiliencyResult:
    """
    Get container app resiliency policy.


    :param str app_name: Name of the Container App.
    :param str name: Name of the resiliency policy.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['appName'] = app_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:app/v20230801preview:getAppResiliency', __args__, opts=opts, typ=GetAppResiliencyResult).value

    return AwaitableGetAppResiliencyResult(
        circuit_breaker_policy=pulumi.get(__ret__, 'circuit_breaker_policy'),
        http_connection_pool=pulumi.get(__ret__, 'http_connection_pool'),
        http_retry_policy=pulumi.get(__ret__, 'http_retry_policy'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tcp_connection_pool=pulumi.get(__ret__, 'tcp_connection_pool'),
        tcp_retry_policy=pulumi.get(__ret__, 'tcp_retry_policy'),
        timeout_policy=pulumi.get(__ret__, 'timeout_policy'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_app_resiliency)
def get_app_resiliency_output(app_name: Optional[pulumi.Input[str]] = None,
                              name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppResiliencyResult]:
    """
    Get container app resiliency policy.


    :param str app_name: Name of the Container App.
    :param str name: Name of the resiliency policy.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
