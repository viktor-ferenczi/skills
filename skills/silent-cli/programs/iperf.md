# iperf / iperf3

**Platforms:** Multi-platform  
**Category:** Network Testing

## Quick Reference

| Goal | Command |
|------|---------|
| JSON output | `iperf3 -c server -J` |
| Daemon mode | `iperf3 -s -D` |

## Command-Line Flags

- `-J`: JSON output (machine-readable)
- `-D`: Daemon mode (server runs in background)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Start server as daemon
iperf3 -s -D

# Run client with JSON output for parsing
iperf3 -c server -t 10 -J > result.json
```
