# git

**Platforms:** Multi-platform
**Category:** Version Control

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Check repository status | `git status` |
| View commit history | `git log --oneline -20` |
| Show commit details | `git show <commit>` |
| View file changes | `git diff` |
| List branches | `git branch -a` |
| View remote URLs | `git remote -v` |
| Inspect tree objects | `git ls-tree HEAD` |
| Show file content | `git show HEAD:filename` |
| Check tags | `git tag -l` |
| Repository info | `git rev-parse --show-toplevel` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `git commit` | Creates new commits |
| `git push` | Modifies remote repository |
| `git merge` | Modifies branch history |
| `git rebase` | Rewrites commit history |
| `git reset --hard` | Destroys uncommitted changes |
| `git clean` | Deletes untracked files |
| `git branch -D` | Deletes branches |
| `git tag -d` | Deletes tags |

## Environment Variables for Safe Operation

| Variable | Value | Description |
|----------|-------|-------------|
| `GIT_TERMINAL_PROMPT` | `0` | Disable auth/credential prompts |
| `GIT_ASKPASS` | `echo` | Disable password prompts |
| `GIT_SSH_COMMAND` | `ssh -o BatchMode=yes` | Non-interactive SSH |

## Command-Line Flags

- `-q` or `--quiet`: Suppress progress output
- `--porcelain`: Machine-readable output (status)
- `--no-pager`: Disable pager (prevents waiting for input)
- `--diff --quiet`: Exit code only (0 = no changes, 1 = changes)

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe Git Inspection Script

export GIT_TERMINAL_PROMPT=0
export GIT_PAGER=cat

# Repository inspection only - no modifications
echo "=== Repository Status ==="
git status --short

echo "=== Recent Commits ==="
git log --oneline -10

echo "=== Branch Information ==="
git branch -a

echo "=== Remote Configuration ==="
git remote -v

echo "=== Current Commit ==="
git rev-parse HEAD
```
