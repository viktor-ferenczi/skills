# yum/dnf

**Platforms:** Linux (RHEL/CentOS/Fedora)
**Category:** Package Management

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `dnf --version` |
| Show help | `dnf --help` |
| List installed | `dnf list installed` |
| Search packages | `dnf search name` |
| Show info | `dnf info package` |
| List available | `dnf list available` |
| Check updates | `dnf check-update` |
| History | `dnf history list` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `dnf install` | Installs packages |
| `dnf remove` | Removes packages |
| `dnf update` | Updates packages |
| `dnf clean` | Cleans cache |
| `dnf makecache` | Creates cache |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe dnf Inspection Script

# List installed
dnf list installed | head -20

# Search packages
dnf search firefox

# Check updates
dnf check-update
```
