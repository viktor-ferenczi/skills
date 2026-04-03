# pidstat

**Platforms:** Linux
**Category:** System Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show stats | `pidstat` |
| Show help | `pidstat --help` |
| CPU stats | `pidstat -u` |
| Memory stats | `pidstat -r` |
| IO stats | `pidstat -d` |
| Show version | `pidstat --version` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `pidstat` with output to file | Writes data |
| Any pidstat with write options | Creates files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe pidstat Inspection Script

# Show version
pidstat --version

# CPU stats
pidstat -u 1 3

# Memory stats
pidstat -r 1 3
```
