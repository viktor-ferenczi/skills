# powertop

**Platforms:** Linux
**Category:** System Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Run powertop | `powertop` |
| Show help | `powertop --help` |
| Show version | `powertop --version` |
| HTML report | `powertop --html=file` |
| Calibration | `powertop --calibrate` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `powertop --auto-tune` | Tunes system settings |
| `powertop --html` | Writes files |
| Any powertop with write options | Modifies system |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe powertop Inspection Script

# Show version
powertop --version

# Run in read-only mode
powertop
```
