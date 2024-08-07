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
from .. import _utilities
from . import outputs

__all__ = [
    'ListTaskRunDetailsResult',
    'AwaitableListTaskRunDetailsResult',
    'list_task_run_details',
    'list_task_run_details_output',
]

@pulumi.output_type
class ListTaskRunDetailsResult:
    """
    The task run that has the ARM resource and properties. 
    The task run will have the information of request and result of a run.
    """
    def __init__(__self__, force_update_tag=None, id=None, identity=None, location=None, name=None, provisioning_state=None, run_request=None, run_result=None, system_data=None, type=None):
        if force_update_tag and not isinstance(force_update_tag, str):
            raise TypeError("Expected argument 'force_update_tag' to be a str")
        pulumi.set(__self__, "force_update_tag", force_update_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if run_request and not isinstance(run_request, dict):
            raise TypeError("Expected argument 'run_request' to be a dict")
        pulumi.set(__self__, "run_request", run_request)
        if run_result and not isinstance(run_result, dict):
            raise TypeError("Expected argument 'run_result' to be a dict")
        pulumi.set(__self__, "run_result", run_result)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[str]:
        """
        How the run should be forced to rerun even if the run request configuration has not changed
        """
        return pulumi.get(self, "force_update_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityPropertiesResponse']:
        """
        Identity for the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the resource
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of this task run
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="runRequest")
    def run_request(self) -> Optional[Any]:
        """
        The request (parameters) for the run
        """
        return pulumi.get(self, "run_request")

    @property
    @pulumi.getter(name="runResult")
    def run_result(self) -> 'outputs.RunResponse':
        """
        The result of this task run
        """
        return pulumi.get(self, "run_result")

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
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableListTaskRunDetailsResult(ListTaskRunDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListTaskRunDetailsResult(
            force_update_tag=self.force_update_tag,
            id=self.id,
            identity=self.identity,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            run_request=self.run_request,
            run_result=self.run_result,
            system_data=self.system_data,
            type=self.type)


def list_task_run_details(registry_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          task_run_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListTaskRunDetailsResult:
    """
    Gets the detailed information for a given task run that includes all secrets.
    Azure REST API version: 2019-06-01-preview.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    :param str task_run_name: The name of the task run.
    """
    __args__ = dict()
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['taskRunName'] = task_run_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry:listTaskRunDetails', __args__, opts=opts, typ=ListTaskRunDetailsResult).value

    return AwaitableListTaskRunDetailsResult(
        force_update_tag=pulumi.get(__ret__, 'force_update_tag'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        run_request=pulumi.get(__ret__, 'run_request'),
        run_result=pulumi.get(__ret__, 'run_result'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(list_task_run_details)
def list_task_run_details_output(registry_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 task_run_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListTaskRunDetailsResult]:
    """
    Gets the detailed information for a given task run that includes all secrets.
    Azure REST API version: 2019-06-01-preview.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    :param str task_run_name: The name of the task run.
    """
    ...
