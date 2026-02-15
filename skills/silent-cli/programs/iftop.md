# iftop

**Platforms:** Linux  
**Category:** Network Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| Monitor interface | `iftop -i eth0` |
| No DNS | `iftop -n` |
| Non-interactive | `timeout 10 iftop -t -s 10` |

## Command-Line Flags

```bash
iftop                                # Default interface
iftop -i eth0                        # Specific interface
iftop -n                             # No hostname resolution
iftop -N                             # No port resolution
iftop -B                             # Bytes mode
iftop -m 100M                        # Set upper limit
iftop -t -s 10                       # Text mode, 10s
iftop -f "filter"                    # BPF filter
iftop -F net/mask                    # IPv4 network
iftop -G net6/mask6                  # IPv6 network
```
- `-i`: Interface
- `-n`: No hostname resolution
- `-N`: No port resolution
- `-B`: Bytes (not bits)
- `-m`: Rate upper limit
- `-t`: Text mode (non-interactive)
- `-s`: One single snapshot
- `-f`: BPF filter
- `-F`: IPv4 network
- `-G`: IPv6 network
