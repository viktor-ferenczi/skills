# nettop

**Platforms:** macOS
**Category:** Network Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Run nettop | `nettop` |
| List modules | `nettop -m` |
| Show help | `nettop -h` |
| CPU mode | `nettop -c` |
| Network mode | `nettop -n` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `nettop` with logging | Writes log files |
| Any nettop with write options | Creates files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe nettop Inspection Script

# Show help
nettop -h

# List modules
nettop -m

# Network stats
nettop -n -l 5
```
