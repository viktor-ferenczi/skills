# yarn

**Platforms:** Multi-platform  
**Category:** Package Manager (Node.js)

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `yarn install --silent` |
| No progress | `yarn install --no-progress` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `CI` | `true` | CI mode (reduces output, disables interactive prompts) |

## Command-Line Flags

- `--silent`: Silent mode (suppress all output)
- `--no-progress`: Disable progress bar
- `--frozen-lockfile`: Fail if lockfile needs update (avoids interactive prompts)
- `--non-interactive`: Disable interactive prompts

## Recommended Unattended Usage

```bash
#!/bin/bash

export CI=true

yarn install --frozen-lockfile --silent
yarn build --silent
```
