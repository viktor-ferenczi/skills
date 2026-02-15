# npm

**Platforms:** Multi-platform  
**Category:** Package Manager (Node.js)

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `npm install -q` |
| No progress | `npm install --no-progress` |
| CI mode | `npm ci --omit=dev` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `npm_config_loglevel` | `error` | Log level |
| `npm_config_progress` | `false` | Disable progress |
| `npm_config_color` | `false` | Disable color |
| `CI` | `true` | CI mode (disables interactive prompts) |

## Command-Line Flags

```bash
npm install -q                       # Quiet
npm install --quiet                  # Quiet
npm install --silent                 # Silent
npm install --no-progress            # No progress bar
npm ci                               # Clean install from lock (non-interactive)
npm ci --omit=dev                    # Prod deps only
npm ci --silent                      # Silent CI
```
- `-q` or `--quiet`: Quiet
- `--silent`: Silent
- `--no-progress`: No progress bar
- `--loglevel`: error, warn, info, verbose, silly
- `--color false`: No colors

## Recommended Unattended Usage

```bash
#!/bin/bash

export CI=true
export npm_config_loglevel=error
export npm_config_progress=false

npm ci --omit=dev
npm run build --silent
```
