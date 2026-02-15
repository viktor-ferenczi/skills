# dig / nslookup / host

**Platforms:** Multi-platform  
**Category:** DNS Lookup

## Quick Reference

| Goal | Command |
|------|---------|
| Machine-readable lookup | `dig +short example.com` |
| Quick timeout (no hang) | `dig +short +time=2 +tries=1 example.com` |
| Just answer section | `dig +noall +answer example.com` |

## Command-Line Flags

- `+short`: Machine-readable short output (IP addresses only)
- `+noall +answer`: Show only the answer section (clean output for scripting)
- `+time=N`: Query timeout in seconds (prevents hanging)
- `+tries=N`: Number of tries (limit retries in automation)

`dig` is inherently non-interactive. Use `+short` or `+noall +answer` for machine-readable output suitable for scripts.
