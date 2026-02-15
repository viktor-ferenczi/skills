# pg_dump (PostgreSQL backup)

**Platforms:** Multi-platform  
**Category:** Database Backup

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

# Compressed backup
pg_dump -Fc -Z9 database > "backup_$(date +%Y%m%d).dump"

# Parallel directory backup
pg_dump -Fd -j 4 -f "backup_$(date +%Y%m%d)/" database
```
