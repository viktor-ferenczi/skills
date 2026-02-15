# rabbitmqadmin

**Platforms:** Multi-platform  
**Category:** Message Queue (RabbitMQ)

## Quick Reference

| Goal | Command |
|------|---------|
| JSON output | `rabbitmqadmin --format=json list queues` |
| TSV output | `rabbitmqadmin --format=tsv list queues` |
| Dry run | `rabbitmqadmin --dry-run declare queue name=myqueue` |

## Command-Line Flags

- `--format`: Output format (json, tsv, table) — machine-readable output
- `--dry-run`: Don't execute (safe preview)

## Recommended Unattended Usage

```bash
#!/bin/bash

# JSON output for scripting
queues=$(rabbitmqadmin --format=json --host localhost --username admin --password secret list queues)

# Publish message
rabbitmqadmin publish exchange=amq.default routing_key=tasks payload='{"task":"process"}'
```
