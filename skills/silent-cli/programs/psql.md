# psql (PostgreSQL client)

**Platforms:** Multi-platform  
**Category:** Database Client

## Quick Reference

| Goal | Command |
|------|---------|
| Execute SQL | `psql -c 'SELECT 1'` |
| File | `psql -f script.sql` |
| CSV output | `psql -A -F, -c 'SELECT *'` |

## Environment Variables

| Variable | Value | Description |
|----------|-------|-------------|
| `PGHOST` | `localhost` | Host |
| `PGPORT` | `5432` | Port |
| `PGUSER` | `postgres` | Username |
| `PGPASSWORD` | `pass` | Password |
| `PGDATABASE` | `db` | Database |

## Command-Line Flags

```bash
psql -c "SELECT 1"                   # Execute command
psql -f script.sql                   # Execute file
psql -A -F, -c "SELECT *"            # CSV output
psql -t -c "SELECT 1"                # Tuples only (no header/footer)
psql -q -c "SELECT 1"                # Quiet
psql -v var=value -c "SELECT :var"   # Set variable
psql -X -c "SELECT 1"                # No .psqlrc
psql --pset pager=off -c "SELECT *"  # Disable pager
```
- `-c` or `--command`: Execute command
- `-f` or `--file`: Execute file
- `-A` or `--no-align`: Unaligned output
- `-F` or `--field-separator`: Field separator
- `-t` or `--tuples-only`: No header/footer
- `-q` or `--quiet`: Quiet
- `-v` or `--set`: Set variable
- `-X` or `--no-psqlrc`: Skip startup file
- `--pset`: Set printing option

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
