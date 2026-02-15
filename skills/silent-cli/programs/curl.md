# curl

**Platforms:** Multi-platform  
**Category:** Data Transfer

## Quick Reference

| Goal | Command |
|------|---------|
| Silent download | `curl -fsSL -o file url` |
| Quiet with errors | `curl -fsSL url` |
| Check URL (no output) | `curl -fsSL -o /dev/null -w '%{http_code}' url` |

## Command-Line Flags

- `-f` or `--fail`: Fail silently on HTTP errors (no error page output)
- `-s` or `--silent`: Silent mode (no progress meter or error messages)
- `-S` or `--show-error`: Show errors even when in silent mode (use with `-s`)
- `-o` or `--output`: Write output to file instead of stdout
- `--connect-timeout`: Connection timeout (prevents hanging in scripts)
- `--max-time`: Maximum time for the whole operation
- `--retry`: Number of retries on transient errors

## Recommended Unattended Usage

```bash
#!/bin/bash

# Silent download with error handling and timeout
curl -fsSL --connect-timeout 10 --max-time 60 --retry 3 -o file.tar.gz https://example.com/file.tar.gz

# API call with silent output piped to jq
result=$(curl -fsSL -H "Authorization: Bearer $TOKEN" https://api.example.com/data)
```
