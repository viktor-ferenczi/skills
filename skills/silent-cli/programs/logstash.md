# logstash

**Platforms:** Multi-platform  
**Category:** Log Processing

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet mode | `logstash -f config.conf --quiet` |
| Config test | `logstash -t -f config.conf` |

## Command-Line Flags

- `--quiet`: Quiet mode (suppress non-error output)
- `--log.level`: Log level (`fatal`, `error`, `warn`, `info`, `debug`, `trace`) — use `warn` or `error` for silent operation
- `-t` or `--config.test_and_exit`: Test config and exit (non-interactive validation)
- `--config.reload.automatic`: Auto-reload config changes (no manual restart needed)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Validate config first
logstash -t -f /etc/logstash/conf.d/ || exit 1

# Run with auto-reload and minimal logging
logstash -f /etc/logstash/conf.d/ \
    --config.reload.automatic \
    --log.level warn \
    --quiet
```
