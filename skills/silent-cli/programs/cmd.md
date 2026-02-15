# cmd.exe

**Platforms:** Windows  
**Category:** Command Shell

## Quick Reference

| Goal | Command |
|------|---------|
| Execute and exit | `cmd /c command` |
| Execute and stay | `cmd /k command` |
| Silent | `cmd /c command >nul 2>&1` |

## Command-Line Flags

```batch
cmd /c dir                           # Execute and close
cmd /k dir                           # Execute and stay
cmd /c "echo hello && echo world"    # Multiple commands
cmd /c command >nul 2>&1             # Silent (discard output)
cmd /q /c command                    # Echo off (quiet)
cmd /v:on /c command                 # Delayed expansion on
```
- `/c`: Execute and terminate
- `/k`: Execute and remain
- `/q`: Turn echo off (quiet)
- `/v:on`: Enable delayed variable expansion
- `/s`: Strip first and last quote

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
