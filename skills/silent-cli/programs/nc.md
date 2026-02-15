# nc / netcat

**Platforms:** Multi-platform  
**Category:** Network Tools

## Quick Reference

| Goal | Command |
|------|---------|
| Test port | `nc -zv host port` |
| Listen | `nc -l -p port` |
| Transfer file | `nc -q 0 host port < file` |

## Command-Line Flags

```bash
nc -zv host 22                       # Check if port 22 is open
nc -zv host 1-1000                   # Scan ports 1-1000
nc -l -p 1234                        # Listen on port 1234
nc -q 0 host 1234 < file             # Send file
nc -w 3 host 80                      # Timeout after 3s
```

### Common Options
- `-z`: Zero-I/O mode (scanning)
- `-v`: Verbose
- `-l`: Listen mode
- `-p port`: Local port
- `-w timeout`: Timeout
- `-q seconds`: Quit after EOF
- `-u`: UDP mode
- `-k`: Keep listening (after disconnect)

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
