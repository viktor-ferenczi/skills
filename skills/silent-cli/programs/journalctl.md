# journalctl

**Platforms:** Linux (systemd)  
**Category:** Log Viewer

## Quick Reference

| Goal | Command |
|------|---------|
| No pager | `journalctl --no-pager` |
| JSON output | `journalctl -o json` |
| Quiet | `journalctl -q` |

## Command-Line Flags

- `--no-pager`: Disable pager (critical for non-interactive use)
- `-o`: Output format (`json`, `short`, `verbose`) — use `json` for machine-readable output
- `-q`: Quiet (suppress informational messages)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Export service logs to file (no pager)
journalctl -u myservice --no-pager --since '24 hours ago' > service.log

# Get recent errors only
journalctl -p err --since '1 hour ago' --no-pager

# JSON output for processing
journalctl -u myservice -o json --since today
```
