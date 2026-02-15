# terraform

**Platforms:** Multi-platform  
**Category:** Infrastructure as Code

## Command-Line Flags

- `-auto-approve`: Skip confirmation (**safety bypass**, see warning below)
- `-input=false`: Disable interactive prompts for missing variables
- `-no-color`: Disable colored output
- `-json`: JSON output (machine-readable)
- `-compact-warnings`: Compact warning format

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `TF_IN_AUTOMATION` | `true` | Adjusts output for automation (no hints to run other commands) |
| `TF_INPUT` | `false` | Disable interactive prompts globally |

## Recommended Unattended Usage

> **Warning:** `-auto-approve` skips the safety confirmation prompt. Only use it when
> applying a plan that has already been reviewed, or in fully automated pipelines
> with proper safeguards. When applying a saved plan file, `-auto-approve` is
> redundant (Terraform treats passing a plan file as implicit approval).

```bash
#!/bin/bash

export TF_IN_AUTOMATION=true

terraform init -input=false
terraform validate || exit 1
terraform plan -out=plan.tfplan -input=false -no-color || exit 1
terraform apply -input=false -no-color plan.tfplan
```
