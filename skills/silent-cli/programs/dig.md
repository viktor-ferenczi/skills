# dig / nslookup / host

**Platforms:** Multi-platform  
**Category:** DNS Lookup

## Quick Reference

| Goal | Command |
|------|---------|
| Simple lookup | `dig +short example.com` |
| MX records | `dig +short MX example.com` |
| Quiet check | `dig +short +timeout=2 example.com` |

## Command-Line Flags

```bash
dig example.com                      # Full output
dig +short example.com               # Short output (IP only)
dig +short MX example.com            # MX records
dig +short NS example.com            # NS records
dig @8.8.8.8 example.com             # Specific DNS server
dig +short +time=2 +tries=1 example.com  # Quick timeout
```
- `+short`: Short output
- `+time=N`: Query timeout
- `+tries=N`: Number of tries
- `@server`: Use specific DNS server
- `+trace`: Trace delegation
- `+noall +answer`: Just answer section

### nslookup
```bash
nslookup example.com
nslookup -query=MX example.com
```

### host
```bash
host example.com
host -t MX example.com
host -t A example.com
```
