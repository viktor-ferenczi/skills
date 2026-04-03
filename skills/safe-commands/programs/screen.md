# screen

**Platforms:** Linux, macOS
**Category:** Terminal Multiplexer

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `screen --version` |
| Show help | `screen --help` |
| List sessions | `screen -ls` |
| Show windows | `screen -Q windows` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `screen` | Creates session |
| `screen -S name` | Creates named session |
| `screen -X quit` | Kills session |
| Any screen session creation | Creates processes |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe screen Inspection Script

# List sessions
screen -ls
```
