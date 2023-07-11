import time

import numpy as np

from flask import Flask

np.random.seed(0)
matW = np.random.rand(512, 1024)
matX = np.random.rand(1024, 512)
matB = np.random.rand(512, 512)

app = Flask(__name__)


def work_computational_hp():
    global matW, matX, matB
    Y = np.matmul(matW, matX) + matB


def work_computational():
    s = 0
    for i in range(65536):
        s += i**2


@app.route("/", methods=["GET"])
def root():
    return "Up and running\n"


@app.route("/computation", methods=["GET"])
def computation():
    work_computational()
    return "Done computation\n"


@app.route("/computation_hp", methods=["GET"])
def computation_hp():
    work_computational_hp()
    return "Done computation_hp\n"


@app.route("/io", methods=["GET"])
def io():
    time.sleep(0.05)
    return "Done io\n"
