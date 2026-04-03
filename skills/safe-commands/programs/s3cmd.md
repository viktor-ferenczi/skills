# s3cmd

**Platforms:** Multi-platform
**Category:** Cloud Storage

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `s3cmd --version` |
| Show help | `s3cmd --help` |
| List buckets | `s3cmd ls` |
| List objects | `s3cmd ls s3://bucket` |
| Info bucket | `s3cmd info s3://bucket` |
| Get info | `s3cmd info s3://bucket/file` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `s3cmd put` | Uploads files |
| `s3cmd rm` | Deletes objects |
| `s3cmd sync` | Syncs (may delete) |
| `s3cmd mb` | Creates buckets |
| `s3cmd rb` | Removes buckets |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe s3cmd Inspection Script

# List buckets
s3cmd ls

# List objects
s3cmd ls s3://mybucket

# Info bucket
s3cmd info s3://mybucket
```
