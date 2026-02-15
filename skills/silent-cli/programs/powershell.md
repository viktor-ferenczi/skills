# PowerShell

**Platforms:** Windows, Linux, macOS  
**Category:** Shell/Scripting

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive | `powershell -NonInteractive -Command '...'` |
| Silent | `powershell -WindowStyle Hidden -Command '...'` |
| No profile | `powershell -NoProfile -Command '...'` |

## Preference Variables (set inside scripts, not OS env vars)

| Variable | Value | Description |
|----------|-------|-------------|
| `$ProgressPreference` | `SilentlyContinue` | Disable progress bars |
| `$ErrorActionPreference` | `Stop` | Fail on errors |
| `$ConfirmPreference` | `None` | Auto-confirm |

## Command-Line Flags

```powershell
powershell -NonInteractive -Command "..."       # Non-interactive
powershell -WindowStyle Hidden -Command "..."   # Hidden window
powershell -NoProfile -Command "..."            # Skip profile
powershell -NoLogo -Command "..."               # Hide copyright banner
powershell -ExecutionPolicy Bypass -File script.ps1  # Bypass execution policy
```
- `-NonInteractive`: Non-interactive
- `-WindowStyle Hidden`: Hide window
- `-NoProfile`: Don't load profile
- `-NoLogo`: Hide copyright banner
- `-ExecutionPolicy`: Set execution policy (Bypass for unattended)

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
