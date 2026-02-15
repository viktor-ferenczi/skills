# pg_restore (PostgreSQL restore)

**Platforms:** Multi-platform  
**Category:** Database Restore

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `PGPASSWORD` | `secret` | Password (avoids interactive prompt) |

## Recommended Unattended Usage

```bash
#!/bin/bash

export PGHOST=localhost
export PGUSER=postgres
export PGPASSWORD=secret

# Restore to database
pg_restore -d database backup.dump

# Parallel restore
pg_restore -j 4 -d database backup.dump
```
