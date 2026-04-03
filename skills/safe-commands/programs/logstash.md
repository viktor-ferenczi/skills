# logstash

**Platforms:** Multi-platform
**Category:** Log Processing

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `logstash --version` |
| Show help | `logstash --help` |
| Validate config | `logstash --config.test_and_exit` |
| Show plugins | `logstash-plugin list` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `logstash -f config` | Runs logstash (processes data) |
| Any logstash execution | Processes and forwards logs |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe logstash Inspection Script

# Show version
logstash --version

# Validate config
logstash --config.test_and_exit -f logstash.conf
```
