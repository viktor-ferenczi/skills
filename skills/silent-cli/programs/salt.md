# salt / salt-call / salt-ssh

**Platforms:** Multi-platform  
**Category:** Configuration Management

## Quick Reference

| Goal | Command |
|------|---------|
| JSON output | `salt '*' grains.items --out json` |
| Quiet apply | `salt '*' state.apply --out quiet` |
| Text output | `salt '*' test.ping --out txt` |

## Command-Line Flags

- `--out` or `--output`: Output format (json, yaml, txt, quiet) — `quiet` suppresses output, `json` for machine-readable
- `--static`: Return data all at once (no streaming) — better for scripted parsing

## Recommended Unattended Usage

```bash
#!/bin/bash

# JSON output for parsing
salt '*' grains.get os --out json

# Quiet state apply
salt '*' state.apply --out quiet
```
