# iperf / iperf3

**Platforms:** Multi-platform  
**Category:** Network Testing

## Quick Reference

| Goal | Command |
|------|---------|
| Server | `iperf3 -s` |
| Client | `iperf3 -c server` |
| JSON output | `iperf3 -c server -J` |

## Command-Line Flags

### Server
```bash
iperf3 -s                            # Start server
iperf3 -s -p 5202                    # Custom port
iperf3 -s -D                         # Daemon mode
```

### Client
```bash
iperf3 -c server                     # Test to server
iperf3 -c server -p 5202             # Custom port
iperf3 -c server -t 30               # 30 seconds
iperf3 -c server -i 1                # 1s interval reports
iperf3 -c server -J                  # JSON output
iperf3 -c server -f m                # Format: megabits
iperf3 -c server -u                  # UDP test
iperf3 -c server -b 1G               # Bandwidth limit
iperf3 -c server -R                  # Reverse mode
iperf3 -c server -P 10               # 10 parallel streams
```
- `-s`: Server mode
- `-c`: Client mode (server address)
- `-p`: Port
- `-t`: Time (seconds)
- `-i`: Interval (seconds)
- `-J`: JSON output
- `-f`: Format (b/B/k/K/m/M/g/G)
- `-u`: UDP mode
- `-b`: Bandwidth limit
- `-R`: Reverse mode
- `-P`: Parallel streams
- `-D`: Daemon mode
