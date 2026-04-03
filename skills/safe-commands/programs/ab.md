# ab (Apache Benchmark)

**Platforms:** Multi-platform
**Category:** Web Testing

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `ab -V` |
| Show help | `ab -h` |
| Test GET request | `ab -n 100 -c 10 URL` |
| Show headers | `ab -v 2 URL` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `ab -p POSTFILE` | Sends POST data |
| `ab -T content-type` | Sets content type |
| High concurrency tests | May overload server |
| Any ab with write methods | May modify server state |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe ab Inspection Script

# Show version
ab -V

# Simple GET test (low load)
ab -n 10 -c 1 http://localhost/
```
