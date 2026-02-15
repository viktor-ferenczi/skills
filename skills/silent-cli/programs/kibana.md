# kibana (CLI)

**Platforms:** Multi-platform  
**Category:** Data Visualization

## Quick Reference

| Goal | Command |
|------|---------|
| Silent logging | `kibana --logging.silent` |
| Quiet logging | `kibana --logging.quiet` |

## Command-Line Flags

- `--logging.silent`: Suppress all logging output
- `--logging.quiet`: Quiet logging (errors only)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Validate config before starting
kibana --configtest || exit 1

# Start with explicit ES connection
kibana --elasticsearch.hosts http://elasticsearch:9200 --logging.quiet
```
