# tmux

**Platforms:** Multi-platform  
**Category:** Terminal Multiplexer

## Quick Reference

| Goal | Command |
|------|---------|
| Detached session | `tmux new -d -s name` |
| Run command detached | `tmux new -d -s name 'command'` |

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
