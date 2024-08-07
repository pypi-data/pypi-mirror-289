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
    'GetCaCertificateResult',
    'AwaitableGetCaCertificateResult',
    'get_ca_certificate',
    'get_ca_certificate_output',
]

@pulumi.output_type
class GetCaCertificateResult:
    """
    The CA Certificate resource.
    """
    def __init__(__self__, description=None, encoded_certificate=None, expiry_time_in_utc=None, id=None, issue_time_in_utc=None, name=None, provisioning_state=None, system_data=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if encoded_certificate and not isinstance(encoded_certificate, str):
            raise TypeError("Expected argument 'encoded_certificate' to be a str")
        pulumi.set(__self__, "encoded_certificate", encoded_certificate)
        if expiry_time_in_utc and not isinstance(expiry_time_in_utc, str):
            raise TypeError("Expected argument 'expiry_time_in_utc' to be a str")
        pulumi.set(__self__, "expiry_time_in_utc", expiry_time_in_utc)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if issue_time_in_utc and not isinstance(issue_time_in_utc, str):
            raise TypeError("Expected argument 'issue_time_in_utc' to be a str")
        pulumi.set(__self__, "issue_time_in_utc", issue_time_in_utc)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
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
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description for the CA Certificate resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="encodedCertificate")
    def encoded_certificate(self) -> Optional[str]:
        """
        Base64 encoded PEM (Privacy Enhanced Mail) format certificate data.
        """
        return pulumi.get(self, "encoded_certificate")

    @property
    @pulumi.getter(name="expiryTimeInUtc")
    def expiry_time_in_utc(self) -> str:
        """
        Certificate expiry time in UTC. This is a read-only field.
        """
        return pulumi.get(self, "expiry_time_in_utc")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="issueTimeInUtc")
    def issue_time_in_utc(self) -> str:
        """
        Certificate issue time in UTC. This is a read-only field.
        """
        return pulumi.get(self, "issue_time_in_utc")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the CA Certificate resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to the CaCertificate resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetCaCertificateResult(GetCaCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCaCertificateResult(
            description=self.description,
            encoded_certificate=self.encoded_certificate,
            expiry_time_in_utc=self.expiry_time_in_utc,
            id=self.id,
            issue_time_in_utc=self.issue_time_in_utc,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_ca_certificate(ca_certificate_name: Optional[str] = None,
                       namespace_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCaCertificateResult:
    """
    Get properties of a CA certificate.


    :param str ca_certificate_name: Name of the CA certificate.
    :param str namespace_name: Name of the namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    __args__ = dict()
    __args__['caCertificateName'] = ca_certificate_name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventgrid/v20231215preview:getCaCertificate', __args__, opts=opts, typ=GetCaCertificateResult).value

    return AwaitableGetCaCertificateResult(
        description=pulumi.get(__ret__, 'description'),
        encoded_certificate=pulumi.get(__ret__, 'encoded_certificate'),
        expiry_time_in_utc=pulumi.get(__ret__, 'expiry_time_in_utc'),
        id=pulumi.get(__ret__, 'id'),
        issue_time_in_utc=pulumi.get(__ret__, 'issue_time_in_utc'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_ca_certificate)
def get_ca_certificate_output(ca_certificate_name: Optional[pulumi.Input[str]] = None,
                              namespace_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCaCertificateResult]:
    """
    Get properties of a CA certificate.


    :param str ca_certificate_name: Name of the CA certificate.
    :param str namespace_name: Name of the namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    ...
