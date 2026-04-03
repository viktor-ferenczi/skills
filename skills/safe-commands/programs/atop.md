# atop

**Platforms:** Linux
**Category:** System Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Run atop | `atop` |
| Interval mode | `atop interval` |
| Show help | `atop -h` |
| Read log | `atop -r logfile` |
| Show version | `atop -v` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `atop -w` | Writes log files |
| Any atop with write options | Creates files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe atop Inspection Script

# Show version
atop -v

# Run in read-only mode
atop 5

# Read existing log
atop -r /var/log/atop/atop_20240101
```
