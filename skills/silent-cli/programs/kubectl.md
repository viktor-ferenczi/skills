# kubectl

**Platforms:** Multi-platform  
**Category:** Kubernetes CLI

## Quick Reference

| Goal | Command |
|------|---------|
| Silent apply | `kubectl apply -f file.yaml` |
| Quiet get | `kubectl get pods -o name` |
| Wait for ready | `kubectl wait --for=condition=ready pod/name` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `KUBECONFIG` | `/path/to/config` | Config file path |
| `KUBECTL_EDITOR` | `nano` | Default editor |

## Command-Line Flags

```bash
kubectl apply -f file.yaml           # Apply manifest
kubectl apply -f dir/                # Apply directory
kubectl get pods -o name             # Short output
kubectl get pods -o json | jq        # JSON output
kubectl get pods --no-headers        # No headers
kubectl describe pod name            # Details
kubectl logs pod-name                # Logs
kubectl logs -f pod-name             # Follow logs
kubectl delete -f file.yaml          # Delete resources
kubectl wait --for=condition=ready pod/name --timeout=60s
```
- `-f`: File or directory
- `-o`: Output format (json, yaml, wide, name, custom-columns=...)
- `--no-headers`: No headers in table
- `-n` or `--namespace`: Namespace
- `--all-namespaces` or `-A`: All namespaces
- `--dry-run=client`: Simulate without applying
- `--timeout`: Timeout for wait
