// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace squaredup.SquaredUpPackage.Squaredup
{
    /// <summary>
    /// The provider type for the squaredup package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [SquaredupResourceType("pulumi:providers:squaredup")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// API Key for SquaredUp API. May also be set via the SQUAREDUP_API_KEY environment variable.
        /// </summary>
        [Output("apiKey")]
        public Output<string?> ApiKey { get; private set; } = null!;

        /// <summary>
        /// Region of your SquaredUp instance. May also be set via the SQUAREDUP_REGION environment variable.
        /// </summary>
        [Output("region")]
        public Output<string?> Region { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("squaredup", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/squaredup/pulumi-squaredup",
                AdditionalSecretOutputs =
                {
                    "apiKey",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        [Input("apiKey")]
        private Input<string>? _apiKey;

        /// <summary>
        /// API Key for SquaredUp API. May also be set via the SQUAREDUP_API_KEY environment variable.
        /// </summary>
        public Input<string>? ApiKey
        {
            get => _apiKey;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _apiKey = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Region of your SquaredUp instance. May also be set via the SQUAREDUP_REGION environment variable.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public ProviderArgs()
        {
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
