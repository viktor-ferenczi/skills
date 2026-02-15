# rabbitmqadmin

**Platforms:** Multi-platform  
**Category:** Message Queue (RabbitMQ)

## Quick Reference

| Goal | Command |
|------|---------|
| List queues | `rabbitmqadmin list queues` |
| Publish | `rabbitmqadmin publish exchange=amq.default routing_key=myqueue payload='hello'` |
| Get message | `rabbitmqadmin get queue=myqueue` |

## Command-Line Flags

```bash
rabbitmqadmin list queues
rabbitmqadmin list queues name messages
rabbitmqadmin list exchanges
rabbitmqadmin list bindings
rabbitmqadmin declare queue name=myqueue
rabbitmqadmin declare exchange name=myexchange type=direct
rabbitmqadmin publish exchange=amq.default routing_key=myqueue payload='hello'
rabbitmqadmin get queue=myqueue
rabbitmqadmin get queue=myqueue count=10
rabbitmqadmin purge queue name=myqueue
rabbitmqadmin delete queue name=myqueue
rabbitmqadmin --host=remote --port=15672 --username=guest --password=guest list queues
rabbitmqadmin --format=json list queues
rabbitmqadmin --format=tsv list queues
rabbitmqadmin --vhost=/myvhost list queues
```
- `--host`: Management host
- `--port`: Management port
- `--username`: Username
- `--password`: Password
- `--vhost`: Virtual host
- `--format`: Output format (json, tsv, table)
- `--ssl`: Use SSL
- `--dry-run`: Don't execute

## Recommended Unattended Usage

```bash
#!/bin/bash

# JSON output for scripting
queues=$(rabbitmqadmin --format=json --host localhost --username admin --password secret list queues)

# Publish message
rabbitmqadmin publish exchange=amq.default routing_key=tasks payload='{"task":"process"}'
```
