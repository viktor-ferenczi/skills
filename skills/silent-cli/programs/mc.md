# mc (MinIO Client)

**Platforms:** Multi-platform  
**Category:** Object Storage

## Quick Reference

| Goal | Command |
|------|---------|
| List hosts | `mc alias list` |
| Add host | `mc alias set myminio http://localhost:9000 access secret` |
| List buckets | `mc ls myminio` |
| Copy | `mc cp file.txt myminio/bucket/` |

## Command-Line Flags

```bash
mc alias list                        # List configured hosts
mc alias set myminio http://localhost:9000 ACCESSKEY SECRETKEY
mc alias remove myminio              # Remove alias
mc ls myminio                        # List buckets
mc ls myminio/mybucket               # List bucket
mc ls -r myminio/mybucket            # Recursive
mc cp file.txt myminio/mybucket/     # Upload
mc cp myminio/mybucket/file.txt .    # Download
mc cp -r localdir/ myminio/mybucket/ # Recursive
mc mirror localdir/ myminio/mybucket/  # Mirror (sync)
mc mirror --overwrite localdir/ myminio/mybucket/
mc rm myminio/mybucket/file.txt      # Delete
mc rm -r --force myminio/mybucket/dir/  # Recursive delete
mc mb myminio/newbucket              # Make bucket
mc rb myminio/bucket                 # Remove bucket
mc rb --force myminio/bucket         # Remove with contents
mc cat myminio/mybucket/file.txt     # Cat file
mc pipe myminio/mybucket/file.txt    # Pipe to object
mc head myminio/mybucket/file.txt    # First 1KB
mc tail myminio/mybucket/file.txt    # Last 1KB
mc find myminio/mybucket --name '*.txt'  # Find files
mc du myminio/mybucket               # Disk usage
mc stat myminio/mybucket/file.txt    # Object info
mc tree myminio/mybucket             # Directory tree
mc share download myminio/bucket/file --expire 1h
mc share upload myminio/bucket/file --expire 1h
mc policy set public myminio/bucket  # Make public
mc policy set private myminio/bucket # Make private
mc policy get myminio/bucket         # Get policy
mc admin info myminio                # Server info
mc admin user list myminio           # List users
mc admin user add myminio newuser newpassword
mc --quiet cp file.txt myminio/bucket/   # Quiet
mc --json ls myminio                 # JSON output
mc --debug ls myminio                # Debug mode
mc --insecure ls myminio             # Skip TLS verify
```
- `--quiet`: Quiet output
- `--json`: JSON output
- `--debug`: Debug mode
- `--insecure`: Skip TLS verify
- `--overwrite`: Overwrite existing
- `--force`: Force operation
- `-r`: Recursive

## Recommended Unattended Usage

```bash
#!/bin/bash

# Mirror with overwrite
mc mirror --overwrite --remove ./build myminio/mybucket/

# Batch delete with force
mc rm -r --force myminio/mybucket/temp/
```
