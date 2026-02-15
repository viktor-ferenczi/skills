# gem

**Platforms:** Multi-platform  
**Category:** Package Manager (Ruby)

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `gem install -q package` |
| No docs (faster, less output) | `gem install --no-document package` |
| Quiet update | `gem update -q` |

## Command-Line Flags

- `-q` or `--quiet`: Suppress informational output
- `--no-document`: Skip documentation generation (reduces output and speeds up installs)

## ~/.gemrc

```yaml
---
gem: --no-document
```

Setting `--no-document` in `.gemrc` ensures all gem installs are quieter by default in automated environments.
