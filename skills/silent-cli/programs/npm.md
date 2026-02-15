# npm

**Platforms:** Multi-platform  
**Category:** Package Manager (Node.js)

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `npm install -q` |
| No progress | `npm install --no-progress` |
| Production | `npm ci --omit=dev` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `npm_config_loglevel` | `error` | Log level |
| `npm_config_progress` | `false` | Disable progress |
| `npm_config_color` | `false` | Disable color |
| `CI` | `true` | CI mode |

## Command-Line Flags

```bash
npm install -q                       # Quiet
npm install --quiet                  # Quiet
npm install --silent                 # Silent
npm install --no-progress            # No progress bar
npm ci                               # Clean install from lock
npm ci --omit=dev                    # Prod deps only
npm ci --silent                      # Silent CI
npm install -g --silent package      # Global install
npm run build -q                     # Quiet run
npm test -q                          # Quiet test
npm outdated -q                      # Quiet outdated
npm audit --audit-level moderate     # Audit
```
- `-q` or `--quiet`: Quiet
- `--silent`: Silent
- `--no-progress`: No progress bar
- `--loglevel`: error, warn, info, verbose, silly
- `--color false`: No colors
- `--omit=dev`: Production deps only (replaces deprecated --only=production)
- `--no-optional`: Skip optional deps

## Recommended Unattended Usage

```bash
#!/bin/bash

export CI=true
export npm_config_loglevel=error
export npm_config_progress=false

npm ci --omit=dev
npm run build --silent
```
