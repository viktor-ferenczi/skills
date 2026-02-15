# cmd.exe

**Platforms:** Windows  
**Category:** Command Shell

## Quick Reference

| Goal | Command |
|------|---------|
| Execute and exit | `cmd /c command` |
| Silent (discard output) | `cmd /c command >nul 2>&1` |
| Quiet (echo off) | `cmd /q /c command` |

## Command-Line Flags

- `/c`: Execute command and terminate (non-interactive)
- `/q`: Turn echo off (quiet mode)
- `>nul 2>&1`: Redirect all output to null (silent)

## Batch File Silent Mode

```batch
@echo off                            # Disable command echo
setlocal enabledelayedexpansion      # Enable delayed expansion
```

## Recommended Unattended Usage

```batch
@echo off
setlocal enabledelayedexpansion

REM Redirect all output
command >C:\logs\output.log 2>&1

REM Check errorlevel
if errorlevel 1 (
    echo Failed
    exit /b 1
)
```
