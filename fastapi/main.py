import asyncio
import time

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    await asyncio.sleep(0.05)
    return "Hello World"
