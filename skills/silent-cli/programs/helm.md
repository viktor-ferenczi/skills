# helm

**Platforms:** Multi-platform  
**Category:** Kubernetes Package Manager

## Quick Reference

| Goal | Command |
|------|---------|
| Short list | `helm list -q` |
| Wait | `helm install --wait name chart` |
| No hooks | `helm install --no-hooks name chart` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `HELM_NAMESPACE` | `default` | Default namespace |
| `HELM_DRIVER` | `secret` | Storage driver |

## Command-Line Flags

```bash
helm install --wait name chart       # Wait for ready
helm install --wait --timeout 5m name chart
helm upgrade --install name chart    # Upgrade or install
helm uninstall name                  # Uninstall
helm list -q                         # Short list (names only)
helm repo add name url               # Add repo
helm repo update                     # Update repos
helm search repo keyword             # Search repos
helm template name chart             # Render templates
helm lint chart                      # Lint chart
helm package chart                   # Package chart
```
- `-q` or `--short`: Short output (names only, `helm list` only)
- `--wait`: Wait for pods ready
- `--timeout`: Timeout duration
- `--no-hooks`: Disable hooks
- `--dry-run`: Simulate
- `--debug`: Debug output
- `-n` or `--namespace`: Namespace
