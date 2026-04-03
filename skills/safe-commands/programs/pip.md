# pip

**Platforms:** Multi-platform
**Category:** Package Management

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `pip --version` |
| Show help | `pip --help` |
| List packages | `pip list` |
| Show info | `pip show package` |
| Search packages | `pip search name` (deprecated) |
| Check outdated | `pip list --outdated` |
| Freeze | `pip freeze` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `pip install` | Installs packages |
| `pip uninstall` | Removes packages |
| `pip upgrade` | Upgrades packages |
| `pip config set` | Modifies config |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe pip Inspection Script

# List packages
pip list

# Show package info
pip show requests

# Check outdated
pip list --outdated
```
