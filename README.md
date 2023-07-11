# Build and create fastapi container
```bash
docker build -t compare:fastapi -f fastapi.Dockerfile .
docker run --init --rm -d --cpus 2 --name compare_fastapi compare:fastapi
```

# Build and create flask container
```bash
docker build -t compare:flask -f flask.Dockerfile .
docker run --init --rm -d --cpus 2 --name compare_flask compare:flask
```
