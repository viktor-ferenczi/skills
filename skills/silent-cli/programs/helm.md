# helm

**Platforms:** Multi-platform  
**Category:** Kubernetes Package Manager

## Quick Reference

| Goal | Command |
|------|---------|
| Short list | `helm list -q` |
| Wait for ready | `helm install --wait name chart` |

## Command-Line Flags

- `-q` or `--short`: Short output (names only, `helm list` only)
- `--wait`: Wait for pods to be ready before marking release as successful
- `--timeout`: Timeout duration for `--wait`
- `--no-hooks`: Disable hooks
- `--dry-run`: Simulate without applying

## Recommended Unattended Usage

```bash
#!/bin/bash

# Install/upgrade and wait for ready, with timeout
helm upgrade --install myrelease ./chart --wait --timeout 5m -q
```
