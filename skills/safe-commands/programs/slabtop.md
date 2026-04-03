# slabtop

**Platforms:** Linux
**Category:** System Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Run slabtop | `slabtop` |
| Show help | `slabtop --help` |
| Show version | `slabtop --version` |
| Once mode | `slabtop -o` |
| Sort by size | `slabtop -s c` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `slabtop` is read-only | Generally safe |
| Any slabtop execution | Read-only monitoring |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe slabtop Inspection Script

# Show once
slabtop -o

# Sort by cache size
slabtop -o -s c
```
