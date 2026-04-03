# kubectl

**Platforms:** Multi-platform
**Category:** Container & Orchestration

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| List pods | `kubectl get pods` |
| List deployments | `kubectl get deployments` |
| List services | `kubectl get services` |
| Pod details | `kubectl describe pod <name>` |
| View logs | `kubectl logs <pod>` |
| ConfigMap content | `kubectl get configmap <name> -o yaml` |
| Secret metadata | `kubectl get secret <name> -o yaml` |
| Events | `kubectl get events` |
| Node info | `kubectl get nodes` |
| Resource usage | `kubectl top pods` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `kubectl apply -f` | Applies/modifies resources |
| `kubectl create` | Creates new resources |
| `kubectl delete` | Deletes resources |
| `kubectl scale` | Scales deployments |
| `kubectl rollout` | Manages rollouts |
| `kubectl exec` | Executes in containers |
| `kubectl edit` | Edits resources |
| `kubectl patch` | Patches resources |

## Environment Variables for Safe Operation

| Variable | Description |
|----------|-------------|
| `KUBECONFIG` | Path to kubeconfig |
| `KUBERNETES_SERVICE_ACCOUNT` | Service account token |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe Kubernetes Inspection Script

echo "=== Cluster Info ==="
kubectl cluster-info

echo "=== Nodes ==="
kubectl get nodes -o wide

echo "=== Namespaces ==="
kubectl get namespaces

echo "=== Pods (all namespaces) ==="
kubectl get pods --all-namespaces -o wide

echo "=== Deployments ==="
kubectl get deployments --all-namespaces

echo "=== Services ==="
kubectl get services --all-namespaces

echo "=== Recent Events ==="
kubectl get events --all-namespaces --sort-by='.lastTimestamp' | tail -20
```
