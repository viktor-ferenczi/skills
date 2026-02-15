# mpstat

**Platforms:** Linux  
**Category:** System Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| All CPUs | `mpstat -P ALL 1 5` |
| Specific CPU | `mpstat -P 0 1 5` |
| Summary | `mpstat 1 5` |

## Command-Line Flags

```bash
mpstat                               # CPU summary
mpstat -P ALL                        # All CPUs
mpstat -P 0                          # CPU 0 only
mpstat 1 5                           # Every 1s, 5 times
mpstat -u                            # CPU utilization
mpstat -I                            # Interrupt statistics
mpstat -I SUM                        # Interrupts summary
mpstat -I CPU                        # Per-CPU interrupts
```
- `-P`: CPU number or ALL
- `-u`: CPU utilization (default)
- `-I`: Interrupt statistics
- `-A`: Equivalent to -u -I ALL
