# netstat

**Platforms:** Linux, macOS, Windows  
**Category:** Network Statistics

## Quick Reference

| Goal | Command |
|------|---------|
| All connections | `netstat -a` |
| Listening | `netstat -l` |
| TCP only | `netstat -t` |
| With PID | `netstat -p` |
| Statistics | `netstat -s` |

## Command-Line Flags

```bash
netstat -a                           # All connections
netstat -l                           # Listening sockets
netstat -t                           # TCP only
netstat -u                           # UDP only
netstat -n                           # Numeric (no DNS)
netstat -p                           # Show PID/program
netstat -e                           # Extended info
netstat -s                           # Statistics
netstat -r                           # Routing table
netstat -i                           # Interface statistics
netstat -c                           # Continuous output
netstat -an                          # All numeric
netstat -tlnp                        # TCP listening with PID
netstat -tlnpe                       # TCP listening + PID + extended
netstat -tp                          # TCP with PID
netstat -nlp                         # Listening with PID
netstat -plant                       # Common combo
netstat -s --tcp                     # TCP statistics
netstat -s --udp                     # UDP statistics
netstat -g                           # Multicast groups
netstat -M                           # Masqueraded connections
```
- `-a`: All sockets
- `-l`: Listening
- `-t`: TCP
- `-u`: UDP
- `-n`: Numeric
- `-p`: PID/program
- `-e`: Extended
- `-s`: Statistics
- `-r`: Routing
- `-i`: Interfaces
- `-c`: Continuous
- `-g`: Multicast

## Recommended Unattended Usage

```bash
#!/bin/bash

# Check if port 80 is listening
netstat -tlnp | grep ':80 '

# Get connection count per state
netstat -ant | awk '{print $6}' | sort | uniq -c | sort -n
```
