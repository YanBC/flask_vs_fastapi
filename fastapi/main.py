import asyncio

import numpy as np

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

np.random.seed(0)
matW = np.random.rand(512, 1024)
matX = np.random.rand(1024, 512)
matB = np.random.rand(512, 512)

app = FastAPI(default_response_class=PlainTextResponse)


def work_computational_hp():
    global matW, matX, matB
    Y = np.matmul(matW, matX) + matB


def work_computational():
    s = 0
    for i in range(65536):
        s += i**2


@app.get("/")
async def root():
    return "Up and running\n"


@app.get("/computation")
async def computation():
    work_computational()
    return "Done computation\n"


@app.get("/computation_hp")
async def computation_hp():
    work_computational_hp()
    return "Done computation_hp\n"


@app.get("/io")
async def io():
    await asyncio.sleep(0.05)
    return "Done io\n"
