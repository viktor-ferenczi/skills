# gh (GitHub CLI)

**Platforms:** Multi-platform  
**Category:** GitHub Integration

## Quick Reference

| Goal | Command |
|------|---------|
| Silent | `gh pr list --json number,title` |
| JSON output | `gh repo view --json name,url` |
| Quiet | `GH_TOKEN=token gh repo clone owner/repo` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `GH_TOKEN` | `ghp_xxx` | GitHub token |
| `GH_HOST` | `github.com` | GitHub host |
| `GH_REPO` | `owner/repo` | Default repo |

## Command-Line Flags

```bash
gh auth login --with-token < token.txt
gh repo clone owner/repo -- --quiet
gh pr list --json number,title       # JSON output
gh pr merge 123 --squash --auto
gh release create v1.0.0 --generate-notes
gh workflow run workflow.yml -f key=value
gh run list --json databaseId,status
```
- `--json`: JSON output fields (use for machine-readable output)
- `--jq`: Filter with jq
- `-R` or `--repo`: Repository

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
