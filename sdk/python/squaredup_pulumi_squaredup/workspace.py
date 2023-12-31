# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['WorkspaceArgs', 'Workspace']

@pulumi.input_type
class WorkspaceArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 datasources_links: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 open_access_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 workspaces_links: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Workspace resource.
        :param pulumi.Input[str] display_name: The display name of the workspace (Displayed in SquaredUp)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] datasources_links: Links to plugins
        :param pulumi.Input[str] description: The description of the workspace
        :param pulumi.Input[bool] open_access_enabled: Whether open access is enabled for the workspace
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the workspace
        :param pulumi.Input[str] type: Workspace type that can be one of: 'service', 'team', 'application', 'platform', 'product', 'business service', 'microservice', 'customer', 'website', 'component', 'resource', 'system', 'folder', 'other'.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] workspaces_links: Links to workspaces
        """
        pulumi.set(__self__, "display_name", display_name)
        if datasources_links is not None:
            pulumi.set(__self__, "datasources_links", datasources_links)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if open_access_enabled is not None:
            pulumi.set(__self__, "open_access_enabled", open_access_enabled)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if workspaces_links is not None:
            pulumi.set(__self__, "workspaces_links", workspaces_links)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the workspace (Displayed in SquaredUp)
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="datasourcesLinks")
    def datasources_links(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Links to plugins
        """
        return pulumi.get(self, "datasources_links")

    @datasources_links.setter
    def datasources_links(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "datasources_links", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the workspace
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="openAccessEnabled")
    def open_access_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether open access is enabled for the workspace
        """
        return pulumi.get(self, "open_access_enabled")

    @open_access_enabled.setter
    def open_access_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "open_access_enabled", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags of the workspace
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Workspace type that can be one of: 'service', 'team', 'application', 'platform', 'product', 'business service', 'microservice', 'customer', 'website', 'component', 'resource', 'system', 'folder', 'other'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="workspacesLinks")
    def workspaces_links(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Links to workspaces
        """
        return pulumi.get(self, "workspaces_links")

    @workspaces_links.setter
    def workspaces_links(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "workspaces_links", value)


@pulumi.input_type
class _WorkspaceState:
    def __init__(__self__, *,
                 datasources_links: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 last_updated: Optional[pulumi.Input[str]] = None,
                 open_access_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 workspaces_links: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Workspace resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] datasources_links: Links to plugins
        :param pulumi.Input[str] description: The description of the workspace
        :param pulumi.Input[str] display_name: The display name of the workspace (Displayed in SquaredUp)
        :param pulumi.Input[str] last_updated: The last time the workspace was updated
        :param pulumi.Input[bool] open_access_enabled: Whether open access is enabled for the workspace
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the workspace
        :param pulumi.Input[str] type: Workspace type that can be one of: 'service', 'team', 'application', 'platform', 'product', 'business service', 'microservice', 'customer', 'website', 'component', 'resource', 'system', 'folder', 'other'.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] workspaces_links: Links to workspaces
        """
        if datasources_links is not None:
            pulumi.set(__self__, "datasources_links", datasources_links)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if last_updated is not None:
            pulumi.set(__self__, "last_updated", last_updated)
        if open_access_enabled is not None:
            pulumi.set(__self__, "open_access_enabled", open_access_enabled)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if workspaces_links is not None:
            pulumi.set(__self__, "workspaces_links", workspaces_links)

    @property
    @pulumi.getter(name="datasourcesLinks")
    def datasources_links(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Links to plugins
        """
        return pulumi.get(self, "datasources_links")

    @datasources_links.setter
    def datasources_links(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "datasources_links", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the workspace
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the workspace (Displayed in SquaredUp)
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The last time the workspace was updated
        """
        return pulumi.get(self, "last_updated")

    @last_updated.setter
    def last_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated", value)

    @property
    @pulumi.getter(name="openAccessEnabled")
    def open_access_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether open access is enabled for the workspace
        """
        return pulumi.get(self, "open_access_enabled")

    @open_access_enabled.setter
    def open_access_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "open_access_enabled", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The tags of the workspace
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Workspace type that can be one of: 'service', 'team', 'application', 'platform', 'product', 'business service', 'microservice', 'customer', 'website', 'component', 'resource', 'system', 'folder', 'other'.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="workspacesLinks")
    def workspaces_links(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Links to workspaces
        """
        return pulumi.get(self, "workspaces_links")

    @workspaces_links.setter
    def workspaces_links(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "workspaces_links", value)


class Workspace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datasources_links: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 open_access_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 workspaces_links: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Each workspace has its own dashboards, data sources, monitors and scopes.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_squaredup as squaredup
        import squaredup_pulumi_squaredup as squaredup

        sample_data = squaredup.get_datasources(data_source_name="Sample Data")
        sample_data_source = squaredup.Datasource("sampleDataSource",
            display_name="Sample Data",
            data_source_name=sample_data.plugins[0].display_name)
        application_workspace = squaredup.Workspace("applicationWorkspace",
            display_name="Application Team",
            description="Workspace with Dashboards for Application Team")
        devops_workspace = squaredup.Workspace("devopsWorkspace",
            display_name="DevOps Team",
            description="Workspace with Dashboards for DevOps Team",
            type="application",
            tags=[
                "terraform",
                "auto-created",
            ],
            open_access_enabled=True,
            workspaces_links=[application_workspace.id],
            datasources_links=[sample_data_source.id])
        ```

        ## Import

        Workspaces can be imported by specifying workspace id.

        ```sh
         $ pulumi import squaredup:index/workspace:Workspace example space-123
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] datasources_links: Links to plugins
        :param pulumi.Input[str] description: The description of the workspace
        :param pulumi.Input[str] display_name: The display name of the workspace (Displayed in SquaredUp)
        :param pulumi.Input[bool] open_access_enabled: Whether open access is enabled for the workspace
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the workspace
        :param pulumi.Input[str] type: Workspace type that can be one of: 'service', 'team', 'application', 'platform', 'product', 'business service', 'microservice', 'customer', 'website', 'component', 'resource', 'system', 'folder', 'other'.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] workspaces_links: Links to workspaces
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Each workspace has its own dashboards, data sources, monitors and scopes.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_squaredup as squaredup
        import squaredup_pulumi_squaredup as squaredup

        sample_data = squaredup.get_datasources(data_source_name="Sample Data")
        sample_data_source = squaredup.Datasource("sampleDataSource",
            display_name="Sample Data",
            data_source_name=sample_data.plugins[0].display_name)
        application_workspace = squaredup.Workspace("applicationWorkspace",
            display_name="Application Team",
            description="Workspace with Dashboards for Application Team")
        devops_workspace = squaredup.Workspace("devopsWorkspace",
            display_name="DevOps Team",
            description="Workspace with Dashboards for DevOps Team",
            type="application",
            tags=[
                "terraform",
                "auto-created",
            ],
            open_access_enabled=True,
            workspaces_links=[application_workspace.id],
            datasources_links=[sample_data_source.id])
        ```

        ## Import

        Workspaces can be imported by specifying workspace id.

        ```sh
         $ pulumi import squaredup:index/workspace:Workspace example space-123
        ```

        :param str resource_name: The name of the resource.
        :param WorkspaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datasources_links: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 open_access_enabled: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 workspaces_links: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceArgs.__new__(WorkspaceArgs)

            __props__.__dict__["datasources_links"] = datasources_links
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["open_access_enabled"] = open_access_enabled
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
            __props__.__dict__["workspaces_links"] = workspaces_links
            __props__.__dict__["last_updated"] = None
        super(Workspace, __self__).__init__(
            'squaredup:index/workspace:Workspace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datasources_links: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            last_updated: Optional[pulumi.Input[str]] = None,
            open_access_enabled: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            workspaces_links: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Workspace':
        """
        Get an existing Workspace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] datasources_links: Links to plugins
        :param pulumi.Input[str] description: The description of the workspace
        :param pulumi.Input[str] display_name: The display name of the workspace (Displayed in SquaredUp)
        :param pulumi.Input[str] last_updated: The last time the workspace was updated
        :param pulumi.Input[bool] open_access_enabled: Whether open access is enabled for the workspace
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: The tags of the workspace
        :param pulumi.Input[str] type: Workspace type that can be one of: 'service', 'team', 'application', 'platform', 'product', 'business service', 'microservice', 'customer', 'website', 'component', 'resource', 'system', 'folder', 'other'.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] workspaces_links: Links to workspaces
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkspaceState.__new__(_WorkspaceState)

        __props__.__dict__["datasources_links"] = datasources_links
        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["last_updated"] = last_updated
        __props__.__dict__["open_access_enabled"] = open_access_enabled
        __props__.__dict__["tags"] = tags
        __props__.__dict__["type"] = type
        __props__.__dict__["workspaces_links"] = workspaces_links
        return Workspace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="datasourcesLinks")
    def datasources_links(self) -> pulumi.Output[Sequence[str]]:
        """
        Links to plugins
        """
        return pulumi.get(self, "datasources_links")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the workspace
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the workspace (Displayed in SquaredUp)
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> pulumi.Output[str]:
        """
        The last time the workspace was updated
        """
        return pulumi.get(self, "last_updated")

    @property
    @pulumi.getter(name="openAccessEnabled")
    def open_access_enabled(self) -> pulumi.Output[bool]:
        """
        Whether open access is enabled for the workspace
        """
        return pulumi.get(self, "open_access_enabled")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[str]]:
        """
        The tags of the workspace
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Workspace type that can be one of: 'service', 'team', 'application', 'platform', 'product', 'business service', 'microservice', 'customer', 'website', 'component', 'resource', 'system', 'folder', 'other'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="workspacesLinks")
    def workspaces_links(self) -> pulumi.Output[Sequence[str]]:
        """
        Links to workspaces
        """
        return pulumi.get(self, "workspaces_links")

