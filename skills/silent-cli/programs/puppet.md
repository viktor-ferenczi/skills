# puppet

**Platforms:** Multi-platform  
**Category:** Configuration Management

## Quick Reference

| Goal | Command |
|------|---------|
| Dry run | `puppet apply --noop manifest.pp` |
| JSON output | `puppet facts --render-as json` |

## Command-Line Flags

```bash
puppet apply --noop manifest.pp      # Dry run (non-interactive)
puppet facts --render-as json        # JSON output (machine-readable)
```
- `--noop`: No operation (dry run, non-interactive)
- `--render-as`: Output format (json, yaml, console)
