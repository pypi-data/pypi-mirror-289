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
    'GetConnectedEnvironmentsDaprComponentResult',
    'AwaitableGetConnectedEnvironmentsDaprComponentResult',
    'get_connected_environments_dapr_component',
    'get_connected_environments_dapr_component_output',
]

@pulumi.output_type
class GetConnectedEnvironmentsDaprComponentResult:
    """
    Dapr Component.
    """
    def __init__(__self__, component_type=None, id=None, ignore_errors=None, init_timeout=None, metadata=None, name=None, scopes=None, secret_store_component=None, secrets=None, system_data=None, type=None, version=None):
        if component_type and not isinstance(component_type, str):
            raise TypeError("Expected argument 'component_type' to be a str")
        pulumi.set(__self__, "component_type", component_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ignore_errors and not isinstance(ignore_errors, bool):
            raise TypeError("Expected argument 'ignore_errors' to be a bool")
        pulumi.set(__self__, "ignore_errors", ignore_errors)
        if init_timeout and not isinstance(init_timeout, str):
            raise TypeError("Expected argument 'init_timeout' to be a str")
        pulumi.set(__self__, "init_timeout", init_timeout)
        if metadata and not isinstance(metadata, list):
            raise TypeError("Expected argument 'metadata' to be a list")
        pulumi.set(__self__, "metadata", metadata)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if scopes and not isinstance(scopes, list):
            raise TypeError("Expected argument 'scopes' to be a list")
        pulumi.set(__self__, "scopes", scopes)
        if secret_store_component and not isinstance(secret_store_component, str):
            raise TypeError("Expected argument 'secret_store_component' to be a str")
        pulumi.set(__self__, "secret_store_component", secret_store_component)
        if secrets and not isinstance(secrets, list):
            raise TypeError("Expected argument 'secrets' to be a list")
        pulumi.set(__self__, "secrets", secrets)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="componentType")
    def component_type(self) -> Optional[str]:
        """
        Component type
        """
        return pulumi.get(self, "component_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ignoreErrors")
    def ignore_errors(self) -> Optional[bool]:
        """
        Boolean describing if the component errors are ignores
        """
        return pulumi.get(self, "ignore_errors")

    @property
    @pulumi.getter(name="initTimeout")
    def init_timeout(self) -> Optional[str]:
        """
        Initialization timeout
        """
        return pulumi.get(self, "init_timeout")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Sequence['outputs.DaprMetadataResponse']]:
        """
        Component metadata
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[str]]:
        """
        Names of container apps that can use this Dapr component
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter(name="secretStoreComponent")
    def secret_store_component(self) -> Optional[str]:
        """
        Name of a Dapr component to retrieve component secrets from
        """
        return pulumi.get(self, "secret_store_component")

    @property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence['outputs.SecretResponse']]:
        """
        Collection of secrets used by a Dapr component
        """
        return pulumi.get(self, "secrets")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        Component version
        """
        return pulumi.get(self, "version")


class AwaitableGetConnectedEnvironmentsDaprComponentResult(GetConnectedEnvironmentsDaprComponentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectedEnvironmentsDaprComponentResult(
            component_type=self.component_type,
            id=self.id,
            ignore_errors=self.ignore_errors,
            init_timeout=self.init_timeout,
            metadata=self.metadata,
            name=self.name,
            scopes=self.scopes,
            secret_store_component=self.secret_store_component,
            secrets=self.secrets,
            system_data=self.system_data,
            type=self.type,
            version=self.version)


def get_connected_environments_dapr_component(component_name: Optional[str] = None,
                                              connected_environment_name: Optional[str] = None,
                                              resource_group_name: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectedEnvironmentsDaprComponentResult:
    """
    Dapr Component.


    :param str component_name: Name of the Dapr Component.
    :param str connected_environment_name: Name of the connected environment.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['componentName'] = component_name
    __args__['connectedEnvironmentName'] = connected_environment_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:app/v20230502preview:getConnectedEnvironmentsDaprComponent', __args__, opts=opts, typ=GetConnectedEnvironmentsDaprComponentResult).value

    return AwaitableGetConnectedEnvironmentsDaprComponentResult(
        component_type=pulumi.get(__ret__, 'component_type'),
        id=pulumi.get(__ret__, 'id'),
        ignore_errors=pulumi.get(__ret__, 'ignore_errors'),
        init_timeout=pulumi.get(__ret__, 'init_timeout'),
        metadata=pulumi.get(__ret__, 'metadata'),
        name=pulumi.get(__ret__, 'name'),
        scopes=pulumi.get(__ret__, 'scopes'),
        secret_store_component=pulumi.get(__ret__, 'secret_store_component'),
        secrets=pulumi.get(__ret__, 'secrets'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_connected_environments_dapr_component)
def get_connected_environments_dapr_component_output(component_name: Optional[pulumi.Input[str]] = None,
                                                     connected_environment_name: Optional[pulumi.Input[str]] = None,
                                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConnectedEnvironmentsDaprComponentResult]:
    """
    Dapr Component.


    :param str component_name: Name of the Dapr Component.
    :param str connected_environment_name: Name of the connected environment.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
