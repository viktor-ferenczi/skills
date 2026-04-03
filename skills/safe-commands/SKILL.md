---
name: safe-commands
description: Collection of safe, read-only CLI commands for 149 tools. Environment variables and parameters for running command line programs reliably without modifying system state. Includes query-only modes, dry-run options, and non-destructive alternatives.
tags: [cli, automation, scripting, safe-commands, read-only, query, dry-run, non-destructive]
version: 2.0.0
author: Viktor Ferenczi
license: MIT
---

# Safe CLI Commands - Read-Only Execution Skill

## Overview

This skill provides a comprehensive reference for running command line programs in **safe, read-only mode**. It documents environment variables, command-line flags, and configuration options to:

- **Query-only operations** - Retrieve information without modifications
- **Dry-run mode** - Preview changes without applying them
- **Read-only access** - Prevent accidental writes or deletions
- **Safe defaults** - Use non-destructive command alternatives
- **Audit and inspection** - Tools for system analysis without changes

## Coverage

- **149 programs documented**
- **111 unique categories** (version control, cloud CLIs, databases, security, monitoring, etc.)
- **Multi-platform coverage:** Linux, macOS, Windows
- **Includes:** Core utilities, development tools, CI/CD tools, cloud platforms, container tools

## Structure

```
/
├── SKILL.md              # This file - skill overview
├── INDEX_BY_NAME.md      # Program index alphabetically
├── INDEX_BY_CATEGORY.md  # Program index by category
├── PLATFORM_COVERAGE.md  # Platform coverage statistics
├── programs/             # Individual program documentation (155 files)
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
- [**INDEX_BY_CATEGORY.md**](INDEX_BY_CATEGORY.md) - Programs organized by category
- [**PLATFORM_COVERAGE.md**](PLATFORM_COVERAGE.md) - Platform coverage statistics

## Universal Safe Mode Environment Variables

| Variable | Value | Effect |
|----------|-------|--------|
| `DRY_RUN` | `true` | Many tools respect this for preview mode |
| `NO_WRITE` | `1` | Prevent write operations where supported |
| `READ_ONLY` | `1` | Enable read-only mode where available |
| `TERM` | `dumb` | Minimal terminal, prevents interactive prompts |
| `TZ` | `UTC` | Sets timezone, prevents timezone prompts |
| `PYTHONUNBUFFERED` | `1` | Unbuffered Python output |

## Safe Command Patterns by Category

### Version Control (Git, GitHub, GitLab)
- Use `git status`, `git log`, `git show` - never `git commit`, `git push`
- Use `--dry-run` with git operations that might modify
- Clone with `--depth 1` for read-only inspection

### Cloud Platforms (AWS, Azure, GCP)
- Use `describe-*`, `get-*`, `list-*` commands only
- Avoid `create-*`, `delete-*`, `update-*`, `put-*`
- Use IAM read-only roles when possible

### Container & Orchestration (Docker, Kubernetes)
- Use `docker inspect`, `docker logs`, `docker ps`
- Use `kubectl get`, `kubectl describe`, `kubectl logs`
- Avoid `docker run`, `kubectl apply`, `kubectl delete`

### Databases (MySQL, PostgreSQL, MongoDB)
- Use `SELECT` queries only - never `INSERT`, `UPDATE`, `DELETE`
- Connect with read-only user credentials
- Use `--read-only` connection flags where available

### File Operations
- Use `cat`, `less`, `head`, `tail` for viewing
- Use `ls`, `find`, `stat` for listing
- Avoid `rm`, `mv`, `cp`, `chmod` in production

## Program Documentation Format

Each program file includes:
- **Platforms supported**
- **Category**
- **Safe Commands** - Read-only, non-destructive commands
- **Dangerous Commands** - Commands to avoid in safe mode
- **Environment variables** - Relevant env vars for safe operation
- **Recommended Safe Usage** - Example scripts

## Safety Guidelines

1. **Always verify** command intent before execution
2. **Use read-only credentials** when available
3. **Test in staging** before running in production
4. **Log all operations** for audit trails
5. **Use dry-run** flags where available
6. **Avoid sudo/root** unless absolutely necessary

## Contributing

When adding safe command documentation:
1. Identify read-only alternatives for each tool
2. Document dangerous commands to avoid
3. Test commands in isolated environment
4. Note any side effects (logging, metrics)
5. Follow the established Markdown format
