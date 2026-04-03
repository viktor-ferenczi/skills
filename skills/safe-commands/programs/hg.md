# hg (Mercurial)

**Platforms:** Multi-platform
**Category:** Version Control

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `hg --version` |
| Show help | `hg help` |
| Show status | `hg status` |
| Show log | `hg log -l 10` |
| Show branches | `hg branches` |
| Show paths | `hg paths` |
| Show config | `hg showconfig` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `hg commit` | Creates commits |
| `hg push` | Pushes to remote |
| `hg merge` | Merges branches |
| `hg rollback` | Rolls back repo |
| `hg strip` | Removes changesets |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe hg Inspection Script

# Show status
hg status

# Show log
hg log -l 10

# Show branches
hg branches
```
