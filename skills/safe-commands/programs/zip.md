# zip

**Platforms:** Multi-platform
**Category:** File Compression

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `zip --version` |
| Show help | `zip --help` |
| Test archive | `zip -T archive.zip` |
| List contents | `unzip -l archive.zip` |
| Show info | `zipinfo archive.zip` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `zip archive.zip files` | Creates archives |
| `unzip archive.zip` | Extracts files |
| `zip -d` | Deletes from archive |
| Any zip/unzip operation | Creates/modifies files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe zip Inspection Script

# Test archive
zip -T archive.zip

# List contents
unzip -l archive.zip

# Show info
zipinfo archive.zip
```
