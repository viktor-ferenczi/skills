# sc (Service Control)

**Platforms:** Windows  
**Category:** Service Management

## Quick Reference

| Goal | Command |
|------|---------|
| Query service | `sc query servicename` |
| Start service | `sc start servicename` |
| Create service | `sc create name binPath= "path"` |

## Command-Line Flags

```batch
sc query                             # List all services
sc query servicename                 # Query specific service
sc query type= service state= running # List running services
sc start servicename                 # Start service
sc stop servicename                  # Stop service
sc config servicename start= auto    # Auto-start
sc create MyService binPath= "C:\path\service.exe" start= auto
sc delete servicename                # Delete service
sc qc servicename                    # Query config
```
- `query`: Query service status
- `start`: Start service
- `stop`: Stop service
- `config`: Configure service
- `create`: Create service
- `delete`: Delete service
- `qc`: Query configuration
- Note: Space after `=` is required

## PowerShell Alternative

```powershell
Get-Service                          # List services
Start-Service -Name servicename
Stop-Service -Name servicename -Force
Set-Service -Name servicename -StartupType Automatic
```
