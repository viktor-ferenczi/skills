# ps

**Platforms:** Multi-platform  
**Category:** Process Status

## Quick Reference

| Goal | Command |
|------|---------|
| All processes | `ps aux` |
| Specific format | `ps -eo pid,ppid,cmd` |
| No header | `ps --no-headers` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `PS_PERSONALITY` | `linux` | Set personality |

## Command-Line Flags

```bash
ps aux                                  # BSD format
ps -ef                                  # Standard format
ps -eo pid,ppid,cmd --no-headers        # Custom format, no headers
ps aux | grep [p]attern                 # Filter processes
```
- `aux`: BSD format, all users
- `-ef`: Full format
- `-e`: All processes
- `-o`: User-defined format
- `--no-headers`: No header line
