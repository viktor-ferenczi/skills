# winget (Windows Package Manager)

**Platforms:** Windows
**Category:** Package Management

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `winget --version` |
| Show help | `winget --help` |
| List installed | `winget list` |
| Search packages | `winget search name` |
| Show package | `winget show package` |
| Check upgrades | `winget upgrade` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `winget install` | Installs packages |
| `winget upgrade` | Upgrades packages |
| `winget uninstall` | Removes packages |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe winget Inspection Script

# List installed
winget list

# Search packages
winget search firefox
```
