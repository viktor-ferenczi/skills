# vault (HashiCorp)

**Platforms:** Multi-platform  
**Category:** Secrets Management

## Command-Line Flags

- `-format=json`: Machine-readable JSON output
- `-field`: Extract specific field (avoids parsing)

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `VAULT_ADDR` | `http://127.0.0.1:8200` | Vault server address (avoids interactive prompt) |
| `VAULT_TOKEN` | `s.xxx` | Authentication token (avoids login prompt) |

## Recommended Unattended Usage

```bash
#!/bin/bash

export VAULT_ADDR='https://vault.example.com'
export VAULT_TOKEN='s.xxx'

# Get secret to environment
DB_PASS=$(vault kv get -field=password secret/db/credentials)
export DB_PASS
```
