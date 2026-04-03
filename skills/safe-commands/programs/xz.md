# xz

**Platforms:** Linux, macOS
**Category:** File Compression

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `xz --version` |
| Show help | `xz --help` |
| Test file | `xz -t file.xz` |
| List info | `xz -l file.xz` |
| Decompress to stdout | `xz -dc file.xz` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `xz file` | Compresses (removes original) |
| `xz -d file.xz` | Decompresses |
| `xz -k` | Keeps original but creates new |
| Any xz compression/decompression | Creates/modifies files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe xz Inspection Script

# Test file integrity
xz -t file.xz

# List info
xz -l file.xz
```
