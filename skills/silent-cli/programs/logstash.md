# logstash

**Platforms:** Multi-platform  
**Category:** Log Processing

## Quick Reference

| Goal | Command |
|------|---------|
| Run | `logstash -f config.conf` |
| Config test | `logstash -t -f config.conf` |
| Auto-reload | `logstash -f config.conf --config.reload.automatic` |

## Command-Line Flags

```bash
logstash -f config.conf              # Run with config
logstash -f /etc/logstash/conf.d/    # Config directory
logstash -t -f config.conf           # Config test only
logstash -f config.conf --config.test_and_exit
logstash -f config.conf --config.reload.automatic
logstash -e 'input { stdin {} } output { stdout {} }'  # Inline config
logstash --modules netflow           # Run module
logstash --setup --modules netflow   # Setup and run module
logstash -f config.conf --log.level info
logstash -f config.conf --log.level warn
logstash -f config.conf --log.level error
logstash -f config.conf --quiet
logstash -f config.conf -w 4         # 4 worker threads
logstash -f config.conf --pipeline.batch.size 125
logstash -f config.conf --pipeline.batch.delay 50
logstash --path.settings /etc/logstash
```
- `-f` or `--path.config`: Config file/directory
- `-t` or `--config.test_and_exit`: Test config
- `-e` or `--config.string`: Inline config
- `--config.reload.automatic`: Auto-reload
- `--modules`: Enable module
- `--setup`: Setup module
- `--log.level`: Log level (fatal, error, warn, info, debug, trace)
- `--quiet`: Quiet
- `-w` or `--pipeline.workers`: Worker threads
- `--pipeline.batch.size`: Batch size
- `--pipeline.batch.delay`: Batch delay
- `--path.settings`: Settings directory

## Recommended Unattended Usage

```bash
#!/bin/bash

# Validate config first
logstash -t -f /etc/logstash/conf.d/ || exit 1

# Run with auto-reload and minimal logging
logstash -f /etc/logstash/conf.d/     --config.reload.automatic     --log.level warn     --quiet
```
