// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

//go:generate go run generate.go
package squaredup

import (
	_ "embed"
	"fmt"
	"path/filepath"
	"strings"

	"github.com/ettle/strcase"
	pf "github.com/pulumi/pulumi-terraform-bridge/pf/tfbridge"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shim "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim"
	"github.com/pulumi/pulumi/sdk/v3/go/common/resource"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/contract"
	"github.com/squaredup/pulumi-squaredup/provider/pkg/version"
	shimprovider "github.com/squaredup/terraform-provider-squaredup/shim"
)

//go:embed cmd/pulumi-resource-squaredup/bridge-metadata.json
var bridgeMetadata []byte

// all of the token components used below.
const (
	// This variable controls the default name of the package in the package
	mainMod = "index" // the squaredup module
)

func convertName(name string) string {
	idx := strings.Index(name, "_")
	contract.Assertf(idx > 0 && idx < len(name)-1, "Invalid snake case name %s", name)
	name = name[idx+1:]
	contract.Assertf(len(name) > 0, "Invalid snake case name %s", name)
	return strcase.ToPascal(name)
}

func makeDataSource(mod string, name string) tokens.ModuleMember {
	name = convertName(name)
	return tfbridge.MakeDataSource("squaredup", mod, "get"+name)
}

func makeResource(mod string, res string) tokens.Type {
	return tfbridge.MakeResource("squaredup", mod, convertName(res))
}

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c shim.ResourceConfig) error {
	return nil
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := pf.ShimProvider(shimprovider.NewProvider())

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:                 p,
		Name:              "squaredup",
		DisplayName:       "Squaredup",
		Publisher:         "squaredup",
		LogoURL:           "", //TODO:https://raw.githubusercontent.com/squaredup/pulumi-squaredup/main/docs/squaredup.png"
		PluginDownloadURL: "github://api.github.com/squaredup/pulumi-squaredup",
		Description:       "A Pulumi package for creating and managing Squaredup resources",
		Keywords: []string{
			"pulumi",
			"squaredup",
			"category/cloud",
		},
		License:      "Apache-2.0",
		Homepage:     "https://www.squaredup.com",
		Repository:   "https://github.com/squaredup/pulumi-squaredup",
		Version:      version.Version,
		GitHubOrg:    "squaredup",
		MetadataInfo: tfbridge.NewProviderMetadata(bridgeMetadata),
		Config: map[string]*tfbridge.SchemaInfo{
			"region": {
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"SQUAREUP_REGION"},
				},
			},
			"api_key": {
				Secret: tfbridge.BoolRef(true),
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"SQUAREDUP_API_KEY"},
				},
			},
		},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			"squaredup_data_source": {Tok: makeResource(mainMod, "squaredup_data_source")},
			"squaredup_workspace":   {Tok: makeResource(mainMod, "squaredup_workspace")},
			"squaredup_dashboard":   {Tok: makeResource(mainMod, "squaredup_dashboard")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"squaredup_datasources": {
				Tok: makeDataSource(mainMod, "squaredup_datasources"),
			},
			"squaredup_data_streams": {
				Tok: makeDataSource(mainMod, "squaredup_data_streams"),
			},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			PackageName: "@squaredup/pulumi-squaredup",

			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
			},
			DevDependencies: map[string]string{
				"@types/node": "^10.0.0", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
		},
		Python: &tfbridge.PythonInfo{
			PackageName: "squaredup_pulumi_squaredup",

			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/squaredup/pulumi-%[1]s/sdk/", "squaredup"),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				"squaredup",
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			RootNamespace: "squaredup.SquaredUpPackage",

			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
		},
		Java: &tfbridge.JavaInfo{
			BasePackage: "com.pulumi.squaredup",
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
