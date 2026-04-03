# md5sum

**Platforms:** Linux, macOS
**Category:** File Utilities

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Checksum file | `md5sum file` |
| Check mode | `md5sum -c file.md5` |
| Show help | `md5sum --help` |
| Show version | `md5sum --version` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `md5sum` is read-only | Generally safe |
| Piping to destructive commands | May cause issues |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe md5sum Inspection Script

# Checksum file
md5sum file.txt

# Check mode
md5sum -c file.txt.md5
```
