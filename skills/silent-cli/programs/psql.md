# psql (PostgreSQL client)

**Platforms:** Multi-platform  
**Category:** Database Client

## Quick Reference

| Goal | Command |
|------|---------|
| Quiet | `psql -q -c 'SELECT 1'` |
| Tuples only | `psql -t -c 'SELECT 1'` |
| CSV output | `psql -A -F, -t -c 'SELECT *'` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `PGPASSWORD` | `pass` | Password (avoids interactive prompt) |

## Command-Line Flags

```bash
psql -c "SELECT 1"                   # Execute command (non-interactive)
psql -f script.sql                   # Execute file (non-interactive)
psql -A -F, -c "SELECT *"            # CSV output (machine-readable)
psql -t -c "SELECT 1"                # Tuples only (no header/footer)
psql -q -c "SELECT 1"                # Quiet
psql -X -c "SELECT 1"                # No .psqlrc (predictable output)
psql --pset pager=off -c "SELECT *"  # Disable pager (non-interactive safe)
```
- `-c` or `--command`: Execute command (non-interactive)
- `-f` or `--file`: Execute file (non-interactive)
- `-A` or `--no-align`: Unaligned output (machine-readable)
- `-F` or `--field-separator`: Field separator
- `-t` or `--tuples-only`: No header/footer (machine-readable)
- `-q` or `--quiet`: Quiet
- `-X` or `--no-psqlrc`: Skip startup file (predictable output)
- `--pset pager=off`: Disable pager

## Recommended Unattended Usage

```bash
#!/bin/bash

export PGHOST=localhost
export PGUSER=postgres
export PGPASSWORD=secret

# CSV output
psql -A -F, -t -c "SELECT * FROM table" database > output.csv

# Quiet execution
psql -q -X -c "CREATE TABLE test (id int);" database
```
