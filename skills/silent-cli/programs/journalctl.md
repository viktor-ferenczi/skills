# journalctl

**Platforms:** Linux (systemd)  
**Category:** Log Viewer

## Quick Reference

| Goal | Command |
|------|---------|
| All logs | `journalctl` |
| Service | `journalctl -u service` |
| Follow | `journalctl -f` |
| Since | `journalctl --since '1 hour ago'` |

## Command-Line Flags

```bash
journalctl                           # All logs
journalctl -n 100                    # Last 100 lines
journalctl -f                        # Follow
journalctl -u nginx                  # Service logs
journalctl -u nginx -f               # Service logs, follow
journalctl --since '1 hour ago'      # Since time
journalctl --since '2024-01-01 00:00:00'
journalctl --until '1 hour ago'      # Until time
journalctl --since today --until '2 hours ago'
journalctl -p err                    # Priority (emerg, alert, crit, err, warning, notice, info, debug)
journalctl -k                        # Kernel logs only
journalctl -b                        # Current boot
journalctl -b -1                     # Previous boot
journalctl --list-boots              # List boots
journalctl --disk-usage              # Disk usage
journalctl --vacuum-time=30d         # Retain 30 days
journalctl --vacuum-size=1G          # Retain 1GB
journalctl -o json                   # JSON output
journalctl -o short                  # Short output
journalctl -o verbose                # Verbose output
journalctl --no-pager                # No pager
journalctl --identifier=myapp        # By syslog identifier
journalctl _PID=1234                 # By PID
journalctl _UID=1000                 # By UID
journalctl /usr/bin/nginx            # By executable path
journalctl -r                        # Reverse (newest first)
journalctl -q                        # Quiet (no info messages)
```
- `-n`: Number of lines
- `-f`: Follow
- `-u`: Unit/service
- `--since`/`--until`: Time range
- `-p`: Priority
- `-k`: Kernel only
- `-b`: Boot
- `-o`: Output format
- `--no-pager`: No pager
- `--identifier`: Syslog identifier
- `_PID`/`_UID`: Match fields
- `-r`: Reverse
- `-q`: Quiet

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
