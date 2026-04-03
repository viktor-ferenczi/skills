# ufw (Uncomplicated Firewall)

**Platforms:** Linux
**Category:** Firewall/Security

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `ufw version` |
| Show help | `ufw --help` |
| Show status | `ufw status` |
| Show verbose | `ufw status verbose` |
| Show numbered | `ufw status numbered` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `ufw enable` | Enables firewall |
| `ufw disable` | Disables firewall |
| `ufw allow` | Adds rules |
| `ufw deny` | Adds rules |
| `ufw delete` | Deletes rules |
| `ufw reset` | Resets firewall |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe ufw Inspection Script

# Show status
ufw status

# Show verbose
ufw status verbose
```
