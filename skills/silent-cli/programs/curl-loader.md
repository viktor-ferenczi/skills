# curl-loader

**Platforms:** Linux  
**Category:** Load Testing

## Quick Reference

| Goal | Command |
|------|---------|
| Config file | `curl-loader -f config.conf` |
| Verbose | `curl-loader -v -f config.conf` |
| URL list | `curl-loader -f urls.txt` |

## Configuration File

```ini
########### GENERAL SECTION #################
CYCLES_NUM=1
USERS_NUM=10
USER_AGENT= curl-loader/0.56
LOGIN_URL=http://localhost/login.cgi
LOGIN_POST_DATA=username=root&passwd=admin

########### URLs SECTION ####################
URL=http://localhost/index.html
URL=http://localhost/page.html
```

## Command-Line Flags

```bash
curl-loader -f config.conf           # Run with config
curl-loader -v -f config.conf        # Verbose
curl-loader -d 10 -f config.conf     # Run for 10 seconds
curl-loader -r 5 -f config.conf      # 5 rounds
```
- `-f`: Configuration file
- `-v`: Verbose
- `-d`: Duration in seconds
- `-r`: Number of rounds
