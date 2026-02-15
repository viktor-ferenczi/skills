# yum / dnf / microdnf

**Platforms:** Linux (RHEL, CentOS, Fedora, Amazon Linux)  
**Category:** Package Management

## Quick Reference

| Goal | Command |
|------|---------|
| Silent install | `yum install -y -q package` |
| Quiet update | `dnf update -y -q` |
| Minimal install | `microdnf install -y package` |

## Environment Variables

*No specific environment variables for yum/dnf silent mode. Use CLI flags instead.*

## Command-Line Flags

### yum
```bash
yum install -y -q package            # Quiet, auto-yes
yum update -y -q                     # Quiet update
yum list installed -q                # Quiet list
yum clean all -q                     # Quiet clean
```
- `-y` or `--assumeyes`: Auto-confirm
- `-q` or `--quiet`: Quiet
- `--nogpgcheck`: Skip GPG check (security risk)
- `--disablerepo=*`: Disable all repos
- `--enablerepo=repo`: Enable specific repo

### dnf
```bash
dnf install -y -q package            # Quiet, auto-yes
dnf update -y -q                     # Quiet update
dnf list installed -q                # Quiet list
dnf clean all -q                     # Quiet clean
dnf makecache -q                     # Quiet cache refresh
```
- `-y` or `--assumeyes`: Auto-confirm
- `-q` or `--quiet`: Quiet
- `--nogpgcheck`: Skip GPG check (security risk)
- `--setopt=install_weak_deps=False`: Skip weak dependencies
- `--best`: Use best available version

### microdnf
```bash
microdnf install -y package          # Auto-yes
microdnf update -y                   # Auto-yes update
microdnf clean all                   # Clean cache
```
- `-y` or `--assumeyes`: Auto-confirm
- `--nodocs`: Skip documentation
- `--setopt=install_weak_deps=0`: Skip weak deps
- `--setopt=tsflags=nodocs`: Skip docs

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
