# pg_restore

**Platforms:** Multi-platform
**Category:** Database

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `pg_restore --version` |
| Show help | `pg_restore --help` |
| List contents | `pg_restore -l dumpfile` |
| Show TOC | `pg_restore --list dumpfile` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `pg_restore -d db dump` | Restores database |
| `pg_restore -c` | Cleans before restore |
| Any pg_restore execution | Modifies database |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe pg_restore Inspection Script

# List contents
pg_restore -l backup.dump

# Show help
pg_restore --help
```
