# dotnet

**Platforms:** Multi-platform  
**Category:** .NET Build Tool

## Quick Reference

| Goal | Command |
|------|---------|
| Build (errors only) | `dotnet build -v quiet` |
| No logo/banner | `dotnet build --nologo -v quiet` |
| Quiet test | `dotnet test -v quiet --nologo --logger "console;verbosity=minimal"` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `DOTNET_CLI_TELEMETRY_OPTOUT` | `1` | Disable telemetry (avoids first-run message) |
| `DOTNET_NOLOGO` | `true` | Suppress logo and telemetry message |
| `DOTNET_SKIP_FIRST_TIME_EXPERIENCE` | `true` | Skip first-run experience (SDK < 6) |
| `NO_COLOR` | `1` | Disable colored output |
| `DOTNET_SYSTEM_CONSOLE_ALLOW_ANSI_COLOR_REDIRECTION` | `0` | Prevent ANSI color in redirected output |
| `CI` | `true` | Indicates CI environment |

## Command-Line Flags

- `-v` or `--verbosity`: Verbosity level (`quiet`, `minimal`, `normal`, `detailed`, `diagnostic`) — use `quiet` for errors only
- `--nologo`: Suppress startup banner
- `--logger`: Test logger configuration (use `"console;verbosity=minimal"` for minimal test output)

## Recommended Unattended Usage

```bash
#!/bin/bash

export DOTNET_CLI_TELEMETRY_OPTOUT=1
export DOTNET_NOLOGO=true
export NO_COLOR=1

# Build showing only errors, no progress, no color
dotnet build -c Release -v quiet --nologo

# Run tests with minimal output
dotnet test -v quiet --nologo --no-build --logger "console;verbosity=minimal"
```
