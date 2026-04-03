# nc (netcat)

**Platforms:** Multi-platform
**Category:** Network Utilities

## Safe Commands (Read-Only)

| Goal | Command |
|------|---------|
| Show help | `nc -h` |
| Show version | `nc -V` |
| Port scan | `nc -zv host port` |
| Banner grab | `nc -v host port` |
| UDP scan | `nc -zvu host port` |

## Dangerous Commands (Avoid in Safe Mode)

| Command | Risk |
|---------|------|
| `nc -l` | Listens for connections |
| `nc -e` | Executes commands (backdoor) |
| `nc -c` | Executes commands |
| File transfer | May send/receive data |

## Recommended Safe Usage

```bash
#!/bin/bash
# Safe nc Inspection Script

# Port scan
nc -zv example.com 80

# Banner grab
nc -v example.com 22
```
