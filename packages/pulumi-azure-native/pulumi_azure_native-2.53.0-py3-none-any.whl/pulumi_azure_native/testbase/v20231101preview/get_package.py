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
    'GetPackageResult',
    'AwaitableGetPackageResult',
    'get_package',
    'get_package_output',
]

@pulumi.output_type
class GetPackageResult:
    """
    The Test Base Package resource.
    """
    def __init__(__self__, application_name=None, blob_path=None, draft_package_id=None, first_party_apps=None, flighting_ring=None, gallery_apps=None, id=None, inplace_upgrade_os_pair=None, intune_enrollment_metadata=None, is_enabled=None, last_modified_time=None, location=None, name=None, package_status=None, provisioning_state=None, system_data=None, tags=None, target_os_list=None, test_types=None, tests=None, type=None, validation_results=None, version=None):
        if application_name and not isinstance(application_name, str):
            raise TypeError("Expected argument 'application_name' to be a str")
        pulumi.set(__self__, "application_name", application_name)
        if blob_path and not isinstance(blob_path, str):
            raise TypeError("Expected argument 'blob_path' to be a str")
        pulumi.set(__self__, "blob_path", blob_path)
        if draft_package_id and not isinstance(draft_package_id, str):
            raise TypeError("Expected argument 'draft_package_id' to be a str")
        pulumi.set(__self__, "draft_package_id", draft_package_id)
        if first_party_apps and not isinstance(first_party_apps, list):
            raise TypeError("Expected argument 'first_party_apps' to be a list")
        pulumi.set(__self__, "first_party_apps", first_party_apps)
        if flighting_ring and not isinstance(flighting_ring, str):
            raise TypeError("Expected argument 'flighting_ring' to be a str")
        pulumi.set(__self__, "flighting_ring", flighting_ring)
        if gallery_apps and not isinstance(gallery_apps, list):
            raise TypeError("Expected argument 'gallery_apps' to be a list")
        pulumi.set(__self__, "gallery_apps", gallery_apps)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if inplace_upgrade_os_pair and not isinstance(inplace_upgrade_os_pair, dict):
            raise TypeError("Expected argument 'inplace_upgrade_os_pair' to be a dict")
        pulumi.set(__self__, "inplace_upgrade_os_pair", inplace_upgrade_os_pair)
        if intune_enrollment_metadata and not isinstance(intune_enrollment_metadata, dict):
            raise TypeError("Expected argument 'intune_enrollment_metadata' to be a dict")
        pulumi.set(__self__, "intune_enrollment_metadata", intune_enrollment_metadata)
        if is_enabled and not isinstance(is_enabled, bool):
            raise TypeError("Expected argument 'is_enabled' to be a bool")
        pulumi.set(__self__, "is_enabled", is_enabled)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if package_status and not isinstance(package_status, str):
            raise TypeError("Expected argument 'package_status' to be a str")
        pulumi.set(__self__, "package_status", package_status)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_os_list and not isinstance(target_os_list, list):
            raise TypeError("Expected argument 'target_os_list' to be a list")
        pulumi.set(__self__, "target_os_list", target_os_list)
        if test_types and not isinstance(test_types, list):
            raise TypeError("Expected argument 'test_types' to be a list")
        pulumi.set(__self__, "test_types", test_types)
        if tests and not isinstance(tests, list):
            raise TypeError("Expected argument 'tests' to be a list")
        pulumi.set(__self__, "tests", tests)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if validation_results and not isinstance(validation_results, list):
            raise TypeError("Expected argument 'validation_results' to be a list")
        pulumi.set(__self__, "validation_results", validation_results)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="applicationName")
    def application_name(self) -> str:
        """
        Application name
        """
        return pulumi.get(self, "application_name")

    @property
    @pulumi.getter(name="blobPath")
    def blob_path(self) -> Optional[str]:
        """
        The file path of the package.
        """
        return pulumi.get(self, "blob_path")

    @property
    @pulumi.getter(name="draftPackageId")
    def draft_package_id(self) -> Optional[str]:
        """
        The id of draft package. Used to create or update this package from a draft package.
        """
        return pulumi.get(self, "draft_package_id")

    @property
    @pulumi.getter(name="firstPartyApps")
    def first_party_apps(self) -> Optional[Sequence['outputs.FirstPartyAppDefinitionResponse']]:
        """
        The list of first party applications to test along with user application.
        """
        return pulumi.get(self, "first_party_apps")

    @property
    @pulumi.getter(name="flightingRing")
    def flighting_ring(self) -> Optional[str]:
        """
        The flighting ring for feature update.
        """
        return pulumi.get(self, "flighting_ring")

    @property
    @pulumi.getter(name="galleryApps")
    def gallery_apps(self) -> Sequence['outputs.GalleryAppDefinitionResponse']:
        """
        The list of gallery apps to test along with user application.
        """
        return pulumi.get(self, "gallery_apps")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="inplaceUpgradeOSPair")
    def inplace_upgrade_os_pair(self) -> Optional['outputs.InplaceUpgradeOSInfoResponse']:
        """
        Specifies the baseline os and target os for inplace upgrade.
        """
        return pulumi.get(self, "inplace_upgrade_os_pair")

    @property
    @pulumi.getter(name="intuneEnrollmentMetadata")
    def intune_enrollment_metadata(self) -> Optional['outputs.IntuneEnrollmentMetadataResponse']:
        """
        The metadata of Intune enrollment.
        """
        return pulumi.get(self, "intune_enrollment_metadata")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> bool:
        """
        Flag showing that whether the package is enabled. It doesn't schedule test for package which is not enabled.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> str:
        """
        The UTC timestamp when the package was last modified.
        """
        return pulumi.get(self, "last_modified_time")

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
    @pulumi.getter(name="packageStatus")
    def package_status(self) -> str:
        """
        The status of the package.
        """
        return pulumi.get(self, "package_status")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
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
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetOSList")
    def target_os_list(self) -> Optional[Sequence['outputs.TargetOSInfoResponse']]:
        """
        Specifies the target OSs of specific OS Update types.
        """
        return pulumi.get(self, "target_os_list")

    @property
    @pulumi.getter(name="testTypes")
    def test_types(self) -> Sequence[str]:
        """
        OOB, functional or flow driven. Mapped to the data in 'tests' property.
        """
        return pulumi.get(self, "test_types")

    @property
    @pulumi.getter
    def tests(self) -> Optional[Sequence['outputs.TestResponse']]:
        """
        The detailed test information.
        """
        return pulumi.get(self, "tests")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="validationResults")
    def validation_results(self) -> Sequence['outputs.PackageValidationResultResponse']:
        """
        The validation results. There's validation on package when it's created or updated.
        """
        return pulumi.get(self, "validation_results")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Application version
        """
        return pulumi.get(self, "version")


class AwaitableGetPackageResult(GetPackageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPackageResult(
            application_name=self.application_name,
            blob_path=self.blob_path,
            draft_package_id=self.draft_package_id,
            first_party_apps=self.first_party_apps,
            flighting_ring=self.flighting_ring,
            gallery_apps=self.gallery_apps,
            id=self.id,
            inplace_upgrade_os_pair=self.inplace_upgrade_os_pair,
            intune_enrollment_metadata=self.intune_enrollment_metadata,
            is_enabled=self.is_enabled,
            last_modified_time=self.last_modified_time,
            location=self.location,
            name=self.name,
            package_status=self.package_status,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            target_os_list=self.target_os_list,
            test_types=self.test_types,
            tests=self.tests,
            type=self.type,
            validation_results=self.validation_results,
            version=self.version)


def get_package(package_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                test_base_account_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPackageResult:
    """
    Gets a Test Base Package.


    :param str package_name: The resource name of the Test Base Package.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    __args__ = dict()
    __args__['packageName'] = package_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['testBaseAccountName'] = test_base_account_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:testbase/v20231101preview:getPackage', __args__, opts=opts, typ=GetPackageResult).value

    return AwaitableGetPackageResult(
        application_name=pulumi.get(__ret__, 'application_name'),
        blob_path=pulumi.get(__ret__, 'blob_path'),
        draft_package_id=pulumi.get(__ret__, 'draft_package_id'),
        first_party_apps=pulumi.get(__ret__, 'first_party_apps'),
        flighting_ring=pulumi.get(__ret__, 'flighting_ring'),
        gallery_apps=pulumi.get(__ret__, 'gallery_apps'),
        id=pulumi.get(__ret__, 'id'),
        inplace_upgrade_os_pair=pulumi.get(__ret__, 'inplace_upgrade_os_pair'),
        intune_enrollment_metadata=pulumi.get(__ret__, 'intune_enrollment_metadata'),
        is_enabled=pulumi.get(__ret__, 'is_enabled'),
        last_modified_time=pulumi.get(__ret__, 'last_modified_time'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        package_status=pulumi.get(__ret__, 'package_status'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        target_os_list=pulumi.get(__ret__, 'target_os_list'),
        test_types=pulumi.get(__ret__, 'test_types'),
        tests=pulumi.get(__ret__, 'tests'),
        type=pulumi.get(__ret__, 'type'),
        validation_results=pulumi.get(__ret__, 'validation_results'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_package)
def get_package_output(package_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       test_base_account_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPackageResult]:
    """
    Gets a Test Base Package.


    :param str package_name: The resource name of the Test Base Package.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    ...
