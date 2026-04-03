# npx

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `npx --version` |
| Show help | `npx --help` |
| Run package | `npx package --help` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `npx package` | Executes packages |
| Any npx execution | Runs external code |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe npx Inspection Script

# Show version
npx --version

# Show help for package
npx eslint --help
```
