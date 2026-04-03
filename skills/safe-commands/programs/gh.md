# gh (GitHub CLI)

**Platforms:** Multi-platform
**Category:** Version Control

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `gh --version` |
| Show help | `gh --help` |
| List repos | `gh repo list` |
| View repo | `gh repo view` |
| List issues | `gh issue list` |
| View issue | `gh issue view` |
| List PRs | `gh pr list` |
| View PR | `gh pr view` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `gh repo create` | Creates repository |
| `gh issue create` | Creates issue |
| `gh pr create` | Creates pull request |
| `gh pr merge` | Merges pull request |
| `gh repo delete` | Deletes repository |
| `gh issue close` | Closes issue |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe gh Inspection Script

# Show version
gh --version

# List repos
gh repo list

# View repo
gh repo view owner/repo

# List issues
gh issue list
```
