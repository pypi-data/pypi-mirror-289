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

__all__ = [
    'GetFirewallSupportInfoResult',
    'AwaitableGetFirewallSupportInfoResult',
    'get_firewall_support_info',
    'get_firewall_support_info_output',
]

@pulumi.output_type
class GetFirewallSupportInfoResult:
    """
    Support information for the resource
    """
    def __init__(__self__, account_id=None, account_registered=None, free_trial=None, free_trial_credit_left=None, free_trial_days_left=None, help_url=None, product_serial=None, product_sku=None, register_url=None, support_url=None, user_domain_supported=None, user_registered=None):
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if account_registered and not isinstance(account_registered, str):
            raise TypeError("Expected argument 'account_registered' to be a str")
        pulumi.set(__self__, "account_registered", account_registered)
        if free_trial and not isinstance(free_trial, str):
            raise TypeError("Expected argument 'free_trial' to be a str")
        pulumi.set(__self__, "free_trial", free_trial)
        if free_trial_credit_left and not isinstance(free_trial_credit_left, int):
            raise TypeError("Expected argument 'free_trial_credit_left' to be a int")
        pulumi.set(__self__, "free_trial_credit_left", free_trial_credit_left)
        if free_trial_days_left and not isinstance(free_trial_days_left, int):
            raise TypeError("Expected argument 'free_trial_days_left' to be a int")
        pulumi.set(__self__, "free_trial_days_left", free_trial_days_left)
        if help_url and not isinstance(help_url, str):
            raise TypeError("Expected argument 'help_url' to be a str")
        pulumi.set(__self__, "help_url", help_url)
        if product_serial and not isinstance(product_serial, str):
            raise TypeError("Expected argument 'product_serial' to be a str")
        pulumi.set(__self__, "product_serial", product_serial)
        if product_sku and not isinstance(product_sku, str):
            raise TypeError("Expected argument 'product_sku' to be a str")
        pulumi.set(__self__, "product_sku", product_sku)
        if register_url and not isinstance(register_url, str):
            raise TypeError("Expected argument 'register_url' to be a str")
        pulumi.set(__self__, "register_url", register_url)
        if support_url and not isinstance(support_url, str):
            raise TypeError("Expected argument 'support_url' to be a str")
        pulumi.set(__self__, "support_url", support_url)
        if user_domain_supported and not isinstance(user_domain_supported, str):
            raise TypeError("Expected argument 'user_domain_supported' to be a str")
        pulumi.set(__self__, "user_domain_supported", user_domain_supported)
        if user_registered and not isinstance(user_registered, str):
            raise TypeError("Expected argument 'user_registered' to be a str")
        pulumi.set(__self__, "user_registered", user_registered)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[str]:
        """
        Support account associated with given resource
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="accountRegistered")
    def account_registered(self) -> Optional[str]:
        """
        account registered in Customer Support Portal
        """
        return pulumi.get(self, "account_registered")

    @property
    @pulumi.getter(name="freeTrial")
    def free_trial(self) -> Optional[str]:
        """
        Product usage is in free trial period
        """
        return pulumi.get(self, "free_trial")

    @property
    @pulumi.getter(name="freeTrialCreditLeft")
    def free_trial_credit_left(self) -> Optional[int]:
        """
        Free trial credit remaining
        """
        return pulumi.get(self, "free_trial_credit_left")

    @property
    @pulumi.getter(name="freeTrialDaysLeft")
    def free_trial_days_left(self) -> Optional[int]:
        """
        Free trial days remaining
        """
        return pulumi.get(self, "free_trial_days_left")

    @property
    @pulumi.getter(name="helpURL")
    def help_url(self) -> Optional[str]:
        """
        URL for paloaltonetworks live community
        """
        return pulumi.get(self, "help_url")

    @property
    @pulumi.getter(name="productSerial")
    def product_serial(self) -> Optional[str]:
        """
        product Serial associated with given resource
        """
        return pulumi.get(self, "product_serial")

    @property
    @pulumi.getter(name="productSku")
    def product_sku(self) -> Optional[str]:
        """
        product SKU associated with given resource
        """
        return pulumi.get(self, "product_sku")

    @property
    @pulumi.getter(name="registerURL")
    def register_url(self) -> Optional[str]:
        """
        URL for registering product in paloaltonetworks Customer Service Portal
        """
        return pulumi.get(self, "register_url")

    @property
    @pulumi.getter(name="supportURL")
    def support_url(self) -> Optional[str]:
        """
        URL for paloaltonetworks Customer Service Portal
        """
        return pulumi.get(self, "support_url")

    @property
    @pulumi.getter(name="userDomainSupported")
    def user_domain_supported(self) -> Optional[str]:
        """
        user domain is supported in Customer Support Portal
        """
        return pulumi.get(self, "user_domain_supported")

    @property
    @pulumi.getter(name="userRegistered")
    def user_registered(self) -> Optional[str]:
        """
        user registered in Customer Support Portal
        """
        return pulumi.get(self, "user_registered")


class AwaitableGetFirewallSupportInfoResult(GetFirewallSupportInfoResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirewallSupportInfoResult(
            account_id=self.account_id,
            account_registered=self.account_registered,
            free_trial=self.free_trial,
            free_trial_credit_left=self.free_trial_credit_left,
            free_trial_days_left=self.free_trial_days_left,
            help_url=self.help_url,
            product_serial=self.product_serial,
            product_sku=self.product_sku,
            register_url=self.register_url,
            support_url=self.support_url,
            user_domain_supported=self.user_domain_supported,
            user_registered=self.user_registered)


def get_firewall_support_info(email: Optional[str] = None,
                              firewall_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirewallSupportInfoResult:
    """
    support info for firewall.


    :param str email: email address on behalf of which this API called
    :param str firewall_name: Firewall resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['email'] = email
    __args__['firewallName'] = firewall_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cloudngfw/v20220829:getFirewallSupportInfo', __args__, opts=opts, typ=GetFirewallSupportInfoResult).value

    return AwaitableGetFirewallSupportInfoResult(
        account_id=pulumi.get(__ret__, 'account_id'),
        account_registered=pulumi.get(__ret__, 'account_registered'),
        free_trial=pulumi.get(__ret__, 'free_trial'),
        free_trial_credit_left=pulumi.get(__ret__, 'free_trial_credit_left'),
        free_trial_days_left=pulumi.get(__ret__, 'free_trial_days_left'),
        help_url=pulumi.get(__ret__, 'help_url'),
        product_serial=pulumi.get(__ret__, 'product_serial'),
        product_sku=pulumi.get(__ret__, 'product_sku'),
        register_url=pulumi.get(__ret__, 'register_url'),
        support_url=pulumi.get(__ret__, 'support_url'),
        user_domain_supported=pulumi.get(__ret__, 'user_domain_supported'),
        user_registered=pulumi.get(__ret__, 'user_registered'))


@_utilities.lift_output_func(get_firewall_support_info)
def get_firewall_support_info_output(email: Optional[pulumi.Input[Optional[str]]] = None,
                                     firewall_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirewallSupportInfoResult]:
    """
    support info for firewall.


    :param str email: email address on behalf of which this API called
    :param str firewall_name: Firewall resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
