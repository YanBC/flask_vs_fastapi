import ast
import shutil
import subprocess
import sys

import pandas as pd

# ip_addr = sys.argv[1]
# saved_path = sys.argv[2]


_SIEGE_CMD = shutil.which("siege")
_URLS = ["io", "computation", "computation_hp"]
_IP_ADDRS = {"fastapi": "172.17.0.3", "flask": "172.17.0.4"}
_PORT = 8000
_MAX_CONCURRENCY = 65
_DURATION_IN_SECONDS = 5


def run_test(uri: str, csv_path: str):
    global _SIEGE_CMD, _MAX_CONCURRENCY, _DURATION_IN_SECONDS

    stats = dict()
    for concurrency in range(1, _MAX_CONCURRENCY):
        print(f"  concurrency: {concurrency}")
        full_cmd = f"{_SIEGE_CMD} {uri} -t {_DURATION_IN_SECONDS}s -c {concurrency}"
        completed = subprocess.run(full_cmd, shell=True, capture_output=True)
        result = ast.literal_eval(completed.stdout.decode())
        result["siege_c"] = concurrency
        stats[concurrency] = result

    columes = sorted(list(stats[1].keys()))
    data = []
    for concurrency in range(1, _MAX_CONCURRENCY):
        stat = stats[concurrency]
        dpoint = []
        for name in columes:
            dpoint.append(stat[name])
        data.append(dpoint)

    data_frame = pd.DataFrame(data, columns=columes)
    # print(data_frame)
    data_frame.to_csv(csv_path, index=False)


if __name__ == "__main__":
    est = len(_IP_ADDRS) * len(_URLS) * (_MAX_CONCURRENCY - 1) * _DURATION_IN_SECONDS
    print(f"estimate run time: {est} seconds")
    for app in _IP_ADDRS:
        for work_type in _URLS:
            addr = _IP_ADDRS[app]
            endpoint = f"http://{addr}:{_PORT}/{work_type}"
            saved_path = f"{work_type}.{app}.csv"

            print(f"running test on {endpoint}")
            run_test(endpoint, saved_path)
