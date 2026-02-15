# lsof (list open files)

**Platforms:** Linux, macOS  
**Category:** File/Process Inspection

## Quick Reference

| Goal | Command |
|------|---------|
| File users | `lsof /path/to/file` |
| Port | `lsof -i :80` |
| Process | `lsof -p 1234` |
| User | `lsof -u username` |
| Network | `lsof -i` |

## Command-Line Flags

```bash
lsof                                 # All open files
lsof /path/to/file                   # Processes using file
lsof +D /path/to/dir                 # Files in directory
lsof -p 1234                         # Files for PID
lsof -p 1234,5678                    # Multiple PIDs
lsof -u username                     # Files for user
lsof -u ^root                        # Exclude root
lsof -i                              # All network files
lsof -i TCP                          # TCP only
lsof -i UDP                          # UDP only
lsof -i :80                          # Port 80
lsof -i TCP:80                       # TCP port 80
lsof -i @192.168.1.1                # IP address
lsof -i @192.168.1.1:22             # IP:port
lsof -a -u username -i               # AND conditions
lsof -c nginx                        # Command starts with
lsof -c ^nginx                       # Exclude command
lsof -n                              # No DNS lookup
lsof -P                              # No port names
lsof -t                              # Terse (PIDs only)
lsof -t -i :80                       # PIDs using port 80
lsof +L1                             # Open but unlinked files
lsof -N                              # NFS files
lsof -d 0-2                          # File descriptors 0,1,2
lsof -d cwd                          # Current working dir
lsof -d txt                          # Program text
lsof -d mem                          # Memory mapped files
lsof -r 5                            # Repeat every 5 sec
lsof -F pcn                          # Parsable output
```
- `-a`: AND conditions
- `-p`: Process ID
- `-u`: User
- `-c`: Command
- `-i`: Network selection
- `-n`: No DNS
- `-P`: No port names
- `-t`: Terse output
- `-r`: Repeat mode
- `-F`: Field output

## Recommended Unattended Usage

```bash
#!/bin/bash

# Find process using port 80
lsof -t -i :80

# Kill processes using port
kill $(lsof -t -i :8080)

# Find deleted but open files
lsof +L1
```
