# hg (Mercurial)

**Platforms:** Multi-platform  
**Category:** Version Control

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet clone | `hg clone -q repo` |
| Non-interactive | `hg --noninteractive update` |

## Command-Line Flags

- `-q` or `--quiet`: Quiet output
- `--noninteractive`: Non-interactive mode (no prompts)
- `-y` or `--noninteractive`: Always answer yes to prompts

## Recommended Unattended Usage

```bash
#!/bin/bash

# Clone and update quietly, non-interactively
hg clone -q --noninteractive repo
hg update -q --noninteractive
hg commit -q -m "message"
hg push -q --noninteractive
```
