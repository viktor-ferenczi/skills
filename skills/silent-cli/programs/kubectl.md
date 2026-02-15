# kubectl

**Platforms:** Multi-platform  
**Category:** Kubernetes CLI

## Quick Reference

| Goal | Command |
|------|---------|
| Machine-readable output | `kubectl get pods -o json` |
| No headers | `kubectl get pods --no-headers` |
| Wait for ready | `kubectl wait --for=condition=ready pod/name` |

## Command-Line Flags

- `-o`: Output format (`json`, `yaml`, `name`, `custom-columns=...`) — machine-readable formats
- `--no-headers`: No headers in table output
- `--dry-run=client`: Simulate without applying
- `--timeout`: Timeout for `wait` command

## Recommended Unattended Usage

```bash
#!/bin/bash

# Apply manifest (inherently non-interactive)
kubectl apply -f file.yaml

# Wait for pod readiness with timeout
kubectl wait --for=condition=ready pod/name --timeout=60s

# Machine-readable output for scripting
kubectl get pods -o json | jq '.items[].metadata.name'
kubectl get pods -o name --no-headers
```
