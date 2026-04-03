# mc (MinIO Client)

**Platforms:** Multi-platform
**Category:** Cloud Storage

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `mc --version` |
| Show help | `mc --help` |
| List buckets | `mc ls` |
| List objects | `mc ls alias/bucket` |
| Cat object | `mc cat alias/bucket/file` |
| Show info | `mc info alias/bucket` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `mc cp` | Copies/uploads files |
| `mc rm` | Deletes objects |
| `mc mb` | Creates buckets |
| `mc rb` | Removes buckets |
| `mc sync` | Syncs (may delete) |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe mc Inspection Script

# List buckets
mc ls

# List objects
mc ls myminio/bucket

# Show info
mc info myminio/bucket
```
