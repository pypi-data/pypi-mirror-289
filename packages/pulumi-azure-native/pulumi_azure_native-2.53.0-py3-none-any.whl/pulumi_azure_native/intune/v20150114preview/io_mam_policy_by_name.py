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

__all__ = ['IoMAMPolicyByNameArgs', 'IoMAMPolicyByName']

@pulumi.input_type
class IoMAMPolicyByNameArgs:
    def __init__(__self__, *,
                 friendly_name: pulumi.Input[str],
                 host_name: pulumi.Input[str],
                 access_recheck_offline_timeout: Optional[pulumi.Input[str]] = None,
                 access_recheck_online_timeout: Optional[pulumi.Input[str]] = None,
                 app_sharing_from_level: Optional[pulumi.Input[str]] = None,
                 app_sharing_to_level: Optional[pulumi.Input[str]] = None,
                 authentication: Optional[pulumi.Input[str]] = None,
                 clipboard_sharing_level: Optional[pulumi.Input[str]] = None,
                 data_backup: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_compliance: Optional[pulumi.Input[str]] = None,
                 file_encryption_level: Optional[pulumi.Input[str]] = None,
                 file_sharing_save_as: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_browser: Optional[pulumi.Input[str]] = None,
                 offline_wipe_timeout: Optional[pulumi.Input[str]] = None,
                 pin: Optional[pulumi.Input[str]] = None,
                 pin_num_retry: Optional[pulumi.Input[int]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 touch_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IoMAMPolicyByName resource.
        :param pulumi.Input[str] host_name: Location hostName for the tenant
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] policy_name: Unique name for the policy
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource Tags
        """
        pulumi.set(__self__, "friendly_name", friendly_name)
        pulumi.set(__self__, "host_name", host_name)
        if access_recheck_offline_timeout is not None:
            pulumi.set(__self__, "access_recheck_offline_timeout", access_recheck_offline_timeout)
        if access_recheck_online_timeout is not None:
            pulumi.set(__self__, "access_recheck_online_timeout", access_recheck_online_timeout)
        if app_sharing_from_level is None:
            app_sharing_from_level = 'none'
        if app_sharing_from_level is not None:
            pulumi.set(__self__, "app_sharing_from_level", app_sharing_from_level)
        if app_sharing_to_level is None:
            app_sharing_to_level = 'none'
        if app_sharing_to_level is not None:
            pulumi.set(__self__, "app_sharing_to_level", app_sharing_to_level)
        if authentication is None:
            authentication = 'required'
        if authentication is not None:
            pulumi.set(__self__, "authentication", authentication)
        if clipboard_sharing_level is None:
            clipboard_sharing_level = 'blocked'
        if clipboard_sharing_level is not None:
            pulumi.set(__self__, "clipboard_sharing_level", clipboard_sharing_level)
        if data_backup is None:
            data_backup = 'allow'
        if data_backup is not None:
            pulumi.set(__self__, "data_backup", data_backup)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if device_compliance is None:
            device_compliance = 'enable'
        if device_compliance is not None:
            pulumi.set(__self__, "device_compliance", device_compliance)
        if file_encryption_level is None:
            file_encryption_level = 'deviceLocked'
        if file_encryption_level is not None:
            pulumi.set(__self__, "file_encryption_level", file_encryption_level)
        if file_sharing_save_as is None:
            file_sharing_save_as = 'allow'
        if file_sharing_save_as is not None:
            pulumi.set(__self__, "file_sharing_save_as", file_sharing_save_as)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if managed_browser is None:
            managed_browser = 'required'
        if managed_browser is not None:
            pulumi.set(__self__, "managed_browser", managed_browser)
        if offline_wipe_timeout is not None:
            pulumi.set(__self__, "offline_wipe_timeout", offline_wipe_timeout)
        if pin is None:
            pin = 'required'
        if pin is not None:
            pulumi.set(__self__, "pin", pin)
        if pin_num_retry is not None:
            pulumi.set(__self__, "pin_num_retry", pin_num_retry)
        if policy_name is not None:
            pulumi.set(__self__, "policy_name", policy_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if touch_id is None:
            touch_id = 'enable'
        if touch_id is not None:
            pulumi.set(__self__, "touch_id", touch_id)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[str]:
        """
        Location hostName for the tenant
        """
        return pulumi.get(self, "host_name")

    @host_name.setter
    def host_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "host_name", value)

    @property
    @pulumi.getter(name="accessRecheckOfflineTimeout")
    def access_recheck_offline_timeout(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "access_recheck_offline_timeout")

    @access_recheck_offline_timeout.setter
    def access_recheck_offline_timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_recheck_offline_timeout", value)

    @property
    @pulumi.getter(name="accessRecheckOnlineTimeout")
    def access_recheck_online_timeout(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "access_recheck_online_timeout")

    @access_recheck_online_timeout.setter
    def access_recheck_online_timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_recheck_online_timeout", value)

    @property
    @pulumi.getter(name="appSharingFromLevel")
    def app_sharing_from_level(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "app_sharing_from_level")

    @app_sharing_from_level.setter
    def app_sharing_from_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_sharing_from_level", value)

    @property
    @pulumi.getter(name="appSharingToLevel")
    def app_sharing_to_level(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "app_sharing_to_level")

    @app_sharing_to_level.setter
    def app_sharing_to_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_sharing_to_level", value)

    @property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "authentication")

    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication", value)

    @property
    @pulumi.getter(name="clipboardSharingLevel")
    def clipboard_sharing_level(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "clipboard_sharing_level")

    @clipboard_sharing_level.setter
    def clipboard_sharing_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "clipboard_sharing_level", value)

    @property
    @pulumi.getter(name="dataBackup")
    def data_backup(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "data_backup")

    @data_backup.setter
    def data_backup(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_backup", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="deviceCompliance")
    def device_compliance(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "device_compliance")

    @device_compliance.setter
    def device_compliance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_compliance", value)

    @property
    @pulumi.getter(name="fileEncryptionLevel")
    def file_encryption_level(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "file_encryption_level")

    @file_encryption_level.setter
    def file_encryption_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_encryption_level", value)

    @property
    @pulumi.getter(name="fileSharingSaveAs")
    def file_sharing_save_as(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "file_sharing_save_as")

    @file_sharing_save_as.setter
    def file_sharing_save_as(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_sharing_save_as", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="managedBrowser")
    def managed_browser(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "managed_browser")

    @managed_browser.setter
    def managed_browser(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "managed_browser", value)

    @property
    @pulumi.getter(name="offlineWipeTimeout")
    def offline_wipe_timeout(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "offline_wipe_timeout")

    @offline_wipe_timeout.setter
    def offline_wipe_timeout(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "offline_wipe_timeout", value)

    @property
    @pulumi.getter
    def pin(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "pin")

    @pin.setter
    def pin(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pin", value)

    @property
    @pulumi.getter(name="pinNumRetry")
    def pin_num_retry(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "pin_num_retry")

    @pin_num_retry.setter
    def pin_num_retry(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "pin_num_retry", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique name for the policy
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource Tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="touchId")
    def touch_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "touch_id")

    @touch_id.setter
    def touch_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "touch_id", value)


class IoMAMPolicyByName(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_recheck_offline_timeout: Optional[pulumi.Input[str]] = None,
                 access_recheck_online_timeout: Optional[pulumi.Input[str]] = None,
                 app_sharing_from_level: Optional[pulumi.Input[str]] = None,
                 app_sharing_to_level: Optional[pulumi.Input[str]] = None,
                 authentication: Optional[pulumi.Input[str]] = None,
                 clipboard_sharing_level: Optional[pulumi.Input[str]] = None,
                 data_backup: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_compliance: Optional[pulumi.Input[str]] = None,
                 file_encryption_level: Optional[pulumi.Input[str]] = None,
                 file_sharing_save_as: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_browser: Optional[pulumi.Input[str]] = None,
                 offline_wipe_timeout: Optional[pulumi.Input[str]] = None,
                 pin: Optional[pulumi.Input[str]] = None,
                 pin_num_retry: Optional[pulumi.Input[int]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 touch_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        iOS Policy entity for Intune MAM.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] host_name: Location hostName for the tenant
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] policy_name: Unique name for the policy
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource Tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IoMAMPolicyByNameArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        iOS Policy entity for Intune MAM.

        :param str resource_name: The name of the resource.
        :param IoMAMPolicyByNameArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IoMAMPolicyByNameArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_recheck_offline_timeout: Optional[pulumi.Input[str]] = None,
                 access_recheck_online_timeout: Optional[pulumi.Input[str]] = None,
                 app_sharing_from_level: Optional[pulumi.Input[str]] = None,
                 app_sharing_to_level: Optional[pulumi.Input[str]] = None,
                 authentication: Optional[pulumi.Input[str]] = None,
                 clipboard_sharing_level: Optional[pulumi.Input[str]] = None,
                 data_backup: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 device_compliance: Optional[pulumi.Input[str]] = None,
                 file_encryption_level: Optional[pulumi.Input[str]] = None,
                 file_sharing_save_as: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_browser: Optional[pulumi.Input[str]] = None,
                 offline_wipe_timeout: Optional[pulumi.Input[str]] = None,
                 pin: Optional[pulumi.Input[str]] = None,
                 pin_num_retry: Optional[pulumi.Input[int]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 touch_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IoMAMPolicyByNameArgs.__new__(IoMAMPolicyByNameArgs)

            __props__.__dict__["access_recheck_offline_timeout"] = access_recheck_offline_timeout
            __props__.__dict__["access_recheck_online_timeout"] = access_recheck_online_timeout
            if app_sharing_from_level is None:
                app_sharing_from_level = 'none'
            __props__.__dict__["app_sharing_from_level"] = app_sharing_from_level
            if app_sharing_to_level is None:
                app_sharing_to_level = 'none'
            __props__.__dict__["app_sharing_to_level"] = app_sharing_to_level
            if authentication is None:
                authentication = 'required'
            __props__.__dict__["authentication"] = authentication
            if clipboard_sharing_level is None:
                clipboard_sharing_level = 'blocked'
            __props__.__dict__["clipboard_sharing_level"] = clipboard_sharing_level
            if data_backup is None:
                data_backup = 'allow'
            __props__.__dict__["data_backup"] = data_backup
            __props__.__dict__["description"] = description
            if device_compliance is None:
                device_compliance = 'enable'
            __props__.__dict__["device_compliance"] = device_compliance
            if file_encryption_level is None:
                file_encryption_level = 'deviceLocked'
            __props__.__dict__["file_encryption_level"] = file_encryption_level
            if file_sharing_save_as is None:
                file_sharing_save_as = 'allow'
            __props__.__dict__["file_sharing_save_as"] = file_sharing_save_as
            if friendly_name is None and not opts.urn:
                raise TypeError("Missing required property 'friendly_name'")
            __props__.__dict__["friendly_name"] = friendly_name
            if host_name is None and not opts.urn:
                raise TypeError("Missing required property 'host_name'")
            __props__.__dict__["host_name"] = host_name
            __props__.__dict__["location"] = location
            if managed_browser is None:
                managed_browser = 'required'
            __props__.__dict__["managed_browser"] = managed_browser
            __props__.__dict__["offline_wipe_timeout"] = offline_wipe_timeout
            if pin is None:
                pin = 'required'
            __props__.__dict__["pin"] = pin
            __props__.__dict__["pin_num_retry"] = pin_num_retry
            __props__.__dict__["policy_name"] = policy_name
            __props__.__dict__["tags"] = tags
            if touch_id is None:
                touch_id = 'enable'
            __props__.__dict__["touch_id"] = touch_id
            __props__.__dict__["group_status"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["num_of_apps"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:intune:IoMAMPolicyByName"), pulumi.Alias(type_="azure-native:intune/v20150114privatepreview:IoMAMPolicyByName")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IoMAMPolicyByName, __self__).__init__(
            'azure-native:intune/v20150114preview:IoMAMPolicyByName',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IoMAMPolicyByName':
        """
        Get an existing IoMAMPolicyByName resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IoMAMPolicyByNameArgs.__new__(IoMAMPolicyByNameArgs)

        __props__.__dict__["access_recheck_offline_timeout"] = None
        __props__.__dict__["access_recheck_online_timeout"] = None
        __props__.__dict__["app_sharing_from_level"] = None
        __props__.__dict__["app_sharing_to_level"] = None
        __props__.__dict__["authentication"] = None
        __props__.__dict__["clipboard_sharing_level"] = None
        __props__.__dict__["data_backup"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["device_compliance"] = None
        __props__.__dict__["file_encryption_level"] = None
        __props__.__dict__["file_sharing_save_as"] = None
        __props__.__dict__["friendly_name"] = None
        __props__.__dict__["group_status"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_browser"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["num_of_apps"] = None
        __props__.__dict__["offline_wipe_timeout"] = None
        __props__.__dict__["pin"] = None
        __props__.__dict__["pin_num_retry"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["touch_id"] = None
        __props__.__dict__["type"] = None
        return IoMAMPolicyByName(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessRecheckOfflineTimeout")
    def access_recheck_offline_timeout(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "access_recheck_offline_timeout")

    @property
    @pulumi.getter(name="accessRecheckOnlineTimeout")
    def access_recheck_online_timeout(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "access_recheck_online_timeout")

    @property
    @pulumi.getter(name="appSharingFromLevel")
    def app_sharing_from_level(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "app_sharing_from_level")

    @property
    @pulumi.getter(name="appSharingToLevel")
    def app_sharing_to_level(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "app_sharing_to_level")

    @property
    @pulumi.getter
    def authentication(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "authentication")

    @property
    @pulumi.getter(name="clipboardSharingLevel")
    def clipboard_sharing_level(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "clipboard_sharing_level")

    @property
    @pulumi.getter(name="dataBackup")
    def data_backup(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "data_backup")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceCompliance")
    def device_compliance(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "device_compliance")

    @property
    @pulumi.getter(name="fileEncryptionLevel")
    def file_encryption_level(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "file_encryption_level")

    @property
    @pulumi.getter(name="fileSharingSaveAs")
    def file_sharing_save_as(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "file_sharing_save_as")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="groupStatus")
    def group_status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "group_status")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedBrowser")
    def managed_browser(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "managed_browser")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numOfApps")
    def num_of_apps(self) -> pulumi.Output[int]:
        return pulumi.get(self, "num_of_apps")

    @property
    @pulumi.getter(name="offlineWipeTimeout")
    def offline_wipe_timeout(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "offline_wipe_timeout")

    @property
    @pulumi.getter
    def pin(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "pin")

    @property
    @pulumi.getter(name="pinNumRetry")
    def pin_num_retry(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "pin_num_retry")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource Tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="touchId")
    def touch_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "touch_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

