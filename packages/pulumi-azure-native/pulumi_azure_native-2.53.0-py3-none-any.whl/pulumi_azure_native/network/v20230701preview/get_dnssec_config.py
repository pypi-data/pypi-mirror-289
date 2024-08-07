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
    'GetDnssecConfigResult',
    'AwaitableGetDnssecConfigResult',
    'get_dnssec_config',
    'get_dnssec_config_output',
]

@pulumi.output_type
class GetDnssecConfigResult:
    """
    Represents the DNSSEC configuration.
    """
    def __init__(__self__, etag=None, id=None, name=None, provisioning_state=None, signing_keys=None, system_data=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if signing_keys and not isinstance(signing_keys, list):
            raise TypeError("Expected argument 'signing_keys' to be a list")
        pulumi.set(__self__, "signing_keys", signing_keys)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        The etag of the DNSSEC configuration.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of the DNSSEC configuration.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the DNSSEC configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning State of the DNSSEC configuration.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="signingKeys")
    def signing_keys(self) -> Sequence['outputs.SigningKeyResponse']:
        """
        The list of signing keys.
        """
        return pulumi.get(self, "signing_keys")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the DNSSEC configuration.
        """
        return pulumi.get(self, "type")


class AwaitableGetDnssecConfigResult(GetDnssecConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDnssecConfigResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            signing_keys=self.signing_keys,
            system_data=self.system_data,
            type=self.type)


def get_dnssec_config(resource_group_name: Optional[str] = None,
                      zone_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDnssecConfigResult:
    """
    Gets the DNSSEC configuration.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str zone_name: The name of the DNS zone (without a terminating dot).
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['zoneName'] = zone_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230701preview:getDnssecConfig', __args__, opts=opts, typ=GetDnssecConfigResult).value

    return AwaitableGetDnssecConfigResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        signing_keys=pulumi.get(__ret__, 'signing_keys'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_dnssec_config)
def get_dnssec_config_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                             zone_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDnssecConfigResult]:
    """
    Gets the DNSSEC configuration.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str zone_name: The name of the DNS zone (without a terminating dot).
    """
    ...
