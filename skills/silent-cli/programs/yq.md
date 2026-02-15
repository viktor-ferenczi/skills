# yq

**Platforms:** Multi-platform  
**Category:** YAML Processor

## Quick Reference

| Goal | Command |
|------|---------|
| Read value | `yq '.key' file.yaml` |
| Update value | `yq '.key = "value"' file.yaml` |
| Convert JSON | `yq -o json file.yaml` |

## Command-Line Flags

```bash
yq '.key' file.yaml                  # Read value
yq '.key.subkey' file.yaml           # Nested value
yq '.key' file.yaml -r               # Raw output
yq '.key = "value"' file.yaml        # Update (output to stdout)
yq -i '.key = "value"' file.yaml     # Update in-place
yq -P file.json                      # Convert JSON to YAML
yq -o json file.yaml                 # Convert YAML to JSON
yq eval-all '. as $item ireduce ({}; . * $item )' f1.yaml f2.yaml  # Merge
```
- `-r` or `--raw-output`: Raw output
- `-i` or `--inplace`: Edit in place
- `-P` or `--prettyPrint`: Pretty print
- `-o` or `--output-format`: Output format (json, yaml)
- `-e` or `--exit-status`: Exit 1 if no matches
- `-n` or `--null-input`: Use null input
- `-p` or `--input-format`: Input format
