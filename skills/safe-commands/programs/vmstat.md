# vmstat

**Platforms:** Linux, macOS
**Category:** System Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show stats | `vmstat` |
| Interval | `vmstat interval count` |
| Show help | `vmstat --help` |
| Show version | `vmstat --version` |
| Active | `vmstat -a` |
| Slab info | `vmstat -s` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `vmstat` with output to file | Writes data |
| Any vmstat with write options | Creates files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe vmstat Inspection Script

# Show version
vmstat --version

# Single report
vmstat

# Active processes
vmstat -a 1 3
```
