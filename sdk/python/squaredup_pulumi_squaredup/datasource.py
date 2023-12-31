# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DatasourceArgs', 'Datasource']

@pulumi.input_type
class DatasourceArgs:
    def __init__(__self__, *,
                 data_source_name: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 agent_group_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Datasource resource.
        :param pulumi.Input[str] data_source_name: Display name of the data source
        :param pulumi.Input[str] display_name: The display name of the data source (Displayed in SquaredUp)
        :param pulumi.Input[str] agent_group_id: The ID of the agent group to which the data source should connect to (on-prem data sources only)
        :param pulumi.Input[str] config: Sensitive configuration for the data source. Needs to be a valid JSON
        """
        pulumi.set(__self__, "data_source_name", data_source_name)
        pulumi.set(__self__, "display_name", display_name)
        if agent_group_id is not None:
            pulumi.set(__self__, "agent_group_id", agent_group_id)
        if config is not None:
            pulumi.set(__self__, "config", config)

    @property
    @pulumi.getter(name="dataSourceName")
    def data_source_name(self) -> pulumi.Input[str]:
        """
        Display name of the data source
        """
        return pulumi.get(self, "data_source_name")

    @data_source_name.setter
    def data_source_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_source_name", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the data source (Displayed in SquaredUp)
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="agentGroupId")
    def agent_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the agent group to which the data source should connect to (on-prem data sources only)
        """
        return pulumi.get(self, "agent_group_id")

    @agent_group_id.setter
    def agent_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_group_id", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[str]]:
        """
        Sensitive configuration for the data source. Needs to be a valid JSON
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config", value)


@pulumi.input_type
class _DatasourceState:
    def __init__(__self__, *,
                 agent_group_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 data_source_name: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 last_updated: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Datasource resources.
        :param pulumi.Input[str] agent_group_id: The ID of the agent group to which the data source should connect to (on-prem data sources only)
        :param pulumi.Input[str] config: Sensitive configuration for the data source. Needs to be a valid JSON
        :param pulumi.Input[str] data_source_name: Display name of the data source
        :param pulumi.Input[str] display_name: The display name of the data source (Displayed in SquaredUp)
        :param pulumi.Input[str] last_updated: The last time the data source was updated
        """
        if agent_group_id is not None:
            pulumi.set(__self__, "agent_group_id", agent_group_id)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if data_source_name is not None:
            pulumi.set(__self__, "data_source_name", data_source_name)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if last_updated is not None:
            pulumi.set(__self__, "last_updated", last_updated)

    @property
    @pulumi.getter(name="agentGroupId")
    def agent_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the agent group to which the data source should connect to (on-prem data sources only)
        """
        return pulumi.get(self, "agent_group_id")

    @agent_group_id.setter
    def agent_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "agent_group_id", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[str]]:
        """
        Sensitive configuration for the data source. Needs to be a valid JSON
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter(name="dataSourceName")
    def data_source_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the data source
        """
        return pulumi.get(self, "data_source_name")

    @data_source_name.setter
    def data_source_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_source_name", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the data source (Displayed in SquaredUp)
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> Optional[pulumi.Input[str]]:
        """
        The last time the data source was updated
        """
        return pulumi.get(self, "last_updated")

    @last_updated.setter
    def last_updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_updated", value)


class Datasource(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_group_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 data_source_name: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Data Sources are used to query third party APIs and SquaredUp visualizes the results

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_squaredup as squaredup
        import squaredup_pulumi_squaredup as squaredup

        sample_data = squaredup.get_datasources(data_source_name="Sample Data")
        sample_data_source = squaredup.Datasource("sampleDataSource",
            display_name="Sample Data",
            data_source_name=sample_data.plugins[0].display_name)
        ado_datasource = squaredup.Datasource("adoDatasource",
            display_name="Azure DevOps",
            data_source_name="Azure DevOps",
            config=json.dumps({
                "org": "org-name",
                "accessToken": "access-token",
            }))
        ```

        ## Import

        Data Source can be imported by specifying datasource id.

        ```sh
         $ pulumi import squaredup:index/datasource:Datasource example config-123
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_group_id: The ID of the agent group to which the data source should connect to (on-prem data sources only)
        :param pulumi.Input[str] config: Sensitive configuration for the data source. Needs to be a valid JSON
        :param pulumi.Input[str] data_source_name: Display name of the data source
        :param pulumi.Input[str] display_name: The display name of the data source (Displayed in SquaredUp)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatasourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Data Sources are used to query third party APIs and SquaredUp visualizes the results

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_squaredup as squaredup
        import squaredup_pulumi_squaredup as squaredup

        sample_data = squaredup.get_datasources(data_source_name="Sample Data")
        sample_data_source = squaredup.Datasource("sampleDataSource",
            display_name="Sample Data",
            data_source_name=sample_data.plugins[0].display_name)
        ado_datasource = squaredup.Datasource("adoDatasource",
            display_name="Azure DevOps",
            data_source_name="Azure DevOps",
            config=json.dumps({
                "org": "org-name",
                "accessToken": "access-token",
            }))
        ```

        ## Import

        Data Source can be imported by specifying datasource id.

        ```sh
         $ pulumi import squaredup:index/datasource:Datasource example config-123
        ```

        :param str resource_name: The name of the resource.
        :param DatasourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatasourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_group_id: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 data_source_name: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DatasourceArgs.__new__(DatasourceArgs)

            __props__.__dict__["agent_group_id"] = agent_group_id
            __props__.__dict__["config"] = None if config is None else pulumi.Output.secret(config)
            if data_source_name is None and not opts.urn:
                raise TypeError("Missing required property 'data_source_name'")
            __props__.__dict__["data_source_name"] = data_source_name
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["last_updated"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["config"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Datasource, __self__).__init__(
            'squaredup:index/datasource:Datasource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            agent_group_id: Optional[pulumi.Input[str]] = None,
            config: Optional[pulumi.Input[str]] = None,
            data_source_name: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            last_updated: Optional[pulumi.Input[str]] = None) -> 'Datasource':
        """
        Get an existing Datasource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] agent_group_id: The ID of the agent group to which the data source should connect to (on-prem data sources only)
        :param pulumi.Input[str] config: Sensitive configuration for the data source. Needs to be a valid JSON
        :param pulumi.Input[str] data_source_name: Display name of the data source
        :param pulumi.Input[str] display_name: The display name of the data source (Displayed in SquaredUp)
        :param pulumi.Input[str] last_updated: The last time the data source was updated
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DatasourceState.__new__(_DatasourceState)

        __props__.__dict__["agent_group_id"] = agent_group_id
        __props__.__dict__["config"] = config
        __props__.__dict__["data_source_name"] = data_source_name
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["last_updated"] = last_updated
        return Datasource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="agentGroupId")
    def agent_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the agent group to which the data source should connect to (on-prem data sources only)
        """
        return pulumi.get(self, "agent_group_id")

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[Optional[str]]:
        """
        Sensitive configuration for the data source. Needs to be a valid JSON
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="dataSourceName")
    def data_source_name(self) -> pulumi.Output[str]:
        """
        Display name of the data source
        """
        return pulumi.get(self, "data_source_name")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the data source (Displayed in SquaredUp)
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> pulumi.Output[str]:
        """
        The last time the data source was updated
        """
        return pulumi.get(self, "last_updated")

