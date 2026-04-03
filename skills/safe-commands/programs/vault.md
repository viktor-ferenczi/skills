# vault (HashiCorp)

**Platforms:** Multi-platform
**Category:** Security/Secrets

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `vault version` |
| Show help | `vault --help` |
| Read secret | `vault kv get secret/path` |
| List secrets | `vault kv list secret/` |
| Show status | `vault status` |
| Show config | `vault read sys/config` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `vault kv put` | Writes secrets |
| `vault kv delete` | Deletes secrets |
| `vault kv patch` | Modifies secrets |
| `vault write` | Writes data |
| `vault delete` | Deletes data |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe vault Inspection Script

# Read secret
vault kv get secret/myapp

# List secrets
vault kv list secret/
```
