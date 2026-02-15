# ssh / scp / sftp

**Platforms:** Multi-platform  
**Category:** Remote Access

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive SSH | `ssh -o BatchMode=yes host` |
| Quiet SSH | `ssh -q host` |
| Quiet copy | `scp -q file host:/path` |
| SFTP batch mode | `sftp -b batchfile host` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `SSH_AUTH_SOCK` | `/path` | SSH agent socket (avoids key passphrase prompts) |

## SSH Command-Line Flags

```bash
ssh -o BatchMode=yes host            # Non-interactive (fail instead of prompt)
ssh -o StrictHostKeyChecking=accept-new host # Auto-accept new host keys
# WARNING: StrictHostKeyChecking changes are security-sensitive.
# Confirm with the human operator before using =accept-new or =no.
ssh -o ConnectTimeout=10 host        # 10s timeout
ssh -q host                          # Quiet
ssh -n host command                  # Redirect stdin from /dev/null
ssh -T host                          # Disable pseudo-tty
```
- `-o BatchMode=yes`: Non-interactive — fail on password prompts instead of asking
- `-q`: Quiet — suppress warnings and diagnostic messages
- `-n`: Redirect stdin from /dev/null — prevents reading from stdin
- `-T`: Disable pseudo-tty allocation
- `-o StrictHostKeyChecking=accept-new`: Auto-accept new host keys (**security-sensitive**)
- `-o ConnectTimeout=N`: Connection timeout

## SCP Command-Line Flags

- `-q`: Quiet — disable progress meter
- `-o BatchMode=yes`: Non-interactive

## SFTP Command-Line Flags

```bash
echo 'put file' | sftp -b - host     # Batch mode from stdin
sftp -b batchfile host               # Batch from file
sftp -o BatchMode=yes host           # Non-interactive
```
- `-b`: Batch mode — read commands from file (use `-` for stdin)
- `-o BatchMode=yes`: Non-interactive

## Recommended Unattended Usage

```bash
#!/bin/bash

SSH_OPTS="-o BatchMode=yes -o StrictHostKeyChecking=accept-new -o ConnectTimeout=10"
# WARNING: StrictHostKeyChecking=accept-new auto-accepts unknown host keys.
# This is a security-sensitive setting. Confirm with the human operator before using.
# Use =yes (default) to reject unknown hosts, =accept-new to auto-accept only new hosts,
# or =no to disable all verification (NOT recommended - vulnerable to MITM attacks).

# Execute remote command
ssh $SSH_OPTS user@host 'hostname'

# Copy files
scp $SSH_OPTS -q file user@host:/path

# With specific key
ssh -i /path/to/key -o BatchMode=yes user@host
```
