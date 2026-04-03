# kafka-console-consumer

**Platforms:** Multi-platform
**Category:** Message Queue

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Consume messages | `kafka-console-consumer --topic` |
| From beginning | `kafka-console-consumer --from-beginning` |
| Max messages | `kafka-console-consumer --max-messages` |
| Show help | `kafka-console-consumer --help` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| Long-running consumer | May consume大量 messages |
| Without --max-messages | Runs indefinitely |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe kafka-console-consumer Inspection Script

# Consume 10 messages
kafka-console-consumer --bootstrap-server localhost:9092 --topic my-topic --max-messages 10

# From beginning (limited)
kafka-console-consumer --bootstrap-server localhost:9092 --topic my-topic --from-beginning --max-messages 20
```
