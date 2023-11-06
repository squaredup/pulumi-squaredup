---
title: Squaredup Installation & Configuration
meta_desc: Information on how to install the Squaredup provider.
layout: installation
---

## Installation

The Pulumi Squaredup provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@squaredup/pulumi-squaredup`](https://www.npmjs.com/package/@squaredup/pulumi-squaredup)
* Python: [`squaredup_pulumi_squaredup`](https://pypi.org/project/squaredup_pulumi_squaredup/)
* Go: [`github.com/squaredup/pulumi-squaredup/sdk/go/squaredup`](https://pkg.go.dev/github.com/squaredup/pulumi-squaredup/sdk/go/squaredup)
* .NET: [`squaredup.SquaredUpPackage.Squaredup`](https://www.nuget.org/packages/squaredup.SquaredUpPackage.Squaredup)


## Configuration

> Note:  
> Replace the following **sample content**, with the configuration options
> of the wrapped Terraform provider and remove this note.

The following configuration points are available for the `squaredup` provider:

- `squaredup:apiKey` (environment: `squaredup_API_KEY`) - the API key for `squaredup`
- `squaredup:region` (environment: `squaredup_REGION`) - the region in which to deploy resources

### Provider Binary

The Squaredup provider binary is a third party binary. It can be installed using the `pulumi plugin` command.

```bash
pulumi plugin install resource squaredup <version>
```

Replace the version string `<version>` with your desired version.
