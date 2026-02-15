# kind

**Platforms:** Multi-platform  
**Category:** Local Kubernetes (Docker-based)

## Quick Reference

| Goal | Command |
|------|---------|
| Create cluster | `kind create cluster` |
| Quiet | `kind create cluster -q` |
| From config | `kind create cluster --config config.yaml` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `KIND_EXPERIMENTAL_PROVIDER` | `podman` | Use alternative provider |

## Command-Line Flags

```bash
kind create cluster                  # Create cluster
kind create cluster -q               # Quiet
kind create cluster --name mycluster
kind create cluster --config kind.yaml
kind delete cluster                  # Delete
kind delete cluster --name mycluster
kind get clusters                    # List clusters
kind get nodes                       # List nodes
kind load docker-image myimage:tag   # Load image
kind export kubeconfig               # Export config
```
- `-q` or `--quiet`: Quiet
- `--name`: Cluster name
- `--config`: Config file
- `--image`: Node image
