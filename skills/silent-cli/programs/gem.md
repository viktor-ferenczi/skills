# gem

**Platforms:** Multi-platform  
**Category:** Package Manager (Ruby)

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `gem install -q package` |
| No docs | `gem install --no-document package` |
| Batch | `gem install --conservative package` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `GEM_HOME` | `/path` | Gem installation path |
| `GEM_PATH` | `/path` | Gem search path |

## Command-Line Flags

```bash
gem install package -q               # Quiet
gem install package --no-document    # Skip docs (faster)
gem install package --conservative   # Don't upgrade deps
gem uninstall package -a -x          # All versions, executables
gem list -q                          # Quiet list
gem update --system -q               # Update system quietly
gem update -q                        # Update gems quietly
```
- `-q` or `--quiet`: Quiet
- `--no-document`: Skip documentation
- `--conservative`: Don't update deps
- `-v` or `--version`: Specific version
- `-a` or `--all`: All versions
- `-x` or `--executables`: Remove executables

## ~/.gemrc

```yaml
---
gem: --no-document
```
