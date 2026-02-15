# mysqldump

**Platforms:** Multi-platform  
**Category:** Database Backup

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive backup | `mysqldump --defaults-file=/etc/mysql/backup.cnf database > backup.sql` |
| No locks | `mysqldump --single-transaction database > backup.sql` |

## Command-Line Flags

```bash
mysqldump -u user -p -q database > backup.sql   # Quick mode (stdout, non-interactive)
mysqldump -u user -p --lock-tables=false database > backup.sql
```
- `-q` or `--quick`: Quick mode
- `--single-transaction`: Consistent dump without locks (non-interactive safe)
- `--lock-tables=false`: Don't lock tables

## Recommended Unattended Usage

```bash
#!/bin/bash

mysqldump --defaults-file=/etc/mysql/backup.cnf     --single-transaction     --routines     --triggers     database > "backup_$(date +%Y%m%d).sql"
```
