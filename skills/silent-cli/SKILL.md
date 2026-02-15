---
name: silent-cli
description: Environment variables and parameters for running command line programs reliably in non-interactive environments (unattended). Includes silent modes, color/disable TTY, and reduced output options for 149 CLI tools.
tags: [cli, automation, scripting, unattended, environment-variables, flags, ci-cd, devops]
version: 1.1.0
author: Viktor Ferenczi
license: MIT
---

# Silent and Unattended CLI Execution Skill

## Overview

This skill provides a comprehensive reference for running command line programs in unattended/non-interactive environments. 
It documents environment variables, command-line flags, and configuration options to:

- **Disable interactive prompts** - Ensure programs run without user input
- **Suppress progress indicators** - Disable spinners, progress bars, and real-time updates
- **Disable colored output** - Remove ANSI color codes and terminal formatting
- **Reduce output verbosity** - Limit output to essential information only
- **Force non-TTY mode** - Prevent programs from detecting terminal capabilities

## Coverage

- **149 programs documented**
- **114 unique categories** (version control, cloud CLIs, databases, security, monitoring, etc.)
- **Multi-platform coverage:** Linux, macOS, Windows
- **Includes:** Core utilities, development tools, CI/CD tools, cloud platforms, container tools, security scanners

## Structure

```
/
├── SKILL.md              # This file - skill overview
├── INDEX_BY_NAME.md      # Program index alphabetically
├── INDEX_BY_CATEGORY.md  # Program index by category
├── PLATFORM_COVERAGE.md  # Platform coverage statistics
├── programs/             # Individual program documentation (149 files)
│   ├── git.md
│   ├── curl.md
│   ├── aws.md
│   ├── docker.md
│   └── ...
└── scripts/              # Helper scripts (if needed)
```

## Quick Reference

See the program indexes for complete listings:
- [**INDEX_BY_NAME.md**](INDEX_BY_NAME.md) - Alphabetical listing of all programs
- [**INDEX_BY_CATEGORY.md**](INDEX_BY_CATEGORY.md) - Programs organized by category (Cloud, Database, Security, Monitoring, etc.)
- [**PLATFORM_COVERAGE.md**](PLATFORM_COVERAGE.md) - Platform coverage statistics (Multi-platform, Linux, Windows, macOS)

## Universal Environment Variables

These environment variables affect many programs:

| Variable | Value | Effect |
|----------|-------|--------|
| `CI` | `true` | Indicates continuous integration environment, triggers non-interactive mode for many tools |
| `DEBIAN_FRONTEND` | `noninteractive` | Prevents apt/dpkg from prompting (Debian/Ubuntu) |
| `FORCE_COLOR` | `0` | Disables colored output (Node.js, some JS tools) |
| `NO_COLOR` | `1` | Disables colored output (growing standard) |
| `TERM` | `dumb` | Minimal terminal capabilities |
| `TZ` | `UTC` | Sets timezone, prevents timezone prompts |
| `PYTHONUNBUFFERED` | `1` | Unbuffered Python output |
| `NODE_NO_WARNINGS` | `1` | Suppress Node.js warnings |

## Category Highlights

### Cloud Platforms
AWS CLI, Azure CLI, Google Cloud SDK, S3 tools (s3cmd, gsutil, mc, rclone)

### Container & Orchestration  
Docker, Podman, Kubernetes (kubectl, helm, minikube, kind)

### Version Control
Git, GitHub CLI, GitLab CLI

### Build Tools
Make, CMake, Maven, Gradle, npm, yarn, pnpm, pip

### Databases
MySQL, PostgreSQL, MongoDB, Redis, SQLite

### Security & Testing
Nmap, sqlmap, Metasploit, OpenVAS, Nikto, WPScan, Burp Suite, Hashcat, John the Ripper

### Monitoring & Logging
Prometheus, Grafana, ELK Stack (Elasticsearch, Logstash, Kibana, Beats)

### CI/CD
Jenkins CLI, GitLab Runner, GitHub Actions runner

### Infrastructure as Code
Terraform, Ansible, Packer, Vault, Consul, Nomad

## Usage Examples

### Debian/Ubuntu Package Installation
```bash
export DEBIAN_FRONTEND=noninteractive
export CI=true
apt-get update -qq && apt-get install -y -qq package-name
```

### NPM CI Installation
```bash
export CI=true
export NODE_ENV=production
npm ci --silent --no-progress
```

### Docker Unattended
```bash
export DOCKER_CLI_EXPERIMENTAL=enabled
export BUILDKIT_PROGRESS=plain
docker build --progress=plain -t myimage .
```

### Python Script
```bash
export PYTHONUNBUFFERED=1
export PYTHONDONTWRITEBYTECODE=1
python script.py
```

## Program Documentation Format

Each program file includes:
- **Platforms supported**
- **Category**
- **Quick Reference table** - Common commands
- **Command-line flags** - Detailed flag reference
- **Environment variables** - Relevant env vars
- **Recommended Unattended Usage** - Example scripts

## Contributing

When adding new programs:
1. Research official documentation for unattended/silent flags
2. Test in a clean environment
3. Document environment variables and flags
4. Note platform-specific differences
5. Follow the established Markdown format
