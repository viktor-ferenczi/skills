# winget

**Platforms:** Windows 10/11  
**Category:** Package Manager

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `winget install --id Package.Id --silent` |
| No progress | `winget install --id Package.Id --disable-interactivity` |
| Accept terms | `winget install --accept-package-agreements` |

## Command-Line Flags

```powershell
winget install --id Git.Git --silent --accept-package-agreements
winget install --id Microsoft.VisualStudioCode --silent --accept-source-agreements
winget upgrade --all --silent --accept-package-agreements
winget list --source winget
winget export -o packages.json
winget import -i packages.json --accept-package-agreements
```
- `--silent`: Silent install
- `--accept-package-agreements`: Accept license
- `--accept-source-agreements`: Accept source agreements
- `--disable-interactivity`: No interactive prompts
- `--id`: Use package ID
- `--exact` or `-e`: Exact match
- `--source`: Source (winget, msstore)
- `--scope`: Scope (user, machine)
- `--location`: Install location
- `--override`: Override arguments

## Recommended Unattended Usage

```powershell
# Install with all confirmations
winget install --id Git.Git `
    --silent `
    --accept-package-agreements `
    --accept-source-agreements

# Upgrade all
winget upgrade --all --silent --accept-package-agreements
```
