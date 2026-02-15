# nohup

**Platforms:** Multi-platform  
**Category:** Process Control

## Quick Reference

| Goal | Command |
|------|---------|
| Run detached | `nohup command &` |
| Output to file | `nohup command > output.log 2>&1 &` |

## Command-Line Flags

```bash
nohup command                        # Ignore HUP signal
nohup command &                      # Run in background
nohup command > output.log 2>&1 &    # Redirect output, background
```

## Output Redirection

By default, nohup redirects:
- stdout to `nohup.out` (or `$HOME/nohup.out`)
- stderr to same as stdout

## Recommended Unattended Usage

```bash
#!/bin/bash

# Run long task detached
nohup ./long-running-script.sh > /var/log/script.log 2>&1 &
pid=$!
echo "Started with PID: $pid"

# Alternative with setsid
setsid ./script.sh < /dev/null > /var/log/script.log 2>&1 &
```
