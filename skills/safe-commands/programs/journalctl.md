# journalctl

**Platforms:** Linux
**Category:** System Logging

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show logs | `journalctl` |
| Show help | `journalctl --help` |
| Last N lines | `journalctl -n 100` |
| By unit | `journalctl -u service` |
| By priority | `journalctl -p err` |
| Since time | `journalctl --since "1 hour ago"` |
| List boots | `journalctl --list-boots` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `journalctl --rotate` | Rotates logs |
| `journalctl --vacuum` | Removes old logs |
| `journalctl --flush` | Flushes logs |
| Any journalctl with write options | Modifies journal |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe journalctl Inspection Script

# Last 100 lines
journalctl -n 100

# By unit
journalctl -u sshd

# By priority
journalctl -p err -n 50
```
