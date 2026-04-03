# bundle (Ruby Bundler)

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `bundle --version` |
| Show help | `bundle --help` |
| Show config | `bundle config` |
| List gems | `bundle list` |
| Show outdated | `bundle outdated` |
| Check gems | `bundle check` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `bundle install` | Installs gems |
| `bundle update` | Updates gems |
| `bundle add` | Adds gems |
| `bundle remove` | Removes gems |
| `bundle clean` | Removes gems |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe bundle Inspection Script

# Show version
bundle --version

# List gems
bundle list

# Check gems
bundle check
```
