# lsof (list open files)

**Platforms:** Linux, macOS  
**Category:** File/Process Inspection

## Quick Reference

| Goal | Command |
|------|---------|
| Terse (PIDs only) | `lsof -t -i :80` |
| Parsable output | `lsof -F pcn` |

## Command-Line Flags

- `-t`: Terse output (PIDs only, ideal for scripting)
- `-F`: Field/parsable output (machine-readable)
- `-n`: No DNS lookup (avoids delays/hangs in automation)
- `-P`: No port name resolution (avoids delays)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Find process using port 80 (PIDs only)
lsof -t -i :80

# Kill processes using port (scripted)
kill $(lsof -t -i :8080)

# Machine-readable field output
lsof -F pcn -i :80
```
