# rsync

**Platforms:** Multi-platform  
**Category:** File Transfer

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet sync | `rsync -aq source/ dest/` |
| Quiet over SSH | `rsync -aq -e 'ssh -o BatchMode=yes' source/ user@host:/dest/` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `RSYNC_RSH` | `ssh -o BatchMode=yes` | Remote shell (non-interactive SSH) |

## Command-Line Flags

- `-q` or `--quiet`: Quiet — suppress non-error messages

## Recommended Unattended Usage

```bash
#!/bin/bash

rsync -aq --delete --exclude='.git' \
    -e 'ssh -o BatchMode=yes -o StrictHostKeyChecking=accept-new' \
    ./source/ user@host:/dest/
# WARNING: StrictHostKeyChecking=accept-new auto-accepts unknown host keys.
# This is a security-sensitive setting. Confirm with the human operator before using.
# Use =yes (default) to reject unknown hosts, =accept-new to auto-accept only new hosts,
# or =no to disable all verification (NOT recommended - vulnerable to MITM attacks).
```
