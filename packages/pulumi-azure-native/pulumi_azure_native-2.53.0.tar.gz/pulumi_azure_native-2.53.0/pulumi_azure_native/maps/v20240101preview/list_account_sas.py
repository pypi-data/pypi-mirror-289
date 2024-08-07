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
from ._enums import *

__all__ = [
    'ListAccountSasResult',
    'AwaitableListAccountSasResult',
    'list_account_sas',
    'list_account_sas_output',
]

@pulumi.output_type
class ListAccountSasResult:
    """
    A new Sas token which can be used to access the Maps REST APIs and is controlled by the specified Managed identity permissions on Azure (IAM) Role Based Access Control.
    """
    def __init__(__self__, account_sas_token=None):
        if account_sas_token and not isinstance(account_sas_token, str):
            raise TypeError("Expected argument 'account_sas_token' to be a str")
        pulumi.set(__self__, "account_sas_token", account_sas_token)

    @property
    @pulumi.getter(name="accountSasToken")
    def account_sas_token(self) -> str:
        """
        The shared access signature access token.
        """
        return pulumi.get(self, "account_sas_token")


class AwaitableListAccountSasResult(ListAccountSasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListAccountSasResult(
            account_sas_token=self.account_sas_token)


def list_account_sas(account_name: Optional[str] = None,
                     expiry: Optional[str] = None,
                     max_rate_per_second: Optional[int] = None,
                     principal_id: Optional[str] = None,
                     regions: Optional[Sequence[str]] = None,
                     resource_group_name: Optional[str] = None,
                     signing_key: Optional[Union[str, 'SigningKey']] = None,
                     start: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListAccountSasResult:
    """
    Create and list an account shared access signature token. Use this SAS token for authentication to Azure Maps REST APIs through various Azure Maps SDKs. As prerequisite to create a SAS Token.

    Prerequisites:
    1. Create or have an existing User Assigned Managed Identity in the same Azure region as the account.
    2. Create or update an Azure Maps account with the same Azure region as the User Assigned Managed Identity is placed.


    :param str account_name: The name of the Maps Account.
    :param str expiry: The date time offset of when the token validity expires. For example "2017-05-24T10:42:03.1567373Z". Maximum duration allowed is 24 hours between `start` and `expiry`.
    :param int max_rate_per_second: Required parameter which represents the desired maximum request per second to allowed for the given SAS token. This does not guarantee perfect accuracy in measurements but provides application safe guards of abuse with eventual enforcement.
    :param str principal_id: The principal Id also known as the object Id of a User Assigned Managed Identity currently assigned to the Maps Account. To assign a Managed Identity of the account, use operation Create or Update an assign a User Assigned Identity resource Id.
    :param Sequence[str] regions: Optional, allows control of which region locations are permitted access to Azure Maps REST APIs with the SAS token. Example: "eastus", "westus2". Omitting this parameter will allow all region locations to be accessible.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param Union[str, 'SigningKey'] signing_key: The Maps account key to use for signing. Picking `primaryKey` or `secondaryKey` will use the Maps account Shared Keys, and using `managedIdentity` will use the auto-renewed private key to sign the SAS.
    :param str start: The date time offset of when the token validity begins. For example "2017-05-24T10:42:03.1567373Z". Maximum duration allowed is 24 hours between `start` and `expiry`.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['expiry'] = expiry
    __args__['maxRatePerSecond'] = max_rate_per_second
    __args__['principalId'] = principal_id
    __args__['regions'] = regions
    __args__['resourceGroupName'] = resource_group_name
    __args__['signingKey'] = signing_key
    __args__['start'] = start
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:maps/v20240101preview:listAccountSas', __args__, opts=opts, typ=ListAccountSasResult).value

    return AwaitableListAccountSasResult(
        account_sas_token=pulumi.get(__ret__, 'account_sas_token'))


@_utilities.lift_output_func(list_account_sas)
def list_account_sas_output(account_name: Optional[pulumi.Input[str]] = None,
                            expiry: Optional[pulumi.Input[str]] = None,
                            max_rate_per_second: Optional[pulumi.Input[int]] = None,
                            principal_id: Optional[pulumi.Input[str]] = None,
                            regions: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            signing_key: Optional[pulumi.Input[Union[str, 'SigningKey']]] = None,
                            start: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListAccountSasResult]:
    """
    Create and list an account shared access signature token. Use this SAS token for authentication to Azure Maps REST APIs through various Azure Maps SDKs. As prerequisite to create a SAS Token.

    Prerequisites:
    1. Create or have an existing User Assigned Managed Identity in the same Azure region as the account.
    2. Create or update an Azure Maps account with the same Azure region as the User Assigned Managed Identity is placed.


    :param str account_name: The name of the Maps Account.
    :param str expiry: The date time offset of when the token validity expires. For example "2017-05-24T10:42:03.1567373Z". Maximum duration allowed is 24 hours between `start` and `expiry`.
    :param int max_rate_per_second: Required parameter which represents the desired maximum request per second to allowed for the given SAS token. This does not guarantee perfect accuracy in measurements but provides application safe guards of abuse with eventual enforcement.
    :param str principal_id: The principal Id also known as the object Id of a User Assigned Managed Identity currently assigned to the Maps Account. To assign a Managed Identity of the account, use operation Create or Update an assign a User Assigned Identity resource Id.
    :param Sequence[str] regions: Optional, allows control of which region locations are permitted access to Azure Maps REST APIs with the SAS token. Example: "eastus", "westus2". Omitting this parameter will allow all region locations to be accessible.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param Union[str, 'SigningKey'] signing_key: The Maps account key to use for signing. Picking `primaryKey` or `secondaryKey` will use the Maps account Shared Keys, and using `managedIdentity` will use the auto-renewed private key to sign the SAS.
    :param str start: The date time offset of when the token validity begins. For example "2017-05-24T10:42:03.1567373Z". Maximum duration allowed is 24 hours between `start` and `expiry`.
    """
    ...
