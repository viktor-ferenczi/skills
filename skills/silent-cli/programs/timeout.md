# timeout

**Platforms:** Linux, macOS (gtimeout)  
**Category:** Process Control

## Quick Reference

| Goal | Command |
|------|---------|
| Kill after 30s | `timeout 30 command` |
| Signal after 10s | `timeout -s KILL 10 command` |
| Preserve exit code | `timeout --preserve-status 30 cmd` |

## Command-Line Flags

```bash
timeout 30 command                   # SIGTERM after 30s
timeout -s KILL 30 command           # SIGKILL after 30s
timeout --signal=KILL 30 command     # Same
timeout -k 5 30 command              # SIGKILL 5s after SIGTERM
timeout --preserve-status 30 command # Exit with cmd's status
```
- `-s` or `--signal=SIGNAL`: Signal to send
- `-k` or `--kill-after=DURATION`: SIGKILL delay after SIGTERM
- `--preserve-status`: Exit with command's status (or 124 on timeout)
- `-f` or `--foreground`: Run in foreground (when not in terminal)

## Exit Codes

- `124`: Command timed out
- `125`: timeout command failed
- `126`: Command found but cannot be invoked
- `127`: Command not found
- `137` (128+9): Command killed (SIGKILL)
- Other: Command's exit status (with --preserve-status)
