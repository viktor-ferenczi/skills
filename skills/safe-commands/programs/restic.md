# restic

**Platforms:** Multi-platform
**Category:** Backup

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `restic --version` |
| Show help | `restic --help` |
| List snapshots | `restic snapshots` |
| List files | `restic ls snapshot-id` |
| Stats | `restic stats snapshot-id` |
| Check repo | `restic check` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `restic backup` | Creates backups |
| `restic forget` | Forgets snapshots |
| `restic prune` | Prunes repository |
| `restic unlock` | Removes locks |
| Any restic write operation | Modifies repository |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe restic Inspection Script

# List snapshots
restic snapshots

# Check repository
restic check

# List files in snapshot
restic ls latest
```
