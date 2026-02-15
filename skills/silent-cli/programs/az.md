# az (Azure CLI)

**Platforms:** Multi-platform  
**Category:** Cloud (Microsoft Azure)

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive login | `az login --service-principal -u appid -p password --tenant tenant` |
| Suppress warnings | `az --only-show-errors <command>` |
| Auto-confirm | `az <command> --yes` |
| Machine-readable output | `az <command> --output json` |

## Command-Line Flags

- `--output json|tsv|none`: Machine-readable output format (use `none` to suppress output entirely)
- `--only-show-errors`: Suppress warnings, show only errors
- `--yes`: Auto-confirm destructive operations without prompting
- `--no-prompt`: Disable interactive prompts (fall back to default or error)
- `--query`: JMESPath query to filter output

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive with service principal
az login --service-principal \
    --username $AZURE_CLIENT_ID \
    --password $AZURE_CLIENT_SECRET \
    --tenant $AZURE_TENANT_ID

# Create VM without prompts
az vm create \
    --resource-group myrg \
    --name myvm \
    --image Ubuntu2204 \
    --admin-username admin \
    --generate-ssh-keys \
    --yes \
    --only-show-errors
```
