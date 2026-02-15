# powertop

**Platforms:** Linux
**Category:** Power Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| CSV report | `powertop --time=60 --csv=report.csv --iteration=1 -q` |
| HTML report | `powertop --time=60 --html=report.html --iteration=1 -q` |

## Command-Line Flags

- `-t SECONDS` or `--time[=SECONDS]`: Collect data for specified seconds, then exit (non-interactive)
- `-i N` or `--iteration[=N]`: Number of measurement iterations
- `-C [FILE]` or `--csv[=FILENAME]`: Generate CSV report (default: `powertop.csv`)
- `-r [FILE]` or `--html[=FILENAME]`: Generate HTML report (default: `powertop.html`)
- `-q` or `--quiet`: Suppress stderr output

## Recommended Unattended Usage

```bash
#!/bin/bash

# 60-second measurement, single iteration, CSV output, quiet
powertop --time=60 --csv=report.csv --iteration=1 --quiet
```
