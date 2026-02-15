# git

**Platforms:** Multi-platform  
**Category:** Version Control

## Quick Reference

| Goal | Command |
|------|---------|
| Silent clone | `git clone -q repo` |
| Quiet pull | `git pull -q` |
| Non-interactive (no prompts) | `GIT_TERMINAL_PROMPT=0 git clone repo` |
| Machine-readable status | `git status --porcelain` |
| Exit code only (diff) | `git diff --quiet` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `GIT_TERMINAL_PROMPT` | `0` | Disable auth/credential prompts |
| `GIT_ASKPASS` | `echo` | Disable password prompts |
| `GIT_SSH_COMMAND` | `ssh -o BatchMode=yes` | Non-interactive SSH (no password prompt) |

## Command-Line Flags

- `-q` or `--quiet`: Suppress progress and informational output (clone, pull, push, fetch, checkout)
- `--porcelain`: Machine-readable output (status)
- `--no-pager`: Disable pager (prevents waiting for user input)
- `--diff --quiet`: Exit code only (0 = no changes, 1 = changes)

## Recommended Unattended Usage

```bash
#!/bin/bash

export GIT_TERMINAL_PROMPT=0
export GIT_SSH_COMMAND='ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new'
# WARNING: StrictHostKeyChecking=accept-new auto-accepts unknown host keys.
# This is a security-sensitive setting. Confirm with the human operator before using.
# Use =yes (default) to reject unknown hosts, =accept-new to auto-accept only new hosts,
# or =no to disable all verification (NOT recommended - vulnerable to MITM attacks).

# Clone and checkout
git clone -q --depth 1 "$REPO_URL" "$DIR"
cd "$DIR"
git checkout -q "$BRANCH"

# Check if clean
if git diff --quiet; then
    echo "Working directory is clean"
fi

# Get commit hash
commit=$(git rev-parse --short HEAD)
```
