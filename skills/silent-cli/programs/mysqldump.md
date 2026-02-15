# mysqldump

**Platforms:** Multi-platform  
**Category:** Database Backup

## Quick Reference

| Goal | Command |
|------|---------|
| Backup | `mysqldump -u user database > backup.sql` |
| No locks | `mysqldump --single-transaction database > backup.sql` |
| Specific tables | `mysqldump database table1 table2` |

## Command-Line Flags

```bash
mysqldump -u user -p database > backup.sql
mysqldump -u user -p --all-databases > all.sql
mysqldump -u user -p --single-transaction database > backup.sql
mysqldump -u user -p --no-data database > schema.sql  # Schema only
mysqldump -u user -p --no-create-info database > data.sql  # Data only
mysqldump -u user -p --routines database > backup.sql  # Include routines
mysqldump -u user -p --triggers database > backup.sql
mysqldump -u user -p --compress database > backup.sql
mysqldump -u user -p -q database > backup.sql  # Quick mode
mysqldump -u user -p --lock-tables=false database > backup.sql
```
- `-u`: Username
- `-p`: Password
- `--all-databases`: All databases
- `--single-transaction`: Consistent dump without locks
- `--no-data`: Schema only
- `--no-create-info`: Data only
- `--routines`: Include stored procedures
- `--triggers`: Include triggers
- `--compress`: Compress communication
- `-q` or `--quick`: Quick mode
- `--lock-tables=false`: Don't lock tables

## Recommended Unattended Usage

```bash
#!/bin/bash

mysqldump --defaults-file=/etc/mysql/backup.cnf     --single-transaction     --routines     --triggers     database > "backup_$(date +%Y%m%d).sql"
```
