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

__all__ = [
    'GetExternalNetworkResult',
    'AwaitableGetExternalNetworkResult',
    'get_external_network',
    'get_external_network_output',
]

@pulumi.output_type
class GetExternalNetworkResult:
    """
    Defines the ExternalNetwork item.
    """
    def __init__(__self__, administrative_state=None, annotation=None, disabled_on_resources=None, export_route_policy_id=None, id=None, import_route_policy_id=None, name=None, network_to_network_interconnect_id=None, option_a_properties=None, option_b_properties=None, peering_option=None, provisioning_state=None, system_data=None, type=None):
        if administrative_state and not isinstance(administrative_state, str):
            raise TypeError("Expected argument 'administrative_state' to be a str")
        pulumi.set(__self__, "administrative_state", administrative_state)
        if annotation and not isinstance(annotation, str):
            raise TypeError("Expected argument 'annotation' to be a str")
        pulumi.set(__self__, "annotation", annotation)
        if disabled_on_resources and not isinstance(disabled_on_resources, list):
            raise TypeError("Expected argument 'disabled_on_resources' to be a list")
        pulumi.set(__self__, "disabled_on_resources", disabled_on_resources)
        if export_route_policy_id and not isinstance(export_route_policy_id, str):
            raise TypeError("Expected argument 'export_route_policy_id' to be a str")
        pulumi.set(__self__, "export_route_policy_id", export_route_policy_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if import_route_policy_id and not isinstance(import_route_policy_id, str):
            raise TypeError("Expected argument 'import_route_policy_id' to be a str")
        pulumi.set(__self__, "import_route_policy_id", import_route_policy_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_to_network_interconnect_id and not isinstance(network_to_network_interconnect_id, str):
            raise TypeError("Expected argument 'network_to_network_interconnect_id' to be a str")
        pulumi.set(__self__, "network_to_network_interconnect_id", network_to_network_interconnect_id)
        if option_a_properties and not isinstance(option_a_properties, dict):
            raise TypeError("Expected argument 'option_a_properties' to be a dict")
        pulumi.set(__self__, "option_a_properties", option_a_properties)
        if option_b_properties and not isinstance(option_b_properties, dict):
            raise TypeError("Expected argument 'option_b_properties' to be a dict")
        pulumi.set(__self__, "option_b_properties", option_b_properties)
        if peering_option and not isinstance(peering_option, str):
            raise TypeError("Expected argument 'peering_option' to be a str")
        pulumi.set(__self__, "peering_option", peering_option)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="administrativeState")
    def administrative_state(self) -> str:
        """
        AdministrativeState of the externalNetwork. Example: Enabled | Disabled.
        """
        return pulumi.get(self, "administrative_state")

    @property
    @pulumi.getter
    def annotation(self) -> Optional[str]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter(name="disabledOnResources")
    def disabled_on_resources(self) -> Sequence[str]:
        """
        List of resources the externalNetwork is disabled on. Can be either entire NetworkFabric or NetworkRack.
        """
        return pulumi.get(self, "disabled_on_resources")

    @property
    @pulumi.getter(name="exportRoutePolicyId")
    def export_route_policy_id(self) -> Optional[str]:
        """
        ARM resource ID of exportRoutePolicy.
        """
        return pulumi.get(self, "export_route_policy_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="importRoutePolicyId")
    def import_route_policy_id(self) -> Optional[str]:
        """
        ARM resource ID of importRoutePolicy.
        """
        return pulumi.get(self, "import_route_policy_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkToNetworkInterconnectId")
    def network_to_network_interconnect_id(self) -> str:
        """
        Gets the networkToNetworkInterconnectId of the resource.
        """
        return pulumi.get(self, "network_to_network_interconnect_id")

    @property
    @pulumi.getter(name="optionAProperties")
    def option_a_properties(self) -> Optional['outputs.ExternalNetworkPropertiesResponseOptionAProperties']:
        """
        option A properties object
        """
        return pulumi.get(self, "option_a_properties")

    @property
    @pulumi.getter(name="optionBProperties")
    def option_b_properties(self) -> Optional['outputs.OptionBPropertiesResponse']:
        """
        option B properties object
        """
        return pulumi.get(self, "option_b_properties")

    @property
    @pulumi.getter(name="peeringOption")
    def peering_option(self) -> str:
        """
        Peering option list.
        """
        return pulumi.get(self, "peering_option")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets the provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

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


class AwaitableGetExternalNetworkResult(GetExternalNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExternalNetworkResult(
            administrative_state=self.administrative_state,
            annotation=self.annotation,
            disabled_on_resources=self.disabled_on_resources,
            export_route_policy_id=self.export_route_policy_id,
            id=self.id,
            import_route_policy_id=self.import_route_policy_id,
            name=self.name,
            network_to_network_interconnect_id=self.network_to_network_interconnect_id,
            option_a_properties=self.option_a_properties,
            option_b_properties=self.option_b_properties,
            peering_option=self.peering_option,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_external_network(external_network_name: Optional[str] = None,
                         l3_isolation_domain_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExternalNetworkResult:
    """
    Implements ExternalNetworks GET method.
    Azure REST API version: 2023-02-01-preview.

    Other available API versions: 2023-06-15.


    :param str external_network_name: Name of the ExternalNetwork
    :param str l3_isolation_domain_name: Name of the L3IsolationDomain
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['externalNetworkName'] = external_network_name
    __args__['l3IsolationDomainName'] = l3_isolation_domain_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetworkfabric:getExternalNetwork', __args__, opts=opts, typ=GetExternalNetworkResult).value

    return AwaitableGetExternalNetworkResult(
        administrative_state=pulumi.get(__ret__, 'administrative_state'),
        annotation=pulumi.get(__ret__, 'annotation'),
        disabled_on_resources=pulumi.get(__ret__, 'disabled_on_resources'),
        export_route_policy_id=pulumi.get(__ret__, 'export_route_policy_id'),
        id=pulumi.get(__ret__, 'id'),
        import_route_policy_id=pulumi.get(__ret__, 'import_route_policy_id'),
        name=pulumi.get(__ret__, 'name'),
        network_to_network_interconnect_id=pulumi.get(__ret__, 'network_to_network_interconnect_id'),
        option_a_properties=pulumi.get(__ret__, 'option_a_properties'),
        option_b_properties=pulumi.get(__ret__, 'option_b_properties'),
        peering_option=pulumi.get(__ret__, 'peering_option'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_external_network)
def get_external_network_output(external_network_name: Optional[pulumi.Input[str]] = None,
                                l3_isolation_domain_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExternalNetworkResult]:
    """
    Implements ExternalNetworks GET method.
    Azure REST API version: 2023-02-01-preview.

    Other available API versions: 2023-06-15.


    :param str external_network_name: Name of the ExternalNetwork
    :param str l3_isolation_domain_name: Name of the L3IsolationDomain
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
