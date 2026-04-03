# tshark (Wireshark CLI)

**Platforms:** Multi-platform
**Category:** Network Analysis

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `tshark --version` |
| Show help | `tshark --help` |
| List interfaces | `tshark -D` |
| Read pcap | `tshark -r file.pcap` |
| Capture limited | `tshark -c 10` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `tshark -w file` | Writes capture files |
| Long captures | May fill disk |
| Any tshark with -w | Creates files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe tshark Inspection Script

# List interfaces
tshark -D

# Read existing pcap
tshark -r capture.pcap | head -20
```
