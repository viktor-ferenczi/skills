# pnpm

**Platforms:** Multi-platform  
**Category:** Package Manager (Node.js)

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `pnpm install --silent` |
| Silent reporter | `pnpm install --reporter=silent` |
| Frozen lockfile | `pnpm install --frozen-lockfile` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `CI` | `true` | CI mode (disables interactive prompts) |
| `npm_config_loglevel` | `silent` | Silent mode (pnpm respects npm config) |

## Command-Line Flags

```bash
pnpm install --silent                # Silent
pnpm install --reporter=silent       # Silent reporter
pnpm install --frozen-lockfile       # Fail if lock updates (CI-safe)
pnpm run --silent build              # Run silently
```
- `--silent`: Silent
- `--reporter=silent|default|append-only`: Output reporter
- `--frozen-lockfile`: Fail on lockfile changes (non-interactive safe)

## Recommended Unattended Usage

```bash
#!/bin/bash

export CI=true

pnpm install --frozen-lockfile --silent
pnpm build --silent
```
