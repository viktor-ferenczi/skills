# composer

**Platforms:** Multi-platform  
**Category:** Dependency Manager (PHP)

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet install | `composer install -q` |
| No dev | `composer install --no-dev` |
| Silent | `composer install --quiet` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `COMPOSER_HOME` | `/path` | Composer home |
| `COMPOSER_CACHE_DIR` | `/path` | Cache directory |
| `COMPOSER_NO_INTERACTION` | `1` | No interaction |

## Command-Line Flags

```bash
composer install -q                  # Quiet
composer install --quiet             # Silent
composer install --no-dev            # No dev dependencies
composer install --no-interaction    # No prompts
composer install --no-progress       # No progress bar
composer install --optimize-autoloader
composer update -q                   # Quiet update
composer require package -q          # Add package quietly
```
- `-q` or `--quiet`: Quiet
- `--no-dev`: Skip dev dependencies
- `--no-interaction` or `-n`: No interaction
- `--no-progress`: No progress
- `--optimize-autoloader`: Optimize autoloader
- `--classmap-authoritative`: Authoritative classmap
- `--apcu-autoloader`: APCu autoloader
- `--prefer-dist`: Prefer dist packages
- `--prefer-source`: Prefer source
- `--no-scripts`: Skip scripts
- `--no-plugins`: Disable plugins
