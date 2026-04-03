# ping

**Platforms:** Multi-platform
**Category:** Network Utilities

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Ping host | `ping -c 4 host` |
| Show help | `ping --help` |
| Show version | `ping -V` |
| Quick ping | `ping -c 1 host` |
| Flood ping | `ping -f host` (requires root) |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `ping -f` | Flood ping (may overwhelm) |
| Continuous ping | May trigger alerts |
| High frequency ping | Network stress |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe ping Inspection Script

# Quick ping
ping -c 3 example.com

# With timestamp
ping -c 3 -D example.com
```
