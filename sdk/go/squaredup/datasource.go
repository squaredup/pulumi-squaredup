// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package squaredup

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"github.com/squaredup/pulumi-squaredup/sdk/go/squaredup/internal"
)

// Data Sources are used to query third party APIs and SquaredUp visualizes the results
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"encoding/json"
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/squaredup/pulumi-squaredup/sdk/go/squaredup"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			sampleData, err := squaredup.GetDatasources(ctx, &squaredup.GetDatasourcesArgs{
//				DataSourceName: pulumi.StringRef("Sample Data"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = squaredup.NewDatasource(ctx, "sampleDataSource", &squaredup.DatasourceArgs{
//				DisplayName:    pulumi.String("Sample Data"),
//				DataSourceName: *pulumi.String(sampleData.Plugins[0].DisplayName),
//			})
//			if err != nil {
//				return err
//			}
//			tmpJSON0, err := json.Marshal(map[string]interface{}{
//				"org":         "org-name",
//				"accessToken": "access-token",
//			})
//			if err != nil {
//				return err
//			}
//			json0 := string(tmpJSON0)
//			_, err = squaredup.NewDatasource(ctx, "adoDatasource", &squaredup.DatasourceArgs{
//				DisplayName:    pulumi.String("Azure DevOps"),
//				DataSourceName: pulumi.String("Azure DevOps"),
//				Config:         pulumi.String(json0),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// Data Source can be imported by specifying datasource id.
//
// ```sh
//
//	$ pulumi import squaredup:index/datasource:Datasource example config-123
//
// ```
type Datasource struct {
	pulumi.CustomResourceState

	// The ID of the agent group to which the data source should connect to (on-prem data sources only)
	AgentGroupId pulumi.StringOutput `pulumi:"agentGroupId"`
	// Sensitive configuration for the data source. Needs to be a valid JSON
	Config pulumi.StringPtrOutput `pulumi:"config"`
	// Display name of the data source
	DataSourceName pulumi.StringOutput `pulumi:"dataSourceName"`
	// The display name of the data source (Displayed in SquaredUp)
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// The last time the data source was updated
	LastUpdated pulumi.StringOutput `pulumi:"lastUpdated"`
}

// NewDatasource registers a new resource with the given unique name, arguments, and options.
func NewDatasource(ctx *pulumi.Context,
	name string, args *DatasourceArgs, opts ...pulumi.ResourceOption) (*Datasource, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DataSourceName == nil {
		return nil, errors.New("invalid value for required argument 'DataSourceName'")
	}
	if args.DisplayName == nil {
		return nil, errors.New("invalid value for required argument 'DisplayName'")
	}
	if args.Config != nil {
		args.Config = pulumi.ToSecret(args.Config).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"config",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Datasource
	err := ctx.RegisterResource("squaredup:index/datasource:Datasource", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDatasource gets an existing Datasource resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDatasource(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DatasourceState, opts ...pulumi.ResourceOption) (*Datasource, error) {
	var resource Datasource
	err := ctx.ReadResource("squaredup:index/datasource:Datasource", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Datasource resources.
type datasourceState struct {
	// The ID of the agent group to which the data source should connect to (on-prem data sources only)
	AgentGroupId *string `pulumi:"agentGroupId"`
	// Sensitive configuration for the data source. Needs to be a valid JSON
	Config *string `pulumi:"config"`
	// Display name of the data source
	DataSourceName *string `pulumi:"dataSourceName"`
	// The display name of the data source (Displayed in SquaredUp)
	DisplayName *string `pulumi:"displayName"`
	// The last time the data source was updated
	LastUpdated *string `pulumi:"lastUpdated"`
}

type DatasourceState struct {
	// The ID of the agent group to which the data source should connect to (on-prem data sources only)
	AgentGroupId pulumi.StringPtrInput
	// Sensitive configuration for the data source. Needs to be a valid JSON
	Config pulumi.StringPtrInput
	// Display name of the data source
	DataSourceName pulumi.StringPtrInput
	// The display name of the data source (Displayed in SquaredUp)
	DisplayName pulumi.StringPtrInput
	// The last time the data source was updated
	LastUpdated pulumi.StringPtrInput
}

func (DatasourceState) ElementType() reflect.Type {
	return reflect.TypeOf((*datasourceState)(nil)).Elem()
}

type datasourceArgs struct {
	// The ID of the agent group to which the data source should connect to (on-prem data sources only)
	AgentGroupId *string `pulumi:"agentGroupId"`
	// Sensitive configuration for the data source. Needs to be a valid JSON
	Config *string `pulumi:"config"`
	// Display name of the data source
	DataSourceName string `pulumi:"dataSourceName"`
	// The display name of the data source (Displayed in SquaredUp)
	DisplayName string `pulumi:"displayName"`
}

// The set of arguments for constructing a Datasource resource.
type DatasourceArgs struct {
	// The ID of the agent group to which the data source should connect to (on-prem data sources only)
	AgentGroupId pulumi.StringPtrInput
	// Sensitive configuration for the data source. Needs to be a valid JSON
	Config pulumi.StringPtrInput
	// Display name of the data source
	DataSourceName pulumi.StringInput
	// The display name of the data source (Displayed in SquaredUp)
	DisplayName pulumi.StringInput
}

func (DatasourceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*datasourceArgs)(nil)).Elem()
}

type DatasourceInput interface {
	pulumi.Input

	ToDatasourceOutput() DatasourceOutput
	ToDatasourceOutputWithContext(ctx context.Context) DatasourceOutput
}

func (*Datasource) ElementType() reflect.Type {
	return reflect.TypeOf((**Datasource)(nil)).Elem()
}

func (i *Datasource) ToDatasourceOutput() DatasourceOutput {
	return i.ToDatasourceOutputWithContext(context.Background())
}

func (i *Datasource) ToDatasourceOutputWithContext(ctx context.Context) DatasourceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatasourceOutput)
}

func (i *Datasource) ToOutput(ctx context.Context) pulumix.Output[*Datasource] {
	return pulumix.Output[*Datasource]{
		OutputState: i.ToDatasourceOutputWithContext(ctx).OutputState,
	}
}

// DatasourceArrayInput is an input type that accepts DatasourceArray and DatasourceArrayOutput values.
// You can construct a concrete instance of `DatasourceArrayInput` via:
//
//	DatasourceArray{ DatasourceArgs{...} }
type DatasourceArrayInput interface {
	pulumi.Input

	ToDatasourceArrayOutput() DatasourceArrayOutput
	ToDatasourceArrayOutputWithContext(context.Context) DatasourceArrayOutput
}

type DatasourceArray []DatasourceInput

func (DatasourceArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Datasource)(nil)).Elem()
}

func (i DatasourceArray) ToDatasourceArrayOutput() DatasourceArrayOutput {
	return i.ToDatasourceArrayOutputWithContext(context.Background())
}

func (i DatasourceArray) ToDatasourceArrayOutputWithContext(ctx context.Context) DatasourceArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatasourceArrayOutput)
}

func (i DatasourceArray) ToOutput(ctx context.Context) pulumix.Output[[]*Datasource] {
	return pulumix.Output[[]*Datasource]{
		OutputState: i.ToDatasourceArrayOutputWithContext(ctx).OutputState,
	}
}

// DatasourceMapInput is an input type that accepts DatasourceMap and DatasourceMapOutput values.
// You can construct a concrete instance of `DatasourceMapInput` via:
//
//	DatasourceMap{ "key": DatasourceArgs{...} }
type DatasourceMapInput interface {
	pulumi.Input

	ToDatasourceMapOutput() DatasourceMapOutput
	ToDatasourceMapOutputWithContext(context.Context) DatasourceMapOutput
}

type DatasourceMap map[string]DatasourceInput

func (DatasourceMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Datasource)(nil)).Elem()
}

func (i DatasourceMap) ToDatasourceMapOutput() DatasourceMapOutput {
	return i.ToDatasourceMapOutputWithContext(context.Background())
}

func (i DatasourceMap) ToDatasourceMapOutputWithContext(ctx context.Context) DatasourceMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatasourceMapOutput)
}

func (i DatasourceMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*Datasource] {
	return pulumix.Output[map[string]*Datasource]{
		OutputState: i.ToDatasourceMapOutputWithContext(ctx).OutputState,
	}
}

type DatasourceOutput struct{ *pulumi.OutputState }

func (DatasourceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Datasource)(nil)).Elem()
}

func (o DatasourceOutput) ToDatasourceOutput() DatasourceOutput {
	return o
}

func (o DatasourceOutput) ToDatasourceOutputWithContext(ctx context.Context) DatasourceOutput {
	return o
}

func (o DatasourceOutput) ToOutput(ctx context.Context) pulumix.Output[*Datasource] {
	return pulumix.Output[*Datasource]{
		OutputState: o.OutputState,
	}
}

// The ID of the agent group to which the data source should connect to (on-prem data sources only)
func (o DatasourceOutput) AgentGroupId() pulumi.StringOutput {
	return o.ApplyT(func(v *Datasource) pulumi.StringOutput { return v.AgentGroupId }).(pulumi.StringOutput)
}

// Sensitive configuration for the data source. Needs to be a valid JSON
func (o DatasourceOutput) Config() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Datasource) pulumi.StringPtrOutput { return v.Config }).(pulumi.StringPtrOutput)
}

// Display name of the data source
func (o DatasourceOutput) DataSourceName() pulumi.StringOutput {
	return o.ApplyT(func(v *Datasource) pulumi.StringOutput { return v.DataSourceName }).(pulumi.StringOutput)
}

// The display name of the data source (Displayed in SquaredUp)
func (o DatasourceOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v *Datasource) pulumi.StringOutput { return v.DisplayName }).(pulumi.StringOutput)
}

// The last time the data source was updated
func (o DatasourceOutput) LastUpdated() pulumi.StringOutput {
	return o.ApplyT(func(v *Datasource) pulumi.StringOutput { return v.LastUpdated }).(pulumi.StringOutput)
}

type DatasourceArrayOutput struct{ *pulumi.OutputState }

func (DatasourceArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Datasource)(nil)).Elem()
}

func (o DatasourceArrayOutput) ToDatasourceArrayOutput() DatasourceArrayOutput {
	return o
}

func (o DatasourceArrayOutput) ToDatasourceArrayOutputWithContext(ctx context.Context) DatasourceArrayOutput {
	return o
}

func (o DatasourceArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*Datasource] {
	return pulumix.Output[[]*Datasource]{
		OutputState: o.OutputState,
	}
}

func (o DatasourceArrayOutput) Index(i pulumi.IntInput) DatasourceOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Datasource {
		return vs[0].([]*Datasource)[vs[1].(int)]
	}).(DatasourceOutput)
}

type DatasourceMapOutput struct{ *pulumi.OutputState }

func (DatasourceMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Datasource)(nil)).Elem()
}

func (o DatasourceMapOutput) ToDatasourceMapOutput() DatasourceMapOutput {
	return o
}

func (o DatasourceMapOutput) ToDatasourceMapOutputWithContext(ctx context.Context) DatasourceMapOutput {
	return o
}

func (o DatasourceMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*Datasource] {
	return pulumix.Output[map[string]*Datasource]{
		OutputState: o.OutputState,
	}
}

func (o DatasourceMapOutput) MapIndex(k pulumi.StringInput) DatasourceOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Datasource {
		return vs[0].(map[string]*Datasource)[vs[1].(string)]
	}).(DatasourceOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DatasourceInput)(nil)).Elem(), &Datasource{})
	pulumi.RegisterInputType(reflect.TypeOf((*DatasourceArrayInput)(nil)).Elem(), DatasourceArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DatasourceMapInput)(nil)).Elem(), DatasourceMap{})
	pulumi.RegisterOutputType(DatasourceOutput{})
	pulumi.RegisterOutputType(DatasourceArrayOutput{})
	pulumi.RegisterOutputType(DatasourceMapOutput{})
}