# rsync

**Platforms:** Multi-platform  
**Category:** File Transfer

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet sync | `rsync -aq source/ dest/` |
| With delete | `rsync -aq --delete source/ dest/` |
| Over SSH | `rsync -aq -e ssh source/ user@host:/dest/` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `RSYNC_RSH` | `ssh -o BatchMode=yes` | Remote shell |

## Command-Line Flags

```bash
rsync -aq source/ dest/              # Quiet archive sync
rsync -av source/ dest/              # Verbose archive
rsync -aq --delete source/ dest/     # Delete extraneous
rsync -aq -e 'ssh -o BatchMode=yes' source/ host:/dest/
rsync -aq --exclude='*.tmp' source/ dest/
rsync -aq --include='*.txt' --exclude='*' source/ dest/
rsync -aq --bwlimit=1000 source/ dest/  # Limit bandwidth (KB/s)
rsync -aq --partial source/ dest/    # Partial transfer resume
rsync -aqP source/ dest/             # Progress + partial
```
- `-a` or `--archive`: Archive mode (equiv to -rlptgoD)
- `-q` or `--quiet`: Quiet
- `-v` or `--verbose`: Verbose
- `-r` or `--recursive`: Recursive
- `-P`: --partial --progress
- `--delete`: Delete extraneous dest files
- `--exclude=PATTERN`: Exclude pattern
- `--include=PATTERN`: Include pattern
- `-e` or `--rsh`: Remote shell
- `--bwlimit`: Bandwidth limit
- `--partial`: Keep partial files

## Recommended Unattended Usage

```bash
#!/bin/bash

rsync -aq --delete --exclude='.git' \
    -e 'ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new' \
    ./source/ user@host:/dest/
# WARNING: StrictHostKeyChecking=accept-new auto-accepts unknown host keys.
# This is a security-sensitive setting. Confirm with the human operator before using.
# Use =yes (default) to reject unknown hosts, =accept-new to auto-accept only new hosts,
# or =no to disable all verification (NOT recommended - vulnerable to MITM attacks).
```
