# iftop

**Platforms:** Linux
**Category:** Network Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Run iftop | `iftop` |
| Show help | `iftop -h` |
| Interface | `iftop -i eth0` |
| Text mode | `iftop -t` |
| Batch mode | `iftop -b` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `iftop` with logging | Writes log files |
| Any iftop with write options | Creates files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe iftop Inspection Script

# Show help
iftop -h

# Text mode (5 seconds)
iftop -t -s 5

# Batch mode
iftop -b -n 5
```
