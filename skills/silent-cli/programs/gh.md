# gh (GitHub CLI)

**Platforms:** Multi-platform  
**Category:** GitHub Integration

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive auth | `gh auth login --with-token < token.txt` |
| Machine-readable output | `gh pr list --json number,title` |
| Quiet clone | `gh repo clone owner/repo -- --quiet` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `GH_TOKEN` | `ghp_xxx` | GitHub token (avoids interactive login prompt) |
| `GH_PROMPT_DISABLED` | `1` | Disable interactive prompts |

## Command-Line Flags

- `--json`: Machine-readable JSON output (specify fields)
- `--jq`: Filter JSON output with jq expressions

## Recommended Unattended Usage

```bash
#!/bin/bash

export GH_TOKEN="ghp_xxx"

# Clone repository
gh repo clone owner/repo -- --quiet

# Create PR
gh pr create --title "Fix bug" --body "Description" --base main

# Merge PR
gh pr merge 123 --squash --auto --delete-branch
```
