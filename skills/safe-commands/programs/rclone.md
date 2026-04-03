# rclone

**Platforms:** Multi-platform
**Category:** Cloud Storage

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `rclone version` |
| Show help | `rclone --help` |
| List remotes | `rclone listremotes` |
| List files | `rclone lsf remote:bucket` |
| Size | `rclone size remote:bucket` |
| Checksum | `rclone checksum remote:bucket` |
| Diff | `rclone diff remote:bucket` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `rclone copy` | Copies files |
| `rclone sync` | Syncs (may delete) |
| `rclone move` | Moves/deletes files |
| `rclone delete` | Deletes files |
| `rclone purge` | Purges directory |
| `rclone mkdir` | Creates directories |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe rclone Inspection Script

# List remotes
rclone listremotes

# List files
rclone lsf myremote:bucket

# Show size
rclone size myremote:bucket
```
