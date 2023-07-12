# Performance: FastAPI vs Flask

## About FastAPI and Flask
- General data flow from the bottom up: pysical -> datalink -> IP -> transport -> application (HTTP -> WSGI/ASGI data)
- More specifically, in the application layer: Nginx -> WSGI/ASGI middleware (e.g. uWSGI/Gunicorn/uvicorn) -> Flask/Django/FastAPI
- WSGI: HTTP request -> WSGI environ
- WSGI middlewares like uWSGI start and manage multiple Flask applications to handle client requests
- Deep in the WSGI specification, there is a limitation that constrains web apps to use one worker to handle a client request/response cycle.
- In other words, even if you create a beautifully written async Flask handler, [it would not change the number of concurrent request you web app can handle](https://flask.palletsprojects.com/en/2.3.x/async-await/#performance).

## metrics

## start containers
```bash

# fastapi container
docker run --init --rm -itd \
    --name compare_fastapi \
    -v $(pwd)/fastapi:/fastapi \
    --cpus 4 \
    --memory 512M \
    --memory-swap -1 \
    compare:fastapi \
    bash

# flask container
docker run --init --rm -itd \
     --name compare_flask \
    -v $(pwd)/flask:/flask \
    --cpus 4 \
    --memory 512M \
    --memory-swap -1 \
    compare:flask \
    bash

# run fastapi app
docker exec -it compare_fastapi uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2
# in another terminal, run flask app
docker exec -it compare_flask uwsgi -w hello:app --http 0.0.0.0:8000 --master --workers 2
```

## io bound case
-

## computation bound
