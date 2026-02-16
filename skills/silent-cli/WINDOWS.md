# Windows Notes

## Deleting Reserved-Name Files

On Windows, some CLI tools may accidentally create files with reserved names like `nul`, `con`, `aux`, etc. These cannot be deleted normally. Use the `\\?\` prefix to bypass the Win32 name parser:

```cmd
del "\\?\%cd%\nul"
```

This works from `cmd.exe`. From PowerShell, use:

```powershell
cmd /c 'del "\\?\%cd%\nul"'
```
