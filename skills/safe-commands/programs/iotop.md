# iotop

**Platforms:** Linux
**Category:** System Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Run iotop | `iotop` |
| Batch mode | `iotop -b` |
| Show help | `iotop --help` |
| Show version | `iotop --version` |
| Total stats | `iotop -o` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `iotop` with logging | Writes log files |
| Any iotop with write options | Creates files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe iotop Inspection Script

# Show version
iotop --version

# Batch mode (single iteration)
iotop -b -n 1

# Only active processes
iotop -o -b -n 5
```
