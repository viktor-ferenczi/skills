# ssh / scp / sftp

**Platforms:** Multi-platform  
**Category:** Remote Access

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive | `ssh -o BatchMode=yes host` |
| Execute command | `ssh host 'command'` |
| Quiet | `ssh -q host` |
| Copy file | `scp -q file host:/path` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `SSH_AUTH_SOCK` | `/path` | SSH agent socket |

## SSH Command-Line Flags

```bash
ssh -o BatchMode=yes host            # Non-interactive
ssh -o StrictHostKeyChecking=accept-new host # Auto-accept new host keys
# WARNING: StrictHostKeyChecking changes are security-sensitive.
# Confirm with the human operator before using =accept-new or =no.
ssh -o ConnectTimeout=10 host        # 10s timeout
ssh -q host                          # Quiet
ssh -n host command                  # Redirect stdin
ssh -f host command                  # Background
ssh -T host                          # Disable pseudo-tty
ssh -i keyfile host                  # Use specific key
```

## SCP Command-Line Flags

```bash
scp -q file host:/path               # Quiet copy
scp -r dir host:/path                # Recursive
scp -P 2222 file host:/path          # Custom port
scp -i keyfile file host:/path       # Use key
scp -o BatchMode=yes file host:/path # Non-interactive
scp -C file host:/path               # Compress
```

## SFTP Command-Line Flags

```bash
echo 'put file' | sftp -b - host     # Batch mode
sftp -b batchfile host               # Batch from file
sftp -o BatchMode=yes host           # Non-interactive
```

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
