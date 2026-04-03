# netstat

**Platforms:** Multi-platform
**Category:** Network Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| All connections | `netstat -a` |
| TCP connections | `netstat -t` |
| UDP connections | `netstat -u` |
| Listening ports | `netstat -l` |
| Numeric output | `netstat -n` |
| Process info | `netstat -p` |
| Statistics | `netstat -s` |
| Interface info | `netstat -i` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `netstat` piped to kill | Terminates processes |
| `netstat` used for config changes | May modify network |
| Any netstat output for modification | Affects system state |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe netstat Inspection Script

# All connections
netstat -an | head -30

# Listening ports
netstat -tuln

# TCP connections
netstat -tn

# Statistics
netstat -s | head -50

# Interface info
netstat -i
```
