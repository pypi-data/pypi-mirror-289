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
    'GetStaticSiteResult',
    'AwaitableGetStaticSiteResult',
    'get_static_site',
    'get_static_site_output',
]

@pulumi.output_type
class GetStaticSiteResult:
    """
    Static Site ARM resource.
    """
    def __init__(__self__, allow_config_file_updates=None, branch=None, build_properties=None, content_distribution_endpoint=None, custom_domains=None, database_connections=None, default_hostname=None, enterprise_grade_cdn_status=None, id=None, identity=None, key_vault_reference_identity=None, kind=None, linked_backends=None, location=None, name=None, private_endpoint_connections=None, provider=None, public_network_access=None, repository_token=None, repository_url=None, sku=None, staging_environment_policy=None, tags=None, template_properties=None, type=None, user_provided_function_apps=None):
        if allow_config_file_updates and not isinstance(allow_config_file_updates, bool):
            raise TypeError("Expected argument 'allow_config_file_updates' to be a bool")
        pulumi.set(__self__, "allow_config_file_updates", allow_config_file_updates)
        if branch and not isinstance(branch, str):
            raise TypeError("Expected argument 'branch' to be a str")
        pulumi.set(__self__, "branch", branch)
        if build_properties and not isinstance(build_properties, dict):
            raise TypeError("Expected argument 'build_properties' to be a dict")
        pulumi.set(__self__, "build_properties", build_properties)
        if content_distribution_endpoint and not isinstance(content_distribution_endpoint, str):
            raise TypeError("Expected argument 'content_distribution_endpoint' to be a str")
        pulumi.set(__self__, "content_distribution_endpoint", content_distribution_endpoint)
        if custom_domains and not isinstance(custom_domains, list):
            raise TypeError("Expected argument 'custom_domains' to be a list")
        pulumi.set(__self__, "custom_domains", custom_domains)
        if database_connections and not isinstance(database_connections, list):
            raise TypeError("Expected argument 'database_connections' to be a list")
        pulumi.set(__self__, "database_connections", database_connections)
        if default_hostname and not isinstance(default_hostname, str):
            raise TypeError("Expected argument 'default_hostname' to be a str")
        pulumi.set(__self__, "default_hostname", default_hostname)
        if enterprise_grade_cdn_status and not isinstance(enterprise_grade_cdn_status, str):
            raise TypeError("Expected argument 'enterprise_grade_cdn_status' to be a str")
        pulumi.set(__self__, "enterprise_grade_cdn_status", enterprise_grade_cdn_status)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if key_vault_reference_identity and not isinstance(key_vault_reference_identity, str):
            raise TypeError("Expected argument 'key_vault_reference_identity' to be a str")
        pulumi.set(__self__, "key_vault_reference_identity", key_vault_reference_identity)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if linked_backends and not isinstance(linked_backends, list):
            raise TypeError("Expected argument 'linked_backends' to be a list")
        pulumi.set(__self__, "linked_backends", linked_backends)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if provider and not isinstance(provider, str):
            raise TypeError("Expected argument 'provider' to be a str")
        pulumi.set(__self__, "provider", provider)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if repository_token and not isinstance(repository_token, str):
            raise TypeError("Expected argument 'repository_token' to be a str")
        pulumi.set(__self__, "repository_token", repository_token)
        if repository_url and not isinstance(repository_url, str):
            raise TypeError("Expected argument 'repository_url' to be a str")
        pulumi.set(__self__, "repository_url", repository_url)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if staging_environment_policy and not isinstance(staging_environment_policy, str):
            raise TypeError("Expected argument 'staging_environment_policy' to be a str")
        pulumi.set(__self__, "staging_environment_policy", staging_environment_policy)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if template_properties and not isinstance(template_properties, dict):
            raise TypeError("Expected argument 'template_properties' to be a dict")
        pulumi.set(__self__, "template_properties", template_properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_provided_function_apps and not isinstance(user_provided_function_apps, list):
            raise TypeError("Expected argument 'user_provided_function_apps' to be a list")
        pulumi.set(__self__, "user_provided_function_apps", user_provided_function_apps)

    @property
    @pulumi.getter(name="allowConfigFileUpdates")
    def allow_config_file_updates(self) -> Optional[bool]:
        """
        <code>false</code> if config file is locked for this static web app; otherwise, <code>true</code>.
        """
        return pulumi.get(self, "allow_config_file_updates")

    @property
    @pulumi.getter
    def branch(self) -> Optional[str]:
        """
        The target branch in the repository.
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter(name="buildProperties")
    def build_properties(self) -> Optional['outputs.StaticSiteBuildPropertiesResponse']:
        """
        Build properties to configure on the repository.
        """
        return pulumi.get(self, "build_properties")

    @property
    @pulumi.getter(name="contentDistributionEndpoint")
    def content_distribution_endpoint(self) -> str:
        """
        The content distribution endpoint for the static site.
        """
        return pulumi.get(self, "content_distribution_endpoint")

    @property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Sequence[str]:
        """
        The custom domains associated with this static site.
        """
        return pulumi.get(self, "custom_domains")

    @property
    @pulumi.getter(name="databaseConnections")
    def database_connections(self) -> Sequence['outputs.DatabaseConnectionOverviewResponse']:
        """
        Database connections for the static site
        """
        return pulumi.get(self, "database_connections")

    @property
    @pulumi.getter(name="defaultHostname")
    def default_hostname(self) -> str:
        """
        The default autogenerated hostname for the static site.
        """
        return pulumi.get(self, "default_hostname")

    @property
    @pulumi.getter(name="enterpriseGradeCdnStatus")
    def enterprise_grade_cdn_status(self) -> Optional[str]:
        """
        State indicating the status of the enterprise grade CDN serving traffic to the static web app.
        """
        return pulumi.get(self, "enterprise_grade_cdn_status")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedServiceIdentityResponse']:
        """
        Managed service identity.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="keyVaultReferenceIdentity")
    def key_vault_reference_identity(self) -> str:
        """
        Identity to use for Key Vault Reference authentication.
        """
        return pulumi.get(self, "key_vault_reference_identity")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="linkedBackends")
    def linked_backends(self) -> Sequence['outputs.StaticSiteLinkedBackendResponse']:
        """
        Backends linked to the static side
        """
        return pulumi.get(self, "linked_backends")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource Location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.ResponseMessageEnvelopeRemotePrivateEndpointConnectionResponse']:
        """
        Private endpoint connections
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter
    def provider(self) -> Optional[str]:
        """
        The provider that submitted the last deployment to the primary environment of the static site.
        """
        return pulumi.get(self, "provider")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        State indicating whether public traffic are allowed or not for a static web app. Allowed Values: 'Enabled', 'Disabled' or an empty string.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="repositoryToken")
    def repository_token(self) -> Optional[str]:
        """
        A user's github repository token. This is used to setup the Github Actions workflow file and API secrets.
        """
        return pulumi.get(self, "repository_token")

    @property
    @pulumi.getter(name="repositoryUrl")
    def repository_url(self) -> Optional[str]:
        """
        URL for the repository of the static site.
        """
        return pulumi.get(self, "repository_url")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuDescriptionResponse']:
        """
        Description of a SKU for a scalable resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="stagingEnvironmentPolicy")
    def staging_environment_policy(self) -> Optional[str]:
        """
        State indicating whether staging environments are allowed or not allowed for a static web app.
        """
        return pulumi.get(self, "staging_environment_policy")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="templateProperties")
    def template_properties(self) -> Optional['outputs.StaticSiteTemplateOptionsResponse']:
        """
        Template options for generating a new repository.
        """
        return pulumi.get(self, "template_properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userProvidedFunctionApps")
    def user_provided_function_apps(self) -> Sequence['outputs.StaticSiteUserProvidedFunctionAppResponse']:
        """
        User provided function apps registered with the static site
        """
        return pulumi.get(self, "user_provided_function_apps")


class AwaitableGetStaticSiteResult(GetStaticSiteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStaticSiteResult(
            allow_config_file_updates=self.allow_config_file_updates,
            branch=self.branch,
            build_properties=self.build_properties,
            content_distribution_endpoint=self.content_distribution_endpoint,
            custom_domains=self.custom_domains,
            database_connections=self.database_connections,
            default_hostname=self.default_hostname,
            enterprise_grade_cdn_status=self.enterprise_grade_cdn_status,
            id=self.id,
            identity=self.identity,
            key_vault_reference_identity=self.key_vault_reference_identity,
            kind=self.kind,
            linked_backends=self.linked_backends,
            location=self.location,
            name=self.name,
            private_endpoint_connections=self.private_endpoint_connections,
            provider=self.provider,
            public_network_access=self.public_network_access,
            repository_token=self.repository_token,
            repository_url=self.repository_url,
            sku=self.sku,
            staging_environment_policy=self.staging_environment_policy,
            tags=self.tags,
            template_properties=self.template_properties,
            type=self.type,
            user_provided_function_apps=self.user_provided_function_apps)


def get_static_site(name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStaticSiteResult:
    """
    Description for Gets the details of a static site.


    :param str name: Name of the static site.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20220901:getStaticSite', __args__, opts=opts, typ=GetStaticSiteResult).value

    return AwaitableGetStaticSiteResult(
        allow_config_file_updates=pulumi.get(__ret__, 'allow_config_file_updates'),
        branch=pulumi.get(__ret__, 'branch'),
        build_properties=pulumi.get(__ret__, 'build_properties'),
        content_distribution_endpoint=pulumi.get(__ret__, 'content_distribution_endpoint'),
        custom_domains=pulumi.get(__ret__, 'custom_domains'),
        database_connections=pulumi.get(__ret__, 'database_connections'),
        default_hostname=pulumi.get(__ret__, 'default_hostname'),
        enterprise_grade_cdn_status=pulumi.get(__ret__, 'enterprise_grade_cdn_status'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        key_vault_reference_identity=pulumi.get(__ret__, 'key_vault_reference_identity'),
        kind=pulumi.get(__ret__, 'kind'),
        linked_backends=pulumi.get(__ret__, 'linked_backends'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        provider=pulumi.get(__ret__, 'provider'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        repository_token=pulumi.get(__ret__, 'repository_token'),
        repository_url=pulumi.get(__ret__, 'repository_url'),
        sku=pulumi.get(__ret__, 'sku'),
        staging_environment_policy=pulumi.get(__ret__, 'staging_environment_policy'),
        tags=pulumi.get(__ret__, 'tags'),
        template_properties=pulumi.get(__ret__, 'template_properties'),
        type=pulumi.get(__ret__, 'type'),
        user_provided_function_apps=pulumi.get(__ret__, 'user_provided_function_apps'))


@_utilities.lift_output_func(get_static_site)
def get_static_site_output(name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStaticSiteResult]:
    """
    Description for Gets the details of a static site.


    :param str name: Name of the static site.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
