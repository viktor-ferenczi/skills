# redis-cli

**Platforms:** Multi-platform  
**Category:** Database Client (Redis)

## Quick Reference

| Goal | Command |
|------|---------|
| Raw output | `redis-cli --raw GET key` |
| CSV output | `redis-cli --csv LRANGE list 0 -1` |
| Pipe/batch | `cat commands.txt | redis-cli --pipe` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `REDISCLI_AUTH` | `password` | Authentication password (avoids interactive password prompt) |

## Command-Line Flags

- `--raw`: Raw output (no formatting) — machine-readable
- `--csv`: CSV output — machine-readable
- `--pipe`: Pipeline mode — bulk non-interactive import

## Recommended Unattended Usage

```bash
#!/bin/bash

# Scan and delete keys matching pattern
redis-cli --scan --pattern 'temp:*' | xargs -L1 redis-cli DEL

# Bulk import
cat <<EOF | redis-cli --pipe
SET key1 value1
SET key2 value2
EOF
```
