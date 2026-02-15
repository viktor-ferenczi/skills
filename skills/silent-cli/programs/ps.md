# ps

**Platforms:** Multi-platform  
**Category:** Process Status

## Quick Reference

| Goal | Command |
|------|---------|
| No header | `ps --no-headers -eo pid,ppid,cmd` |

## Command-Line Flags

```bash
ps -eo pid,ppid,cmd --no-headers        # Custom format, no headers (machine-readable)
```
- `--no-headers`: No header line (machine-readable output)
- `-o`: User-defined format (machine-readable)
