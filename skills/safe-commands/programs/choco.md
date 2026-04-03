# choco (Chocolatey)

**Platforms:** Windows
**Category:** Package Management

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `choco --version` |
| Show help | `choco --help` |
| List installed | `choco list --local-only` |
| Search packages | `choco search name` |
| Show info | `choco info package` |
| Show outdated | `choco outdated` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `choco install` | Installs packages |
| `choco upgrade` | Upgrades packages |
| `choco uninstall` | Removes packages |
| `choco feature enable` | Enables features |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe choco Inspection Script

# Show version
choco --version

# List installed
choco list --local-only

# Show outdated
choco outdated
```
