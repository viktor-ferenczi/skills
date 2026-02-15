# screen

**Platforms:** Multi-platform  
**Category:** Terminal Multiplexer

## Quick Reference

| Goal | Command |
|------|---------|
| Detached session | `screen -dmS name command` |
| Send command to session | `screen -S name -X stuff "command\n"` |
| Kill session | `screen -S name -X quit` |

## Command-Line Flags

- `-d`: Detach session
- `-m`: Force new session (ignore $STY)
- `-S`: Session name
- `-X`: Execute command in session (non-interactive control)

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
