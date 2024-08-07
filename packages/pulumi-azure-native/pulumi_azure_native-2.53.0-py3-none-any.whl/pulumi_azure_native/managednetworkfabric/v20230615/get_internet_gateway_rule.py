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
    'GetInternetGatewayRuleResult',
    'AwaitableGetInternetGatewayRuleResult',
    'get_internet_gateway_rule',
    'get_internet_gateway_rule_output',
]

@pulumi.output_type
class GetInternetGatewayRuleResult:
    """
    The Internet Gateway Rule resource definition.
    """
    def __init__(__self__, annotation=None, id=None, internet_gateway_ids=None, location=None, name=None, provisioning_state=None, rule_properties=None, system_data=None, tags=None, type=None):
        if annotation and not isinstance(annotation, str):
            raise TypeError("Expected argument 'annotation' to be a str")
        pulumi.set(__self__, "annotation", annotation)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if internet_gateway_ids and not isinstance(internet_gateway_ids, list):
            raise TypeError("Expected argument 'internet_gateway_ids' to be a list")
        pulumi.set(__self__, "internet_gateway_ids", internet_gateway_ids)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if rule_properties and not isinstance(rule_properties, dict):
            raise TypeError("Expected argument 'rule_properties' to be a dict")
        pulumi.set(__self__, "rule_properties", rule_properties)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def annotation(self) -> Optional[str]:
        """
        Switch configuration description.
        """
        return pulumi.get(self, "annotation")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="internetGatewayIds")
    def internet_gateway_ids(self) -> Sequence[str]:
        """
        List of Internet Gateway resource Id.
        """
        return pulumi.get(self, "internet_gateway_ids")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="ruleProperties")
    def rule_properties(self) -> 'outputs.RulePropertiesResponse':
        """
        Rules for the InternetGateways
        """
        return pulumi.get(self, "rule_properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetInternetGatewayRuleResult(GetInternetGatewayRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInternetGatewayRuleResult(
            annotation=self.annotation,
            id=self.id,
            internet_gateway_ids=self.internet_gateway_ids,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            rule_properties=self.rule_properties,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_internet_gateway_rule(internet_gateway_rule_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInternetGatewayRuleResult:
    """
    Gets an Internet Gateway Rule resource.


    :param str internet_gateway_rule_name: Name of the Internet Gateway rule.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['internetGatewayRuleName'] = internet_gateway_rule_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:managednetworkfabric/v20230615:getInternetGatewayRule', __args__, opts=opts, typ=GetInternetGatewayRuleResult).value

    return AwaitableGetInternetGatewayRuleResult(
        annotation=pulumi.get(__ret__, 'annotation'),
        id=pulumi.get(__ret__, 'id'),
        internet_gateway_ids=pulumi.get(__ret__, 'internet_gateway_ids'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        rule_properties=pulumi.get(__ret__, 'rule_properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_internet_gateway_rule)
def get_internet_gateway_rule_output(internet_gateway_rule_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInternetGatewayRuleResult]:
    """
    Gets an Internet Gateway Rule resource.


    :param str internet_gateway_rule_name: Name of the Internet Gateway rule.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
