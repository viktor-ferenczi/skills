# git

**Platforms:** Multi-platform  
**Category:** Version Control

## Quick Reference

| Goal | Command |
|------|---------|
| Silent clone | `git clone -q repo` |
| Quiet pull | `git pull -q` |
| Non-interactive | `GIT_TERMINAL_PROMPT=0 git clone repo` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `GIT_TERMINAL_PROMPT` | `0` | Disable auth prompts |
| `GIT_ASKPASS` | `echo` | Disable password prompts |
| `GIT_SSH_COMMAND` | `ssh -o BatchMode=yes` | Non-interactive SSH |
| `GIT_TRACE` | `0` | Disable trace |
| `GIT_CONFIG_GLOBAL` | `/path` | Global config file |

## Command-Line Flags

```bash
git clone -q repo                    # Quiet clone
git clone --depth 1 -q repo          # Shallow, quiet
git pull -q                          # Quiet pull
git push -q                          # Quiet push
git fetch -q                         # Quiet fetch
git checkout -q branch               # Quiet checkout
git status -s                        # Short status
git diff --quiet                     # Exit code only
git diff --stat                      # Diff stats only
git log --oneline                    # One line per commit
git log --format='%H %s'             # Custom format
git ls-files                         # List tracked files
git rev-parse --short HEAD           # Current commit hash
```
- `-q` or `--quiet`: Quiet
- `-s` or `--short`: Short output (status)
- `--quiet`: Suppress output
- `--porcelain`: Machine-readable output
- `--no-pager`: No pager

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
