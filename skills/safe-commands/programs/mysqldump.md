# mysqldump

**Platforms:** Multi-platform
**Category:** Database

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `mysqldump --version` |
| Show help | `mysqldump --help` |
| Dump schema | `mysqldump --no-data db` |
| Dump single table | `mysqldump db table` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `mysqldump` | Creates database dumps |
| With --result-file | Writes files |
| Any mysqldump execution | Reads and exports data |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe mysqldump Inspection Script

# Show version
mysqldump --version

# Dump schema only (no data)
mysqldump --no-data mydb
```
