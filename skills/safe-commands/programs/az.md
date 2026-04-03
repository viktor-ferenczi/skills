# az (Azure CLI)

**Platforms:** Multi-platform
**Category:** Cloud Platforms

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `az version` |
| Show help | `az --help` |
| List subscriptions | `az account list` |
| Show current sub | `az account show` |
| List resource groups | `az group list` |
| List resources | `az resource list` |
| Show deployment | `az deployment show` |
| List VMs | `az vm list` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `az vm create` | Creates VMs (costs money) |
| `az vm delete` | Deletes VMs |
| `az group create` | Creates resource groups |
| `az group delete` | Deletes resource groups |
| `az deployment create` | Creates deployments |
| `az deployment delete` | Deletes deployments |
| `az account set` | Changes context |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe az Inspection Script

# Show version
az version

# List subscriptions
az account list --output table

# List resource groups
az group list --output table

# List resources
az resource list --output table
```
