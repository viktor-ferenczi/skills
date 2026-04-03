# pg_dump

**Platforms:** Multi-platform
**Category:** Database

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `pg_dump --version` |
| Show help | `pg_dump --help` |
| Dump schema | `pg_dump -s db` |
| Dump single table | `pg_dump -t table db` |
| List tables | `pg_dump -l db` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `pg_dump db > file` | Creates database dumps |
| With -f | Writes files |
| Any pg_dump execution | Reads and exports data |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe pg_dump Inspection Script

# Show version
pg_dump --version

# List tables
pg_dump -l mydb

# Dump schema only
pg_dump -s mydb
```
