# salt / salt-call / salt-ssh

**Platforms:** Multi-platform  
**Category:** Configuration Management

## Quick Reference

| Goal | Command |
|------|---------|
| Test ping | `salt '*' test.ping --out txt` |
| JSON output | `salt '*' grains.items --out json` |
| Quiet | `salt '*' state.apply --out quiet` |

## Command-Line Flags

```bash
salt '*' test.ping                   # Test connectivity
salt '*' test.ping --out json        # JSON output
salt '*' test.ping --out txt         # Text output
salt '*' grains.items                # Get grains
salt '*' state.apply                 # Apply states
salt '*' state.apply webserver       # Apply specific state
salt '*' state.highstate             # Apply highstate
salt-run jobs.list_jobs              # List jobs
salt-key -L                          # List keys
salt-key -A                          # Accept all keys
salt-call test.ping                  # Local execution
salt-ssh '*' test.ping               # SSH execution
```
- `--out` or `--output`: Output format (json, yaml, txt, quiet, etc.)
- `--static`: Return data all at once
- `--async`: Run asynchronously
- `--batch`: Batch size

## Recommended Unattended Usage

```bash
#!/bin/bash

# JSON output for parsing
salt '*' grains.get os --out json

# Quiet state apply
salt '*' state.apply --out quiet
```
