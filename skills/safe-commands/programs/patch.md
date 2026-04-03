# patch

**Platforms:** Multi-platform
**Category:** File Utilities

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `patch --version` |
| Show help | `patch --help` |
| Dry-run | `patch --dry-run < diff` |
| Check | `patch --check < diff` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `patch < diff` | Applies patches |
| `patch -R` | Reverses patches |
| Any patch without --dry-run | Modifies files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe patch Inspection Script

# Dry-run
patch --dry-run < fix.patch

# Check
patch --check < fix.patch
```
