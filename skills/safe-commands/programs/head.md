# head

**Platforms:** Linux, macOS
**Category:** Text Processing

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| First lines | `head -n 100 file` |
| First bytes | `head -c 1000 file` |
| Multiple files | `head file1 file2` |
| With filename | `head -v file` |
| Quiet mode | `head -q file` |
| All but last | `head -n -10 file` |
| Default (10 lines) | `head file` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `head` piped to destructive commands | May modify/delete data |
| Any head output used for modification | Affects system state |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe head Inspection Script

# First 100 lines
head -n 100 /var/log/syslog

# First 1000 bytes
head -c 1000 /var/log/syslog

# Multiple files
head -n 50 /var/log/syslog /var/log/auth.log

# All but last 10 lines
head -n -10 /var/log/syslog
```
