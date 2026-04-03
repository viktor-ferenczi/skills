# grafana-cli

**Platforms:** Multi-platform
**Category:** Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `grafana-cli --version` |
| Show help | `grafana-cli --help` |
| List plugins | `grafana-cli plugins ls` |
| Plugin info | `grafana-cli plugins info plugin` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `grafana-cli plugins install` | Installs plugins |
| `grafana-cli plugins update` | Updates plugins |
| `grafana-cli plugins remove` | Removes plugins |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe grafana-cli Inspection Script

# Show version
grafana-cli --version

# List plugins
grafana-cli plugins ls

# Plugin info
grafana-cli plugins info grafana-clock-panel
```
