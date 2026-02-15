# kafka-console-producer

**Platforms:** Multi-platform  
**Category:** Message Queue (Apache Kafka)

## Quick Reference

| Goal | Command |
|------|---------|
| Produce from stdin (non-interactive) | `echo 'message' \| kafka-console-producer --topic mytopic --bootstrap-server localhost:9092` |
| Produce from file | `kafka-console-producer --topic mytopic --bootstrap-server localhost:9092 < messages.txt` |

## Command-Line Flags

- `--request-timeout-ms`: Request timeout (prevents hanging in automation)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Produce messages from file (non-interactive, reads from stdin/file)
cat messages.txt | kafka-console-producer \
    --topic mytopic \
    --bootstrap-server localhost:9092 \
    --request-timeout-ms 10000

# Produce with key
echo "user1:login event" | kafka-console-producer \
    --topic events \
    --bootstrap-server localhost:9092 \
    --property parse.key=true \
    --property key.separator=:
```
