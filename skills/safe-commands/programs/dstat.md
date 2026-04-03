# dstat

**Platforms:** Linux
**Category:** System Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Run dstat | `dstat` |
| Show help | `dstat --help` |
| List plugins | `dstat --list` |
| Show version | `dstat --version` |
| CPU stats | `dstat --cpu` |
| Disk stats | `dstat --disk` |
| Network stats | `dstat --net` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `dstat` with output to file | Writes data |
| Any dstat with write options | Creates files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe dstat Inspection Script

# Show version
dstat --version

# List plugins
dstat --list

# CPU stats (5 samples)
dstat --cpu 5
```
