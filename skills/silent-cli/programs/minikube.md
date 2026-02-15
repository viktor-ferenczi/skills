# minikube

**Platforms:** Multi-platform  
**Category:** Local Kubernetes

## Quick Reference

| Goal | Command |
|------|---------|
| JSON output | `minikube start --output=json` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `MINIKUBE_IN_STYLE` | `false` | Disable emoji/style |

## Command-Line Flags

```bash
minikube start --wait=true           # Wait for apiserver (non-interactive wait)
minikube start --output=json         # JSON output (machine-readable)
```
- `--wait=true`: Wait for apiserver
- `--output`: Output format (text, json)
