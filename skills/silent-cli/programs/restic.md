# restic

**Platforms:** Multi-platform  
**Category:** Backup Tool

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet backup | `restic backup /home --quiet` |
| JSON output | `restic backup /home --json` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `RESTIC_REPOSITORY` | `/backup` | Repository location (avoids interactive `-r` prompt) |
| `RESTIC_PASSWORD` | `mypassword` | Repository password (avoids interactive password prompt) |
| `RESTIC_PASSWORD_FILE` | `/etc/restic/password` | Password file (avoids interactive password prompt) |

## Command-Line Flags

- `--quiet`: Quiet — suppress normal output
- `--json`: JSON output — machine-readable

## Recommended Unattended Usage

```bash
#!/bin/bash

export RESTIC_REPOSITORY=s3:s3.amazonaws.com/mybucket
export RESTIC_PASSWORD_FILE=/etc/restic/pass

# Backup with excludes
restic backup / --exclude={/dev,/proc,/sys,/tmp,/var/tmp} --tag automated

# Forget old snapshots
restic forget --keep-daily 7 --keep-weekly 4 --keep-monthly 6 --prune
```
