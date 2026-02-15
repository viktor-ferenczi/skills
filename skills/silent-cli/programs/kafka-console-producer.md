# kafka-console-producer

**Platforms:** Multi-platform  
**Category:** Message Queue (Apache Kafka)

## Quick Reference

| Goal | Command |
|------|---------|
| Produce | `echo 'message' | kafka-console-producer --topic mytopic --bootstrap-server localhost:9092` |
| From file | `kafka-console-producer --topic mytopic --bootstrap-server localhost:9092 < messages.txt` |
| With key | `echo 'key:message' | kafka-console-producer --topic mytopic --property parse.key=true ...` |

## Command-Line Flags

```bash
echo 'message' | kafka-console-producer --topic mytopic --bootstrap-server localhost:9092
cat messages.txt | kafka-console-producer --topic mytopic --bootstrap-server localhost:9092
kafka-console-producer --topic mytopic --bootstrap-server localhost:9092 --request-timeout-ms 5000
echo 'key:message' | kafka-console-producer --topic mytopic --bootstrap-server localhost:9092 --property parse.key=true --property key.separator=:
kafka-console-producer --topic mytopic --bootstrap-server localhost:9092 --producer.config producer.properties
kafka-console-producer --topic mytopic --bootstrap-server localhost:9092 --compression-codec gzip
```
- `--topic`: Topic to produce to
- `--bootstrap-server`: Kafka brokers
- `--request-timeout-ms`: Request timeout
- `--producer.config`: Producer config file
- `--property`: Producer properties
- `--compression-codec`: Compression (gzip, snappy, lz4, zstd)
- `--batch-size`: Batch size
- `--linger-ms`: Linger time

## Recommended Unattended Usage

```bash
#!/bin/bash

# Produce messages from file
cat messages.txt | kafka-console-producer     --topic mytopic     --bootstrap-server localhost:9092     --request-timeout-ms 10000

# Produce with key
echo "user1:login event" | kafka-console-producer     --topic events     --bootstrap-server localhost:9092     --property parse.key=true     --property key.separator=:
```
