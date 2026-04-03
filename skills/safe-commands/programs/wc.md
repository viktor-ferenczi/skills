# wc

**Platforms:** Linux, macOS
**Category:** Text Processing

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Line count | `wc -l file` |
| Word count | `wc -w file` |
| Byte count | `wc -c file` |
| Char count | `wc -m file` |
| Max line length | `wc -L file` |
| All counts | `wc file` |
| Multiple files | `wc file1 file2` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `wc` piped to destructive commands | May modify/delete data |
| Any wc output used for modification | Affects system state |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe wc Inspection Script

# Line count
wc -l /var/log/syslog

# Word count
wc -w /var/log/syslog

# Byte count
wc -c /var/log/syslog

# All counts
wc /var/log/syslog

# Multiple files
wc -l /var/log/*.log
```
