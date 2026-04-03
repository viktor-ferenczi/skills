# yarn

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `yarn --version` |
| Show help | `yarn --help` |
| List packages | `yarn list` |
| Show config | `yarn config list` |
| Search packages | `yarn search name` |
| Show package info | `yarn info package` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `yarn install` | Installs packages |
| `yarn upgrade` | Updates packages |
| `yarn remove` | Removes packages |
| `yarn publish` | Publishes package |
| `yarn init` | Initializes project |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe yarn Inspection Script

# Show version
yarn --version

# List packages
yarn list --depth 0

# Show config
yarn config list
```
