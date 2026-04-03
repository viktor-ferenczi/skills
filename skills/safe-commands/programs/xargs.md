# xargs

**Platforms:** Linux, macOS
**Category:** System Utilities

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show help | `xargs --help` |
| Show version | `xargs --version` |
| Echo input | `echo input | xargs echo` |
| Show args | `echo input | xargs -t echo` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `xargs rm` | Deletes files |
| `xargs chmod` | Changes permissions |
| `xargs chown` | Changes ownership |
| Any xargs with destructive command | May cause damage |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe xargs Inspection Script

# Echo input
echo "file1 file2" | xargs echo

# Show what would run
echo "file1" | xargs -t ls
```
