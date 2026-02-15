# tshark

**Platforms:** Multi-platform  
**Category:** Network Packet Analysis

## Command-Line Flags

- `-q`: Quiet (suppress packet output during capture)
- `-Q`: Super quiet (suppress even summary)
- `-T fields`: Machine-readable field output
- `-T json`: JSON output
- `-T ek`: Elasticsearch output
- `-l`: Line buffered (for piping)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Capture with ring buffer
sudo tshark -i eth0 -b filesize:100000 -b files:10 -w /var/capture/trace.pcap -q

# Extract specific fields from capture
tshark -r capture.pcap -T fields -e ip.src -e ip.dst -e http.host -Y http.request -E header=y
```
