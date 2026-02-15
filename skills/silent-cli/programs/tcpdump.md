# tcpdump

**Platforms:** Multi-platform  
**Category:** Network Packet Analysis

## Quick Reference

| Goal | Command |
|------|---------|
| Capture | `sudo tcpdump -i eth0` |
| Write file | `sudo tcpdump -w capture.pcap` |
| Read file | `tcpdump -r capture.pcap` |
| Port filter | `sudo tcpdump port 80` |

## Command-Line Flags

```bash
sudo tcpdump -i eth0                 # Capture on interface
sudo tcpdump -i any                  # Any interface
sudo tcpdump -D                      # List interfaces
sudo tcpdump -c 100                  # Capture 100 packets
sudo tcpdump -w capture.pcap         # Write to file
sudo tcpdump -r capture.pcap         # Read from file
sudo tcpdump -A                      # ASCII output
sudo tcpdump -X                      # Hex and ASCII
sudo tcpdump -n                      # No DNS
sudo tcpdump -nn                     # No DNS, no ports
sudo tcpdump -v                      # Verbose
sudo tcpdump -vv                     # More verbose
sudo tcpdump -vvv                    # Most verbose
sudo tcpdump -tttt                   # Human-readable timestamps
sudo tcpdump -e                      # Link-level headers
sudo tcpdump -q                      # Quick/quiet
sudo tcpdump -s 0                    # Full packet capture
sudo tcpdump port 80                 # Filter by port
sudo tcpdump src host 192.168.1.1    # Filter by source
sudo tcpdump dst host 192.168.1.1    # Filter by destination
sudo tcpdump host 192.168.1.1        # Source or destination
sudo tcpdump net 192.168.1.0/24      # Filter by network
sudo tcpdump icmp                    # ICMP only
sudo tcpdump tcp                     # TCP only
sudo tcpdump udp                     # UDP only
sudo tcpdump portrange 1-1024        # Port range
sudo tcpdump 'tcp[13] & 2 != 0'      # TCP SYN packets
sudo tcpdump -l                      # Line buffered
sudo tcpdump -U                      # Unbuffered
sudo tcpdump -C 100 -w capture.pcap  # Rotate at 100MB
sudo tcpdump -W 10 -C 100 -w capture.pcap  # Keep 10 files
```
- `-i`: Interface
- `-D`: List interfaces
- `-c`: Count
- `-w`: Write file
- `-r`: Read file
- `-A`/`-X`: Output format
- `-n`/`-nn`: No DNS
- `-v`/`-vv`/`-vvv`: Verbosity
- `-s`: Snaplen
- `-l`: Line buffered
- `-C`: File size rotate
- `-W`: File count

## Recommended Unattended Usage

```bash
#!/bin/bash

# Capture to file (rotating)
sudo tcpdump -i eth0 -C 100 -W 10 -w /var/capture/capture.pcap -q

# Capture specific traffic quietly
sudo tcpdump -i eth0 port 80 -c 1000 -w http.pcap -q
```
