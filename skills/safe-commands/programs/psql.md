# psql (PostgreSQL)

**Platforms:** Multi-platform
**Category:** Database

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Connect read-only | `psql -U readonly` |
| List databases | `psql -l` |
| List tables | `psql -c "\dt"` |
| Describe table | `psql -c "\d table_name"` |
| Select data | `psql -c "SELECT * FROM table LIMIT 10;"` |
| Show indexes | `psql -c "\di"` |
| Show users | `psql -c "\du"` |
| Show config | `psql -c "SHOW ALL;"` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `INSERT` | Adds data to database |
| `UPDATE` | Modifies existing data |
| `DELETE` | Removes data from database |
| `CREATE` | Creates new tables/databases |
| `DROP` | Deletes tables/databases |
| `ALTER` | Modifies table structure |
| `GRANT` | Changes permissions |
| `REVOKE` | Removes permissions |

## Environment Variables for Safe Operation

| Variable | Description |
|----------|-------------|
| `PGUSER` | Read-only user name |
| `PGPASSWORD` | Read-only password |
| `PGHOST` | Database host |
| `PGDATABASE` | Default database |
| `PGOPTIONS` | Additional options |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe psql Inspection Script

# List databases
psql -U readonly -l

# List tables
psql -U readonly -d mydb -c "\dt"

# Describe table
psql -U readonly -d mydb -c "\d users"

# Select data (limited)
psql -U readonly -d mydb -c "SELECT * FROM users LIMIT 10;"

# Show indexes
psql -U readonly -d mydb -c "\di"
```
