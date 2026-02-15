# screen

**Platforms:** Multi-platform  
**Category:** Terminal Multiplexer

## Quick Reference

| Goal | Command |
|------|---------|
| Detached session | `screen -dmS name command` |
| List sessions | `screen -ls` |
| Reattach | `screen -r name` |

## Command-Line Flags

```bash
screen -dmS session_name             # Create detached session
screen -dmS session_name command     # Create detached with command
screen -ls                           # List sessions
screen -r session_name               # Reattach
screen -rD session_name              # Reattach, detach others
screen -S session_name -X quit       # Kill session
screen -S session_name -X stuff "command
"  # Send command
```
- `-d`: Detach
- `-m`: Ignore $STY (force new session)
- `-S`: Session name
- `-r`: Reattach
- `-D`: Power detach (detach + logout)
- `-X`: Execute command
- `-ls`: List sessions

## Recommended Unattended Usage

```bash
#!/bin/bash

# Start detached session
screen -dmS worker ./worker.sh

# Send commands to session
screen -S worker -X stuff "status
"

# Kill session
screen -S worker -X quit
```
