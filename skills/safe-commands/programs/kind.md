# kind (Kubernetes IN Docker)

**Platforms:** Multi-platform
**Category:** Container Orchestration

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `kind version` |
| Show help | `kind --help` |
| List clusters | `kind get clusters` |
| Get kubeconfig | `kind get kubeconfig` |
| Export logs | `kind export logs` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `kind create cluster` | Creates clusters |
| `kind delete cluster` | Deletes clusters |
| `kind load docker-image` | Loads images |
| `kind build node-image` | Builds images |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe kind Inspection Script

# List clusters
kind get clusters

# Get kubeconfig
kind get kubeconfig
```
