# rabbitmqctl

**Platforms:** Multi-platform  
**Category:** Message Queue (RabbitMQ)

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet mode | `rabbitmqctl -q list_queues` |

## Command-Line Flags

- `-q`: Quiet — suppresses informational messages, outputs only data

## Recommended Unattended Usage

```bash
#!/bin/bash

# Quiet status check
rabbitmqctl -q status > /dev/null 2>&1 && echo "Running" || echo "Not running"

# List queue depths
rabbitmqctl -q list_queues name messages_ready messages_unacknowledged
```
