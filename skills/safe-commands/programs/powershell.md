# powershell

**Platforms:** Multi-platform
**Category:** Shell

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `powershell -Version` |
| Show help | `powershell -Help` |
| List commands | `Get-Command` |
| Get info | `Get-Help command` |
| List modules | `Get-Module -ListAvailable` |
| Show env vars | `Get-ChildItem Env:` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `Remove-Item` | Deletes files |
| `Set-Content` | Writes files |
| `Invoke-Expression` | Executes code |
| `New-Item` | Creates files |
| `Stop-Process` | Terminates processes |

## Recommended Safe Usage

```powershell
# Safe powershell Inspection Script

# Show version
$PSVersionTable.PSVersion

# List commands
Get-Command | Select-Object -First 20 Name

# Show env vars
Get-ChildItem Env:
```
