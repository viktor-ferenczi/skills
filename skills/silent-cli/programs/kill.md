# kill / killall / pkill

**Platforms:** Multi-platform  
**Category:** Process Control

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet killall | `killall -q processname` |
| Check if exists | `kill -0 <pid>` |

## Command-Line Flags

### kill
- `-0`: Check if process exists (exit code only, no signal sent — useful for scripts)

### killall
- `-q`: Quiet (don't complain if no processes found)
- `-w`: Wait for termination to complete

## Recommended Unattended Usage

```bash
#!/bin/bash

# Quietly kill process, no error if not found
killall -q processname

# Check if process exists before acting
kill -0 "$PID" 2>/dev/null && echo "running" || echo "not running"
```
