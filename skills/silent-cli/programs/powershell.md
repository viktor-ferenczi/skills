# PowerShell

**Platforms:** Windows, Linux, macOS  
**Category:** Shell/Scripting

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive | `powershell -Command 'script'` |
| Silent | `powershell -WindowStyle Hidden -Command '...'` |
| File execution | `powershell -File script.ps1` |

## Preference Variables (set inside scripts, not OS env vars)

| Variable | Value | Description |
|----------|-------|-------------|
| `$ProgressPreference` | `SilentlyContinue` | Disable progress bars |
| `$ErrorActionPreference` | `Stop` | Fail on errors |
| `$ConfirmPreference` | `None` | Auto-confirm |

## Command-Line Flags

```powershell
powershell -Command "Get-Process"               # Execute command
powershell -File script.ps1                     # Execute script
powershell -WindowStyle Hidden -Command "..."   # Hidden window
powershell -NoProfile -Command "..."            # Skip profile
powershell -NonInteractive -Command "..."       # Non-interactive
powershell -ExecutionPolicy Bypass -File script.ps1
```
- `-Command`: Execute command
- `-File`: Execute script file
- `-WindowStyle Hidden`: Hide window
- `-NoProfile`: Don't load profile
- `-NonInteractive`: Non-interactive
- `-ExecutionPolicy`: Set execution policy
- `-NoLogo`: Hide copyright banner

## Recommended Unattended Usage

```powershell
# In script, suppress progress
$ProgressPreference = 'SilentlyContinue'
$ErrorActionPreference = 'Stop'

# Invoke command remotely
Invoke-Command -ComputerName server -ScriptBlock { command } -ErrorAction Stop

# Silent install
Start-Process msiexec -ArgumentList '/quiet','/i','package.msi' -Wait
```
