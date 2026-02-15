# duplicity

**Platforms:** Linux, macOS  
**Category:** Encrypted Backup

## Quick Reference

| Goal | Command |
|------|---------|
| Full backup | `duplicity full /source file:///backup` |
| Incremental | `duplicity /source file:///backup` |
| List | `duplicity list-current-files file:///backup` |
| Restore | `duplicity restore file:///backup /restore` |

## Command-Line Flags

```bash
# Full backup
duplicity full /home/user file:///backup/destination
duplicity full /home/user s3+http://bucket
duplicity full /home/user rsync://user@host/backup
duplicity full /home/user scp://user@host/backup
duplicity full /home/user ftp://user:pass@host/backup

# Incremental backup (default)
duplicity /home/user file:///backup/destination

# List files
duplicity list-current-files file:///backup
duplicity list-current-files --time 3D file:///backup

# Restore
duplicity restore file:///backup /restore/path
duplicity restore --time 7D file:///backup /restore/path

# Verify
duplicity verify file:///backup /source

# Remove old backups
duplicity remove-older-than 6M file:///backup --force
duplicity remove-all-but-n-full 3 file:///backup --force
duplicity remove-all-inc-of-but-n-full 1 file:///backup --force

# Collection status
duplicity collection-status file:///backup

# Options
--encrypt-key KEYID                  # GPG key
--sign-key KEYID                     # Sign with key
--full-if-older-than 1M              # Force full monthly
--volsize 250                        # Volume size MB
--asynchronous-upload                # Async upload
--dry-run                            # Test only
--verbosity {0,2,4,5,9}              # Verbosity level
```
- `full`: Force full backup
- `list-current-files`: List files
- `restore`: Restore backup
- `verify`: Verify backup
- `remove-older-than`: Remove old
- `remove-all-but-n-full`: Keep N full
- `collection-status`: Status info
- `--encrypt-key`: Encryption key
- `--full-if-older-than`: Force full backup
- `--dry-run`: Test run

## Environment Variables

```bash
export PASSPHRASE='encryption password'
export FTP_PASSWORD='ftp password'
export AWS_ACCESS_KEY_ID=xxx
export AWS_SECRET_ACCESS_KEY=xxx
```

## Recommended Unattended Usage

```bash
#!/bin/bash

export PASSPHRASE=$(cat /etc/backup/passphrase)

# Monthly full, daily incremental
if [ $(date +%d) == "01" ]; then
    duplicity full /home file:///backup --full-if-older-than 1M
else
    duplicity /home file:///backup
fi

# Remove old backups
if [ $(date +%d) == "01" ]; then
    duplicity remove-older-than 6M file:///backup --force
fi
```
