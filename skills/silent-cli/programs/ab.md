# ab (Apache Bench)

**Platforms:** Multi-platform  
**Category:** Load Testing

## Quick Reference

| Goal | Command |
|------|---------|
| Basic test | `ab -n 1000 -c 10 http://localhost/` |
| JSON output | `ab -n 1000 -c 10 -g results.tsv http://localhost/` |
| Quiet | `ab -q -n 1000 http://localhost/` |

## Command-Line Flags

```bash
ab -n 1000 -c 10 http://localhost/   # 1000 requests, 10 concurrent
ab -n 10000 -c 100 -t 60 http://localhost/  # 60s test
ab -q -n 1000 http://localhost/      # Quiet
ab -v 0 -n 1000 http://localhost/    # No progress
ab -H "Authorization: Bearer token" http://localhost/
ab -p post.txt -T application/json http://localhost/api
ab -k -n 1000 http://localhost/      # Keep-alive
ab -r -n 1000 http://localhost/      # Don't exit on socket errors
ab -s 120 -n 1000 http://localhost/  # 120s timeout
```
- `-n`: Number of requests
- `-c`: Concurrent requests
- `-t`: Timelimit (seconds)
- `-q`: Quiet
- `-v`: Verbosity level
- `-H`: Custom header
- `-p`: POST file
- `-T`: Content type
- `-k`: Use HTTP KeepAlive
- `-r`: Don't exit on socket errors
- `-s`: Timeout
