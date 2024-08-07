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
    'GetRaiBlocklistItemResult',
    'AwaitableGetRaiBlocklistItemResult',
    'get_rai_blocklist_item',
    'get_rai_blocklist_item_output',
]

@pulumi.output_type
class GetRaiBlocklistItemResult:
    """
    Cognitive Services RaiBlocklist Item.
    """
    def __init__(__self__, etag=None, id=None, name=None, properties=None, system_data=None, tags=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
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
    def etag(self) -> str:
        """
        Resource Etag.
        """
        return pulumi.get(self, "etag")

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
    def properties(self) -> 'outputs.RaiBlocklistItemPropertiesResponse':
        """
        Properties of Cognitive Services RaiBlocklist Item.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
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


class AwaitableGetRaiBlocklistItemResult(GetRaiBlocklistItemResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRaiBlocklistItemResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_rai_blocklist_item(account_name: Optional[str] = None,
                           rai_blocklist_item_name: Optional[str] = None,
                           rai_blocklist_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRaiBlocklistItemResult:
    """
    Gets the specified custom blocklist Item associated with the custom blocklist.


    :param str account_name: The name of Cognitive Services account.
    :param str rai_blocklist_item_name: The name of the RaiBlocklist Item associated with the custom blocklist
    :param str rai_blocklist_name: The name of the RaiBlocklist associated with the Cognitive Services Account
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['raiBlocklistItemName'] = rai_blocklist_item_name
    __args__['raiBlocklistName'] = rai_blocklist_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cognitiveservices/v20240601preview:getRaiBlocklistItem', __args__, opts=opts, typ=GetRaiBlocklistItemResult).value

    return AwaitableGetRaiBlocklistItemResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_rai_blocklist_item)
def get_rai_blocklist_item_output(account_name: Optional[pulumi.Input[str]] = None,
                                  rai_blocklist_item_name: Optional[pulumi.Input[str]] = None,
                                  rai_blocklist_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRaiBlocklistItemResult]:
    """
    Gets the specified custom blocklist Item associated with the custom blocklist.


    :param str account_name: The name of Cognitive Services account.
    :param str rai_blocklist_item_name: The name of the RaiBlocklist Item associated with the custom blocklist
    :param str rai_blocklist_name: The name of the RaiBlocklist associated with the Cognitive Services Account
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
