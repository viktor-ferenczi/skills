# ss (socket statistics)

**Platforms:** Linux  
**Category:** Network Statistics

## Quick Reference

| Goal | Command |
|------|---------|
| All | `ss -a` |
| Listening | `ss -l` |
| TCP | `ss -t` |
| Process | `ss -p` |
| Summary | `ss -s` |

## Command-Line Flags

```bash
ss                                   # Established connections
ss -a                                # All sockets
ss -l                                # Listening
ss -t                                # TCP
ss -u                                # UDP
ss -x                                # Unix sockets
ss -w                                # Raw sockets
ss -n                                # Numeric
ss -p                                # Show processes
ss -s                                # Summary statistics
ss -e                                # Extended info
ss -m                                # Memory info
ss -i                                # TCP internal info
ss -o                                # Timers
ss -r                                # Resolve names
ss -4                                # IPv4 only
ss -6                                # IPv6 only
ss -tlnp                             # TCP listening + process
ss -tlnpe                            # + extended info
ss -tan                              # All TCP numeric
ss -tan state established            # Filter by state
ss -tan state time-wait
ss -tan '( dport = :http or sport = :http )'
ss -tan '( dport = :ssh or dport = :22 )'
ss -o state established '( dport = :ssh or sport = :ssh )'
ss -mtp                              # TCP with memory + process
ss -i -K state established           # Show and reset TCP info
```
- `-a`: All sockets
- `-l`: Listening
- `-t`/`-u`/`-x`/`-w`: Protocol filter
- `-n`: Numeric
- `-p`: Show processes
- `-s`: Summary
- `-e`: Extended
- `-m`: Memory
- `-i`: Internal info
- `-o`: Timers
- `-4`/`-6`: IP version
- `state`: Filter by TCP state

## Recommended Unattended Usage

```bash
#!/bin/bash

# Fast check for listening ports (faster than netstat)
ss -tlnp

# Find high connection count to a port
ss -tan '( dport = :80 )' | wc -l
```
