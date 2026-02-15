# boundary (HashiCorp)

**Platforms:** Multi-platform  
**Category:** Identity-based Access

## Quick Reference

| Goal | Command |
|------|---------|
| Login | `boundary authenticate` |
| Connect | `boundary connect ssh -target-id ttcp_xxx` |
| List targets | `boundary targets list -scope-id p_xxx` |

## Command-Line Flags

```bash
boundary dev                         # Dev mode
boundary authenticate password -auth-method-id ampw_xxx -login-name admin
boundary authenticate oidc -auth-method-id amoidc_xxx
boundary accounts list -auth-method-id ampw_xxx
boundary auth-methods list -recursive
boundary connect ssh -target-id ttcp_xxx
boundary connect ssh -target-name mytarget -scope-name myscope
boundary connect rdp -target-id ttcp_xxx
boundary connect http -target-id ttcp_xxx
boundary connect postgres -target-id ttcp_xxx
boundary targets list -scope-id p_xxx
boundary targets authorize-session -id ttcp_xxx
boundary hosts list -host-catalog-id hcst_xxx
boundary host-catalogs list -scope-id p_xxx
boundary sessions list -scope-id p_xxx
boundary sessions cancel -id s_xxx
boundary users list -recursive
boundary roles list -scope-id p_xxx
boundary groups list -scope-id p_xxx
boundary scopes list -recursive
boundary database init -config boundary.hcl
boundary database migrate -config boundary.hcl
boundary server -config boundary.hcl
```
- `-addr`: Boundary address (BOUNDARY_ADDR)
- `-token`: Auth token (BOUNDARY_TOKEN)
- `-tls-insecure`: Skip TLS verification
- `-format`: Output format

## Environment Variables

```bash
export BOUNDARY_ADDR='https://boundary.example.com'
export BOUNDARY_TOKEN='at_xxx'
export BOUNDARY_TLS_INSECURE=true
```
