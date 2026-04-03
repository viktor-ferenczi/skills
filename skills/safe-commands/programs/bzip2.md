# bzip2

**Platforms:** Multi-platform
**Category:** File Operations

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Test integrity | `bzip2 -t file.bz2` |
| Show info | `bzip2 -v file.bz2` |
| Keep original | `bzip2 -k file` |
| Fast compress | `bzip2 -1 file` |
| Best compress | `bzip2 -9 file` |
| Decompress | `bzip2 -d file.bz2` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `bzip2 file` | Compresses (removes original) |
| `bunzip2 file.bz2` | Decompresses (removes .bz2) |
| Any bzip2 without -k | Removes original file |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe bzip2 Inspection Script

# Test integrity
bzip2 -t archive.tar.bz2

# Show info
bzip2 -v archive.tar.bz2

# Compress keeping original
bzip2 -k file.txt

# Decompress keeping original
bzip2 -dk archive.tar.bz2
```
