# kafka-console-producer

**Platforms:** Multi-platform
**Category:** Message Queue

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show help | `kafka-console-producer --help` |
| Show version | `kafka-console-producer --version` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `kafka-console-producer --topic` | Produces messages |
| Any producer execution | Sends messages to Kafka |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe kafka-console-producer Inspection Script

# Show help
kafka-console-producer --help

# Show version
kafka-console-producer --version
```
