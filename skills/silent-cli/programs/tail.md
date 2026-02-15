# tail

**Platforms:** Multi-platform  
**Category:** Text Processing

## Quick Reference

| Goal | Command |
|------|---------|
| Last 10 lines | `tail file` |
| Last N lines | `tail -n 20 file` |
| Follow | `tail -f file` |
| From line N | `tail -n +100 file` |

## Command-Line Flags

```bash
tail file                            # Last 10 lines
tail -n 5 file                       # Last 5 lines
tail -5 file                         # Last 5 lines (legacy)
tail -n +100 file                    # From line 100 to end
tail -c 100 file                     # Last 100 bytes
tail -c 1k file                      # Last 1KB
tail -f file                         # Follow (like tail -f)
tail -F file                         # Follow, retry if file changes
tail -f file1 file2                  # Follow multiple
tail -q file1 file2                  # No headers
tail -v file                         # Always show header
tail -s 5 -f file                    # Check every 5 seconds
tail -n 5 --pid=1234 -f file         # Stop when PID 1234 dies
tail -z file                         # Null-terminated lines
tail --max-unchanged-stats=5 -f file # Check rotation
```
- `-n`: Number of lines
- `-c`: Number of bytes
- `-f`: Follow (monitor)
- `-F`: Follow with retry
- `-q` or `--quiet`: No headers
- `-v` or `--verbose`: Always show filename
- `-s`: Sleep interval (follow)
- `--pid`: Stop when PID dies
- `-z`: Null-terminated

## Recommended Unattended Usage

```bash
#!/bin/bash

# Monitor log and extract errors
tail -f /var/log/app.log | grep ERROR

# Get last N lines without filename header
tail -q -n 100 file.txt
```
