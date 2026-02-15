# date

**Platforms:** Multi-platform  
**Category:** Date/Time

## Quick Reference

| Goal | Command |
|------|---------|
| Current time | `date` |
| Unix timestamp | `date +%s` |
| Custom format | `date +"%Y-%m-%d %H:%M:%S"` |
| Parse date | `date -d "2023-01-01" +%s` |

## Command-Line Flags

```bash
date                                 # Current date/time
date +%s                             # Unix timestamp
date +"%Y-%m-%d"                     # 2023-12-31
date +"%H:%M:%S"                     # 14:30:00
date +"%Y-%m-%dT%H:%M:%SZ"           # ISO 8601
date -u                              # UTC
date -d "@1704067200"                # From timestamp (Linux)
date -r 1704067200                   # From timestamp (macOS)
date -d "2023-01-01" +%s             # To timestamp (Linux)
date -j -f "%Y-%m-%d" "2023-01-01" +%s  # To timestamp (macOS)
```

### Linux (GNU date)
- `-d` or `--date=STRING`: Parse date string
- `-u` or `--utc`: UTC
- `-r FILE` or `--reference=FILE`: Use file's timestamp
- `+%s`: Seconds since epoch
- `+%Y`: Year, `+%m`: Month, `+%d`: Day
- `+%H`: Hour, `+%M`: Minute, `+%S`: Second

### macOS (BSD date)
- `-u`: UTC
- `-r SECONDS`: Seconds since epoch
- `-j`: Don't set date
- `-f FORMAT`: Input format
- `+FORMAT`: Output format

## Recommended Unattended Usage

```bash
#!/bin/bash

# ISO timestamp
ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

# Filename timestamp
filename="backup_$(date +%Y%m%d_%H%M%S).tar.gz"

# Calculate future date (Linux)
future=$(date -d "+7 days" +"%Y-%m-%d")
```
