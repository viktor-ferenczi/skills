# pg_restore (PostgreSQL restore)

**Platforms:** Multi-platform  
**Category:** Database Restore

## Quick Reference

| Goal | Command |
|------|---------|
| Restore | `pg_restore -d database backup.dump` |
| List contents | `pg_restore -l backup.dump` |
| Parallel | `pg_restore -d database -j 4 backup.dump` |

## Command-Line Flags

```bash
pg_restore -d database backup.dump   # Restore to database
pg_restore -C -d postgres backup.dump  # Create database
pg_restore -l backup.dump            # List contents
pg_restore -L list.txt backup.dump   # Restore from list
pg_restore -t table -d database backup.dump  # Single table
pg_restore -n schema -d database backup.dump  # Single schema
pg_restore -j 4 -d database backup.dump  # Parallel restore
pg_restore --clean -d database backup.dump  # Clean before restore
pg_restore --data-only -d database backup.dump  # Data only
pg_restore --schema-only -d database backup.dump  # Schema only
```
- `-d` or `--dbname`: Target database
- `-C` or `--create`: Create database
- `-l` or `--list`: List archive contents
- `-L` or `--use-list`: Use specific list
- `-t` or `--table`: Restore specific table
- `-n` or `--schema`: Restore specific schema
- `-j` or `--jobs`: Parallel jobs
- `--clean`: Clean (drop) objects before creating
- `--data-only`: Data only
- `--schema-only`: Schema only
