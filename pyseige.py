import ast
import shutil
import subprocess
import sys

import pandas as pd

url = sys.argv[1]
saved_path = sys.argv[2]
siege_cmd = shutil.which("siege")
_MAX_CONCURRENCY = 33

stats = dict()

for concurrency in range(1, _MAX_CONCURRENCY):
    full_cmd = f"{siege_cmd} {url} -t 5s -c {concurrency}"
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
data_frame.to_csv(saved_path, index=False)
