# terraform

**Platforms:** Multi-platform
**Category:** Infrastructure as Code

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Validate config | `terraform validate` |
| Format check | `terraform fmt -check` |
| Show version | `terraform version` |
| Show providers | `terraform providers` |
| Show state | `terraform state show` |
| List resources | `terraform state list` |
| Pull state | `terraform state pull` |
| Graph (dry-run) | `terraform graph` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `terraform init` | Initializes (downloads) |
| `terraform plan` | Creates plan file |
| `terraform apply` | Applies changes |
| `terraform destroy` | Destroys infrastructure |
| `terraform refresh` | Refreshes state |
| `terraform taint` | Marks resources tainted |
| `terraform state push` | Pushes state |
| `terraform state replace` | Replaces state |
| `terraform state rm` | Removes from state |
| `terraform import` | Imports resources |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe terraform Inspection Script

# Validate config
terraform validate

# Format check
terraform fmt -check

# Show version
terraform version

# List resources in state
terraform state list

# Show specific resource
terraform state show aws_instance.web

# Pull state (read-only)
terraform state pull | head -50
```
