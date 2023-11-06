// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Each workspace has its own dashboards, data sources, monitors and scopes.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as squaredup from "@pulumi/squaredup";
 * import * as squaredup from "@squaredup/pulumi-squaredup";
 *
 * const sampleData = squaredup.getDatasources({
 *     dataSourceName: "Sample Data",
 * });
 * const sampleDataSource = new squaredup.Datasource("sampleDataSource", {
 *     displayName: "Sample Data",
 *     dataSourceName: sampleData.then(sampleData => sampleData.plugins?.[0]?.displayName),
 * });
 * const applicationWorkspace = new squaredup.Workspace("applicationWorkspace", {
 *     displayName: "Application Team",
 *     description: "Workspace with Dashboards for Application Team",
 * });
 * const devopsWorkspace = new squaredup.Workspace("devopsWorkspace", {
 *     displayName: "DevOps Team",
 *     description: "Workspace with Dashboards for DevOps Team",
 *     type: "application",
 *     tags: [
 *         "terraform",
 *         "auto-created",
 *     ],
 *     openAccessEnabled: true,
 *     workspacesLinks: [applicationWorkspace.id],
 *     datasourcesLinks: [sampleDataSource.id],
 * });
 * ```
 *
 * ## Import
 *
 * Workspaces can be imported by specifying workspace id.
 *
 * ```sh
 *  $ pulumi import squaredup:index/workspace:Workspace example space-123
 * ```
 */
export class Workspace extends pulumi.CustomResource {
    /**
     * Get an existing Workspace resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WorkspaceState, opts?: pulumi.CustomResourceOptions): Workspace {
        return new Workspace(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'squaredup:index/workspace:Workspace';

    /**
     * Returns true if the given object is an instance of Workspace.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Workspace {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Workspace.__pulumiType;
    }

    /**
     * Links to plugins
     */
    public readonly datasourcesLinks!: pulumi.Output<string[]>;
    /**
     * The description of the workspace
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The display name of the workspace (Displayed in SquaredUp)
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * The last time the workspace was updated
     */
    public /*out*/ readonly lastUpdated!: pulumi.Output<string>;
    /**
     * Whether open access is enabled for the workspace
     */
    public readonly openAccessEnabled!: pulumi.Output<boolean>;
    /**
     * The tags of the workspace
     */
    public readonly tags!: pulumi.Output<string[]>;
    /**
     * Workspace type that can be one of: 'service', 'team', 'application', 'platform', 'product', 'business service', 'microservice', 'customer', 'website', 'component', 'resource', 'system', 'folder', 'other'.
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * Links to workspaces
     */
    public readonly workspacesLinks!: pulumi.Output<string[]>;

    /**
     * Create a Workspace resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WorkspaceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: WorkspaceArgs | WorkspaceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as WorkspaceState | undefined;
            resourceInputs["datasourcesLinks"] = state ? state.datasourcesLinks : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["displayName"] = state ? state.displayName : undefined;
            resourceInputs["lastUpdated"] = state ? state.lastUpdated : undefined;
            resourceInputs["openAccessEnabled"] = state ? state.openAccessEnabled : undefined;
            resourceInputs["tags"] = state ? state.tags : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
            resourceInputs["workspacesLinks"] = state ? state.workspacesLinks : undefined;
        } else {
            const args = argsOrState as WorkspaceArgs | undefined;
            if ((!args || args.displayName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'displayName'");
            }
            resourceInputs["datasourcesLinks"] = args ? args.datasourcesLinks : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["openAccessEnabled"] = args ? args.openAccessEnabled : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["type"] = args ? args.type : undefined;
            resourceInputs["workspacesLinks"] = args ? args.workspacesLinks : undefined;
            resourceInputs["lastUpdated"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Workspace.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Workspace resources.
 */
export interface WorkspaceState {
    /**
     * Links to plugins
     */
    datasourcesLinks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The description of the workspace
     */
    description?: pulumi.Input<string>;
    /**
     * The display name of the workspace (Displayed in SquaredUp)
     */
    displayName?: pulumi.Input<string>;
    /**
     * The last time the workspace was updated
     */
    lastUpdated?: pulumi.Input<string>;
    /**
     * Whether open access is enabled for the workspace
     */
    openAccessEnabled?: pulumi.Input<boolean>;
    /**
     * The tags of the workspace
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Workspace type that can be one of: 'service', 'team', 'application', 'platform', 'product', 'business service', 'microservice', 'customer', 'website', 'component', 'resource', 'system', 'folder', 'other'.
     */
    type?: pulumi.Input<string>;
    /**
     * Links to workspaces
     */
    workspacesLinks?: pulumi.Input<pulumi.Input<string>[]>;
}

/**
 * The set of arguments for constructing a Workspace resource.
 */
export interface WorkspaceArgs {
    /**
     * Links to plugins
     */
    datasourcesLinks?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The description of the workspace
     */
    description?: pulumi.Input<string>;
    /**
     * The display name of the workspace (Displayed in SquaredUp)
     */
    displayName: pulumi.Input<string>;
    /**
     * Whether open access is enabled for the workspace
     */
    openAccessEnabled?: pulumi.Input<boolean>;
    /**
     * The tags of the workspace
     */
    tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Workspace type that can be one of: 'service', 'team', 'application', 'platform', 'product', 'business service', 'microservice', 'customer', 'website', 'component', 'resource', 'system', 'folder', 'other'.
     */
    type?: pulumi.Input<string>;
    /**
     * Links to workspaces
     */
    workspacesLinks?: pulumi.Input<pulumi.Input<string>[]>;
}