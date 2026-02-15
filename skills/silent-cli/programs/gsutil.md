# gsutil

**Platforms:** Multi-platform  
**Category:** Cloud Storage (Google Cloud)

## Quick Reference

| Goal | Command |
|------|---------|
| List buckets | `gsutil ls` |
| List bucket | `gsutil ls gs://bucket` |
| Copy | `gsutil cp file.txt gs://bucket/` |
| Sync | `gsutil rsync -r local/ gs://bucket/` |
| Remove | `gsutil rm gs://bucket/file.txt` |

## Command-Line Flags

```bash
gsutil ls                            # List buckets
gsutil ls gs://mybucket              # List bucket contents
gsutil ls -r gs://mybucket           # Recursive
gsutil ls -l gs://mybucket           # With sizes
gsutil ls -L gs://mybucket/file      # Full details
gsutil cp file.txt gs://mybucket/    # Copy to bucket
gsutil cp gs://mybucket/file.txt .   # Copy from bucket
gsutil cp -r localdir gs://mybucket/ # Recursive copy
gsutil cp -z html gs://mybucket/     # Compress
gsutil cp -Z gs://mybucket/          # Compress all
gsutil mv file.txt gs://mybucket/    # Move
gsutil rm gs://mybucket/file.txt     # Delete
gsutil rm -r gs://mybucket/dir/      # Recursive delete
gsutil cat gs://mybucket/file.txt    # Cat file
gsutil cp gs://bucket/file.txt -     # Output to stdout
gsutil rsync -r local/ gs://bucket/  # Sync
gsutil rsync -d -r local/ gs://bucket/  # Delete extra files
gsutil mb gs://newbucket             # Make bucket
gsutil rb gs://bucket                # Remove bucket
gsutil du gs://bucket                # Disk usage
gsutil du -h gs://bucket             # Human readable
gsutil du -sh gs://bucket            # Summary
gsutil stat gs://bucket/file         # File info
gsutil hash file.txt                 # Calculate hash
gsutil cp -h "Content-Type:text/html" file.txt gs://bucket/
gsutil setmeta -h "Content-Type:text/html" gs://bucket/file
gsutil acl get gs://bucket/file      # Get ACL
gsutil acl set public-read gs://bucket/file  # Set public
gsutil iam ch allUsers:objectViewer gs://bucket  # Make public
gsutil versioning get gs://bucket    # Check versioning
gsutil versioning set on gs://bucket # Enable versioning
gsutil -m cp -r local/ gs://bucket/  # Parallel (multithread)
gsutil -h "Cache-Control:public,max-age=3600" cp file gs://bucket/
```
- `-r`: Recursive
- `-l`: List with details
- `-L`: Full details
- `-z`: Compress
- `-Z`: Compress all
- `-d`: Delete extra (rsync)
- `-h`: Human readable / header
- `-m`: Multithreaded
- `-s`: Summary

## Environment Variables

```bash
export CLOUDSDK_CORE_PROJECT=myproject
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
```

## Recommended Unattended Usage

```bash
#!/bin/bash

# Sync with deletion and parallel upload
gsutil -m rsync -d -r ./build gs://mybucket/

# Copy with content type
gsutil -h "Content-Type:application/json" cp *.json gs://bucket/
```
