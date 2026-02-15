# iotop

**Platforms:** Linux
**Category:** Disk I/O Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| Batch snapshot | `iotop -b -n 1` |
| Timestamped, no headers | `iotop -b -n 5 -t -qqq` |
| Kilobyte units for parsing | `iotop -b -n 5 -t -k -qqq` |

## Command-Line Flags

- `-b` or `--batch`: Non-interactive mode (no TUI), suitable for logging
- `-n NUM` or `--iter=NUM`: Number of iterations before exiting
- `-d SEC` or `--delay=SEC`: Delay between iterations (default: 1, accepts fractional)
- `-t` or `--time`: Prefix each line with a timestamp (implies `--batch`)
- `-q` or `--quiet`: Suppress headers (`-q` first iteration only, `-qq` no column names, `-qqq` no I/O summary)
- `-k` or `--kilobytes`: Use kilobytes instead of human-friendly units (easier to parse)
- `-a` or `--accumulated`: Show accumulated I/O instead of bandwidth

## Recommended Unattended Usage

```bash
#!/bin/bash

# 5 samples, timestamped, consistent units, minimal headers
iotop -b -n 5 -t -k -qqq
```
