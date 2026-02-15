# apt / apt-get / apt-cache

**Platforms:** Linux (Debian, Ubuntu, and derivatives)  
**Category:** Package Management

## Quick Reference

| Goal | Command |
|------|---------|
| Non-interactive install | `apt-get install -y -qq package` |
| Silent update | `apt-get update -qq` |
| Unattended upgrade | `apt-get upgrade -y -qq` |
| No install recommends | `apt-get install -y --no-install-recommends pkg` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `DEBIAN_FRONTEND` | `noninteractive` | **Critical** - Prevents all interactive prompts |
| `DEBCONF_NONINTERACTIVE_SEEN` | `true` | Marks debconf as non-interactive seen |
| `APT_LISTCHANGES_FRONTEND` | `none` | Disable package list changes display |
| `APT_LISTBUGS_FRONTEND` | `none` | Disable bug list display |

## Command-Line Flags

### apt-get
```bash
apt-get update -qq
apt-get install -y -qq --no-install-recommends package
```
- `-y` or `--yes`: Automatic yes to prompts
- `-qq`: No output except errors (very quiet)
- `-q` or `--quiet`: Reduced output
- `--no-install-recommends`: Don't install recommended packages
- `--no-upgrade`: Don't upgrade existing packages
- `--only-upgrade`: Only upgrade, don't install new
- `--allow-downgrades`: Allow package downgrades
- `--allow-remove-essential`: Allow removing essential packages
- `--allow-change-held-packages`: Allow changing held packages
- `-o Dpkg::Options::="--force-confdef"`: Use default config on conflict
- `-o Dpkg::Options::="--force-confold"`: Keep old config on conflict

### apt
```bash
apt update -qq
apt install -y -qq --no-install-recommends package
```
- Same flags as apt-get generally
- Note: `apt` is designed for interactive use, prefer `apt-get` for scripts

### apt-cache
```bash
apt-cache search -q package
apt-cache policy package
```
- `-q`: Quiet mode
- `-n` or `--names-only`: Search names only (faster)

## Configuration Files

### /etc/apt/apt.conf.d/99unattended
```
APT::Get::Assume-Yes "true";
APT::Get::Quiet "true";
APT::Install-Recommends "false";
DPkg::options { "--force-confdef"; "--force-confold"; }
```

## Recommended Unattended Usage

```bash
#!/bin/bash

# Essential: Set noninteractive frontend
export DEBIAN_FRONTEND=noninteractive
export DEBCONF_NONINTERACTIVE_SEEN=true
export APT_LISTCHANGES_FRONTEND=none

# Update with minimal output
apt-get update -qq

# Install with no interaction, no recommends
apt-get install -y -qq --no-install-recommends \
    -o Dpkg::Options::="--force-confdef" \
    -o Dpkg::Options::="--force-confold" \
    package1 package2

# Clean up
apt-get clean
rm -rf /var/lib/apt/lists/*
```

### Docker-friendly minimal install
```bash
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq && \
apt-get install -y -qq --no-install-recommends \
    curl ca-certificates && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
```

## Handling Config File Prompts

```bash
# Method 1: Force old config (keep existing)
apt-get install -y -o Dpkg::Options::="--force-confold" package

# Method 2: Force new config (use package maintainer's)
apt-get install -y -o Dpkg::Options::="--force-confnew" package

# Method 3: Force default (use debconf priority)
apt-get install -y -o Dpkg::Options::="--force-confdef" package
```

## Pre-seeding Debconf

```bash
# Pre-answer questions
echo 'package-name question-type question answer' | debconf-set-selections

# Example: Pre-accept MySQL license
echo 'mysql-apt-config mysql-apt-config/select-server select mysql-8.0' | debconf-set-selections
```

