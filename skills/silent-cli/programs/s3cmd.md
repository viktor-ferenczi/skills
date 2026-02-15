# s3cmd

**Platforms:** Multi-platform  
**Category:** Cloud Storage (S3-compatible)

## Quick Reference

| Goal | Command |
|------|---------|
| List buckets | `s3cmd ls` |
| List bucket | `s3cmd ls s3://bucket` |
| Copy | `s3cmd put file.txt s3://bucket/` |
| Sync | `s3cmd sync local/ s3://bucket/` |
| Get | `s3cmd get s3://bucket/file.txt` |

## Command-Line Flags

```bash
s3cmd ls                             # List buckets
s3cmd ls s3://mybucket               # List bucket
s3cmd ls -r s3://mybucket            # Recursive
s3cmd la                             # List all (all buckets)
s3cmd put file.txt s3://mybucket/    # Upload
s3cmd put -r localdir/ s3://mybucket/  # Recursive upload
s3cmd get s3://mybucket/file.txt     # Download
s3cmd get -r s3://mybucket/dir/ ./   # Recursive download
s3cmd sync localdir/ s3://mybucket/  # Sync
s3cmd sync --delete-removed localdir/ s3://mybucket/
s3cmd del s3://mybucket/file.txt     # Delete
s3cmd rm s3://mybucket/file.txt      # Same as del
s3cmd rm -r s3://mybucket/dir/       # Recursive delete
s3cmd mb s3://newbucket              # Make bucket
s3cmd rb s3://bucket                 # Remove bucket
s3cmd rb -r s3://bucket              # Remove with contents
s3cmd du s3://bucket                 # Disk usage
s3cmd du -H s3://bucket              # Human readable
s3cmd info s3://bucket               # Bucket info
s3cmd info s3://bucket/file.txt      # File info
s3cmd cat s3://bucket/file.txt       # Cat file
s3cmd cp s3://bucket1/file s3://bucket2/  # Copy between buckets
s3cmd mv s3://bucket/file.txt s3://bucket/newname.txt
s3cmd signurl s3://bucket/file.txt +3600  # Signed URL (1 hour)
s3cmd setacl s3://bucket/file --acl-public
s3cmd setacl s3://bucket/file --acl-private
s3cmd setacl s3://bucket/file --acl-grant=read:user@example.com
s3cmd ws-create s3://bucket          # Enable website
s3cmd ws-delete s3://bucket          # Disable website
s3cmd ws-info s3://bucket            # Website info
s3cmd --configure                    # Interactive config
s3cmd --dump-config                  # Show config
s3cmd -c /path/to/config ls          # Use custom config
```
- `-r`: Recursive
- `-H`: Human readable
- `--delete-removed`: Delete removed files (sync)
- `-c`: Config file
- `-v`: Verbose
- `-d` or `--debug`: Debug output
- `-n` or `--dry-run`: Dry run (simulate)
- `-P` or `--acl-public`: Make public

## Configuration File (~/.s3cfg)

```ini
[default]
access_key = xxx
secret_key = xxx
bucket_location = us-east-1
host_base = s3.amazonaws.com
host_bucket = %(bucket)s.s3.amazonaws.com
website_endpoint = http://%(bucket)s.s3-website-%(location)s.amazonaws.com/
```

## Recommended Unattended Usage

```bash
#!/bin/bash

# Sync with config file
s3cmd -c /etc/backup/s3cfg sync --delete-removed /backup/ s3://mybucket/

# Upload and make public
s3cmd put file.txt s3://mybucket/ --acl-public
```
