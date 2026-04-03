# gem

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `gem --version` |
| Show help | `gem --help` |
| List gems | `gem list` |
| Search gems | `gem search name` |
| Show gem info | `gem info name` |
| Show dependencies | `gem dependency name` |
| Query list | `gem query --list` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `gem install` | Installs gems |
| `gem update` | Updates gems |
| `gem uninstall` | Removes gems |
| `gem build` | Builds gem |
| `gem push` | Pushes to server |
| `gem cert` | Manages certs |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe gem Inspection Script

# Show version
gem --version

# List gems
gem list

# Search gems
gem search rails

# Show gem info
gem info rails
```
