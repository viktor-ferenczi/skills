# top

**Platforms:** Linux, macOS
**Category:** System Monitoring

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Run top | `top` |
| Batch mode | `top -b` |
| Iterations | `top -b -n 1` |
| By user | `top -u username` |
| Delay | `top -d 5` |
| PID focus | `top -p PID` |
| Sort by mem | `top -o %MEM` |
| Sort by cpu | `top -o %CPU` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `top` interactive 'k' command | Kills processes |
| `top` interactive 'd' command | Changes delay (minor) |
| `top` piped to kill operations | Terminates processes |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe top Inspection Script

# Single iteration batch mode
top -b -n 1 | head -30

# By user
top -b -n 1 -u $(whoami)

# CPU sorted
top -b -n 1 -o %CPU | head -20

# Memory sorted
top -b -n 1 -o %MEM | head -20
```
