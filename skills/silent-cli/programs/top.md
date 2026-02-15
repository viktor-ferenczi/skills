# top

**Platforms:** Linux
**Category:** System Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| Single snapshot | `top -b -n 1` |
| 5 samples at 2s interval | `top -b -n 5 -d 2` |
| Wide output for logging | `top -b -n 1 -w 512` |

## Command-Line Flags

- `-b`: Batch mode (no TUI, output suitable for piping or logging)
- `-n NUMBER`: Exit after NUMBER iterations
- `-d SECS`: Delay between updates (supports fractional seconds like `0.5`)
- `-w [COLUMNS]`: Output width (up to 512 in batch mode)
- `-o FIELD`: Sort by named field (e.g., `%MEM`, `%CPU`)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Single snapshot of all processes, wide output
top -b -n 1 -w 200

# Collect 5 samples at 2-second intervals
top -b -n 5 -d 2 > top_report.txt
```
