# tmux

**Platforms:** Linux, macOS
**Category:** Terminal Multiplexer

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `tmux -V` |
| Show help | `tmux -h` |
| List sessions | `tmux ls` |
| List windows | `tmux list-windows` |
| List panes | `tmux list-panes` |
| Show messages | `tmux display-message` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `tmux new` | Creates sessions |
| `tmux kill-session` | Kills sessions |
| `tmux send-keys` | Sends input |
| `tmux split-window` | Creates panes |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe tmux Inspection Script

# List sessions
tmux ls

# List windows
tmux list-windows
```
