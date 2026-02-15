# glab (GitLab CLI)

**Platforms:** Multi-platform  
**Category:** GitLab Integration

## Quick Reference

| Goal | Command |
|------|---------|
| Silent | `glab mr list --output json` |
| JSON output | `glab repo view --output json` |
| Quiet | `GITLAB_TOKEN=token glab mr create` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `GITLAB_TOKEN` | `glpat-xxx` | GitLab token |
| `GITLAB_HOST` | `gitlab.com` | GitLab host |
| `GITLAB_REPO` | `owner/repo` | Default repo |

## Command-Line Flags

```bash
glab auth login --token TOKEN --hostname gitlab.com
glab repo clone owner/repo
glab mr list --output json           # JSON output
glab mr create --title "Fix" --description "Desc"
glab mr merge 123 --squash --yes
```
- `--output`: Output format (json, yaml, table)
- `-R` or `--repo`: Repository
- `-g` or `--group`: Group
