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
    'GetSAPSizingRecommendationsResult',
    'AwaitableGetSAPSizingRecommendationsResult',
    'get_sap_sizing_recommendations',
    'get_sap_sizing_recommendations_output',
]

@pulumi.output_type
class GetSAPSizingRecommendationsResult:
    """
    The SAP sizing recommendation result.
    """
    def __init__(__self__, deployment_type=None):
        if deployment_type and not isinstance(deployment_type, str):
            raise TypeError("Expected argument 'deployment_type' to be a str")
        pulumi.set(__self__, "deployment_type", deployment_type)

    @property
    @pulumi.getter(name="deploymentType")
    def deployment_type(self) -> str:
        """
        The type of SAP deployment, single server or Three tier.
        """
        return pulumi.get(self, "deployment_type")


class AwaitableGetSAPSizingRecommendationsResult(GetSAPSizingRecommendationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSAPSizingRecommendationsResult(
            deployment_type=self.deployment_type)


def get_sap_sizing_recommendations(app_location: Optional[str] = None,
                                   database_type: Optional[Union[str, 'SAPDatabaseType']] = None,
                                   db_memory: Optional[float] = None,
                                   db_scale_method: Optional[Union[str, 'SAPDatabaseScaleMethod']] = None,
                                   deployment_type: Optional[Union[str, 'SAPDeploymentType']] = None,
                                   environment: Optional[Union[str, 'SAPEnvironmentType']] = None,
                                   high_availability_type: Optional[Union[str, 'SAPHighAvailabilityType']] = None,
                                   location: Optional[str] = None,
                                   sap_product: Optional[Union[str, 'SAPProductType']] = None,
                                   saps: Optional[float] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSAPSizingRecommendationsResult:
    """
    Get SAP sizing recommendations by providing input SAPS for application tier and memory required for database tier


    :param str app_location: The geo-location where the resource is to be created.
    :param Union[str, 'SAPDatabaseType'] database_type: The database type.
    :param float db_memory: The database memory configuration.
    :param Union[str, 'SAPDatabaseScaleMethod'] db_scale_method: The DB scale method.
    :param Union[str, 'SAPDeploymentType'] deployment_type: The deployment type. Eg: SingleServer/ThreeTier
    :param Union[str, 'SAPEnvironmentType'] environment: Defines the environment type - Production/Non Production.
    :param Union[str, 'SAPHighAvailabilityType'] high_availability_type: The high availability type.
    :param str location: The name of Azure region.
    :param Union[str, 'SAPProductType'] sap_product: Defines the SAP Product type.
    :param float saps: The SAP Application Performance Standard measurement.
    """
    __args__ = dict()
    __args__['appLocation'] = app_location
    __args__['databaseType'] = database_type
    __args__['dbMemory'] = db_memory
    __args__['dbScaleMethod'] = db_scale_method
    __args__['deploymentType'] = deployment_type
    __args__['environment'] = environment
    __args__['highAvailabilityType'] = high_availability_type
    __args__['location'] = location
    __args__['sapProduct'] = sap_product
    __args__['saps'] = saps
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:workloads/v20211201preview:getSAPSizingRecommendations', __args__, opts=opts, typ=GetSAPSizingRecommendationsResult).value

    return AwaitableGetSAPSizingRecommendationsResult(
        deployment_type=pulumi.get(__ret__, 'deployment_type'))


@_utilities.lift_output_func(get_sap_sizing_recommendations)
def get_sap_sizing_recommendations_output(app_location: Optional[pulumi.Input[str]] = None,
                                          database_type: Optional[pulumi.Input[Union[str, 'SAPDatabaseType']]] = None,
                                          db_memory: Optional[pulumi.Input[float]] = None,
                                          db_scale_method: Optional[pulumi.Input[Optional[Union[str, 'SAPDatabaseScaleMethod']]]] = None,
                                          deployment_type: Optional[pulumi.Input[Union[str, 'SAPDeploymentType']]] = None,
                                          environment: Optional[pulumi.Input[Union[str, 'SAPEnvironmentType']]] = None,
                                          high_availability_type: Optional[pulumi.Input[Optional[Union[str, 'SAPHighAvailabilityType']]]] = None,
                                          location: Optional[pulumi.Input[str]] = None,
                                          sap_product: Optional[pulumi.Input[Union[str, 'SAPProductType']]] = None,
                                          saps: Optional[pulumi.Input[float]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSAPSizingRecommendationsResult]:
    """
    Get SAP sizing recommendations by providing input SAPS for application tier and memory required for database tier


    :param str app_location: The geo-location where the resource is to be created.
    :param Union[str, 'SAPDatabaseType'] database_type: The database type.
    :param float db_memory: The database memory configuration.
    :param Union[str, 'SAPDatabaseScaleMethod'] db_scale_method: The DB scale method.
    :param Union[str, 'SAPDeploymentType'] deployment_type: The deployment type. Eg: SingleServer/ThreeTier
    :param Union[str, 'SAPEnvironmentType'] environment: Defines the environment type - Production/Non Production.
    :param Union[str, 'SAPHighAvailabilityType'] high_availability_type: The high availability type.
    :param str location: The name of Azure region.
    :param Union[str, 'SAPProductType'] sap_product: Defines the SAP Product type.
    :param float saps: The SAP Application Performance Standard measurement.
    """
    ...
