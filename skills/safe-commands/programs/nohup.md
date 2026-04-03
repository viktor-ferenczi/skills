# nohup

**Platforms:** Linux, macOS
**Category:** System Utilities

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show help | `nohup --help` |
| Show version | `nohup --version` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `nohup command &` | Runs command in background |
| Any nohup execution | Starts persistent processes |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe nohup Inspection Script

# Show help
nohup --help

# Show version
nohup --version
```
