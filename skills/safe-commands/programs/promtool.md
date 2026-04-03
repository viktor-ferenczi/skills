# promtool (Prometheus)

**Platforms:** Multi-platform
**Category:** Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `promtool --version` |
| Show help | `promtool --help` |
| Check config | `promtool check config` |
| Check rules | `promtool check rules` |
| Query | `promtool query instant` |
| Series | `promtool series` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `promtool tsdb create` | Creates TSDB |
| `promtool tsdb dump` | Dumps TSDB |
| Any promtool write operation | Modifies data |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe promtool Inspection Script

# Check config
promtool check config prometheus.yml

# Check rules
promtool check rules rules.yml
```
