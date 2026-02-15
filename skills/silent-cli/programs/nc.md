# nc / netcat

**Platforms:** Multi-platform  
**Category:** Network Tools

## Quick Reference

| Goal | Command |
|------|---------|
| Silent port test | `nc -z -w 5 host port` |
| Auto-quit | `nc -q 0 host port < file` |

## Command-Line Flags

```bash
nc -z host 22                        # Zero-I/O mode (scan only, no interactive)
nc -w 3 host 80                      # Timeout after 3s (auto-exit)
nc -q 0 host 1234 < file             # Quit after EOF
```
- `-z`: Zero-I/O mode (scanning, non-interactive)
- `-w timeout`: Timeout (auto-exit)
- `-q seconds`: Quit after EOF

## Recommended Unattended Usage

```bash
#!/bin/bash
# Test if service is up
if nc -z -w 5 host 22; then
    echo "SSH is accessible"
fi

# Wait for service
while ! nc -z localhost 3306; do
    sleep 1
done
```
