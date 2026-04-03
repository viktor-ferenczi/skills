# kill

**Platforms:** Linux, macOS
**Category:** System Utilities

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| List signals | `kill -l` |
| Show help | `kill --help` |
| Show version | `kill --version` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `kill PID` | Terminates process |
| `kill -9 PID` | Force kills process |
| `kill -1 PID` | Sends SIGHUP |
| Any kill with PID | May terminate processes |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe kill Inspection Script

# List signals
kill -l

# Show version
kill --version
```
