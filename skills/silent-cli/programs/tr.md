# tr

**Platforms:** Multi-platform  
**Category:** Text Translation

## Recommended Unattended Usage

```bash
#!/bin/bash

# Clean input: remove non-printable, squeeze spaces
cleaned=$(echo "$input" | tr -cd '[:print:]' | tr -s ' ')

# Generate random password
tr -dc 'a-zA-Z0-9' < /dev/urandom | head -c 32
```
