# curl

**Platforms:** Multi-platform  
**Category:** Data Transfer

## Quick Reference

| Goal | Command |
|------|---------|
| Silent download | `curl -fsSL -o file url` |
| Quiet with errors | `curl -fsSL url` |
| Check URL | `curl -fsSL -o /dev/null -w '%{http_code}' url` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `CURL_CA_BUNDLE` | `/path/to/ca.crt` | CA certificates |
| `HTTP_PROXY` | `http://proxy:port` | HTTP proxy |
| `HTTPS_PROXY` | `http://proxy:port` | HTTPS proxy |

## Command-Line Flags

```bash
curl -fsSL -o file https://example.com/file    # Silent download
curl -fsSL https://example.com/api | jq .      # API call
curl -I -fsSL https://example.com              # Headers only
curl -fsSL -H "Authorization: Bearer $TOKEN" url
```
- `-f` or `--fail`: Fail on HTTP error
- `-s` or `--silent`: Silent mode
- `-S` or `--show-error`: Show errors with -s
- `-L` or `--location`: Follow redirects
- `-o` or `--output`: Write to file
- `-I` or `--head`: Headers only
- `-H` or `--header`: Custom headers
- `-X` or `--request`: HTTP method
- `-d` or `--data`: POST data
- `-k` or `--insecure`: Skip SSL verify
- `--connect-timeout`: Connection timeout
- `--max-time`: Max operation time
- `--retry`: Number of retries
