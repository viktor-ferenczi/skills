# tar

**Platforms:** Linux, macOS
**Category:** File Operations

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| List archive | `tar -tf archive.tar` |
| List verbose | `tar -tvf archive.tar` |
| Extract to stdout | `tar -xOf archive.tar file` |
| Show sizes | `tar --show-sizes -tvf archive.tar` |
| Gzip list | `tar -tzf archive.tar.gz` |
| Bzip2 list | `tar -tjf archive.tar.bz2` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `tar -xf` | Extracts files (may overwrite) |
| `tar -czf` | Creates archives (writes disk) |
| `tar -xzf` | Extracts gzip archives |
| `tar --overwrite` | Overwrites existing files |
| Any tar extraction without review | May overwrite system files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe tar Inspection Script

# List archive contents
tar -tf archive.tar

# List with details
tar -tvf archive.tar

# List gzip archive
tar -tzf archive.tar.gz

# List bzip2 archive
tar -tjf archive.tar.bz2

# Show sizes
tar --show-sizes -tvf archive.tar
```
