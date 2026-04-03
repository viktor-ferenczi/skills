# grep

**Platforms:** Linux, macOS, Windows (with grep)
**Category:** Text Processing

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Search for pattern | `grep "pattern" file` |
| Case insensitive | `grep -i "pattern" file` |
| Invert match | `grep -v "pattern" file` |
| Line numbers | `grep -n "pattern" file` |
| Count matches | `grep -c "pattern" file` |
| Recursive search | `grep -r "pattern" dir` |
| Only matching | `grep -o "pattern" file` |
| Context lines | `grep -C 3 "pattern" file` |
| Files with match | `grep -l "pattern" dir/*` |
| Files without match | `grep -L "pattern" dir/*` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `grep ... | xargs rm` | Deletes matched files |
| `grep ... | xargs chmod` | Changes permissions |
| Any grep piped to write operations | May modify data |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe grep Inspection Script

# Search log files for errors
grep -i "error" /var/log/*.log

# Find configuration patterns
grep -r "password\|secret\|key" /etc/ 2>/dev/null

# Count occurrences
grep -c "FAILED" /var/log/auth.log

# Show context around matches
grep -B2 -A2 "critical" application.log

# Extract specific patterns
grep -oE "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" access.log
```
