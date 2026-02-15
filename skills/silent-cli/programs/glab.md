# glab (GitLab CLI)

**Platforms:** Multi-platform  
**Category:** GitLab Integration

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive auth | `glab auth login --token TOKEN --hostname gitlab.com` |
| Machine-readable output | `glab mr list --output json` |
| Auto-confirm merge | `glab mr merge 123 --squash --yes` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `GITLAB_TOKEN` | `glpat-xxx` | GitLab token (avoids interactive login prompt) |

## Command-Line Flags

- `--output`: Output format (`json`, `yaml`, `table`) — use `json` for machine-readable output
- `--yes`: Auto-confirm operations (e.g., merge) without prompting
