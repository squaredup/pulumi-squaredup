package shim

import (
	tf "github.com/hashicorp/terraform-plugin-framework/provider"
	"github.com/squaredup/pulumi-squaredup/provider/pkg/version"
	"github.com/squaredup/terraform-provider-squaredup/internal/provider"
)

func NewProvider() tf.Provider {
	return provider.New(version.Version)()
}
