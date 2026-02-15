# restic

**Platforms:** Multi-platform  
**Category:** Backup Tool

## Quick Reference

| Goal | Command |
|------|---------|
| Init | `restic init --repo /backup` |
| Backup | `restic backup /home/user` |
| Snapshots | `restic snapshots` |
| Restore | `restic restore latest --target /restore` |
| Check | `restic check` |

## Command-Line Flags

```bash
# Initialize repository
restic init --repo /backup/local
restic init --repo s3:s3.amazonaws.com/bucket
restic init --repo rclone:remote:bucket

# Backup
restic -r /backup backup /home/user
restic -r /backup backup /home/user --tag production
restic -r /backup backup /home/user --exclude='*.log'
restic -r /backup backup /home/user --exclude-file=excludes.txt
restic -r /backup backup /home/user --files-from=includes.txt
restic -r /backup backup /home/user --one-file-system

# Snapshots
restic -r /backup snapshots
restic -r /backup snapshots --tag production
restic -r /backup snapshots --path /home/user

# Restore
restic -r /backup restore latest --target /restore
restic -r /backup restore abc123 --target /restore
restic -r /backup restore latest --target /restore --include /home/user/file.txt

# Check and maintenance
restic -r /backup check
restic -r /backup check --read-data
restic -r /backup prune              # Remove unneeded data
restic -r /backup prune --keep-daily 7 --keep-weekly 4
restic -r /backup forget --keep-last 5
restic -r /backup forget --prune
restic -r /backup rebuild-index

# Mount
restic -r /backup mount /mnt/restic

# List and cat
restic -r /backup ls latest
restic -r /backup ls latest --path /home/user
restic -r /backup cat blob abc123

# Environment variables
export RESTIC_REPOSITORY=/backup
export RESTIC_PASSWORD=mypassword
export RESTIC_PASSWORD_FILE=/etc/restic/password
export AWS_ACCESS_KEY_ID=xxx
export AWS_SECRET_ACCESS_KEY=xxx

# Quiet operation
restic backup /home --quiet
restic backup /home --json           # JSON output
```
- `-r` or `--repo`: Repository location
- `--tag`: Add tag to snapshot
- `--exclude`: Exclude pattern
- `--exclude-file`: Exclude file
- `--files-from`: Include file
- `--one-file-system`: Don't cross filesystems
- `--target`: Restore target
- `--include`: Include pattern (restore)
- `--keep-*`: Retention policy
- `--prune`: Prune after forget
- `--quiet`: Quiet
- `--json`: JSON output

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
