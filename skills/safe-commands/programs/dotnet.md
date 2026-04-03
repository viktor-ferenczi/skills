# dotnet

**Platforms:** Multi-platform
**Category:** Build Tools

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `dotnet --version` |
| Show help | `dotnet --help` |
| List SDKs | `dotnet --list-sdks` |
| List runtimes | `dotnet --list-runtimes` |
| Build info | `dotnet build --dry-run` |
| Show project | `dotnet sln list` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `dotnet build` | Builds project |
| `dotnet run` | Runs program |
| `dotnet publish` | Publishes app |
| `dotnet clean` | Cleans output |
| `dotnet pack` | Creates package |
| `dotnet add` | Adds references |
| `dotnet remove` | Removes references |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe dotnet Inspection Script

# Show version
dotnet --version

# List SDKs
dotnet --list-sdks

# List runtimes
dotnet --list-runtimes

# Show solution
dotnet sln list
```
