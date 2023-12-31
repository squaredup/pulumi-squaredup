// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Dashboard are used to visualize data from Data Sources
 *
 * ## Import
 *
 * Dashboards can be imported by specifying dashboard id.
 *
 * ```sh
 *  $ pulumi import squaredup:index/dashboard:Dashboard example dash-123
 * ```
 */
export class Dashboard extends pulumi.CustomResource {
    /**
     * Get an existing Dashboard resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DashboardState, opts?: pulumi.CustomResourceOptions): Dashboard {
        return new Dashboard(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'squaredup:index/dashboard:Dashboard';

    /**
     * Returns true if the given object is an instance of Dashboard.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Dashboard {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Dashboard.__pulumiType;
    }

    /**
     * The content of the dashboard. This is the rendered dashboard template with the template bindings applied.
     */
    public /*out*/ readonly dashboardContent!: pulumi.Output<string>;
    /**
     * Dashboard template to use for the dashboard
     */
    public readonly dashboardTemplate!: pulumi.Output<string>;
    /**
     * The display name of the dashboard
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * The group of the dashboard
     */
    public /*out*/ readonly group!: pulumi.Output<string>;
    /**
     * The last updated date of the dashboard
     */
    public /*out*/ readonly lastUpdated!: pulumi.Output<string>;
    /**
     * The name of the dashboard
     */
    public /*out*/ readonly name!: pulumi.Output<string>;
    /**
     * The schema version of the dashboard
     */
    public /*out*/ readonly schemaVersion!: pulumi.Output<string>;
    /**
     * Template Bindings used for replacing mustache template in the dashboard template. Needs to be a JSON encoded string.
     */
    public readonly templateBindings!: pulumi.Output<string>;
    /**
     * The ID of the workspace where the dashboard is located
     */
    public readonly workspaceId!: pulumi.Output<string>;

    /**
     * Create a Dashboard resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DashboardArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DashboardArgs | DashboardState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DashboardState | undefined;
            resourceInputs["dashboardContent"] = state ? state.dashboardContent : undefined;
            resourceInputs["dashboardTemplate"] = state ? state.dashboardTemplate : undefined;
            resourceInputs["displayName"] = state ? state.displayName : undefined;
            resourceInputs["group"] = state ? state.group : undefined;
            resourceInputs["lastUpdated"] = state ? state.lastUpdated : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["schemaVersion"] = state ? state.schemaVersion : undefined;
            resourceInputs["templateBindings"] = state ? state.templateBindings : undefined;
            resourceInputs["workspaceId"] = state ? state.workspaceId : undefined;
        } else {
            const args = argsOrState as DashboardArgs | undefined;
            if ((!args || args.dashboardTemplate === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dashboardTemplate'");
            }
            if ((!args || args.displayName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'displayName'");
            }
            if ((!args || args.workspaceId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'workspaceId'");
            }
            resourceInputs["dashboardTemplate"] = args ? args.dashboardTemplate : undefined;
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["templateBindings"] = args ? args.templateBindings : undefined;
            resourceInputs["workspaceId"] = args ? args.workspaceId : undefined;
            resourceInputs["dashboardContent"] = undefined /*out*/;
            resourceInputs["group"] = undefined /*out*/;
            resourceInputs["lastUpdated"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["schemaVersion"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Dashboard.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Dashboard resources.
 */
export interface DashboardState {
    /**
     * The content of the dashboard. This is the rendered dashboard template with the template bindings applied.
     */
    dashboardContent?: pulumi.Input<string>;
    /**
     * Dashboard template to use for the dashboard
     */
    dashboardTemplate?: pulumi.Input<string>;
    /**
     * The display name of the dashboard
     */
    displayName?: pulumi.Input<string>;
    /**
     * The group of the dashboard
     */
    group?: pulumi.Input<string>;
    /**
     * The last updated date of the dashboard
     */
    lastUpdated?: pulumi.Input<string>;
    /**
     * The name of the dashboard
     */
    name?: pulumi.Input<string>;
    /**
     * The schema version of the dashboard
     */
    schemaVersion?: pulumi.Input<string>;
    /**
     * Template Bindings used for replacing mustache template in the dashboard template. Needs to be a JSON encoded string.
     */
    templateBindings?: pulumi.Input<string>;
    /**
     * The ID of the workspace where the dashboard is located
     */
    workspaceId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Dashboard resource.
 */
export interface DashboardArgs {
    /**
     * Dashboard template to use for the dashboard
     */
    dashboardTemplate: pulumi.Input<string>;
    /**
     * The display name of the dashboard
     */
    displayName: pulumi.Input<string>;
    /**
     * Template Bindings used for replacing mustache template in the dashboard template. Needs to be a JSON encoded string.
     */
    templateBindings?: pulumi.Input<string>;
    /**
     * The ID of the workspace where the dashboard is located
     */
    workspaceId: pulumi.Input<string>;
}
