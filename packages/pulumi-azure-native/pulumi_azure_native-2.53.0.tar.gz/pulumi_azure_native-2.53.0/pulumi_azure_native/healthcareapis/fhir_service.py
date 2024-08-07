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
from ._enums import *
from ._inputs import *

__all__ = ['FhirServiceArgs', 'FhirService']

@pulumi.input_type
class FhirServiceArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 access_policies: Optional[pulumi.Input[Sequence[pulumi.Input['FhirServiceAccessPolicyEntryArgs']]]] = None,
                 acr_configuration: Optional[pulumi.Input['FhirServiceAcrConfigurationArgs']] = None,
                 authentication_configuration: Optional[pulumi.Input['FhirServiceAuthenticationConfigurationArgs']] = None,
                 cors_configuration: Optional[pulumi.Input['FhirServiceCorsConfigurationArgs']] = None,
                 export_configuration: Optional[pulumi.Input['FhirServiceExportConfigurationArgs']] = None,
                 fhir_service_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['ServiceManagedIdentityIdentityArgs']] = None,
                 implementation_guides_configuration: Optional[pulumi.Input['ImplementationGuidesConfigurationArgs']] = None,
                 import_configuration: Optional[pulumi.Input['FhirServiceImportConfigurationArgs']] = None,
                 kind: Optional[pulumi.Input[Union[str, 'FhirServiceKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_version_policy_configuration: Optional[pulumi.Input['ResourceVersionPolicyConfigurationArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a FhirService resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the service instance.
        :param pulumi.Input[str] workspace_name: The name of workspace resource.
        :param pulumi.Input[Sequence[pulumi.Input['FhirServiceAccessPolicyEntryArgs']]] access_policies: Fhir Service access policies.
        :param pulumi.Input['FhirServiceAcrConfigurationArgs'] acr_configuration: Fhir Service Azure container registry configuration.
        :param pulumi.Input['FhirServiceAuthenticationConfigurationArgs'] authentication_configuration: Fhir Service authentication configuration.
        :param pulumi.Input['FhirServiceCorsConfigurationArgs'] cors_configuration: Fhir Service Cors configuration.
        :param pulumi.Input['FhirServiceExportConfigurationArgs'] export_configuration: Fhir Service export configuration.
        :param pulumi.Input[str] fhir_service_name: The name of FHIR Service resource.
        :param pulumi.Input['ServiceManagedIdentityIdentityArgs'] identity: Setting indicating whether the service has a managed identity associated with it.
        :param pulumi.Input['ImplementationGuidesConfigurationArgs'] implementation_guides_configuration: Implementation Guides configuration.
        :param pulumi.Input['FhirServiceImportConfigurationArgs'] import_configuration: Fhir Service import configuration.
        :param pulumi.Input[Union[str, 'FhirServiceKind']] kind: The kind of the service.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input['ResourceVersionPolicyConfigurationArgs'] resource_version_policy_configuration: Determines tracking of history for resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if access_policies is not None:
            pulumi.set(__self__, "access_policies", access_policies)
        if acr_configuration is not None:
            pulumi.set(__self__, "acr_configuration", acr_configuration)
        if authentication_configuration is not None:
            pulumi.set(__self__, "authentication_configuration", authentication_configuration)
        if cors_configuration is not None:
            pulumi.set(__self__, "cors_configuration", cors_configuration)
        if export_configuration is not None:
            pulumi.set(__self__, "export_configuration", export_configuration)
        if fhir_service_name is not None:
            pulumi.set(__self__, "fhir_service_name", fhir_service_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if implementation_guides_configuration is not None:
            pulumi.set(__self__, "implementation_guides_configuration", implementation_guides_configuration)
        if import_configuration is not None:
            pulumi.set(__self__, "import_configuration", import_configuration)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if resource_version_policy_configuration is not None:
            pulumi.set(__self__, "resource_version_policy_configuration", resource_version_policy_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the service instance.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of workspace resource.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FhirServiceAccessPolicyEntryArgs']]]]:
        """
        Fhir Service access policies.
        """
        return pulumi.get(self, "access_policies")

    @access_policies.setter
    def access_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FhirServiceAccessPolicyEntryArgs']]]]):
        pulumi.set(self, "access_policies", value)

    @property
    @pulumi.getter(name="acrConfiguration")
    def acr_configuration(self) -> Optional[pulumi.Input['FhirServiceAcrConfigurationArgs']]:
        """
        Fhir Service Azure container registry configuration.
        """
        return pulumi.get(self, "acr_configuration")

    @acr_configuration.setter
    def acr_configuration(self, value: Optional[pulumi.Input['FhirServiceAcrConfigurationArgs']]):
        pulumi.set(self, "acr_configuration", value)

    @property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> Optional[pulumi.Input['FhirServiceAuthenticationConfigurationArgs']]:
        """
        Fhir Service authentication configuration.
        """
        return pulumi.get(self, "authentication_configuration")

    @authentication_configuration.setter
    def authentication_configuration(self, value: Optional[pulumi.Input['FhirServiceAuthenticationConfigurationArgs']]):
        pulumi.set(self, "authentication_configuration", value)

    @property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> Optional[pulumi.Input['FhirServiceCorsConfigurationArgs']]:
        """
        Fhir Service Cors configuration.
        """
        return pulumi.get(self, "cors_configuration")

    @cors_configuration.setter
    def cors_configuration(self, value: Optional[pulumi.Input['FhirServiceCorsConfigurationArgs']]):
        pulumi.set(self, "cors_configuration", value)

    @property
    @pulumi.getter(name="exportConfiguration")
    def export_configuration(self) -> Optional[pulumi.Input['FhirServiceExportConfigurationArgs']]:
        """
        Fhir Service export configuration.
        """
        return pulumi.get(self, "export_configuration")

    @export_configuration.setter
    def export_configuration(self, value: Optional[pulumi.Input['FhirServiceExportConfigurationArgs']]):
        pulumi.set(self, "export_configuration", value)

    @property
    @pulumi.getter(name="fhirServiceName")
    def fhir_service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of FHIR Service resource.
        """
        return pulumi.get(self, "fhir_service_name")

    @fhir_service_name.setter
    def fhir_service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fhir_service_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ServiceManagedIdentityIdentityArgs']]:
        """
        Setting indicating whether the service has a managed identity associated with it.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ServiceManagedIdentityIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="implementationGuidesConfiguration")
    def implementation_guides_configuration(self) -> Optional[pulumi.Input['ImplementationGuidesConfigurationArgs']]:
        """
        Implementation Guides configuration.
        """
        return pulumi.get(self, "implementation_guides_configuration")

    @implementation_guides_configuration.setter
    def implementation_guides_configuration(self, value: Optional[pulumi.Input['ImplementationGuidesConfigurationArgs']]):
        pulumi.set(self, "implementation_guides_configuration", value)

    @property
    @pulumi.getter(name="importConfiguration")
    def import_configuration(self) -> Optional[pulumi.Input['FhirServiceImportConfigurationArgs']]:
        """
        Fhir Service import configuration.
        """
        return pulumi.get(self, "import_configuration")

    @import_configuration.setter
    def import_configuration(self, value: Optional[pulumi.Input['FhirServiceImportConfigurationArgs']]):
        pulumi.set(self, "import_configuration", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[str, 'FhirServiceKind']]]:
        """
        The kind of the service.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[str, 'FhirServiceKind']]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="resourceVersionPolicyConfiguration")
    def resource_version_policy_configuration(self) -> Optional[pulumi.Input['ResourceVersionPolicyConfigurationArgs']]:
        """
        Determines tracking of history for resources.
        """
        return pulumi.get(self, "resource_version_policy_configuration")

    @resource_version_policy_configuration.setter
    def resource_version_policy_configuration(self, value: Optional[pulumi.Input['ResourceVersionPolicyConfigurationArgs']]):
        pulumi.set(self, "resource_version_policy_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class FhirService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_policies: Optional[pulumi.Input[Sequence[pulumi.Input[Union['FhirServiceAccessPolicyEntryArgs', 'FhirServiceAccessPolicyEntryArgsDict']]]]] = None,
                 acr_configuration: Optional[pulumi.Input[Union['FhirServiceAcrConfigurationArgs', 'FhirServiceAcrConfigurationArgsDict']]] = None,
                 authentication_configuration: Optional[pulumi.Input[Union['FhirServiceAuthenticationConfigurationArgs', 'FhirServiceAuthenticationConfigurationArgsDict']]] = None,
                 cors_configuration: Optional[pulumi.Input[Union['FhirServiceCorsConfigurationArgs', 'FhirServiceCorsConfigurationArgsDict']]] = None,
                 export_configuration: Optional[pulumi.Input[Union['FhirServiceExportConfigurationArgs', 'FhirServiceExportConfigurationArgsDict']]] = None,
                 fhir_service_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['ServiceManagedIdentityIdentityArgs', 'ServiceManagedIdentityIdentityArgsDict']]] = None,
                 implementation_guides_configuration: Optional[pulumi.Input[Union['ImplementationGuidesConfigurationArgs', 'ImplementationGuidesConfigurationArgsDict']]] = None,
                 import_configuration: Optional[pulumi.Input[Union['FhirServiceImportConfigurationArgs', 'FhirServiceImportConfigurationArgsDict']]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'FhirServiceKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_version_policy_configuration: Optional[pulumi.Input[Union['ResourceVersionPolicyConfigurationArgs', 'ResourceVersionPolicyConfigurationArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The description of Fhir Service
        Azure REST API version: 2023-02-28. Prior API version in Azure Native 1.x: 2022-05-15.

        Other available API versions: 2023-09-06, 2023-11-01, 2023-12-01, 2024-03-01, 2024-03-31.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['FhirServiceAccessPolicyEntryArgs', 'FhirServiceAccessPolicyEntryArgsDict']]]] access_policies: Fhir Service access policies.
        :param pulumi.Input[Union['FhirServiceAcrConfigurationArgs', 'FhirServiceAcrConfigurationArgsDict']] acr_configuration: Fhir Service Azure container registry configuration.
        :param pulumi.Input[Union['FhirServiceAuthenticationConfigurationArgs', 'FhirServiceAuthenticationConfigurationArgsDict']] authentication_configuration: Fhir Service authentication configuration.
        :param pulumi.Input[Union['FhirServiceCorsConfigurationArgs', 'FhirServiceCorsConfigurationArgsDict']] cors_configuration: Fhir Service Cors configuration.
        :param pulumi.Input[Union['FhirServiceExportConfigurationArgs', 'FhirServiceExportConfigurationArgsDict']] export_configuration: Fhir Service export configuration.
        :param pulumi.Input[str] fhir_service_name: The name of FHIR Service resource.
        :param pulumi.Input[Union['ServiceManagedIdentityIdentityArgs', 'ServiceManagedIdentityIdentityArgsDict']] identity: Setting indicating whether the service has a managed identity associated with it.
        :param pulumi.Input[Union['ImplementationGuidesConfigurationArgs', 'ImplementationGuidesConfigurationArgsDict']] implementation_guides_configuration: Implementation Guides configuration.
        :param pulumi.Input[Union['FhirServiceImportConfigurationArgs', 'FhirServiceImportConfigurationArgsDict']] import_configuration: Fhir Service import configuration.
        :param pulumi.Input[Union[str, 'FhirServiceKind']] kind: The kind of the service.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the service instance.
        :param pulumi.Input[Union['ResourceVersionPolicyConfigurationArgs', 'ResourceVersionPolicyConfigurationArgsDict']] resource_version_policy_configuration: Determines tracking of history for resources.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] workspace_name: The name of workspace resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FhirServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The description of Fhir Service
        Azure REST API version: 2023-02-28. Prior API version in Azure Native 1.x: 2022-05-15.

        Other available API versions: 2023-09-06, 2023-11-01, 2023-12-01, 2024-03-01, 2024-03-31.

        :param str resource_name: The name of the resource.
        :param FhirServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FhirServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_policies: Optional[pulumi.Input[Sequence[pulumi.Input[Union['FhirServiceAccessPolicyEntryArgs', 'FhirServiceAccessPolicyEntryArgsDict']]]]] = None,
                 acr_configuration: Optional[pulumi.Input[Union['FhirServiceAcrConfigurationArgs', 'FhirServiceAcrConfigurationArgsDict']]] = None,
                 authentication_configuration: Optional[pulumi.Input[Union['FhirServiceAuthenticationConfigurationArgs', 'FhirServiceAuthenticationConfigurationArgsDict']]] = None,
                 cors_configuration: Optional[pulumi.Input[Union['FhirServiceCorsConfigurationArgs', 'FhirServiceCorsConfigurationArgsDict']]] = None,
                 export_configuration: Optional[pulumi.Input[Union['FhirServiceExportConfigurationArgs', 'FhirServiceExportConfigurationArgsDict']]] = None,
                 fhir_service_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['ServiceManagedIdentityIdentityArgs', 'ServiceManagedIdentityIdentityArgsDict']]] = None,
                 implementation_guides_configuration: Optional[pulumi.Input[Union['ImplementationGuidesConfigurationArgs', 'ImplementationGuidesConfigurationArgsDict']]] = None,
                 import_configuration: Optional[pulumi.Input[Union['FhirServiceImportConfigurationArgs', 'FhirServiceImportConfigurationArgsDict']]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'FhirServiceKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_version_policy_configuration: Optional[pulumi.Input[Union['ResourceVersionPolicyConfigurationArgs', 'ResourceVersionPolicyConfigurationArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FhirServiceArgs.__new__(FhirServiceArgs)

            __props__.__dict__["access_policies"] = access_policies
            __props__.__dict__["acr_configuration"] = acr_configuration
            __props__.__dict__["authentication_configuration"] = authentication_configuration
            __props__.__dict__["cors_configuration"] = cors_configuration
            __props__.__dict__["export_configuration"] = export_configuration
            __props__.__dict__["fhir_service_name"] = fhir_service_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["implementation_guides_configuration"] = implementation_guides_configuration
            __props__.__dict__["import_configuration"] = import_configuration
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_version_policy_configuration"] = resource_version_policy_configuration
            __props__.__dict__["tags"] = tags
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["event_state"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_connections"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["public_network_access"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:healthcareapis/v20210601preview:FhirService"), pulumi.Alias(type_="azure-native:healthcareapis/v20211101:FhirService"), pulumi.Alias(type_="azure-native:healthcareapis/v20220131preview:FhirService"), pulumi.Alias(type_="azure-native:healthcareapis/v20220515:FhirService"), pulumi.Alias(type_="azure-native:healthcareapis/v20220601:FhirService"), pulumi.Alias(type_="azure-native:healthcareapis/v20221001preview:FhirService"), pulumi.Alias(type_="azure-native:healthcareapis/v20221201:FhirService"), pulumi.Alias(type_="azure-native:healthcareapis/v20230228:FhirService"), pulumi.Alias(type_="azure-native:healthcareapis/v20230906:FhirService"), pulumi.Alias(type_="azure-native:healthcareapis/v20231101:FhirService"), pulumi.Alias(type_="azure-native:healthcareapis/v20231201:FhirService"), pulumi.Alias(type_="azure-native:healthcareapis/v20240301:FhirService"), pulumi.Alias(type_="azure-native:healthcareapis/v20240331:FhirService")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(FhirService, __self__).__init__(
            'azure-native:healthcareapis:FhirService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FhirService':
        """
        Get an existing FhirService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FhirServiceArgs.__new__(FhirServiceArgs)

        __props__.__dict__["access_policies"] = None
        __props__.__dict__["acr_configuration"] = None
        __props__.__dict__["authentication_configuration"] = None
        __props__.__dict__["cors_configuration"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["event_state"] = None
        __props__.__dict__["export_configuration"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["implementation_guides_configuration"] = None
        __props__.__dict__["import_configuration"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["resource_version_policy_configuration"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return FhirService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> pulumi.Output[Optional[Sequence['outputs.FhirServiceAccessPolicyEntryResponse']]]:
        """
        Fhir Service access policies.
        """
        return pulumi.get(self, "access_policies")

    @property
    @pulumi.getter(name="acrConfiguration")
    def acr_configuration(self) -> pulumi.Output[Optional['outputs.FhirServiceAcrConfigurationResponse']]:
        """
        Fhir Service Azure container registry configuration.
        """
        return pulumi.get(self, "acr_configuration")

    @property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> pulumi.Output[Optional['outputs.FhirServiceAuthenticationConfigurationResponse']]:
        """
        Fhir Service authentication configuration.
        """
        return pulumi.get(self, "authentication_configuration")

    @property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> pulumi.Output[Optional['outputs.FhirServiceCorsConfigurationResponse']]:
        """
        Fhir Service Cors configuration.
        """
        return pulumi.get(self, "cors_configuration")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        An etag associated with the resource, used for optimistic concurrency when editing it.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="eventState")
    def event_state(self) -> pulumi.Output[str]:
        """
        Fhir Service event support status.
        """
        return pulumi.get(self, "event_state")

    @property
    @pulumi.getter(name="exportConfiguration")
    def export_configuration(self) -> pulumi.Output[Optional['outputs.FhirServiceExportConfigurationResponse']]:
        """
        Fhir Service export configuration.
        """
        return pulumi.get(self, "export_configuration")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ServiceManagedIdentityResponseIdentity']]:
        """
        Setting indicating whether the service has a managed identity associated with it.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="implementationGuidesConfiguration")
    def implementation_guides_configuration(self) -> pulumi.Output[Optional['outputs.ImplementationGuidesConfigurationResponse']]:
        """
        Implementation Guides configuration.
        """
        return pulumi.get(self, "implementation_guides_configuration")

    @property
    @pulumi.getter(name="importConfiguration")
    def import_configuration(self) -> pulumi.Output[Optional['outputs.FhirServiceImportConfigurationResponse']]:
        """
        Fhir Service import configuration.
        """
        return pulumi.get(self, "import_configuration")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        The kind of the service.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        """
        The list of private endpoint connections that are set up for this resource.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[str]:
        """
        Control permission for data plane traffic coming from public networks while private endpoint is enabled.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="resourceVersionPolicyConfiguration")
    def resource_version_policy_configuration(self) -> pulumi.Output[Optional['outputs.ResourceVersionPolicyConfigurationResponse']]:
        """
        Determines tracking of history for resources.
        """
        return pulumi.get(self, "resource_version_policy_configuration")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

