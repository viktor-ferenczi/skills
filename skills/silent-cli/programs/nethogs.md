# nethogs

**Platforms:** Linux  
**Category:** Network Monitoring

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive | `timeout 5 nethogs -t` |

## Command-Line Flags

```bash
nethogs -t                           # Trace mode (dump to stdout, non-interactive)
nethogs -c 100                       # 100 refreshes before exit (auto-exit)
```
- `-t`: Trace mode (dump to stdout, non-interactive)
- `-c`: Number of refreshes before exit
