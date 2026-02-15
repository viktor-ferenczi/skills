# kafka-console-consumer

**Platforms:** Multi-platform  
**Category:** Message Queue (Apache Kafka)

## Quick Reference

| Goal | Command |
|------|---------|
| Consume | `kafka-console-consumer --topic mytopic --bootstrap-server localhost:9092` |
| From beginning | `kafka-console-consumer --topic mytopic --from-beginning ...` |
| Group | `kafka-console-consumer --topic mytopic --group mygroup ...` |

## Command-Line Flags

```bash
kafka-console-consumer --topic mytopic --bootstrap-server localhost:9092
kafka-console-consumer --topic mytopic --bootstrap-server localhost:9092 --from-beginning
kafka-console-consumer --topic mytopic --bootstrap-server localhost:9092 --group mygroup
kafka-console-consumer --topic mytopic --bootstrap-server localhost:9092 --max-messages 100
kafka-console-consumer --topic mytopic --bootstrap-server localhost:9092 --timeout-ms 5000
kafka-console-consumer --topic mytopic --bootstrap-server localhost:9092 --property print.key=true
kafka-console-consumer --topic mytopic --bootstrap-server localhost:9092 --property key.separator=,
kafka-console-consumer --topic mytopic --bootstrap-server localhost:9092 --consumer.config consumer.properties
kafka-console-consumer --whitelist 'topic.*' --bootstrap-server localhost:9092
```
- `--topic`: Topic to consume
- `--bootstrap-server`: Kafka brokers
- `--from-beginning`: Consume from beginning
- `--group`: Consumer group
- `--max-messages`: Max messages to consume
- `--timeout-ms`: Timeout in milliseconds
- `--property`: Consumer properties
- `--consumer.config`: Config file
- `--whitelist`: Whitelist pattern
- `--blacklist`: Blacklist pattern

## Recommended Unattended Usage

```bash
#!/bin/bash

# Consume 100 messages and exit
kafka-console-consumer     --topic mytopic     --bootstrap-server localhost:9092     --max-messages 100     --timeout-ms 30000     --property print.key=true
```
