# bundle

**Platforms:** Multi-platform  
**Category:** Dependency Manager (Ruby)

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet install | `bundle install -q` |
| Deployment mode (frozen, no prompts) | `bundle install --deployment` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `BUNDLE_DEPLOYMENT` | `true` | Deployment mode (frozen lockfile, no prompts) |

## Command-Line Flags

- `-q` or `--quiet`: Quiet mode — suppress output
- `--deployment`: Deployment mode (frozen Gemfile.lock, no dev deps, no interactive changes)
- `--frozen`: Fail if Gemfile.lock needs changes (prevents interactive resolution)
- `--local`: Don't fetch remote gems (offline, no network prompts)
- `--no-cache`: Don't update the gem cache
- `--jobs`: Parallel install jobs (no interactive effect, but useful for CI speed)
- `--retry`: Retry count for network failures
