# bundle

**Platforms:** Multi-platform  
**Category:** Dependency Manager (Ruby)

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet install | `bundle install -q` |
| No docs | `bundle install --without development` |
| Deployment | `bundle install --deployment` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `BUNDLE_PATH` | `vendor/bundle` | Install path |
| `BUNDLE_WITHOUT` | `development:test` | Skip groups |
| `BUNDLE_DEPLOYMENT` | `true` | Deployment mode |

## Command-Line Flags

```bash
bundle install -q                    # Quiet
bundle install --quiet               # Quiet
bundle install --without development test
bundle install --deployment          # Deployment mode
bundle install --local               # Use local cache
bundle install --frozen              # Fail if Gemfile.lock changes
bundle update -q                     # Quiet update
bundle exec -q command               # Execute quietly
```
- `-q` or `--quiet`: Quiet
- `--without`: Skip groups
- `--deployment`: Deployment mode (frozen, no dev deps)
- `--local`: Don't fetch remote
- `--frozen`: Fail if Gemfile.lock changes
- `--path`: Install path
- `--jobs`: Parallel jobs
- `--retry`: Retry count
