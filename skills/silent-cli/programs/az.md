# az (Azure CLI)

**Platforms:** Multi-platform  
**Category:** Cloud (Microsoft Azure)

## Quick Reference

| Goal | Command |
|------|---------|
| Login | `az login` |
| List accounts | `az account list` |
| Set subscription | `az account set --subscription mysub` |
| List VMs | `az vm list` |

## Command-Line Flags

```bash
az login                             # Interactive login
az login --service-principal -u appid -p password --tenant tenant
az login --identity                  # Managed identity
az account list                      # List subscriptions
az account set --subscription mysub  # Set subscription
az account show                      # Current subscription
az vm list                           # List VMs
az vm list --resource-group myrg
az vm start --name myvm --resource-group myrg
az vm stop --name myvm --resource-group myrg
az vm deallocate --name myvm --resource-group myrg
az vm delete --name myvm --resource-group myrg --yes
az group list                        # List resource groups
az group create --name myrg --location eastus
az storage account list              # Storage accounts
az storage blob list --account-name mystorage --container mycontainer
az storage blob upload --file file.txt --name file.txt --container mycontainer --account-name mystorage
az webapp list                       # Web apps
az functionapp list                  # Function apps
az aks list                          # AKS clusters
az aks get-credentials --name myaks --resource-group myrg
az sql server list                   # SQL servers
az sql db list --server myserver --resource-group myrg
az cosmosdb list                     # Cosmos DB accounts
az keyvault list                     # Key vaults
az network vnet list                 # Virtual networks
az monitor metrics list --resource myresource
az ad sp list                        # Service principals
az role assignment list              # Role assignments
az --output json vm list
az --output table vm list
az --output tsv vm list
az --query "[].{Name:name, RG:resourceGroup, Status:powerState}" vm list
az --only-show-errors vm list        # Suppress warnings
az vm create --resource-group myrg --name myvm --image Ubuntu2204 --yes
```
- `--subscription`: Subscription ID
- `--resource-group`: Resource group
- `--output`: Output format (json, jsonc, yaml, table, tsv, none)
- `--query`: JMESPath query
- `--only-show-errors`: Suppress warnings
- `--yes`: Auto-confirm

## Environment Variables

```bash
export AZURE_TENANT_ID=xxx
export AZURE_CLIENT_ID=xxx
export AZURE_CLIENT_SECRET=xxx
export AZURE_DEFAULTS_LOCATION=eastus
```

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive with service principal
az login --service-principal     --username $AZURE_CLIENT_ID     --password $AZURE_CLIENT_SECRET     --tenant $AZURE_TENANT_ID

# Create VM without prompts
az vm create     --resource-group myrg     --name myvm     --image Ubuntu2204     --admin-username admin     --generate-ssh-keys     --yes     --only-show-errors
```
