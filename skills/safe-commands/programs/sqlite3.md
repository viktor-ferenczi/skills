# sqlite3

**Platforms:** Multi-platform
**Category:** Database

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Open database | `sqlite3 file.db` |
| List tables | `sqlite3 file.db "SELECT name FROM sqlite_master WHERE type='table';"` |
| Describe table | `sqlite3 file.db "PRAGMA table_info(table_name);"` |
| Select data | `sqlite3 file.db "SELECT * FROM table LIMIT 10;"` |
| Show indexes | `sqlite3 file.db "PRAGMA index_list(table_name);"` |
| Check integrity | `sqlite3 file.db "PRAGMA integrity_check;"` |
| Show schema | `sqlite3 file.db "SELECT sql FROM sqlite_master;"` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `INSERT` | Adds data to database |
| `UPDATE` | Modifies existing data |
| `DELETE` | Removes data from database |
| `CREATE TABLE` | Creates new tables |
| `DROP TABLE` | Deletes tables |
| `ALTER TABLE` | Modifies table structure |
| `VACUUM` | Rebuilds database |
| `PRAGMA writable_schema` | Enables schema writes |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe sqlite3 Inspection Script

# List tables
sqlite3 database.db "SELECT name FROM sqlite_master WHERE type='table';"

# Describe table
sqlite3 database.db "PRAGMA table_info(users);"

# Select data (limited)
sqlite3 database.db "SELECT * FROM users LIMIT 10;"

# Check integrity
sqlite3 database.db "PRAGMA integrity_check;"

# Show schema
sqlite3 database.db "SELECT sql FROM sqlite_master WHERE type='table';"
```
