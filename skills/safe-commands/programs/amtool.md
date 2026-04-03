# amtool

**Platforms:** Multi-platform
**Category:** Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `amtool --version` |
| Show help | `amtool --help` |
| Check config | `amtool check-config` |
| Query alerts | `amtool alert` |
| Show receivers | `amtool receiver` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `amtool silence add` | Adds silences |
| `amtool silence expire` | Expires silences |
| `amtool config update` | Updates config |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe amtool Inspection Script

# Show version
amtool --version

# Check config
amtool check-config

# Query alerts
amtool alert
```
