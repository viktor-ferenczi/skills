# wget

**Platforms:** Multi-platform  
**Category:** Data Transfer

## Quick Reference

| Goal | Command |
|------|---------|
| Silent download | `wget -q -O file url` |
| Quiet progress | `wget --progress=dot -O file url` |
| Continue partial | `wget -c -q url` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `http_proxy` | `http://proxy:port` | HTTP proxy |
| `https_proxy` | `http://proxy:port` | HTTPS proxy |

## Command-Line Flags

```bash
wget -q -O file https://example.com/file       # Quiet download
wget --progress=dot -O file url                # Dot progress
wget -c -q -O file url                         # Continue partial
wget -q --mirror --no-parent -P dir/ url       # Mirror directory
```
- `-q` or `--quiet`: Quiet mode
- `-O` or `--output-document`: Output file (- for stdout)
- `-c` or `--continue`: Resume partial
- `--progress=dot`: Dot progress
- `--no-verbose`: Errors only
- `--timeout=seconds`: Timeout
- `--tries=number`: Number of retries
- `--mirror`: Mirror mode
- `--no-parent`: Don't ascend to parent
- `-P` or `--directory-prefix`: Save directory
- `-N` or `--timestamping`: Only newer files
