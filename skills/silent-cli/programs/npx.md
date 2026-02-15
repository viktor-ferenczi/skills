# npx

**Platforms:** Multi-platform  
**Category:** Package Runner (Node.js)

## Quick Reference

| Goal | Command |
|------|---------|
| Silent run | `npx -q package` |
| No install prompt | `npx --yes package` |
| Use local | `npx -p package command` |

## Command-Line Flags

```bash
npx -q package                       # Quiet
npx --quiet package                  # Quiet
npx --yes package                    # Auto-install
npx -y package                       # Short for --yes
npx --no-install package             # Don't install
npx -p package@version command       # Use specific version
npx --package=package command        # Same
```
- `-q` or `--quiet`: Quiet (suppressed npm output)
- `-y` or `--yes`: Auto-install if missing
- `--no-install`: Don't install, error if missing
- `-p` or `--package`: Package to use
- `-c` or `--call`: Shell script

## Recommended Unattended Usage

```bash
#!/bin/bash

# Auto-install and run
npx -y --quiet create-react-app my-app

# Use specific version
npx -p typescript@4.9 tsc --version

# Run local package
npx --no-install eslint .
```
