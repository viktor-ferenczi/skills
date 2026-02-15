# elasticsearch (CLI tools)

**Platforms:** Multi-platform  
**Category:** Search Engine

## Quick Reference

| Goal | Command |
|------|---------|
| Health | `curl -s http://localhost:9200/_cluster/health` |
| Indices | `curl -s http://localhost:9200/_cat/indices` |
| Search | `curl -s -X POST http://localhost:9200/index/_search -d '{"query":{"match_all":{}}}'` |

## Elasticsearch CLI Tools

### elasticsearch-certutil
```bash
elasticsearch-certutil ca --out elastic-stack-ca.p12 --pass ""
elasticsearch-certutil cert --ca elastic-stack-ca.p12 --out elastic-certificates.p12 --pass ""
```

### elasticsearch-keystore
```bash
elasticsearch-keystore create
elasticsearch-keystore add bootstrap.password
elasticsearch-keystore list
```

### elasticsearch-plugin
```bash
elasticsearch-plugin list
elasticsearch-plugin install analysis-icu
elasticsearch-plugin remove analysis-icu
```

### elasticsearch-setup-passwords
```bash
elasticsearch-setup-passwords auto --batch --url http://localhost:9200
elasticsearch-setup-passwords interactive --batch --url http://localhost:9200
```

### elasticsearch-users
```bash
elasticsearch-users useradd admin -r superuser
elasticsearch-users passwd admin
elasticsearch-users roles admin
```

## HTTP API (curl)

```bash
# Cluster health
curl -s http://localhost:9200/_cluster/health?pretty

# List indices
curl -s http://localhost:9200/_cat/indices?v

# Create index
curl -s -X PUT http://localhost:9200/myindex -H 'Content-Type: application/json' -d '{"settings":{"number_of_shards":1}}'

# Index document
curl -s -X POST http://localhost:9200/myindex/_doc -H 'Content-Type: application/json' -d '{"field":"value"}'

# Search
curl -s -X POST http://localhost:9200/myindex/_search -H 'Content-Type: application/json' -d '{"query":{"match_all":{}}}'

# Delete index
curl -s -X DELETE http://localhost:9200/myindex
```
