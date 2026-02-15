# openssl

**Platforms:** Multi-platform  
**Category:** Cryptography/Security

## Quick Reference

| Goal | Command |
|------|---------|
| Generate cert | `openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes` |
| Check cert | `openssl x509 -in cert.pem -text -noout` |
| Hash | `echo -n 'text' | openssl dgst -sha256` |

## Command-Line Flags

```bash
# Generate RSA key
openssl genrsa -out key.pem 4096
openssl genrsa -out key.pem 4096 2>/dev/null  # Quiet

# Generate self-signed cert
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj '/CN=localhost'

# Check certificate
openssl x509 -in cert.pem -text -noout
openssl x509 -in cert.pem -noout -dates  # Just dates
openssl x509 -in cert.pem -noout -subject  # Just subject

# Check CSR
openssl req -in csr.pem -text -noout

# Generate CSR
openssl req -new -key key.pem -out csr.pem -subj '/CN=example.com'

# Check private key
openssl rsa -in key.pem -check -noout

# Hash
openssl dgst -sha256 file
openssl dgst -sha256 -binary file | base64
echo -n 'text' | openssl dgst -sha256

# Encrypt/decrypt
openssl enc -aes-256-cbc -salt -in file.txt -out file.txt.enc -k password
openssl enc -aes-256-cbc -d -in file.txt.enc -out file.txt -k password

# Test connection
openssl s_client -connect host:443 -servername host < /dev/null
openssl s_client -connect host:443 </dev/null 2>/dev/null | openssl x509 -noout -text

# Convert formats
openssl pkcs12 -in cert.pfx -out cert.pem -nodes
openssl x509 -in cert.crt -out cert.pem -outform PEM
```

## Recommended Unattended Usage

```bash
#!/bin/bash

# Generate cert without prompts
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes     -subj '/C=US/ST=State/L=City/O=Org/CN=localhost' 2>/dev/null

# Check cert expiry
days=$(openssl x509 -in cert.pem -noout -enddate | cut -d= -f2)
```
