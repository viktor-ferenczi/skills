# base64

**Platforms:** Multi-platform  
**Category:** Encoding

## Quick Reference

| Goal | Command |
|------|---------|
| Encode | `base64 file` |
| Decode | `base64 -d file` |
| Encode string | `echo -n 'text' | base64` |

## Command-Line Flags

```bash
base64 file                          # Encode file
base64 -w 0 file                     # No line wrapping
echo -n 'text' | base64              # Encode string
base64 -d file.b64                   # Decode
base64 -d <<< "dGV4dA=="             # Decode here-string
echo 'dGV4dA==' | base64 -d          # Decode from pipe
```

### Linux (GNU coreutils)
- `-d` or `--decode`: Decode
- `-w` or `--wrap=COLS`: Wrap at COLS (0 for no wrap)
- `-i` or `--ignore-garbage`: Ignore non-alphabet chars

### macOS (BSD)
- `-d` or `-D`: Decode
- `-b`: Decodes base64, outputs hexdump
- `-i`: Read from file
- `-o`: Write to file

## Recommended Unattended Usage

```bash
#!/bin/bash

# Encode credentials for HTTP Basic Auth
auth=$(echo -n 'user:pass' | base64 -w 0)

# Decode secret
secret=$(base64 -d <<< "$encoded_secret")

# Encode file
cat file.bin | base64 -w 0 > file.b64
```
