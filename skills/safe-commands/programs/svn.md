# svn (Subversion)

**Platforms:** Multi-platform
**Category:** Version Control

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `svn --version` |
| Show help | `svn help` |
| Show status | `svn status` |
| Show log | `svn log -l 10` |
| Show info | `svn info` |
| List repo | `svn list URL` |
| Show diff | `svn diff` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `svn commit` | Commits changes |
| `svn add` | Adds files |
| `svn delete` | Deletes files |
| `svn copy` | Copies files |
| `svn move` | Moves files |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe svn Inspection Script

# Show status
svn status

# Show log
svn log -l 10

# List repository
svn list https://svn.example.com/repo
```
