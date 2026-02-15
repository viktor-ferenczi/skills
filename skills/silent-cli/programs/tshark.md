# tshark

**Platforms:** Multi-platform  
**Category:** Network Packet Analysis

## Quick Reference

| Goal | Command |
|------|---------|
| Capture | `sudo tshark -i eth0` |
| Write | `sudo tshark -w capture.pcap` |
| Read | `tshark -r capture.pcap` |
| Fields | `tshark -T fields -e ip.src` |

## Command-Line Flags

```bash
sudo tshark -i eth0                  # Capture
sudo tshark -i any                   # Any interface
sudo tshark -D                       # List interfaces
sudo tshark -c 100                   # Capture count
sudo tshark -w capture.pcap          # Write to file
sudo tshark -r capture.pcap          # Read file
sudo tshark -r capture.pcap -V       # Verbose decode
sudo tshark -f "port 80"             # Capture filter
sudo tshark -Y "http.request"        # Display filter
sudo tshark -T fields -e ip.src -e ip.dst -e http.host
sudo tshark -T json                  # JSON output
sudo tshark -T ek                    # Elastic output
tshark -G fields                     # List fields
tshark -G protocols                  # List protocols
sudo tshark -q                       # Quiet
sudo tshark -Q                       # Super quiet
sudo tshark -l                       # Line buffered
sudo tshark -n                       # No DNS
sudo tshark -N n                     # No DNS (specific)
sudo tshark -t a                     # Absolute time
sudo tshark -t r                     # Relative time
sudo tshark -x                       # Hex dump
sudo tshark -X lua_script:script.lua # Lua script
sudo tshark -b filesize:10000 -b files:5 -w capture.pcap  # Ring buffer
```
- `-i`: Interface
- `-D`: List interfaces
- `-c`: Packet count
- `-w`: Write file
- `-r`: Read file
- `-f`: Capture filter
- `-Y`: Display filter
- `-T`: Output format
- `-e`: Field to print
- `-G`: List fields/protocols
- `-q`/`-Q`: Quiet
- `-n`: No DNS
- `-t`: Time format
- `-b`: Ring buffer

## Recommended Unattended Usage

```bash
#!/bin/bash

# Capture with ring buffer
sudo tshark -i eth0 -b filesize:100000 -b files:10 -w /var/capture/trace.pcap -q

# Extract specific fields from capture
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e http.host -Y http.request -E header=y
```
