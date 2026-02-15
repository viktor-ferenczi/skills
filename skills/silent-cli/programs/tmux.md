# tmux

**Platforms:** Multi-platform  
**Category:** Terminal Multiplexer

## Quick Reference

| Goal | Command |
|------|---------|
| Detached session | `tmux new -d -s name` |
| Run command | `tmux new -d -s name 'command'` |
| List sessions | `tmux ls` |

## Command-Line Flags

```bash
tmux new -d -s session_name          # Create detached
tmux new -d -s session_name 'cmd'    # Create detached with command
tmux ls                              # List sessions
tmux attach -t session_name          # Attach
tmux kill-session -t session_name    # Kill session
tmux send-keys -t session_name 'cmd' Enter
```

## tmux Commands

```bash
tmux new-session -d -s name          # New detached session
tmux new-window -t name -n win       # New window
tmux split-window -t name            # Split window
tmux send-keys -t name:0 'cmd' C-m   # Send command
tmux capture-pane -t name -p         # Capture output
tmux show-messages -t name           # Show messages
```

## Recommended Unattended Usage

```bash
#!/bin/bash

# Start detached session
tmux new -d -s worker

# Run command in session
tmux send-keys -t worker './script.sh' Enter

# Get output
tmux capture-pane -t worker -p

# Kill session
tmux kill-session -t worker
```
