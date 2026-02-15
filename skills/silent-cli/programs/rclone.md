# rclone

**Platforms:** Multi-platform  
**Category:** Cloud Storage Sync

## Quick Reference

| Goal | Command |
|------|---------|
| List remotes | `rclone listremotes` |
| List files | `rclone ls remote:` |
| Copy | `rclone copy local remote:bucket` |
| Sync | `rclone sync local remote:bucket` |
| Mount | `rclone mount remote:bucket /mnt/bucket` |

## Command-Line Flags

```bash
rclone listremotes                   # List configured remotes
rclone ls remote:                    # List files
rclone ls remote:bucket              # List bucket
rclone lsd remote:                   # List directories
rclone tree remote:bucket            # Tree view
rclone copy localdir remote:bucket   # Copy (skip existing)
rclone copyto localfile remote:bucket/file
rclone sync localdir remote:bucket   # Sync (make identical)
rclone sync --dry-run localdir remote:bucket  # Dry run
rclone sync --interactive localdir remote:bucket  # Confirm
rclone move localdir remote:bucket   # Move (delete source)
rclone move --dry-run localdir remote:bucket
rclone delete remote:bucket/dir      # Delete files
rclone purge remote:bucket/dir       # Delete dir and contents
rclone mkdir remote:bucket/newdir
rclone rmdir remote:bucket/emptydir
rclone cat remote:bucket/file.txt    # Cat file
rclone cat remote:bucket/file.txt | less
rclone head remote:bucket/file.txt   # First 10 lines
rclone tail remote:bucket/file.txt   # Last 10 lines
rclone size remote:bucket            # Total size
rclone size remote:bucket --json
rclone check localdir remote:bucket  # Compare
rclone check --one-way localdir remote:bucket
rclone bisync localdir remote:bucket # Bidirectional sync
rclone mount remote:bucket /mnt/bucket  # FUSE mount
rclone mount --daemon remote:bucket /mnt/bucket
rclone serve http remote:bucket      # HTTP server
rclone serve ftp remote:bucket       # FTP server
rclone serve sftp remote:bucket      # SFTP server
rclone about remote:                 # Storage info
rclone dedupe remote:bucket          # Deduplicate
rclone cleanup remote:bucket         # Cleanup old versions
rclone config                        # Interactive config
rclone config show                   # Show config
rclone version                       # Version
rclone --version
rclone --verbose copy localdir remote:bucket
rclone --quiet copy localdir remote:bucket
rclone --stats 10s copy localdir remote:bucket
rclone --transfers 8 copy localdir remote:bucket
rclone --checkers 16 copy localdir remote:bucket
rclone --bwlimit 1M copy localdir remote:bucket
rclone --max-size 100M copy localdir remote:bucket
rclone --min-size 1k copy localdir remote:bucket
rclone --exclude '*.tmp' copy localdir remote:bucket
rclone --include '*.jpg' copy localdir remote:bucket
rclone --delete-excluded sync localdir remote:bucket
rclone --backup-dir remote:backup sync localdir remote:bucket
rclone --dry-run sync localdir remote:bucket
rclone -P sync localdir remote:bucket  # Progress
```
- `-v` or `--verbose`: Verbose
- `-q` or `--quiet`: Quiet
- `-P` or `--progress`: Show progress
- `--dry-run`: Test run
- `--stats`: Stats interval
- `--transfers`: Parallel transfers
- `--checkers`: Parallel checks
- `--bwlimit`: Bandwidth limit
- `--max-size`/`--min-size`: Size filters
- `--exclude`/`--include`: Name filters
- `--delete-excluded`: Delete excluded files
- `--backup-dir`: Backup directory

## Recommended Unattended Usage

```bash
#!/bin/bash

# Sync with progress and bandwidth limit
rclone sync -P --bwlimit 10M --transfers 8 ./backup remote:bucket/

# Dry run first
rclone sync --dry-run ./data remote:data/ || exit 1
rclone sync ./data remote:data/
```
