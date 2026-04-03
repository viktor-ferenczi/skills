# loki (Grafana Loki CLI - logcli)

**Platforms:** Multi-platform
**Category:** Log Aggregation

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `logcli version` |
| Show help | `logcli --help` |
| Query logs | `logcli query "{app=\"app\"}"` |
| List labels | `logcli labels` |
| Label values | `logcli label-values label` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `logcli` queries are read-only | Generally safe |
| High volume queries | May impact performance |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe logcli Inspection Script

# List labels
logcli labels

# Query limited logs
logcli query '{app="app"}' --limit=100
```
