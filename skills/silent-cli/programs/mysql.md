# mysql (MariaDB/MySQL client)

**Platforms:** Multi-platform  
**Category:** Database Client

## Quick Reference

| Goal | Command |
|------|---------|
| Execute SQL | `mysql -u user -p -e 'SELECT 1'` |
| Import file | `mysql -u user database < file.sql` |
| Batch mode | `mysql -B -N -e 'SELECT * FROM table'` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `MYSQL_PWD` | `password` | Password (insecure) |
| `MYSQL_HOST` | `localhost` | Default host |

## Command-Line Flags

```bash
mysql -u user -p -e "SELECT 1"       # Execute query
mysql -u user -p database < script.sql  # Import SQL
mysql -u user -p -B -N -e "SELECT * FROM table"  # Batch, no names
mysql -u user -p --batch --skip-column-names -e "SELECT *"
mysql -u user -p --silent -e "SELECT *"  # Silent
mysql -u user -p -e "SELECT *" 2>/dev/null  # Suppress warnings
mysql -u user -p --raw -e "SELECT *"  # No escaping
```
- `-u` or `--user`: Username
- `-p` or `--password`: Password (prompt if no value)
- `-e` or `--execute`: Execute command
- `-B` or `--batch`: Batch mode (tab-separated)
- `-N` or `--skip-column-names`: No column headers
- `--silent`: Silent mode
- `--raw`: Raw output (no escaping)
- `-h` or `--host`: Host
- `-P` or `--port`: Port
- `-D` or `--database`: Database

## Recommended Unattended Usage

```bash
#!/bin/bash

# Using defaults file (secure)
mysql --defaults-file=/path/to/my.cnf -e "SELECT 1"

# Batch output for scripting
result=$(mysql -u user -p'pass' -B -N -e "SELECT COUNT(*) FROM table" database)
```
