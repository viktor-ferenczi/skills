# mpstat

**Platforms:** Linux
**Category:** System Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show stats | `mpstat` |
| All CPUs | `mpstat -P ALL` |
| Interval | `mpstat interval count` |
| Show help | `mpstat --help` |
| Show version | `mpstat --version` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `mpstat` with output to file | Writes data |
| Any mpstat with write options | Creates files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe mpstat Inspection Script

# Show version
mpstat --version

# All CPUs stats
mpstat -P ALL 1 3

# Single report
mpstat
```
