# tee

**Platforms:** Multi-platform  
**Category:** Output Redirection

## Quick Reference

| Goal | Command |
|------|---------|
| Write to file | `command | tee file` |
| Append | `command | tee -a file` |
| Multiple files | `command | tee file1 file2` |
| Ignore interrupt | `command | tee -i file` |

## Command-Line Flags

```bash
echo 'output' | tee file.txt         # Write to file and stdout
echo 'output' | tee -a file.txt      # Append to file
echo 'output' | tee file1.txt file2.txt  # Multiple files
command | tee log.txt | grep ERROR   # Tee then process
echo 'output' | tee -i file.txt      # Ignore interrupts
sudo tee /etc/config.txt <<EOF       # Write with sudo
config line 1
config line 2
EOF
command 2>&1 | tee output.log        # Capture stdout and stderr
```
- `-a` or `--append`: Append
- `-i` or `--ignore-interrupts`: Ignore interrupt signals

## Recommended Unattended Usage

```bash
#!/bin/bash

# Log output and display it
make 2>&1 | tee build.log

# Append to log with timestamp
echo "$(date): Starting process" | tee -a process.log
```
