# prometheus-service-discovery

## Install Requirements
```
pip install -r requirements.yaml
```
## File Based

### Start first metrics server

```
fastapi dev server1.py --host localhost --port 9123
```

### Start Prometheus (listens on default port 9090)

```
./prometheus --config.file=prometheus.yml
```

### Start second metrics server

```
fastapi dev server2.py --host localhost --port 9125
```

## API Based

If not started already, start both metrics servers. In separate terminal windows:

```
fastapi dev server1.py --host localhost --port 9123
fastapi dev server2.py --host localhost --port 9125
```

### Start target server

```
fastapi dev target-server.py --host localhost --port 8123
```

### Start Prometheus

```
./prometheus --config.file=prometheus.yml
fastapi dev
```
