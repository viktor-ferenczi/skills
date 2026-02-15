# fluent-bit

**Platforms:** Multi-platform  
**Category:** Log Processing

## Quick Reference

| Goal | Command |
|------|---------|
| Test config | `fluent-bit --dry-run -c fluent-bit.conf` |
| Quiet | `fluent-bit -c fluent-bit.conf -o /dev/null` |
| JSON output | `fluent-bit -c config.conf -o stdout -p format=json` |

## Command-Line Flags

```bash
fluent-bit --dry-run -c fluent-bit.conf
fluent-bit -c fluent-bit.conf        # Run
fluent-bit -c fluent-bit.conf -R parsers.conf
fluent-bit -i cpu -o stdout          # Quick test
fluent-bit -i cpu -F grep -p 'Match=cpu' -o stdout
```
- `-c` or `--config`: Config file
- `-R` or `--parser`: Parsers file
- `-i` or `--input`: Input plugin
- `-o` or `--output`: Output plugin
- `-F` or `--filter`: Filter plugin
- `--dry-run`: Validate config
- `-f` or `--flush`: Flush interval
