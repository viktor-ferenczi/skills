# mongo / mongosh (MongoDB client)

**Platforms:** Multi-platform  
**Category:** Database Client (MongoDB)

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet | `mongo --quiet --eval 'db.stats()'` |
| JSON output | `mongosh --json --eval 'db.stats()'` |

## mongo Command-Line Flags

```bash
mongo --eval "db.stats()"            # Execute JavaScript (non-interactive)
mongo script.js                      # Run script file (non-interactive)
mongo --quiet script.js              # Quiet mode
mongo --eval "db.collection.find()" 2>/dev/null
```

## mongosh Command-Line Flags

```bash
mongosh --quiet --eval "db.stats()"  # Quiet mode
mongosh --file script.js             # Run script file (non-interactive)
mongosh --json --eval "db.stats()"   # JSON output (machine-readable)
```
- `--eval`: Execute JavaScript (non-interactive)
- `--quiet`: Quiet mode
- `--json`: JSON output (mongosh)
- `--file`: Execute file (non-interactive)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Using connection string
mongosh "mongodb://localhost:27017/mydb" --quiet --eval "db.stats()"

# JSON output for parsing
mongosh --quiet --json --eval "JSON.stringify(db.stats())"
```
