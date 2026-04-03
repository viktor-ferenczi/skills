# mongo (MongoDB Shell)

**Platforms:** Multi-platform
**Category:** Database

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `mongosh --version` |
| Show help | `mongosh --help` |
| List DBs | `mongosh --eval "show dbs"` |
| List collections | `mongosh --eval "show collections"` |
| Find docs | `mongosh --eval "db.collection.find().limit(10)"` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `db.collection.insert()` | Inserts documents |
| `db.collection.update()` | Updates documents |
| `db.collection.delete()` | Deletes documents |
| `db.collection.drop()` | Drops collection |
| `db.dropDatabase()` | Drops database |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe mongo Inspection Script

# List databases
mongosh --eval "show dbs"

# List collections
mongosh --eval "use mydb; show collections"

# Find limited docs
mongosh --eval "db.collection.find().limit(10).toArray()"
```
