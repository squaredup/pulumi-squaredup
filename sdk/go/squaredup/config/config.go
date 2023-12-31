// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
	"github.com/squaredup/pulumi-squaredup/sdk/go/squaredup/internal"
)

var _ = internal.GetEnvOrDefault

// API Key for SquaredUp API. May also be set via the SQUAREDUP_API_KEY environment variable.
func GetApiKey(ctx *pulumi.Context) string {
	return config.Get(ctx, "squaredup:apiKey")
}

// Region of your SquaredUp instance. May also be set via the SQUAREDUP_REGION environment variable.
func GetRegion(ctx *pulumi.Context) string {
	return config.Get(ctx, "squaredup:region")
}
