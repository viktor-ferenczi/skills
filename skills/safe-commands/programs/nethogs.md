# nethogs

**Platforms:** Linux
**Category:** Network Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Run nethogs | `nethogs` |
| Show help | `nethogs -h` |
| Interface | `nethogs eth0` |
| Text mode | `nethogs -t` |
| Version | `nethogs -V` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `nethogs` with logging | Writes log files |
| Any nethogs with write options | Creates files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe nethogs Inspection Script

# Show version
nethogs -V

# Text mode
nethogs -t

# Monitor interface
nethogs eth0
```
