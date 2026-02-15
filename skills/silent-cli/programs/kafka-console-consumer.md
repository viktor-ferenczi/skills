# kafka-console-consumer

**Platforms:** Multi-platform  
**Category:** Message Queue (Apache Kafka)

## Quick Reference

| Goal | Command |
|------|---------|
| Consume N messages and exit | `kafka-console-consumer --topic mytopic --max-messages 100 --bootstrap-server localhost:9092` |
| Timeout and exit | `kafka-console-consumer --topic mytopic --timeout-ms 5000 --bootstrap-server localhost:9092` |

## Command-Line Flags

- `--max-messages`: Max messages to consume then exit (critical for unattended use)
- `--timeout-ms`: Timeout in milliseconds — exit if no message received within this period

## Recommended Unattended Usage

```bash
#!/bin/bash

# Consume 100 messages and exit
kafka-console-consumer \
    --topic mytopic \
    --bootstrap-server localhost:9092 \
    --max-messages 100 \
    --timeout-ms 30000 \
    --property print.key=true
```
