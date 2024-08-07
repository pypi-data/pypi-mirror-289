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
    'GetCertificateObjectLocalRulestackResult',
    'AwaitableGetCertificateObjectLocalRulestackResult',
    'get_certificate_object_local_rulestack',
    'get_certificate_object_local_rulestack_output',
]

@pulumi.output_type
class GetCertificateObjectLocalRulestackResult:
    """
    LocalRulestack Certificate Object
    """
    def __init__(__self__, audit_comment=None, certificate_self_signed=None, certificate_signer_resource_id=None, description=None, etag=None, id=None, name=None, provisioning_state=None, system_data=None, type=None):
        if audit_comment and not isinstance(audit_comment, str):
            raise TypeError("Expected argument 'audit_comment' to be a str")
        pulumi.set(__self__, "audit_comment", audit_comment)
        if certificate_self_signed and not isinstance(certificate_self_signed, str):
            raise TypeError("Expected argument 'certificate_self_signed' to be a str")
        pulumi.set(__self__, "certificate_self_signed", certificate_self_signed)
        if certificate_signer_resource_id and not isinstance(certificate_signer_resource_id, str):
            raise TypeError("Expected argument 'certificate_signer_resource_id' to be a str")
        pulumi.set(__self__, "certificate_signer_resource_id", certificate_signer_resource_id)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
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
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="auditComment")
    def audit_comment(self) -> Optional[str]:
        """
        comment for this object
        """
        return pulumi.get(self, "audit_comment")

    @property
    @pulumi.getter(name="certificateSelfSigned")
    def certificate_self_signed(self) -> str:
        """
        use certificate self signed
        """
        return pulumi.get(self, "certificate_self_signed")

    @property
    @pulumi.getter(name="certificateSignerResourceId")
    def certificate_signer_resource_id(self) -> Optional[str]:
        """
        Resource Id of certificate signer, to be populated only when certificateSelfSigned is false
        """
        return pulumi.get(self, "certificate_signer_resource_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        user description for this object
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        read only string representing last create or update
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
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


class AwaitableGetCertificateObjectLocalRulestackResult(GetCertificateObjectLocalRulestackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateObjectLocalRulestackResult(
            audit_comment=self.audit_comment,
            certificate_self_signed=self.certificate_self_signed,
            certificate_signer_resource_id=self.certificate_signer_resource_id,
            description=self.description,
            etag=self.etag,
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_certificate_object_local_rulestack(local_rulestack_name: Optional[str] = None,
                                           name: Optional[str] = None,
                                           resource_group_name: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateObjectLocalRulestackResult:
    """
    Get a CertificateObjectLocalRulestackResource


    :param str local_rulestack_name: LocalRulestack resource name
    :param str name: certificate name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['localRulestackName'] = local_rulestack_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20240119preview:getCertificateObjectLocalRulestack', __args__, opts=opts, typ=GetCertificateObjectLocalRulestackResult).value

    return AwaitableGetCertificateObjectLocalRulestackResult(
        audit_comment=pulumi.get(__ret__, 'audit_comment'),
        certificate_self_signed=pulumi.get(__ret__, 'certificate_self_signed'),
        certificate_signer_resource_id=pulumi.get(__ret__, 'certificate_signer_resource_id'),
        description=pulumi.get(__ret__, 'description'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_certificate_object_local_rulestack)
def get_certificate_object_local_rulestack_output(local_rulestack_name: Optional[pulumi.Input[str]] = None,
                                                  name: Optional[pulumi.Input[str]] = None,
                                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCertificateObjectLocalRulestackResult]:
    """
    Get a CertificateObjectLocalRulestackResource


    :param str local_rulestack_name: LocalRulestack resource name
    :param str name: certificate name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
