# tcpdump

**Platforms:** Linux, macOS
**Category:** Network Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Capture packets | `tcpdump -i eth0` |
| Show help | `tcpdump --help` |
| Show version | `tcpdump --version` |
| Count packets | `tcpdump -c 10` |
| Read pcap | `tcpdump -r file.pcap` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `tcpdump -w file` | Writes capture files |
| Long captures | May fill disk |
| Any tcpdump with -w | Creates files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe tcpdump Inspection Script

# Capture limited packets (display only)
tcpdump -i eth0 -c 10

# Read existing pcap
tcpdump -r capture.pcap | head -20
```
