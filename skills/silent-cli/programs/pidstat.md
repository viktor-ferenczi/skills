# pidstat

**Platforms:** Linux  
**Category:** Process Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| CPU by PID | `pidstat -u -p PID 1 5` |
| All processes | `pidstat -u 1 5` |
| Memory | `pidstat -r -p PID 1 5` |

## Command-Line Flags

```bash
pidstat                              # CPU stats
pidstat -u                           # CPU utilization
pidstat -r                           # Memory utilization
pidstat -d                           # I/O statistics
pidstat -w                           # Task switching
pidstat -p PID                       # Specific PID
pidstat -p ALL                       # All processes
pidstat -C firefox                   # By command name
pidstat -G firefox                   # By command name regex
pidstat -l                           # Show process name
```
- `-u`: CPU utilization
- `-r`: Memory utilization
- `-d`: I/O statistics
- `-w`: Task switching
- `-p`: Process ID or ALL
- `-C`: Command name filter
- `-G`: Regex filter
- `-l`: Show full process name
