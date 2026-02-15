# vault (HashiCorp)

**Platforms:** Multi-platform  
**Category:** Secrets Management

## Quick Reference

| Goal | Command |
|------|---------|
| Status | `vault status` |
| Login | `vault login` |
| Read secret | `vault kv get secret/path` |
| Write secret | `vault kv put secret/path key=value` |

## Command-Line Flags

```bash
vault status                         # Server status
vault status -format=json            # JSON output
vault login -method=userpass username=myuser
vault login -method=github token=ghp_xxx
vault kv get secret/mysecret         # Get secret
vault kv get -field=password secret/mysecret  # Get specific field
vault kv get -format=json secret/mysecret
vault kv put secret/mysecret key=value key2=value2
vault kv list secret/                # List secrets
vault kv delete secret/mysecret      # Delete secret
vault kv destroy secret/mysecret     # Permanently delete
vault kv undelete secret/mysecret    # Recover deleted
vault policy list                    # List policies
vault policy read mypolicy           # Read policy
vault policy write mypolicy policy.hcl  # Write policy
vault auth list                      # List auth methods
vault auth enable userpass           # Enable auth method
vault auth disable userpass          # Disable auth method
vault secrets list                   # List secret engines
vault secrets enable -path=secret kv  # Enable KV engine
vault token create                   # Create token
vault token revoke token_id          # Revoke token
vault operator unseal                # Unseal vault
vault operator seal                  # Seal vault
vault operator init                  # Initialize vault
vault operator raft list-peers       # Raft peers
vault write auth/userpass/users/myuser password=mypass
vault read auth/token/lookup-self
vault audit list                     # List audit devices
```
- `-address`: Vault address (VAULT_ADDR)
- `-token`: Vault token (VAULT_TOKEN)
- `-format`: Output format (table, json, yaml)
- `-namespace`: Vault namespace

## Environment Variables

```bash
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='s.xxx'
export VAULT_NAMESPACE='admin'
export VAULT_CACERT='/path/to/ca.crt'
```

## Recommended Unattended Usage

```bash
#!/bin/bash

export VAULT_ADDR='https://vault.example.com'
export VAULT_TOKEN='s.xxx'

# Get secret to environment
DB_PASS=$(vault kv get -field=password secret/db/credentials)
export DB_PASS
```
