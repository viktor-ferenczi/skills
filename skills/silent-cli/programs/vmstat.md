# vmstat

**Platforms:** Multi-platform  
**Category:** System Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| Basic | `vmstat 1 5` |
| Wide | `vmstat -w 1 5` |
| Disk | `vmstat -d` |

## Command-Line Flags

```bash
vmstat                               # One snapshot
vmstat 1 5                           # Every 1s, 5 times
vmstat -w                            # Wide output
vmstat -a                            # Active/inactive memory
vmstat -s                            # Event counter statistics
vmstat -d                            # Disk statistics
vmstat -D                            # Disk summary
vmstat -f                            # Forks
vmstat -m                            # Slabinfo
vmstat -S M                          # Display in MB
```
- `-a`: Show active/inactive memory
- `-f`: Show fork count
- `-m`: Show slabinfo
- `-s`: Show event counters
- `-d`: Show disk statistics
- `-D`: Show disk summary
- `-p partition`: Show partition stats
- `-S k|K|m|M`: Unit size
- `-w`: Wide output
