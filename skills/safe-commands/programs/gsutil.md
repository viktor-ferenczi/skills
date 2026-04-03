# gsutil (Google Cloud Storage)

**Platforms:** Multi-platform
**Category:** Cloud Storage

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `gsutil version` |
| Show help | `gsutil --help` |
| List buckets | `gsutil ls` |
| List objects | `gsutil ls gs://bucket` |
| Get object | `gsutil cat gs://bucket/file` |
| Show stats | `gsutil du -sh gs://bucket` |
| Check ACL | `gsutil acl get gs://bucket` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `gsutil cp local gs://` | Uploads data |
| `gsutil rm gs://` | Deletes objects |
| `gsutil rsync` | Syncs (may delete) |
| `gsutil mv` | Moves/deletes objects |
| `gsutil acl set` | Modifies ACL |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe gsutil Inspection Script

# List buckets
gsutil ls

# List objects
gsutil ls gs://my-bucket

# Show stats
gsutil du -sh gs://my-bucket
```
