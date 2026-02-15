# sqlite3

**Platforms:** Multi-platform  
**Category:** Database Client (SQLite)

## Quick Reference

| Goal | Command |
|------|---------|
| Batch mode | `sqlite3 -batch db.sqlite 'SELECT 1'` |
| CSV output | `sqlite3 -csv -noheader db.sqlite 'SELECT *'` |
| JSON output | `sqlite3 -json db.sqlite 'SELECT *'` |

## Command-Line Flags

- `-batch`: Batch mode — disables interactive prompt, exits on errors
- `-csv`: CSV output — machine-readable
- `-json`: JSON output — machine-readable
- `-line`: Line mode (key: value) — machine-readable
- `-list`: List mode — machine-readable
- `-noheader`: Suppress column headers
- `-header`: Include column headers

## Recommended Unattended Usage

```bash
#!/bin/bash

# CSV export
sqlite3 -csv -noheader db.sqlite "SELECT * FROM table" > output.csv

# JSON export
sqlite3 -json db.sqlite "SELECT * FROM table" > output.json

# Batch import
sqlite3 db.sqlite <<EOF
BEGIN;
CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, msg TEXT);
INSERT INTO logs (msg) VALUES ('test');
COMMIT;
EOF
```
