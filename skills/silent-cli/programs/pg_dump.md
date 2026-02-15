# pg_dump (PostgreSQL backup)

**Platforms:** Multi-platform  
**Category:** Database Backup

## Quick Reference

| Goal | Command |
|------|---------|
| Backup | `pg_dump database > backup.sql` |
| Custom format | `pg_dump -Fc database > backup.dump` |
| Parallel | `pg_dump -Fd -j 4 database -f backup/` |

## Command-Line Flags

```bash
pg_dump database > backup.sql        # Plain SQL
pg_dump -Fc database > backup.dump   # Custom format (compressed)
pg_dump -Fd -j 4 database -f backup/ # Directory format, parallel
pg_dump -Ft database > backup.tar    # Tar format
pg_dump -a database > data.sql       # Data only
pg_dump -s database > schema.sql     # Schema only
pg_dump -t table database > backup.sql  # Single table
pg_dump -n schema database > backup.sql  # Single schema
pg_dump --exclude-table=table database  # Exclude table
```
- `-Fc` or `--format=custom`: Custom format (compressed)
- `-Fd` or `--format=directory`: Directory format
- `-Ft` or `--format=tar`: Tar format
- `-j` or `--jobs`: Parallel jobs
- `-a` or `--data-only`: Data only
- `-s` or `--schema-only`: Schema only
- `-t` or `--table`: Specific table
- `-n` or `--schema`: Specific schema
- `--exclude-table`: Exclude table

## Recommended Unattended Usage

```bash
#!/bin/bash

export PGHOST=localhost
export PGUSER=postgres
export PGPASSWORD=secret

# Compressed backup
pg_dump -Fc -Z9 database > "backup_$(date +%Y%m%d).dump"

# Parallel directory backup
pg_dump -Fd -j 4 -f "backup_$(date +%Y%m%d)/" database
```
