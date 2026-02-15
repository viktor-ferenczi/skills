# s3cmd

**Platforms:** Multi-platform  
**Category:** Cloud Storage (S3-compatible)

## Quick Reference

| Goal | Command |
|------|---------|
| Dry run sync | `s3cmd sync -n localdir/ s3://bucket/` |
| Verbose | `s3cmd -v sync localdir/ s3://bucket/` |
| Use config file | `s3cmd -c /etc/backup/s3cfg ls` |

## Command-Line Flags

- `-v`: Verbose output
- `-d` or `--debug`: Debug output
- `-n` or `--dry-run`: Dry run (simulate without changes)
- `-c`: Config file path (avoids interactive `--configure`)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Sync with config file
s3cmd -c /etc/backup/s3cfg sync --delete-removed /backup/ s3://mybucket/

# Upload and make public
s3cmd put file.txt s3://mybucket/ --acl-public
```
