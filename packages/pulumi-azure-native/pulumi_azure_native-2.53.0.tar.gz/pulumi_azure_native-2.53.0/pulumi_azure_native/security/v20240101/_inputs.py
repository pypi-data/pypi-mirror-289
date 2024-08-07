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
    'ExtensionArgs',
    'ExtensionArgsDict',
]

MYPY = False

if not MYPY:
    class ExtensionArgsDict(TypedDict):
        """
        A plan's extension properties
        """
        is_enabled: pulumi.Input[Union[str, 'IsEnabled']]
        """
        Indicates whether the extension is enabled.
        """
        name: pulumi.Input[str]
        """
        The extension name. Supported values are: <br><br>**AgentlessDiscoveryForKubernetes** - API-based discovery of information about Kubernetes cluster architecture, workload objects, and setup. Required for Kubernetes inventory, identity and network exposure detection, attack path analysis and risk hunting as part of the cloud security explorer.
        Available for CloudPosture plan.<br><br>**OnUploadMalwareScanning** - Limits the GB to be scanned per month for each storage account within the subscription. Once this limit reached on a given storage account, Blobs won't be scanned during current calendar month.
        Available for StorageAccounts plan.<br><br>**SensitiveDataDiscovery** - Sensitive data discovery identifies Blob storage container with sensitive data such as credentials, credit cards, and more, to help prioritize and investigate security events.
        Available for StorageAccounts and CloudPosture plans.<br><br>**ContainerRegistriesVulnerabilityAssessments** - Provides vulnerability management for images stored in your container registries.
        Available for CloudPosture and Containers plans.
        """
        additional_extension_properties: NotRequired[Any]
        """
        Property values associated with the extension.
        """
elif False:
    ExtensionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ExtensionArgs:
    def __init__(__self__, *,
                 is_enabled: pulumi.Input[Union[str, 'IsEnabled']],
                 name: pulumi.Input[str],
                 additional_extension_properties: Optional[Any] = None):
        """
        A plan's extension properties
        :param pulumi.Input[Union[str, 'IsEnabled']] is_enabled: Indicates whether the extension is enabled.
        :param pulumi.Input[str] name: The extension name. Supported values are: <br><br>**AgentlessDiscoveryForKubernetes** - API-based discovery of information about Kubernetes cluster architecture, workload objects, and setup. Required for Kubernetes inventory, identity and network exposure detection, attack path analysis and risk hunting as part of the cloud security explorer.
               Available for CloudPosture plan.<br><br>**OnUploadMalwareScanning** - Limits the GB to be scanned per month for each storage account within the subscription. Once this limit reached on a given storage account, Blobs won't be scanned during current calendar month.
               Available for StorageAccounts plan.<br><br>**SensitiveDataDiscovery** - Sensitive data discovery identifies Blob storage container with sensitive data such as credentials, credit cards, and more, to help prioritize and investigate security events.
               Available for StorageAccounts and CloudPosture plans.<br><br>**ContainerRegistriesVulnerabilityAssessments** - Provides vulnerability management for images stored in your container registries.
               Available for CloudPosture and Containers plans.
        :param Any additional_extension_properties: Property values associated with the extension.
        """
        pulumi.set(__self__, "is_enabled", is_enabled)
        pulumi.set(__self__, "name", name)
        if additional_extension_properties is not None:
            pulumi.set(__self__, "additional_extension_properties", additional_extension_properties)

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[Union[str, 'IsEnabled']]:
        """
        Indicates whether the extension is enabled.
        """
        return pulumi.get(self, "is_enabled")

    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[Union[str, 'IsEnabled']]):
        pulumi.set(self, "is_enabled", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The extension name. Supported values are: <br><br>**AgentlessDiscoveryForKubernetes** - API-based discovery of information about Kubernetes cluster architecture, workload objects, and setup. Required for Kubernetes inventory, identity and network exposure detection, attack path analysis and risk hunting as part of the cloud security explorer.
        Available for CloudPosture plan.<br><br>**OnUploadMalwareScanning** - Limits the GB to be scanned per month for each storage account within the subscription. Once this limit reached on a given storage account, Blobs won't be scanned during current calendar month.
        Available for StorageAccounts plan.<br><br>**SensitiveDataDiscovery** - Sensitive data discovery identifies Blob storage container with sensitive data such as credentials, credit cards, and more, to help prioritize and investigate security events.
        Available for StorageAccounts and CloudPosture plans.<br><br>**ContainerRegistriesVulnerabilityAssessments** - Provides vulnerability management for images stored in your container registries.
        Available for CloudPosture and Containers plans.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="additionalExtensionProperties")
    def additional_extension_properties(self) -> Optional[Any]:
        """
        Property values associated with the extension.
        """
        return pulumi.get(self, "additional_extension_properties")

    @additional_extension_properties.setter
    def additional_extension_properties(self, value: Optional[Any]):
        pulumi.set(self, "additional_extension_properties", value)


