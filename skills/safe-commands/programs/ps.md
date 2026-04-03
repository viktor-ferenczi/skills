# ps

**Platforms:** Linux, macOS
**Category:** System Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| List processes | `ps aux` |
| Current session | `ps` |
| By PID | `ps -p PID` |
| By user | `ps -u username` |
| Tree view | `ps --forest` |
| Full format | `ps -ef` |
| Threads | `ps -eLf` |
| By name | `ps -C name` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `ps` piped to `kill` | Terminates processes |
| `ps` piped to `xargs rm` | Deletes files |
| Any ps output used for modification | May affect system state |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe ps Inspection Script

# All processes
ps aux | head -20

# By user
ps -u $(whoami)

# Tree view
ps --forest -u $(whoami)

# Find specific process
ps -C nginx

# Thread info
ps -eLf | grep -i nginx | head -10
```
