# kibana (CLI)

**Platforms:** Multi-platform  
**Category:** Data Visualization

## Quick Reference

| Goal | Command |
|------|---------|
| Start | `kibana` |
| Config test | `kibana --configtest` |
| Optimize | `kibana --optimize` |

## Command-Line Flags

```bash
kibana                               # Start Kibana
kibana --configtest                  # Validate config
kibana --config /path/to/kibana.yml  # Custom config
kibana --dev                         # Development mode
kibana --no-optimize                 # Skip optimization
kibana --optimize                    # Force optimization
kibana --elasticsearch.hosts http://es:9200
kibana --server.host 0.0.0.0
kibana --server.port 5601
kibana --logging.verbose             # Verbose logging
kibana --logging.silent              # Silent logging
kibana --logging.quiet               # Quiet logging
```
- `--configtest`: Validate configuration
- `--config`: Config file path
- `--dev`: Development mode
- `--optimize`: Force optimization
- `--no-optimize`: Skip optimization
- `--elasticsearch.hosts`: ES hosts
- `--server.host`: Server host
- `--server.port`: Server port
- `--logging.verbose/silent/quiet`: Logging control

## Recommended Unattended Usage

```bash
#!/bin/bash

# Validate config before starting
kibana --configtest || exit 1

# Start with explicit ES connection
kibana --elasticsearch.hosts http://elasticsearch:9200 --logging.quiet
```
