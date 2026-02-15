# rabbitmqctl

**Platforms:** Multi-platform  
**Category:** Message Queue (RabbitMQ)

## Quick Reference

| Goal | Command |
|------|---------|
| List queues | `rabbitmqctl list_queues` |
| Status | `rabbitmqctl status` |
| Add user | `rabbitmqctl add_user user pass` |
| Quiet | `rabbitmqctl -q list_queues` |

## Command-Line Flags

```bash
rabbitmqctl status                   # Broker status
rabbitmqctl -q status                # Quiet
rabbitmqctl environment              # Environment
rabbitmqctl list_queues              # List queues
rabbitmqctl list_queues name messages_ready
rabbitmqctl list_exchanges
rabbitmqctl list_bindings
rabbitmqctl list_connections
rabbitmqctl list_channels
rabbitmqctl list_consumers
rabbitmqctl add_user user password
rabbitmqctl delete_user user
rabbitmqctl change_password user newpassword
rabbitmqctl set_user_tags user administrator
rabbitmqctl add_vhost /myvhost
rabbitmqctl delete_vhost /myvhost
rabbitmqctl set_permissions -p /myvhost user ".*" ".*" ".*"
rabbitmqctl purge_queue myqueue
rabbitmqctl stop_app
rabbitmqctl start_app
rabbitmqctl reset
```
- `-q`: Quiet
- `-n`: Node name
- `-p`: VHost
- Common commands: `status`, `environment`, `list_queues`, `list_exchanges`, `list_bindings`, `list_connections`, `list_channels`, `list_consumers`, `add_user`, `delete_user`, `change_password`, `set_user_tags`, `add_vhost`, `delete_vhost`, `set_permissions`, `clear_permissions`, `purge_queue`, `stop_app`, `start_app`, `reset`

## Recommended Unattended Usage

```bash
#!/bin/bash

# Quiet status check
rabbitmqctl -q status > /dev/null 2>&1 && echo "Running" || echo "Not running"

# List queue depths
rabbitmqctl -q list_queues name messages_ready messages_unacknowledged
```
