# npm

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `npm --version` |
| Show help | `npm --help` |
| List packages | `npm ls` |
| Show config | `npm config list` |
| Search packages | `npm search name` |
| Show package info | `npm view package` |
| Show outdated | `npm outdated` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `npm install` | Installs packages |
| `npm update` | Updates packages |
| `npm uninstall` | Removes packages |
| `npm publish` | Publishes package |
| `npm init` | Initializes project |
| `npm config set` | Modifies config |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe npm Inspection Script

# Show version
npm --version

# List packages
npm ls --depth 0

# Show config
npm config list

# Show package info
npm view express
```
