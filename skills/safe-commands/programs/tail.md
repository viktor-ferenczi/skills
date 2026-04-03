# tail

**Platforms:** Linux, macOS
**Category:** Text Processing

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Last lines | `tail -n 100 file` |
| Follow log | `tail -f file` |
| Follow +name | `tail -F file` |
| First N bytes | `tail -c 1000 file` |
| Multiple files | `tail file1 file2` |
| With filename | `tail -v file` |
| Quiet mode | `tail -q file` |
| Line numbers | `tail -n +100 file` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `tail` piped to destructive commands | May modify/delete data |
| `tail -f` in scripts without timeout | May hang indefinitely |
| Any tail output used for modification | Affects system state |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe tail Inspection Script

# Last 100 lines
tail -n 100 /var/log/syslog

# Follow log (with timeout)
timeout 30 tail -f /var/log/syslog

# Last 1000 bytes
tail -c 1000 /var/log/syslog

# Multiple files
tail -n 50 /var/log/syslog /var/log/auth.log
```
