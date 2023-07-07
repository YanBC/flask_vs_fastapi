# Build and create fastapi container
```bash
docker build -t compare:fastapi -f fastapi.Dockerfile .
docker run --init --rm -d --cpus 2 --name compare_fastapi compare:fastapi
```
