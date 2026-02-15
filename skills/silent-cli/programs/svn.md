# svn

**Platforms:** Multi-platform  
**Category:** Version Control

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet checkout | `svn checkout -q repo` |
| Non-interactive | `svn --non-interactive update` |
| Quiet update | `svn update -q` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `SVN_SSH` | `ssh -o BatchMode=yes` | SSH command for non-interactive SSH transport |

## Command-Line Flags

- `-q` or `--quiet`: Quiet — suppress normal output
- `--non-interactive`: No interactive prompts — fail instead of prompting for credentials
- `--no-auth-cache`: Don't cache authentication credentials
- `--trust-server-cert`: Trust server cert (**security-sensitive** — skips TLS verification in non-interactive mode, confirm with human operator before using)
