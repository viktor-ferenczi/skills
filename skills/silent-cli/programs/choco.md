# choco (Chocolatey)

**Platforms:** Windows  
**Category:** Package Manager

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `choco install -y package` |
| No progress | `choco install -y --no-progress package` |
| Quiet | `choco install -y -r package` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `ChocolateyInstall` | `C:\ProgramData\chocolatey` | Install path |
| `ChocolateyToolsLocation` | `C:	ools` | Tools path |

## Command-Line Flags

```powershell
choco install -y package             # Auto-confirm
choco install -y --no-progress package  # No progress
choco install -y -r package          # Reduced output
choco install -y --force package     # Force reinstall
choco upgrade -y all                 # Upgrade all
choco uninstall -y package           # Uninstall
choco list -lo -r                    # List local, reduced
choco outdated -r                    # Outdated packages
```
- `-y` or `--yes`: Auto-confirm
- `--no-progress`: Hide download progress
- `-r` or `--limit-output`: Reduced output
- `--force`: Force reinstall
- `--ignore-dependencies`: Skip dependencies
- `--skip-autouninstaller`: Skip auto-uninstall
- `--version=VERSION`: Specific version

## Recommended Unattended Usage

```powershell
# Set preferences
$env:ChocolateyInstall = 'C:\ProgramData\chocolatey'

# Install silently
choco install -y --no-progress git vscode

# Check if installed
if (choco list -lo -r | Select-String "^git\|") {
    "Git is installed"
}
```
