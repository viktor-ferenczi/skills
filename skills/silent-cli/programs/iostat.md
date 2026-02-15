# iostat

**Platforms:** Multi-platform  
**Category:** System Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| CPU + Disk | `iostat -x 1 5` |
| Extended | `iostat -xz 1` |
| Human readable | `iostat -h` |

## Command-Line Flags

```bash
iostat                               # Basic stats
iostat 1 5                           # Every 1s, 5 times
iostat -x                            # Extended stats
iostat -xz 1                         # Extended, omit idle
iostat -d                            # Device only
iostat -c                            # CPU only
iostat -h                            # Human readable sizes
iostat -k                            # KB/s
iostat -m                            # MB/s
iostat -p sda                        # Specific device
iostat -N                            # LVM names
```
- `-x`: Extended statistics
- `-z`: Omit idle devices
- `-c`: CPU statistics
- `-d`: Device statistics
- `-h`: Human readable
- `-k`: KB/s
- `-m`: MB/s
- `-p`: Device partition
- `-N`: Display LVM names
