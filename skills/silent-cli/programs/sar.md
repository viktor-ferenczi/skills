# sar (sysstat)

**Platforms:** Linux  
**Category:** System Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| CPU | `sar -u 1 5` |
| Memory | `sar -r 1 5` |
| Disk | `sar -d 1 5` |

## Command-Line Flags

```bash
sar -u 1 5                           # CPU every 1s, 5 times
sar -r 1 5                           # Memory
sar -d 1 5                           # Disk
sar -n DEV 1 5                       # Network
sar -q 1 5                           # Load average
sar -b 1 5                           # I/O
sar -f /var/log/sysstat/sa10         # Read from file
```
- `-u`: CPU usage
- `-r`: Memory utilization
- `-d`: Block device activity
- `-n DEV`: Network device statistics
- `-q`: Queue length and load
- `-b`: I/O and transfer rate
- `-f`: Read from data file
- `-s`: Start time
- `-e`: End time
