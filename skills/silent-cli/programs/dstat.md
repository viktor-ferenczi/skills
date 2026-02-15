# dstat

**Platforms:** Linux  
**Category:** System Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| No colors | `dstat --nocolor` |
| CSV output (machine-readable) | `dstat --output report.csv 1 60` |

## Command-Line Flags

- `--nocolor`: Disable color output (suitable for log files and non-TTY)
- `--output`: Write output to CSV file (machine-readable format for automation)

`dstat` is inherently non-interactive. Use `--nocolor` to disable terminal color codes and `--output` for machine-parseable CSV output.
