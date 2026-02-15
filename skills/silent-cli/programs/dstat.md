# dstat

**Platforms:** Linux  
**Category:** System Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| All stats | `dstat` |
| CPU + Disk | `dstat -cd` |
| No colors | `dstat --nocolor` |

## Command-Line Flags

```bash
dstat                                # All stats
dstat 1 10                           # Every 1s, 10 times
dstat -c                             # CPU only
dstat -d                             # Disk only
dstat -n                             # Network only
dstat -m                             # Memory only
dstat -cdngy                         # CPU, disk, net, page, system
dstat --nocolor                      # No colors
dstat --output report.csv 1 60       # Output to CSV
```
- `-c`: CPU stats
- `-d`: Disk stats
- `-n`: Network stats
- `-m`: Memory stats
- `-y`: System stats
- `-p`: Process stats
- `-g`: Page stats
- `--nocolor`: No colors
- `--output`: Output to file
