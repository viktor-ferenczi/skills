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
| `SVN_SSH` | `ssh -o BatchMode=yes` | SSH command |

## Command-Line Flags

```bash
svn checkout -q repo                 # Quiet checkout
svn checkout -q --non-interactive repo
svn update -q                        # Quiet update
svn commit -q -m "message"           # Quiet commit
svn status -q                        # Quiet status
svn export -q repo dir               # Export (no .svn)
svn info --show-item revision        # Get revision number
```
- `-q` or `--quiet`: Quiet
- `--non-interactive`: No interactive prompts
- `--no-auth-cache`: Don't cache auth
- `--username`: Username
- `--password`: Password
- `--trust-server-cert`: Trust server cert (**security-sensitive** - skips TLS verification in non-interactive mode, confirm with human operator before using)
