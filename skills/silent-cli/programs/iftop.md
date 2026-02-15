# iftop

**Platforms:** Linux  
**Category:** Network Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive | `timeout 10 iftop -t -s 10` |

## Command-Line Flags

- `-t`: Text mode (non-interactive, no ncurses)
- `-s`: Capture for N seconds then exit (one single snapshot)
- `-n`: No hostname resolution (avoids DNS delays)
- `-N`: No port resolution

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive text mode, capture 10 seconds
iftop -t -s 10 -n -N -i eth0 2>/dev/null
```
