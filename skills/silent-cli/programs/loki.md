# logcli (Loki CLI)

**Platforms:** Multi-platform  
**Category:** Log Aggregation

## Quick Reference

| Goal | Command |
|------|---------|
| Machine-readable output | `logcli query --output=jsonl '{job="myjob"}'` |

## Command-Line Flags

- `--output`: Output format (`default`, `jsonl`) — use `jsonl` for machine-readable output
- `--quiet`: Suppress query metadata, print only log lines

## Recommended Unattended Usage

```bash
#!/bin/bash

# Query logs with JSON lines output for processing
logcli query --output=jsonl --since=1h '{job="app"}'

# Quiet output for piping
logcli query --quiet '{job="app"}' > logs.txt
```
