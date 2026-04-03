# helm

**Platforms:** Multi-platform
**Category:** Container & Orchestration

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| List charts | `helm list` |
| Show status | `helm status release` |
| Get values | `helm get values release` |
| Show history | `helm history release` |
| Search charts | `helm search repo name` |
| Show chart | `helm show chart repo/chart` |
| Show values | `helm show values repo/chart` |
| Version info | `helm version` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `helm install` | Installs charts |
| `helm upgrade` | Upgrades releases |
| `helm uninstall` | Uninstalls releases |
| `helm rollback` | Rollbacks releases |
| `helm delete` | Deletes releases |
| `helm repo add` | Adds repositories |
| `helm repo remove` | Removes repositories |
| `helm push` | Pushes charts |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe helm Inspection Script

# List releases
helm list

# Show status
helm status my-release

# Get values
helm get values my-release

# Show history
helm history my-release

# Search charts
helm search repo nginx

# Show chart info
helm show chart bitnami/nginx
```
