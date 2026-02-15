# fuser

**Platforms:** Linux, macOS  
**Category:** Process Identification

## Quick Reference

| Goal | Command |
|------|---------|
| Silent check (exit code only) | `fuser -s /path/to/file` |
| Force kill (no prompt) | `fuser -k 8080/tcp 2>/dev/null` |

## Command-Line Flags

- `-s`: Silent mode (no output, exit code only — 0 if file is in use)
- `-k`: Kill processes using the file/port (non-interactive, no confirmation prompt)

**Warning:** `-ki` (interactive kill) will prompt for confirmation — avoid in scripts. Use `-k` alone for unattended operation.

## Recommended Unattended Usage

```bash
#!/bin/bash

# Kill processes using port 8080
fuser -k 8080/tcp 2>/dev/null

# Check if file is in use
if fuser -s /var/lock/mylock; then
    echo "File in use"
else
    echo "File not in use"
fi
```
