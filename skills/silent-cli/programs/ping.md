# ping

**Platforms:** Multi-platform  
**Category:** Network Testing

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet | `ping -c 4 -q host` |
| Silent check | `ping -c 1 host > /dev/null 2>&1` |

## Command-Line Flags

### Linux/macOS
```bash
ping -c 4 -q host                    # Quiet summary only
ping -c 1 -W 2 host                  # 1 packet, 2s timeout (auto-exit)
```
- `-c count`: Number of packets (required for non-interactive use)
- `-W timeout`: Timeout in seconds
- `-q`: Quiet output

### Windows
```bash
ping -n 4 host                       # Fixed count (auto-exit)
```
- `-n count`: Number of packets (required for non-interactive use)
- `-w timeout`: Timeout in milliseconds

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
