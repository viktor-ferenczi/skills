# hg (Mercurial)

**Platforms:** Multi-platform  
**Category:** Version Control

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet clone | `hg clone -q repo` |
| Non-interactive | `hg --noninteractive update` |
| Quiet commit | `hg commit -q -m "msg"` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `HGENCODING` | `UTF-8` | Encoding |

## Command-Line Flags

```bash
hg clone -q repo                     # Quiet clone
hg update -q                         # Quiet update
hg commit -q -m "message"            # Quiet commit
hg push -q                           # Quiet push
hg pull -q                           # Quiet pull
hg status                            # Status
hg id -i                             # Get changeset ID
hg log -r . --template '{node|short}' # Current revision
```
- `-q` or `--quiet`: Quiet
- `--noninteractive`: Non-interactive mode
- `-y` or `--noninteractive`: Always yes
- `-v` or `--verbose`: Verbose
