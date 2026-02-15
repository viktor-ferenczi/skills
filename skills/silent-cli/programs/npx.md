# npx

**Platforms:** Multi-platform  
**Category:** Package Runner (Node.js)

## Quick Reference

| Goal | Command |
|------|---------|
| Silent run | `npx -q package` |
| No install prompt | `npx --yes package` |

## Command-Line Flags

```bash
npx -q package                       # Quiet
npx --quiet package                  # Quiet
npx --yes package                    # Auto-install (no prompt)
npx -y package                       # Short for --yes
npx --no-install package             # Don't install, error if missing (no prompt)
```
- `-q` or `--quiet`: Quiet (suppressed npm output)
- `-y` or `--yes`: Auto-install if missing (avoids interactive prompt)
- `--no-install`: Don't install, error if missing (avoids interactive prompt)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Auto-install and run
npx -y --quiet create-react-app my-app

# Run local package (no install prompt)
npx --no-install eslint .
```
