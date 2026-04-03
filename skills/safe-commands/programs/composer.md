# composer

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `composer --version` |
| Show help | `composer --help` |
| Show info | `composer show` |
| List packages | `composer show --name-only` |
| Validate config | `composer validate` |
| Check platform | `composer check-platform-reqs` |
| Show depends | `composer depends package` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `composer install` | Installs packages |
| `composer update` | Updates packages |
| `composer require` | Adds packages |
| `composer remove` | Removes packages |
| `composer dump-autoload` | Regenerates autoload |
| `composer config` | Modifies config |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe composer Inspection Script

# Show version
composer --version

# Show packages
composer show --name-only

# Validate config
composer validate

# Check platform requirements
composer check-platform-reqs
```
