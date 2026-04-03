# redis-cli

**Platforms:** Multi-platform
**Category:** Database

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Connect | `redis-cli` |
| List keys | `redis-cli KEYS "pattern"` |
| Get value | `redis-cli GET key` |
| Get type | `redis-cli TYPE key` |
| Get length | `redis-cli STRLEN key` |
| List info | `redis-cli INFO` |
| Check memory | `redis-cli MEMORY USAGE key` |
| Scan keys | `redis-cli SCAN 0` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `SET` | Sets/overwrites value |
| `DELETE` | Deletes keys |
| `FLUSHALL` | Clears all data |
| `FLUSHDB` | Clears database |
| `EXPIRE` | Sets expiration |
| `CONFIG SET` | Changes config |
| `ACL SETUSER` | Changes access control |
| `SHUTDOWN` | Stops server |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe redis-cli Inspection Script

# List keys
redis-cli KEYS "*" | head -20

# Get value
redis-cli GET mykey

# Get type
redis-cli TYPE mykey

# Server info
redis-cli INFO | head -50

# Memory usage
redis-cli MEMORY USAGE mykey
```
