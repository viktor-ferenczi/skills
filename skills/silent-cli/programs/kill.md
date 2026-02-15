# kill / killall / pkill

**Platforms:** Multi-platform  
**Category:** Process Control

## Quick Reference

| Goal | Command |
|------|---------|
| Kill by PID | `kill -TERM <pid>` |
| Kill by name | `killall processname` |
| Pattern kill | `pkill pattern` |

## Command-Line Flags

### kill
```bash
kill -TERM <pid>                        # Graceful kill
kill -KILL <pid>                        # Force kill
kill -0 <pid>                           # Check if exists (exit code)
```
- `-TERM` or `-15`: Terminate
- `-KILL` or `-9`: Kill
- `-HUP` or `-1`: Hang up
- `-0`: Check process exists

### killall
```bash
killall -q processname                  # Quiet
killall -w processname                  # Wait for termination
```
- `-q`: Quiet
- `-w`: Wait

### pkill
```bash
pkill -f pattern                        # Match full command line
pkill -x exactname                      # Exact match
pkill -u username                       # User's processes
```
- `-f`: Full command line
- `-x`: Exact match
- `-u`: User
