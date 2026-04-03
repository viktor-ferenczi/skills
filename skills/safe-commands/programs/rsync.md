# rsync

**Platforms:** Linux, macOS
**Category:** File Synchronization

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `rsync --version` |
| Show help | `rsync --help` |
| Dry-run | `rsync -n src/ dest/` |
| List only | `rsync --list-only src/` |
| Compare | `rsync -n -v src/ dest/` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `rsync src/ dest/` | Syncs files |
| `rsync --delete` | Deletes files |
| `rsync -a` | Full archive sync |
| Without -n | Actually copies files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe rsync Inspection Script

# Dry-run
rsync -n -av src/ dest/

# List only
rsync --list-only src/
```
