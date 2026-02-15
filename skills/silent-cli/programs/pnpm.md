# pnpm

**Platforms:** Multi-platform  
**Category:** Package Manager (Node.js)

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `pnpm install --silent` |
| No progress | `pnpm install --reporter=silent` |
| Frozen lockfile | `pnpm install --frozen-lockfile` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `CI` | `true` | CI mode |
| `npm_config_loglevel` | `silent` | Silent mode (pnpm respects npm config) |

## Command-Line Flags

```bash
pnpm install --silent                # Silent
pnpm install --reporter=silent       # Silent reporter
pnpm install --frozen-lockfile       # Fail if lock updates
pnpm install --production            # Prod deps only
pnpm add --silent package            # Add silently
pnpm remove --silent package         # Remove silently
pnpm run --silent build              # Run silently
pnpm build --silent                  # Shorthand
```
- `--silent`: Silent
- `--reporter=silent|default|append-only`: Output reporter
- `--frozen-lockfile`: Fail on lockfile changes
- `--production`: Production deps only
- `--offline`: Offline mode
- `--prefer-offline`: Prefer offline cache
- `--strict-peer-dependencies`: Strict peers

## Recommended Unattended Usage

```bash
#!/bin/bash

export CI=true

pnpm install --frozen-lockfile --silent
pnpm build --silent
```
