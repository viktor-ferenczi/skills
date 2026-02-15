# yum / dnf / microdnf

**Platforms:** Linux (RHEL, CentOS, Fedora, Amazon Linux)  
**Category:** Package Management

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `yum install -y -q package` |
| Quiet update | `dnf update -y -q` |
| Minimal install | `microdnf install -y package` |

## Command-Line Flags

### yum
- `-y` or `--assumeyes`: Auto-confirm (skip prompts)
- `-q` or `--quiet`: Quiet output

### dnf
- `-y` or `--assumeyes`: Auto-confirm (skip prompts)
- `-q` or `--quiet`: Quiet output

### microdnf
- `-y` or `--assumeyes`: Auto-confirm (skip prompts)

## Recommended Unattended Usage

```bash
#!/bin/bash

# DNF (Fedora, RHEL 8+)
dnf install -y -q --setopt=install_weak_deps=False package1 package2
dnf clean all -q

# YUM (RHEL 7, CentOS 7)
yum install -y -q package1 package2
yum clean all -q

# microdnf (container-optimized)
microdnf install -y --nodocs --setopt=install_weak_deps=0 package1 package2
microdnf clean all
```
