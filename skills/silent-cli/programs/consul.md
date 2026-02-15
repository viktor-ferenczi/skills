# consul (HashiCorp)

**Platforms:** Multi-platform  
**Category:** Service Discovery

## Quick Reference

| Goal | Command |
|------|---------|
| Agent | `consul agent -dev` |
| Members | `consul members` |
| Services | `consul catalog services` |
| KV get | `consul kv get key` |

## Command-Line Flags

```bash
consul agent -dev                    # Development mode
consul agent -server -bootstrap-expect=3 -config-dir=/etc/consul
consul members                       # List members
consul members -wan                  # WAN members
consul info                          # Agent info
consul monitor                       # Log monitor
consul leave                         # Graceful leave
consul catalog services              # List services
consul catalog nodes                 # List nodes
consul catalog nodes -service=web    # Nodes for service
consul health service web            # Health check service
consul health node mynode            # Health check node
consul kv get mykey                  # Get key
consul kv get -recurse myprefix/     # Get recursively
consul kv put mykey myvalue          # Put key
consul kv delete mykey               # Delete key
consul kv export myprefix/           # Export keys
consul kv import @backup.json        # Import keys
consul intention get web db          # Get intention
consul intention create web db       # Create intention
consul intention delete web db       # Delete intention
consul acl bootstrap                 # Bootstrap ACL
consul acl policy list               # List ACL policies
consul acl token create -policy-name=web
consul tls ca create                 # Create CA
consul tls cert create -server       # Create server cert
consul snapshot save backup.snap     # Create snapshot
consul snapshot restore backup.snap  # Restore snapshot
consul operator raft list-peers      # List raft peers
```
- `-datacenter`: Datacenter
- `-http-addr`: HTTP API address
- `-token`: ACL token
- `-datacenter`: Target datacenter

## Recommended Unattended Usage

```bash
#!/bin/bash

# Non-interactive bootstrap
consul acl bootstrap -format=json 2>/dev/null

# Get service health
consul health service web -passing-only
```
