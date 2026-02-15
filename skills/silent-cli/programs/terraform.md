# terraform

**Platforms:** Multi-platform  
**Category:** Infrastructure as Code

## Quick Reference

| Goal | Command |
|------|---------|
| Init | `terraform init` |
| Plan | `terraform plan` |
| Apply | `terraform apply` |
| Destroy | `terraform destroy` |

## Command-Line Flags

```bash
terraform init                       # Initialize
terraform init -upgrade             # Upgrade providers
terraform init -backend-config=backend.hcl
terraform validate                   # Validate config
terraform fmt                        # Format code
terraform fmt -check                 # Check format
terraform fmt -recursive
terraform plan                       # Execution plan
terraform plan -out=plan.tfplan      # Save plan
terraform plan -var 'key=value'
terraform plan -var-file=prod.tfvars
terraform plan -target=aws_instance.web
terraform plan -destroy              # Plan destruction
terraform apply                      # Apply changes
terraform apply -auto-approve        # No confirmation
terraform apply plan.tfplan          # Apply saved plan
terraform apply -var-file=prod.tfvars
terraform apply -target=aws_instance.web
terraform apply -replace=aws_instance.web
terraform destroy                    # Destroy all
terraform destroy -auto-approve
terraform destroy -target=aws_instance.web
terraform show                       # Show state/plan
terraform show plan.tfplan
terraform state list                 # List resources
terraform state show aws_instance.web
terraform state rm aws_instance.web  # Remove from state
terraform state mv old new           # Rename resource
terraform import aws_instance.web i-xxx  # Import existing
terraform refresh                    # Refresh state
terraform taint aws_instance.web     # Mark for recreation
terraform untaint aws_instance.web   # Unmark
terraform output                     # Show outputs
terraform output -json
terraform workspace list             # List workspaces
terraform workspace new staging
terraform workspace select staging
terraform workspace delete staging
terraform get                        # Download modules
terraform get -update
terraform providers                  # Show providers
terraform version
terraform -version
```
- `-var`: Set variable
- `-var-file`: Variable file
- `-target`: Target specific resource
- `-auto-approve`: Skip confirmation (**safety bypass**, see warning below)
- `-no-color`: Disable colored output
- `-out`: Save plan to file
- `-json`: JSON output
- `-compact-warnings`: Compact warning format
- `-chdir`: Change working directory

## Environment Variables

```bash
export TF_IN_AUTOMATION=true
export TF_VAR_name=value
export TF_LOG=DEBUG
export TF_LOG_PATH=/tmp/terraform.log
```

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
