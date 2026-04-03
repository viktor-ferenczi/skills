# curl

**Platforms:** Multi-platform
**Category:** Network & HTTP

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Fetch URL content | `curl https://example.com` |
| Check HTTP headers | `curl -I https://example.com` |
| Get response info | `curl -w "%{http_code}" -o /dev/null URL` |
| Download file | `curl -O https://example.com/file` |
| Silent mode | `curl -s https://example.com` |
| Show only errors | `curl -sS https://example.com` |
| Follow redirects | `curl -L https://example.com` |
| Limit download size | `curl -C - -r 0-1048576 URL` |
| Check SSL cert | `curl -vI https://example.com` |
| Test endpoint | `curl -X OPTIONS URL` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `curl -T file URL` | Uploads data to server |
| `curl -X POST/PUT/DELETE` | Modifies server state |
| `curl -d "data" URL` | Sends data (may modify) |
| `curl -F "file=@..."` | Uploads files |
| `curl -u user:pass` | Sends credentials |
| `curl -b cookie` | Sends cookies |
| `curl -H "Auth: ..."` | Sends auth headers |

## Environment Variables for Safe Operation

| Variable | Description |
|----------|-------------|
| `CURL_CA_BUNDLE` | CA certificate path |
| `HTTPS_PROXY` | Proxy for HTTPS |
| `NO_PROXY` | Bypass proxy for hosts |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe curl Inspection Script

# Check website availability
curl -sS -w "HTTP Status: %{http_code}\nTime: %{time_total}s\n" https://example.com

# Get headers only
curl -I https://example.com

# Download with progress
curl -L -O https://example.com/file.tar.gz

# Check SSL certificate
curl -vI https://example.com 2>&1 | grep -E "subject|issuer|expire"

# Test API endpoint (GET only)
curl -s -H "Accept: application/json" https://api.example.com/v1/status
```
