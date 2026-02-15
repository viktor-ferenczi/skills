# redis-cli

**Platforms:** Multi-platform  
**Category:** Database Client (Redis)

## Quick Reference

| Goal | Command |
|------|---------|
| Execute | `redis-cli GET key` |
| Batch | `redis-cli --raw KEYS '*'` |
| Pipe | `cat commands.txt | redis-cli` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `REDISCLI_AUTH` | `password` | Authentication password |

## Command-Line Flags

```bash
redis-cli GET key                    # Execute command
redis-cli --raw GET key              # Raw output
redis-cli --csv LRANGE list 0 -1     # CSV output
redis-cli --eval script.lua 0        # Run Lua script
redis-cli --pipe < commands.txt      # Pipeline
redis-cli -h host -p 6380 GET key    # Custom host/port
redis-cli -a password GET key        # With password
redis-cli -n 1 GET key               # Select database 1
redis-cli --scan --pattern '*'       # Scan keys
redis-cli --bigkeys                  # Find big keys
redis-cli --latency                  # Latency test
```
- `-h` or `--host`: Host
- `-p` or `--port`: Port
- `-a` or `--pass`: Password
- `-n`: Database number
- `-r`: Repeat command
- `-i`: Interval between repeats
- `--raw`: Raw output
- `--csv`: CSV output
- `--eval`: Run Lua script
- `--pipe`: Pipeline mode
- `--scan`: Scan keys
- `--bigkeys`: Find big keys
- `--latency`: Latency test

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
