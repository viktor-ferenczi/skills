# rabbitmqadmin

**Platforms:** Multi-platform
**Category:** Message Queue

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show help | `rabbitmqadmin --help` |
| List vhosts | `rabbitmqadmin list vhosts` |
| List exchanges | `rabbitmqadmin list exchanges` |
| List queues | `rabbitmqadmin list queues` |
| List bindings | `rabbitmqadmin list bindings` |
| Get message | `rabbitmqadmin get queue` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `rabbitmqadmin declare` | Creates resources |
| `rabbitmqadmin delete` | Deletes resources |
| `rabbitmqadmin publish` | Publishes messages |
| `rabbitmqadmin purge` | Purges queues |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe rabbitmqadmin Inspection Script

# List queues
rabbitmqadmin list queues

# List exchanges
rabbitmqadmin list exchanges
```
