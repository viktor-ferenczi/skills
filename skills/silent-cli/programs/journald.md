# systemd-journald

**Platforms:** Linux (systemd)  
**Category:** System Logging

**Note:** journald is a system service, not a CLI tool. Use `journalctl` to query logs.

## Configuration

Edit `/etc/systemd/journald.conf`:

```ini
[Journal]
Storage=persistent
Compress=yes
SystemMaxUse=500M
SystemMaxFileSize=100M
MaxRetentionSec=1month
ForwardToSyslog=no
```

## Restart journald

```bash
systemctl restart systemd-journald
```

## Check status

```bash
systemctl status systemd-journald
```

## Journal directories

- Runtime: `/run/log/journal/`
- Persistent: `/var/log/journal/`

## Permissions

```bash
# Add user to systemd-journal group for access
usermod -a -G systemd-journal username
```
