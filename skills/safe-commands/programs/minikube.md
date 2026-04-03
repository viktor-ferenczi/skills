# minikube

**Platforms:** Multi-platform
**Category:** Container Orchestration

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `minikube version` |
| Show help | `minikube --help` |
| List clusters | `minikube profile list` |
| Show status | `minikube status` |
| Show config | `minikube config view` |
| List addons | `minikube addons list` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `minikube start` | Starts cluster |
| `minikube delete` | Deletes cluster |
| `minikube stop` | Stops cluster |
| `minikube addons enable` | Enables addons |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe minikube Inspection Script

# List clusters
minikube profile list

# Show status
minikube status

# List addons
minikube addons list
```
