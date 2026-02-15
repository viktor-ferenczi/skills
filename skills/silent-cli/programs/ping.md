# ping

**Platforms:** Multi-platform  
**Category:** Network Testing

## Quick Reference

| Goal | Command |
|------|---------|
| Count test | `ping -c 4 host` |
| Quick check | `ping -c 1 -W 2 host` |
| Quiet | `ping -c 4 -q host` |
| Silent check | `ping -c 1 host > /dev/null 2>&1` |

## Command-Line Flags

```bash
ping -c 4 host                       # 4 packets (Linux/macOS)
ping -n 4 host                       # 4 packets (Windows)
ping -c 1 -W 2 host                  # 1 packet, 2s timeout
ping -c 4 -q host                    # Quiet summary only
```

### Linux/macOS
- `-c count`: Number of packets
- `-W timeout`: Timeout in seconds
- `-i interval`: Interval between packets
- `-q`: Quiet output
- `-s size`: Packet size
- `-t ttl`: Time to live

### Windows
- `-n count`: Number of packets
- `-w timeout`: Timeout in milliseconds
- `-l size`: Packet size
- `-i ttl`: Time to live

## Recommended Unattended Usage

```bash
#!/bin/bash
# Check if host is reachable
if ping -c 1 -W 2 host > /dev/null 2>&1; then
    echo "Host is up"
else
    echo "Host is down"
fi
```
