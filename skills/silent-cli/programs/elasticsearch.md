# elasticsearch (CLI tools)

**Platforms:** Multi-platform  
**Category:** Search Engine

## Quick Reference

| Goal | Command |
|------|---------|
| Batch password setup | `elasticsearch-setup-passwords auto --batch --url http://localhost:9200` |
| Non-interactive cert gen | `elasticsearch-certutil ca --out ca.p12 --pass ""` |

## Command-Line Flags

### elasticsearch-setup-passwords
- `--batch`: Non-interactive mode (auto-generate passwords without prompting)

### elasticsearch-certutil
```bash
elasticsearch-certutil ca --out elastic-stack-ca.p12 --pass ""       # Empty passphrase avoids prompt
elasticsearch-certutil cert --ca elastic-stack-ca.p12 --out certs.p12 --pass ""
```
Passing `--pass ""` avoids interactive passphrase prompts.

## Recommended Unattended Usage

```bash
#!/bin/bash

# Generate certificates non-interactively
elasticsearch-certutil ca --out /etc/elasticsearch/ca.p12 --pass ""
elasticsearch-certutil cert --ca /etc/elasticsearch/ca.p12 --out /etc/elasticsearch/certs.p12 --pass ""

# Setup passwords in batch mode
elasticsearch-setup-passwords auto --batch --url http://localhost:9200
```
