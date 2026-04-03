# lsof

**Platforms:** Linux, macOS
**Category:** System Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| List all files | `lsof` |
| By user | `lsof -u username` |
| By PID | `lsof -p PID` |
| By port | `lsof -i :port` |
| By file | `lsof /path` |
| Network files | `lsof -i4` (IPv4) |
| TCP files | `lsof -i tcp` |
| Process info | `lsof -p PID -F` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `lsof` piped to `kill` | Terminates processes |
| `lsof` used for file deletion | May modify system |
| Any lsof output for modification | Affects system state |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe lsof Inspection Script

# All open files
lsof | head -30

# By user
lsof -u $(whoami)

# Network connections
lsof -i4

# Specific port
lsof -i :80

# Process files
lsof -p $(pgrep -f nginx) 2>/dev/null
```
