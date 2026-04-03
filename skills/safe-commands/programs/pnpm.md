# pnpm

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `pnpm --version` |
| Show help | `pnpm --help` |
| List packages | `pnpm ls` |
| Show config | `pnpm config list` |
| Search packages | `pnpm search name` |
| Show package info | `pnpm view package` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `pnpm install` | Installs packages |
| `pnpm update` | Updates packages |
| `pnpm remove` | Removes packages |
| `pnpm publish` | Publishes package |
| `pnpm init` | Initializes project |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe pnpm Inspection Script

# Show version
pnpm --version

# List packages
pnpm ls --depth 0

# Show config
pnpm config list
```
