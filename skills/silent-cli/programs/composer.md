# composer

**Platforms:** Multi-platform  
**Category:** Dependency Manager (PHP)

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet install | `composer install -q` |
| No interaction | `composer install --no-interaction` |
| No progress | `composer install --no-progress` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `COMPOSER_NO_INTERACTION` | `1` | Disable all interactive prompts |

## Command-Line Flags

- `-q` or `--quiet`: Quiet mode — suppress output
- `--no-interaction` or `-n`: No interactive prompts
- `--no-progress`: No progress bar display
- `--no-scripts`: Skip execution of scripts (avoids potential interactive scripts)
- `--no-plugins`: Disable plugins (avoids potential interactive plugins)
