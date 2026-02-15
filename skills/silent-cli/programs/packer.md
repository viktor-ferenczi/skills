# packer (HashiCorp)

**Platforms:** Multi-platform  
**Category:** Machine Image Builder

## Quick Reference

| Goal | Command |
|------|---------|
| Machine-readable | `packer build -machine-readable template.pkr.hcl` |
| Force build | `packer build -force template.pkr.hcl` |
| Auto-cleanup on error | `packer build -on-error=cleanup template.pkr.hcl` |

## Command-Line Flags

```bash
packer build -force template.pkr.hcl             # Force overwrite (no prompt)
packer build -on-error=cleanup template.pkr.hcl  # Auto-cleanup on error (not "ask")
packer build -on-error=abort template.pkr.hcl    # Abort on error (not "ask")
packer build -machine-readable template.pkr.hcl  # Machine-readable output
```
- `-force`: Force overwrite (no prompt)
- `-on-error`: Error behavior (ask, cleanup, abort) — use `cleanup` or `abort` for unattended
- `-machine-readable`: Machine-readable output

## Recommended Unattended Usage

```bash
#!/bin/bash

# Validate, format, and build
packer fmt -write=false template.pkr.hcl || exit 1
packer validate template.pkr.hcl || exit 1
packer build -on-error=cleanup -force template.pkr.hcl
```
