# mc (MinIO Client)

**Platforms:** Multi-platform  
**Category:** Object Storage

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet copy | `mc --quiet cp file.txt myminio/bucket/` |
| JSON output | `mc --json ls myminio` |

## Command-Line Flags

```bash
mc --quiet cp file.txt myminio/bucket/   # Quiet
mc --json ls myminio                 # JSON output
mc rm -r --force myminio/mybucket/dir/  # Recursive delete (no prompt)
mc rb --force myminio/bucket         # Remove bucket with contents (no prompt)
```
- `--quiet`: Quiet output
- `--json`: JSON output
- `--force`: Force operation (no prompt)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Mirror with overwrite
mc mirror --overwrite --remove ./build myminio/mybucket/

# Batch delete with force
mc rm -r --force myminio/mybucket/temp/
```
