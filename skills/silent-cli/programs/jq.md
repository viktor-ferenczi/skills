# jq

**Platforms:** Multi-platform  
**Category:** JSON Processor

## Quick Reference

| Goal | Command |
|------|---------|
| Pretty print | `jq . file.json` |
| Extract field | `jq '.field' file.json` |
| Compact | `jq -c '.field' file.json` |

## Command-Line Flags

```bash
jq . file.json                       # Pretty print
jq -c . file.json                    # Compact
jq -r '.field' file.json             # Raw output (no quotes)
jq -s '.[]' file*.json               # Slurp (array input)
jq -n '{"key": "value"}'             # Null input
jq --arg var value '. + {$var}' file.json  # Pass variable
jq --slurpfile var file.json '. + $var'    # Read file as var
jq --from-file filter.jq data.json   # Read filter from file
jq -f filter.jq data.json            # Same
```
- `-c` or `--compact-output`: Compact
- `-r` or `--raw-output`: Raw strings (no quotes)
- `-R` or `--raw-input`: Read raw strings
- `-s` or `--slurp`: Read all inputs into array
- `-n` or `--null-input`: Use null as input
- `-f` or `--from-file`: Filter from file
- `--arg name value`: Pass string variable
- `--argjson name JSON`: Pass JSON variable
- `--slurpfile name file`: Read JSON file as variable
