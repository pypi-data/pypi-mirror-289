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
    'GetRegistryModelContainerResult',
    'AwaitableGetRegistryModelContainerResult',
    'get_registry_model_container',
    'get_registry_model_container_output',
]

@pulumi.output_type
class GetRegistryModelContainerResult:
    """
    Azure Resource Manager resource envelope.
    """
    def __init__(__self__, id=None, model_container_properties=None, name=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if model_container_properties and not isinstance(model_container_properties, dict):
            raise TypeError("Expected argument 'model_container_properties' to be a dict")
        pulumi.set(__self__, "model_container_properties", model_container_properties)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="modelContainerProperties")
    def model_container_properties(self) -> 'outputs.ModelContainerResponse':
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "model_container_properties")

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
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetRegistryModelContainerResult(GetRegistryModelContainerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegistryModelContainerResult(
            id=self.id,
            model_container_properties=self.model_container_properties,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_registry_model_container(model_name: Optional[str] = None,
                                 registry_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegistryModelContainerResult:
    """
    Azure Resource Manager resource envelope.


    :param str model_name: Container name. This is case-sensitive.
    :param str registry_name: Name of Azure Machine Learning registry. This is case-insensitive
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['modelName'] = model_name
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20230601preview:getRegistryModelContainer', __args__, opts=opts, typ=GetRegistryModelContainerResult).value

    return AwaitableGetRegistryModelContainerResult(
        id=pulumi.get(__ret__, 'id'),
        model_container_properties=pulumi.get(__ret__, 'model_container_properties'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_registry_model_container)
def get_registry_model_container_output(model_name: Optional[pulumi.Input[str]] = None,
                                        registry_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRegistryModelContainerResult]:
    """
    Azure Resource Manager resource envelope.


    :param str model_name: Container name. This is case-sensitive.
    :param str registry_name: Name of Azure Machine Learning registry. This is case-insensitive
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
