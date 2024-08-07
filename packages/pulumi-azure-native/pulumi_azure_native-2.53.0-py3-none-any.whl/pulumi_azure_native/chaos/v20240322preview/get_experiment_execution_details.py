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
    'GetExperimentExecutionDetailsResult',
    'AwaitableGetExperimentExecutionDetailsResult',
    'get_experiment_execution_details',
    'get_experiment_execution_details_output',
]

@pulumi.output_type
class GetExperimentExecutionDetailsResult:
    """
    Model that represents the execution details of an Experiment.
    """
    def __init__(__self__, failure_reason=None, id=None, last_action_at=None, name=None, run_information=None, started_at=None, status=None, stopped_at=None, type=None):
        if failure_reason and not isinstance(failure_reason, str):
            raise TypeError("Expected argument 'failure_reason' to be a str")
        pulumi.set(__self__, "failure_reason", failure_reason)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_action_at and not isinstance(last_action_at, str):
            raise TypeError("Expected argument 'last_action_at' to be a str")
        pulumi.set(__self__, "last_action_at", last_action_at)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if run_information and not isinstance(run_information, dict):
            raise TypeError("Expected argument 'run_information' to be a dict")
        pulumi.set(__self__, "run_information", run_information)
        if started_at and not isinstance(started_at, str):
            raise TypeError("Expected argument 'started_at' to be a str")
        pulumi.set(__self__, "started_at", started_at)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if stopped_at and not isinstance(stopped_at, str):
            raise TypeError("Expected argument 'stopped_at' to be a str")
        pulumi.set(__self__, "stopped_at", stopped_at)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> str:
        """
        The reason why the execution failed.
        """
        return pulumi.get(self, "failure_reason")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        String of the fully qualified resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastActionAt")
    def last_action_at(self) -> str:
        """
        String that represents the last action date time.
        """
        return pulumi.get(self, "last_action_at")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        String of the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="runInformation")
    def run_information(self) -> 'outputs.ExperimentExecutionDetailsPropertiesResponseRunInformation':
        """
        The information of the experiment run.
        """
        return pulumi.get(self, "run_information")

    @property
    @pulumi.getter(name="startedAt")
    def started_at(self) -> str:
        """
        String that represents the start date time.
        """
        return pulumi.get(self, "started_at")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the execution.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="stoppedAt")
    def stopped_at(self) -> str:
        """
        String that represents the stop date time.
        """
        return pulumi.get(self, "stopped_at")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        String of the resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetExperimentExecutionDetailsResult(GetExperimentExecutionDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExperimentExecutionDetailsResult(
            failure_reason=self.failure_reason,
            id=self.id,
            last_action_at=self.last_action_at,
            name=self.name,
            run_information=self.run_information,
            started_at=self.started_at,
            status=self.status,
            stopped_at=self.stopped_at,
            type=self.type)


def get_experiment_execution_details(execution_id: Optional[str] = None,
                                     experiment_name: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExperimentExecutionDetailsResult:
    """
    Execution details of an experiment resource.


    :param str execution_id: GUID that represents a Experiment execution detail.
    :param str experiment_name: String that represents a Experiment resource name.
    :param str resource_group_name: String that represents an Azure resource group.
    """
    __args__ = dict()
    __args__['executionId'] = execution_id
    __args__['experimentName'] = experiment_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:chaos/v20240322preview:getExperimentExecutionDetails', __args__, opts=opts, typ=GetExperimentExecutionDetailsResult).value

    return AwaitableGetExperimentExecutionDetailsResult(
        failure_reason=pulumi.get(__ret__, 'failure_reason'),
        id=pulumi.get(__ret__, 'id'),
        last_action_at=pulumi.get(__ret__, 'last_action_at'),
        name=pulumi.get(__ret__, 'name'),
        run_information=pulumi.get(__ret__, 'run_information'),
        started_at=pulumi.get(__ret__, 'started_at'),
        status=pulumi.get(__ret__, 'status'),
        stopped_at=pulumi.get(__ret__, 'stopped_at'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_experiment_execution_details)
def get_experiment_execution_details_output(execution_id: Optional[pulumi.Input[str]] = None,
                                            experiment_name: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExperimentExecutionDetailsResult]:
    """
    Execution details of an experiment resource.


    :param str execution_id: GUID that represents a Experiment execution detail.
    :param str experiment_name: String that represents a Experiment resource name.
    :param str resource_group_name: String that represents an Azure resource group.
    """
    ...
