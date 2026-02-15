# kind

**Platforms:** Multi-platform  
**Category:** Local Kubernetes (Docker-based)

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet create | `kind create cluster -q` |

## Command-Line Flags

- `-q` or `--quiet`: Quiet output (suppress progress)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Create cluster quietly from config
kind create cluster -q --name mycluster --config kind.yaml

# Delete cluster quietly
kind delete cluster -q --name mycluster
```
