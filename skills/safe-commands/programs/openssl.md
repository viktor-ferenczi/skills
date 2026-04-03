# openssl

**Platforms:** Multi-platform
**Category:** Security/Cryptography

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `openssl version` |
| Show help | `openssl help` |
| View cert | `openssl x509 -in cert.pem -text` |
| View CSR | `openssl req -in req.csr -text` |
| Hash file | `openssl dgst file` |
| Verify cert | `openssl verify cert.pem` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `openssl genrsa` | Generates keys |
| `openssl req -new` | Creates CSRs |
| `openssl x509 -sign` | Signs certificates |
| `openssl enc -e` | Encrypts files |
| `openssl enc -d` | Decrypts files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe openssl Inspection Script

# Show version
openssl version

# View certificate
openssl x509 -in cert.pem -text -noout

# Hash file
openssl dgst file.txt
```
