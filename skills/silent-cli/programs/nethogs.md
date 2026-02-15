# nethogs

**Platforms:** Linux  
**Category:** Network Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| Monitor all | `nethogs` |
| Specific device | `nethogs eth0` |
| Non-interactive | `timeout 5 nethogs -t` |

## Command-Line Flags

```bash
nethogs                              # Monitor all interfaces
nethogs eth0                         # Monitor eth0
nethogs -d 5                         # Refresh every 5s
nethogs -t                           # Trace mode
nethogs -a                           # Show all processes
nethogs -v 0                         # 0=KB/s, 1=total KB, 2=total B
nethogs -c 100                       # 100 refreshes before exit
```
- `-d`: Refresh delay
- `-t`: Trace mode (dump to stdout)
- `-a`: Show all processes
- `-v`: View mode (0=rate, 1=total, 2=raw)
- `-c`: Number of refreshes before exit
- `-p`: Promiscuous mode
