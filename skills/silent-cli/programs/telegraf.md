# telegraf

**Platforms:** Multi-platform  
**Category:** Metrics Collection

## Quick Reference

| Goal | Command |
|------|---------|
| Test config | `telegraf --config telegraf.conf --test` |
| Once | `telegraf --config telegraf.conf --once` |
| Quiet | `telegraf --config telegraf.conf 2>/dev/null` |

## Command-Line Flags

```bash
telegraf --config telegraf.conf --test # Test config
telegraf --config telegraf.conf --once # Run once
telegraf --config telegraf.conf        # Run continuously
telegraf --config-directory /etc/telegraf/telegraf.d
telegraf --input-filter cpu:mem --test
```
- `--config`: Config file
- `--config-directory`: Config directory
- `--test`: Test mode (no output)
- `--once`: Run once, then exit
- `--input-filter`: Filter inputs
- `--output-filter`: Filter outputs
