# mysql (MariaDB/MySQL client)

**Platforms:** Multi-platform  
**Category:** Database Client

## Quick Reference

| Goal | Command |
|------|---------|
| Batch mode | `mysql -B -N -e 'SELECT * FROM table'` |
| Silent | `mysql --silent -e 'SELECT 1'` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `MYSQL_PWD` | `password` | Password (avoids interactive prompt; insecure) |

## Command-Line Flags

```bash
mysql -u user -p -B -N -e "SELECT * FROM table"  # Batch, no column names
mysql -u user -p --batch --skip-column-names -e "SELECT *"
mysql -u user -p --silent -e "SELECT *"  # Silent
mysql -u user -p --raw -e "SELECT *"  # No escaping (machine-readable)
```
- `-e` or `--execute`: Execute command (non-interactive)
- `-B` or `--batch`: Batch mode (tab-separated, no interactive formatting)
- `-N` or `--skip-column-names`: No column headers
- `--silent`: Silent mode
- `--raw`: Raw output (no escaping)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Using defaults file (secure, no password prompt)
mysql --defaults-file=/path/to/my.cnf -e "SELECT 1"

# Batch output for scripting
result=$(mysql -u user -p'pass' -B -N -e "SELECT COUNT(*) FROM table" database)
```
