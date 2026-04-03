# mysql

**Platforms:** Multi-platform
**Category:** Database

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Connect read-only | `mysql -u readonly -p` |
| List databases | `mysql -e "SHOW DATABASES;"` |
| List tables | `mysql -e "SHOW TABLES;"` |
| Describe table | `mysql -e "DESCRIBE table_name;"` |
| Select data | `mysql -e "SELECT * FROM table LIMIT 10;"` |
| Show status | `mysql -e "SHOW STATUS;"` |
| Show variables | `mysql -e "SHOW VARIABLES;"` |
| Show grants | `mysql -e "SHOW GRANTS;"` |

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
| `MYSQL_USER` | Read-only user name |
| `MYSQL_PASSWORD` | Read-only password |
| `MYSQL_HOST` | Database host |
| `MYSQL_DATABASE` | Default database |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe mysql Inspection Script

# List databases
mysql -u readonly -p -e "SHOW DATABASES;"

# List tables
mysql -u readonly -p -D mydb -e "SHOW TABLES;"

# Describe table
mysql -u readonly -p -D mydb -e "DESCRIBE users;"

# Select data (limited)
mysql -u readonly -p -D mydb -e "SELECT * FROM users LIMIT 10;"

# Show status
mysql -u readonly -p -e "SHOW STATUS;" | head -30
```
