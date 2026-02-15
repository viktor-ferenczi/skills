# influx (InfluxDB CLI)

**Platforms:** Multi-platform  
**Category:** Time Series Database

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive query | `influx bucket list --json` |
| Non-interactive setup | `influx setup --username admin --password pass --org org --bucket default --force` |

## Command-Line Flags

- `--json`: JSON output (machine-readable)
- `--force`: Force setup without interactive prompts

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive setup (avoids all prompts)
influx setup --username admin --password pass --org myorg --bucket default --force

# Machine-readable output
influx bucket list --json
```
