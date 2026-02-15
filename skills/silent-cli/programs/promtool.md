# promtool

**Platforms:** Multi-platform  
**Category:** Monitoring (Prometheus)

## Recommended Unattended Usage

```bash
#!/bin/bash

# Validate config and rules (non-interactive, exit code based)
promtool check config prometheus.yml || exit 1
promtool check rules /path/to/rules/*.yml || exit 1
promtool test rules test.yml || exit 1
```
