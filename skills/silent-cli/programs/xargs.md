# xargs

**Platforms:** Multi-platform  
**Category:** Command Building

## Quick Reference

| Goal | Command |
|------|---------|
| Basic | `find . -name '*.txt' | xargs rm` |
| Parallel | `cat urls.txt | xargs -P4 wget` |
| Delimiter | `echo 'a,b,c' | xargs -d',' echo` |
| Max args | `find . -name '*.txt' | xargs -n1 cat` |

## Command-Line Flags

```bash
find . -name '*.txt' | xargs rm      # Delete found files
find . -name '*.txt' -print0 | xargs -0 rm  # Safe for spaces
ls | xargs -I {} mv {} {}.bak        # Rename with backup
seq 1 10 | xargs -n2 echo            # 2 args per command
cat files.txt | xargs cat            # Concatenate files
echo 'a b c' | xargs -n1 echo        # One arg per command
echo 'a,b,c' | xargs -d',' echo      # Comma delimiter
cat urls.txt | xargs -P4 wget        # 4 parallel downloads
find . -name '*.py' | xargs -I {} cp {} /backup/  # With placeholder
echo 'file.txt' | xargs -p cat       # Prompt before execute
echo 'file.txt' | xargs -t cat       # Print command
echo 'file.txt' | xargs --no-run-if-empty cat  # Skip if empty
echo 'arg' | xargs -E 'stop' cat     # Stop at 'stop'
find . -type f | xargs -I {} sh -c 'echo "Processing {}"'  # Complex commands
```
- `-0` or `--null`: Null delimiter (use with -print0)
- `-I` or `--replace`: Replace string
- `-n` or `--max-args`: Max args per command
- `-d` or `--delimiter`: Delimiter
- `-P` or `--max-procs`: Parallel processes
- `-p` or `--interactive`: Prompt
- `-t` or `--verbose`: Print commands
- `--no-run-if-empty`: Skip empty input
- `-E` or `--eof`: EOF string

## Recommended Unattended Usage

```bash
#!/bin/bash

# Safe file processing with null delimiter
find . -name '*.log' -print0 | xargs -0 -I {} gzip {}

# Parallel processing
find . -name '*.jpg' -print0 | xargs -0 -P4 -I {} convert {} {}.png
```
