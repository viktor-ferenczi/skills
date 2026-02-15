# atop

**Platforms:** Linux
**Category:** System Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| Parseable CPU/MEM/DSK | `atop -P CPU,MEM,DSK 5 3` |
| JSON output | `atop -J ALL 10 6` |
| Write raw log for replay | `atop -w /tmp/atop.raw 5 3` |

## Command-Line Flags

- `-P label[,label]...`: Parseable whitespace-separated output (labels: `CPU`, `cpu`, `CPL`, `MEM`, `SWP`, `PAG`, `LVM`, `MDD`, `DSK`, `NET`, `PRG`, `PRC`, `PRM`, `PRD`, `PRN`, or `ALL`)
- `-J label[,label]...`: JSON output for specified labels (same labels as `-P`)
- `-Z`: Replace spaces in command names with underscores, omit parentheses (use with `-P`)
- `-w rawfile`: Write compressed binary raw data to file for later replay
- `-r rawfile`: Read and replay a raw log file
- `-L width`: Set output line width when redirected (default: 80)
- Positional: `interval samples` (e.g., `5 3` = 5s interval, 3 samples)

Auto-detects whether stdout is a terminal. When piped or redirected, it produces flat ASCII output without ncurses.

## Recommended Unattended Usage

```bash
#!/bin/bash

# Parseable output: CPU, memory and disk stats, 5s interval, 3 samples
atop -P CPU,MEM,DSK -Z 5 3

# JSON output: all labels, 10s interval, 6 samples
atop -J ALL 10 6
```
