# fuser

**Platforms:** Linux, macOS  
**Category:** Process Identification

## Quick Reference

| Goal | Command |
|------|---------|
| File users | `fuser /path/to/file` |
| Port | `fuser 80/tcp` |
| Kill | `fuser -k /path/to/file` |
| Mount | `fuser -m /mount/point` |

## Command-Line Flags

```bash
fuser /path/to/file                  # PIDs using file
fuser -v /path/to/file               # Verbose
fuser /path/to/file 2>/dev/null      # Suppress errors
fuser -m /mount/point                # Filesystem users
fuser -c /mount/point                # Same as -m
fuser 80/tcp                         # TCP port 80
fuser 443/tcp                        # TCP port 443
fuser 53/udp                         # UDP port 53
fuser -n tcp 80                      # TCP port 80
fuser -n udp 53                      # UDP port 53
fuser -4 80/tcp                      # IPv4 only
fuser -6 80/tcp                      # IPv6 only
fuser -k /path/to/file               # Kill processes
fuser -ki /path/to/file              # Interactive kill
fuser -k -HUP /path/to/file          # Send HUP signal
fuser -k -9 /path/to/file            # Send KILL signal
fuser -v -m /mount/point             # Verbose mount info
fuser -a /path/to/file               # Show all files
fuser -s /path/to/file               # Silent (exit code only)
```
- `-v`: Verbose
- `-m` or `-c`: Mount point
- `-n`: Name space (tcp, udp, file)
- `-4`/`-6`: IPv4/IPv6
- `-k`: Kill processes
- `-i`: Interactive
- `-s`: Silent
- `-a`: All files
- `-SIGNAL`: Signal to send

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
