# gzip

**Platforms:** Multi-platform
**Category:** File Operations

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Test integrity | `gzip -t file.gz` |
| Show info | `gzip -l file.gz` |
| Show ratio | `gzip -lv file.gz` |
| Keep original | `gzip -k file` |
| Fast compress | `gzip -1 file` |
| Best compress | `gzip -9 file` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `gzip file` | Compresses (removes original) |
| `gzip -d file.gz` | Decompresses (removes .gz) |
| `gunzip file.gz` | Decompresses file |
| Any gzip without -k | Removes original file |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe gzip Inspection Script

# Test integrity
gzip -t archive.tar.gz

# Show compression info
gzip -l archive.tar.gz

# Show with ratio
gzip -lv archive.tar.gz

# Compress keeping original
gzip -k file.txt
```
