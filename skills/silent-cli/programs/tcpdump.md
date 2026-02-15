# tcpdump

**Platforms:** Multi-platform  
**Category:** Network Packet Analysis

## Command-Line Flags

- `-q`: Quick/quiet output
- `-w`: Write to file (no terminal output)
- `-l`: Line buffered (for piping)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Capture to file (rotating)
sudo tcpdump -i eth0 -C 100 -W 10 -w /var/capture/capture.pcap -q

# Capture specific traffic quietly
sudo tcpdump -i eth0 port 80 -c 1000 -w http.pcap -q
```
