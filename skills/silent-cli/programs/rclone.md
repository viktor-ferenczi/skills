# rclone

**Platforms:** Multi-platform  
**Category:** Cloud Storage Sync

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet sync | `rclone --quiet sync localdir remote:bucket` |
| Dry run | `rclone --dry-run sync localdir remote:bucket` |
| JSON size | `rclone size remote:bucket --json` |

## Command-Line Flags

- `-q` or `--quiet`: Quiet — suppress normal output
- `--dry-run`: Test run without making changes
- `-P` or `--progress`: Show progress (disable with `--quiet` for scripts)
- `--stats`: Stats reporting interval (set to `0` to disable)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Sync with progress and bandwidth limit
rclone sync -P --bwlimit 10M --transfers 8 ./backup remote:bucket/

# Dry run first
rclone sync --dry-run ./data remote:data/ || exit 1
rclone sync ./data remote:data/
```
