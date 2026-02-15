# gsutil

**Platforms:** Multi-platform  
**Category:** Cloud Storage (Google Cloud)

## Quick Reference

| Goal | Command |
|------|---------|
| Parallel operation (no prompts) | `gsutil -m rsync -d -r local/ gs://bucket/` |
| Quiet output to stdout | `gsutil cp gs://bucket/file.txt -` |

## Environment Variables

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json  # Service account key (avoids interactive login)
```

## Command-Line Flags

- `-m`: Multithreaded/parallel operations (non-interactive, no per-file prompts)
- `-q`: Quiet mode (suppress progress indicators)

`gsutil` is inherently non-interactive for most operations. It does not prompt for confirmation on destructive operations like `rm` or `rsync -d`. Use service account credentials via `GOOGLE_APPLICATION_CREDENTIALS` to avoid interactive authentication.

## Recommended Unattended Usage

```bash
#!/bin/bash

# Sync with deletion and parallel upload
gsutil -m rsync -d -r ./build gs://mybucket/

# Copy with content type
gsutil -h "Content-Type:application/json" cp *.json gs://bucket/
```
