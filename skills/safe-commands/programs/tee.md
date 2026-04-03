# tee

**Platforms:** Linux, macOS
**Category:** File Utilities

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show help | `tee --help` |
| Show version | `tee --version` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `tee file` | Writes to file |
| `tee -a file` | Appends to file |
| Any tee with file argument | Creates/modifies files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe tee Inspection Script

# Show help
tee --help

# Use with /dev/null (discard output)
echo "test" | tee /dev/null
```
