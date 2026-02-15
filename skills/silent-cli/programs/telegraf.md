# telegraf

**Platforms:** Multi-platform  
**Category:** Metrics Collection

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet | `telegraf --config telegraf.conf 2>/dev/null` |
| Once (non-daemon) | `telegraf --config telegraf.conf --once` |

## Command-Line Flags

- `--test`: Test mode (no output to destinations)
- `--once`: Run once, then exit (non-daemon)
