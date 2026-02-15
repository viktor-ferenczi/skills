# dotnet

**Platforms:** Multi-platform  
**Category:** .NET Build Tool

## Quick Reference

| Goal | Command |
|------|---------|
| Build (errors only) | `dotnet build -v quiet` |
| Build (minimal) | `dotnet build -v minimal` |
| No color | `dotnet build --nologo -v quiet` |
| Restore silently | `dotnet restore -v quiet` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `DOTNET_CLI_TELEMETRY_OPTOUT` | `1` | Disable telemetry |
| `DOTNET_NOLOGO` | `true` | Suppress logo and telemetry message |
| `DOTNET_SKIP_FIRST_TIME_EXPERIENCE` | `true` | Skip first-run experience (SDK < 6) |
| `NO_COLOR` | `1` | Disable colored output |
| `DOTNET_SYSTEM_CONSOLE_ALLOW_ANSI_COLOR_REDIRECTION` | `0` | Prevent ANSI color in redirected output |
| `CI` | `true` | Indicates CI environment |

## Command-Line Flags

```bash
dotnet build                         # Build project
dotnet build -v quiet                # Errors only (quiet verbosity)
dotnet build -v minimal              # Minimal output
dotnet build -v normal               # Normal output (default)
dotnet build -v detailed             # Detailed output
dotnet build -v diagnostic           # Diagnostic output
dotnet build --nologo                # Suppress startup banner
dotnet build -c Release              # Release configuration
dotnet build --no-restore            # Skip restore
dotnet build --no-incremental        # Full rebuild
dotnet build -nowarn:CS0168          # Suppress specific warning
dotnet build -warnaserror            # Treat warnings as errors
dotnet restore                       # Restore NuGet packages
dotnet restore -v quiet              # Quiet restore
dotnet restore --no-cache            # Skip HTTP cache
dotnet publish -c Release            # Publish for deployment
dotnet publish -v quiet              # Quiet publish
dotnet test                          # Run tests
dotnet test -v quiet                 # Quiet test output
dotnet test --no-build               # Skip build
dotnet test --logger "console;verbosity=minimal"  # Minimal test logger
dotnet run                           # Run project
dotnet clean                         # Clean build output
dotnet pack                          # Create NuGet package
dotnet pack -v quiet                 # Quiet pack
```
- `-v` or `--verbosity`: Verbosity level (quiet, minimal, normal, detailed, diagnostic)
- `--nologo`: Suppress startup banner
- `-c` or `--configuration`: Build configuration (Debug, Release)
- `--no-restore`: Skip automatic restore
- `--no-build`: Skip build (for test/run)
- `-nowarn`: Suppress specific warnings
- `-warnaserror`: Treat warnings as errors
- `--logger`: Test logger configuration

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
