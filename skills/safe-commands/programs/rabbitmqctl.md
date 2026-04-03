# rabbitmqctl

**Platforms:** Multi-platform
**Category:** Message Queue

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `rabbitmqctl --version` |
| Show help | `rabbitmqctl --help` |
| Status | `rabbitmqctl status` |
| List vhosts | `rabbitmqctl list_vhosts` |
| List exchanges | `rabbitmqctl list_exchanges` |
| List queues | `rabbitmqctl list_queues` |
| List bindings | `rabbitmqctl list_bindings` |
| Cluster status | `rabbitmqctl cluster_status` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `rabbitmqctl add_vhost` | Creates vhosts |
| `rabbitmqctl delete_vhost` | Deletes vhosts |
| `rabbitmqctl purge_queue` | Purges queues |
| `rabbitmqctl delete_queue` | Deletes queues |
| `rabbitmqctl set_permissions` | Modifies permissions |
| `rabbitmqctl stop_app` | Stops RabbitMQ |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe rabbitmqctl Inspection Script

# Status
rabbitmqctl status

# List queues
rabbitmqctl list_queues

# List exchanges
rabbitmqctl list_exchanges
```
