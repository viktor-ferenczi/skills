# nettop

**Platforms:** macOS
**Category:** Network Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| Logging mode (text) | `nettop -l 5 -s 2 -n -P` |
| CSV output | `nettop -L 5 -s 2 -n -P` |

## Command-Line Flags

- `-l SAMPLES`: Logging mode with raw text output (no TUI); 0 for infinite
- `-L SAMPLES`: Logging mode with CSV output; 0 for infinite
- `-s DELAY`: Delay between updates in seconds (default: 1)
- `-P`: Per-process summary only (skip per-connection details)
- `-n`: Disable address-to-name resolution (avoids DNS delays)
- `-j col,col,...`: Include only specified columns
- `-k col,col,...`: Exclude specified columns

## Recommended Unattended Usage

```bash
#!/bin/bash

# 5 CSV samples, 2s interval, no DNS, process summary only
nettop -L 5 -s 2 -n -P
```
