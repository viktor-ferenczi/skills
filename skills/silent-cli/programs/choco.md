# choco (Chocolatey)

**Platforms:** Windows  
**Category:** Package Manager

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `choco install -y package` |
| No progress | `choco install -y --no-progress package` |
| Reduced output | `choco install -y -r package` |

## Command-Line Flags

- `-y` or `--yes`: Auto-confirm all prompts
- `--no-progress`: Hide download progress bars
- `-r` or `--limit-output`: Reduced/machine-readable output (pipe-friendly)
- `--force`: Force reinstall without prompting

## Recommended Unattended Usage

```powershell
# Install silently with no progress
choco install -y --no-progress git vscode

# Check if installed (machine-readable)
if (choco list -lo -r | Select-String "^git\|") {
    "Git is installed"
}
```
