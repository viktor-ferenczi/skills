# iperf3

**Platforms:** Multi-platform
**Category:** Network Testing

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `iperf3 --version` |
| Show help | `iperf3 --help` |
| Client test | `iperf3 -c server` |
| UDP test | `iperf3 -c server -u` |
| Reverse test | `iperf3 -c server -R` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `iperf3 -s` | Runs server mode |
| High bandwidth tests | May saturate network |
| Long duration tests | May impact network |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe iperf3 Inspection Script

# Show version
iperf3 --version

# Quick client test
iperf3 -c server.example.com -t 5
```
