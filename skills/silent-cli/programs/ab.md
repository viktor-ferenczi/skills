# ab (Apache Bench)

**Platforms:** Multi-platform  
**Category:** Load Testing

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet mode | `ab -q -n 1000 http://localhost/` |
| No progress | `ab -v 0 -n 1000 http://localhost/` |

## Command-Line Flags

- `-q`: Quiet mode — do not show progress when doing more than 150 requests
- `-v 0`: Set verbosity level to 0 (no progress output)
- `-r`: Don't exit on socket receive errors (useful for unattended runs)
- `-s`: Timeout in seconds (prevent hanging in automation)
