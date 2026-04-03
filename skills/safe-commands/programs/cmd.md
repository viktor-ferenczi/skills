# cmd (Windows Command Prompt)

**Platforms:** Windows
**Category:** Shell

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show version | `cmd /c ver` |
| List files | `dir` |
| Show env vars | `set` |
| Show path | `echo %PATH%` |
| Show date/time | `date` / `time` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `del` | Deletes files |
| `erase` | Deletes files |
| `format` | Formats drives |
| `rd /s` | Removes directories |
| `copy` with overwrite | Overwrites files |

## Recommended Safe Usage

```batch
:: Safe cmd Inspection Script

:: Show version
ver

:: List files
dir

:: Show env vars
set
```
