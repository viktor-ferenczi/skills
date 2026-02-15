# yarn

**Platforms:** Multi-platform  
**Category:** Package Manager (Node.js)

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `yarn install --silent` |
| No progress | `yarn install --no-progress` |
| Production | `yarn install --production` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `CI` | `true` | CI mode (reduces output) |

## Command-Line Flags

```bash
yarn install --silent                # Silent
yarn install --no-progress           # No progress
yarn install --production            # Prod deps only
yarn add --silent package            # Add silently
yarn remove --silent package         # Remove silently
yarn run --silent build              # Run silently
yarn test --silent                   # Test silently
yarn global add --silent package     # Global install
yarn upgrade --silent                # Upgrade silently
```
- `--silent`: Silent
- `--no-progress`: No progress
- `--production`: Production deps only
- `--frozen-lockfile`: Fail if lockfile needs update
- `--ignore-engines`: Ignore engine checks
- `--offline`: Offline mode
- `--check-files`: Verify file integrity

## Recommended Unattended Usage

```bash
#!/bin/bash

export CI=true

yarn install --frozen-lockfile --silent
yarn build --silent
```
