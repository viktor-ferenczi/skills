# openssl

**Platforms:** Multi-platform  
**Category:** Cryptography/Security

## Quick Reference

| Goal | Command |
|------|---------|
| No-prompt cert | `openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj '/CN=localhost'` |

## Command-Line Flags

```bash
# Generate RSA key (suppress progress)
openssl genrsa -out key.pem 4096 2>/dev/null

# Generate self-signed cert without prompts (-subj avoids interactive questions)
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj '/CN=localhost'

# Test connection non-interactively
openssl s_client -connect host:443 -servername host < /dev/null
openssl s_client -connect host:443 </dev/null 2>/dev/null | openssl x509 -noout -text
```
- `-subj`: Set subject (avoids interactive prompts)
- `-nodes`: No passphrase (avoids interactive prompt)
- `< /dev/null`: Prevents interactive input for s_client

## Recommended Unattended Usage

```bash
#!/bin/bash

# Generate cert without prompts
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes     -subj '/C=US/ST=State/L=City/O=Org/CN=localhost' 2>/dev/null

# Check cert expiry
days=$(openssl x509 -in cert.pem -noout -enddate | cut -d= -f2)
```
