# packer (HashiCorp)

**Platforms:** Multi-platform  
**Category:** Machine Image Builder

## Quick Reference

| Goal | Command |
|------|---------|
| Build | `packer build template.pkr.hcl` |
| Validate | `packer validate template.pkr.hcl` |
| Format | `packer fmt template.pkr.hcl` |

## Command-Line Flags

```bash
packer build template.pkr.hcl        # Build image
packer build -var 'aws_access_key=xxx' template.pkr.hcl
packer build -var-file=variables.pkrvars.hcl template.pkr.hcl
packer build -only=amazon-ebs template.pkr.hcl
packer build -except=vsphere-iso template.pkr.hcl
packer build -force template.pkr.hcl
packer build -on-error=ask template.pkr.hcl
packer build -on-error=cleanup template.pkr.hcl
packer build -on-error=abort template.pkr.hcl
packer build -parallel-builds=4 template.pkr.hcl
packer validate template.pkr.hcl     # Validate template
packer validate -syntax-only template.pkr.hcl
packer fmt template.pkr.hcl          # Format template
packer fmt -write=false template.pkr.hcl  # Check format only
packer fmt -recursive .              # Format all
packer inspect template.pkr.hcl      # Inspect template
packer version                       # Show version
packer plugins install github.com/hashicorp/amazon
packer plugins list                  # List plugins
packer plugins remove github.com/hashicorp/amazon
packer init template.pkr.hcl         # Init plugins
```
- `-var`: Set variable
- `-var-file`: Variable file
- `-only`: Build only specific sources
- `-except`: Exclude specific sources
- `-force`: Force overwrite
- `-on-error`: Error behavior (ask, cleanup, abort, run-cleanup-provisioner)
- `-parallel-builds`: Max parallel builds
- `-machine-readable`: Machine-readable output

## Recommended Unattended Usage

```bash
#!/bin/bash

# Validate, format, and build
packer fmt -write=false template.pkr.hcl || exit 1
packer validate template.pkr.hcl || exit 1
packer build -on-error=cleanup -force template.pkr.hcl
```
