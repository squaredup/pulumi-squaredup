// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export { DashboardArgs, DashboardState } from "./dashboard";
export type Dashboard = import("./dashboard").Dashboard;
export const Dashboard: typeof import("./dashboard").Dashboard = null as any;
utilities.lazyLoad(exports, ["Dashboard"], () => require("./dashboard"));

export { DatasourceArgs, DatasourceState } from "./datasource";
export type Datasource = import("./datasource").Datasource;
export const Datasource: typeof import("./datasource").Datasource = null as any;
utilities.lazyLoad(exports, ["Datasource"], () => require("./datasource"));

export { GetDataStreamsArgs, GetDataStreamsResult, GetDataStreamsOutputArgs } from "./getDataStreams";
export const getDataStreams: typeof import("./getDataStreams").getDataStreams = null as any;
export const getDataStreamsOutput: typeof import("./getDataStreams").getDataStreamsOutput = null as any;
utilities.lazyLoad(exports, ["getDataStreams","getDataStreamsOutput"], () => require("./getDataStreams"));

export { GetDatasourcesArgs, GetDatasourcesResult, GetDatasourcesOutputArgs } from "./getDatasources";
export const getDatasources: typeof import("./getDatasources").getDatasources = null as any;
export const getDatasourcesOutput: typeof import("./getDatasources").getDatasourcesOutput = null as any;
utilities.lazyLoad(exports, ["getDatasources","getDatasourcesOutput"], () => require("./getDatasources"));

export { ProviderArgs } from "./provider";
export type Provider = import("./provider").Provider;
export const Provider: typeof import("./provider").Provider = null as any;
utilities.lazyLoad(exports, ["Provider"], () => require("./provider"));

export { WorkspaceArgs, WorkspaceState } from "./workspace";
export type Workspace = import("./workspace").Workspace;
export const Workspace: typeof import("./workspace").Workspace = null as any;
utilities.lazyLoad(exports, ["Workspace"], () => require("./workspace"));


// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "squaredup:index/dashboard:Dashboard":
                return new Dashboard(name, <any>undefined, { urn })
            case "squaredup:index/datasource:Datasource":
                return new Datasource(name, <any>undefined, { urn })
            case "squaredup:index/workspace:Workspace":
                return new Workspace(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("squaredup", "index/dashboard", _module)
pulumi.runtime.registerResourceModule("squaredup", "index/datasource", _module)
pulumi.runtime.registerResourceModule("squaredup", "index/workspace", _module)
pulumi.runtime.registerResourcePackage("squaredup", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:squaredup") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});
