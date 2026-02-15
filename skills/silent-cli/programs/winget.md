# winget

**Platforms:** Windows 10/11  
**Category:** Package Manager

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `winget install --id Package.Id --silent` |
| No prompts | `winget install --id Package.Id --disable-interactivity` |
| Accept terms | `winget install --accept-package-agreements` |

## Command-Line Flags

- `--silent`: Silent install (no UI)
- `--accept-package-agreements`: Accept license automatically
- `--accept-source-agreements`: Accept source agreements automatically
- `--disable-interactivity`: No interactive prompts

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
