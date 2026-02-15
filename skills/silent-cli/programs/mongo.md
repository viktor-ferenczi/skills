# mongo / mongosh (MongoDB client)

**Platforms:** Multi-platform  
**Category:** Database Client (MongoDB)

## Quick Reference

| Goal | Command |
|------|---------|
| Execute | `mongo --eval 'db.collection.find()'` |
| Script | `mongo script.js` |
| Quiet | `mongo --quiet --eval 'db.stats()'` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `MONGOSH_EDITOR` | `vim` | Default editor for mongosh |

## mongo Command-Line Flags

```bash
mongo --eval "db.stats()"            # Execute JavaScript
mongo script.js                      # Run script file
mongo --quiet script.js              # Quiet mode
mongo --eval "db.collection.find()" 2>/dev/null
mongo --host host:port --eval "db.adminCommand('ping')"
mongo --username user --password pass --eval "db.stats()"
mongo --authenticationDatabase admin --eval "db.stats()"
```

## mongosh Command-Line Flags

```bash
mongosh --eval "db.stats()"
mongosh --quiet --eval "db.stats()"
mongosh --file script.js
mongosh "mongodb://user:pass@host/db" --eval "db.stats()"
mongosh --json --eval "db.stats()"   # JSON output
```
- `--eval`: Execute JavaScript
- `--quiet`: Quiet mode
- `--host`: Host:port
- `--username` / `--password`: Credentials
- `--authenticationDatabase`: Auth database
- `--json`: JSON output (mongosh)
- `--file`: Execute file

## Recommended Unattended Usage

```bash
#!/bin/bash

# Using connection string
mongosh "mongodb://localhost:27017/mydb" --quiet --eval "db.stats()"

# JSON output for parsing
mongosh --quiet --json --eval "JSON.stringify(db.stats())"
```
