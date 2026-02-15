# minikube

**Platforms:** Multi-platform  
**Category:** Local Kubernetes

## Quick Reference

| Goal | Command |
|------|---------|
| Start silently | `minikube start` |
| Wait | `minikube start --wait=true` |
| No output | `minikube start --output=json` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `MINIKUBE_HOME` | `~/.minikube` | Minikube home |
| `MINIKUBE_IN_STYLE` | `false` | Disable emoji |

## Command-Line Flags

```bash
minikube start                       # Start cluster
minikube start --wait=true           # Wait for apiserver
minikube start --driver=docker       # Use Docker driver
minikube start --memory=4096         # Set memory
minikube start --cpus=4              # Set CPUs
minikube stop                        # Stop cluster
minikube delete                      # Delete cluster
minikube status                      # Check status
minikube kubectl -- get pods         # Use bundled kubectl
minikube ip                          # Get cluster IP
minikube service list                # List services
```
- `--wait=true`: Wait for apiserver
- `--driver`: VM driver (docker, virtualbox, etc.)
- `--memory`: Memory allocation
- `--cpus`: CPU allocation
- `--output`: Output format (text, json)
