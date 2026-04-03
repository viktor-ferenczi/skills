# duplicity

**Platforms:** Linux, macOS
**Category:** Backup

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `duplicity --version` |
| Show help | `duplicity --help` |
| List backups | `duplicity list-current-files URL` |
| Show status | `duplicity collection-status URL` |
| Compare | `duplicity compare URL` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `duplicity backup` | Creates backups |
| `duplicity remove-older-than` | Deletes backups |
| `duplicity cleanup` | Removes old backups |
| Any duplicity write operation | Modifies backup storage |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe duplicity Inspection Script

# Show version
duplicity --version

# List current files
duplicity list-current-files file:///backup

# Show status
duplicity collection-status file:///backup
```
