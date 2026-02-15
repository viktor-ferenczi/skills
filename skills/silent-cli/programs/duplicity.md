# duplicity

**Platforms:** Linux, macOS  
**Category:** Encrypted Backup

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive backup | `PASSPHRASE=xxx duplicity full /source file:///backup` |
| Force remove old | `duplicity remove-older-than 6M file:///backup --force` |
| Quiet operation | `duplicity --verbosity 0 /source file:///backup` |

## Environment Variables

```bash
export PASSPHRASE='encryption password'   # Required for non-interactive GPG operations
export FTP_PASSWORD='ftp password'        # Avoids FTP password prompt
export AWS_ACCESS_KEY_ID=xxx              # Avoids AWS credential prompts
export AWS_SECRET_ACCESS_KEY=xxx
```

Setting `PASSPHRASE` is essential for unattended operation — without it, duplicity will prompt interactively for the GPG passphrase.

## Command-Line Flags

- `--verbosity {0,2,4,5,9}`: Verbosity level (use `0` for silent)
- `--force`: Force removal of old backups without confirmation
- `--dry-run`: Test run without making changes

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
