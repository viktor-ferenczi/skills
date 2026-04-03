# packer (HashiCorp)

**Platforms:** Multi-platform
**Category:** Infrastructure

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `packer --version` |
| Show help | `packer --help` |
| Validate | `packer validate template.pkr.hcl` |
| Inspect | `packer inspect template.pkr.hcl` |
| Show config | `packer console` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `packer build` | Creates images (costs money) |
| `packer fix` | Modifies templates |
| Any packer build | Provisions infrastructure |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe packer Inspection Script

# Validate template
packer validate template.pkr.hcl

# Inspect template
packer inspect template.pkr.hcl
```
