# kafka-topics

**Platforms:** Multi-platform  
**Category:** Message Queue (Apache Kafka)

## Quick Reference

| Goal | Command |
|------|---------|
| List | `kafka-topics --list --bootstrap-server localhost:9092` |
| Describe | `kafka-topics --describe --topic mytopic ...` |
| Create | `kafka-topics --create --topic mytopic --partitions 3 ...` |
| Delete | `kafka-topics --delete --topic mytopic ...` |

## Command-Line Flags

```bash
kafka-topics --list --bootstrap-server localhost:9092
kafka-topics --describe --topic mytopic --bootstrap-server localhost:9092
kafka-topics --create --topic mytopic --partitions 3 --replication-factor 1 --bootstrap-server localhost:9092
kafka-topics --delete --topic mytopic --bootstrap-server localhost:9092
kafka-topics --alter --topic mytopic --partitions 6 --bootstrap-server localhost:9092
kafka-topics --config retention.ms=86400000 --alter --topic mytopic --bootstrap-server localhost:9092
kafka-topics --describe --under-replicated-partitions --bootstrap-server localhost:9092
kafka-topics --describe --unavailable-partitions --bootstrap-server localhost:9092
```
- `--list`: List topics
- `--describe`: Describe topic
- `--create`: Create topic
- `--delete`: Delete topic
- `--alter`: Alter topic
- `--topic`: Topic name
- `--partitions`: Number of partitions
- `--replication-factor`: Replication factor
- `--config`: Topic configuration
- `--bootstrap-server`: Kafka brokers
- `--under-replicated-partitions`: Show under-replicated
- `--unavailable-partitions`: Show unavailable
