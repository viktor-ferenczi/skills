# salt (SaltStack)

**Platforms:** Multi-platform
**Category:** Automation

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `salt --version` |
| Show help | `salt --help` |
| Ping minions | `salt '*' test.ping` |
| List grains | `salt '*' grains.items` |
| List pillars | `salt '*' pillar.items` |
| Show config | `salt '*' config.get` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `salt '*' state.apply` | Applies states |
| `salt '*' cmd.run` | Runs commands |
| `salt '*' pkg.install` | Installs packages |
| Any salt state execution | Makes changes |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe salt Inspection Script

# Ping minions
salt '*' test.ping

# List grains
salt '*' grains.items
```
