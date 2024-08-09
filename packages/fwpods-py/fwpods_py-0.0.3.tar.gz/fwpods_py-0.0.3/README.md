# FWPODS PY

[![github](https://shields.io/badge/github-green?logo=github&color=informational&style=for-the-badge)](https://github.com/fishappy0/FWPODS-Core)

</br><p style="font-size:23px"> A python implementation library based on the paper named "A sliding window-based approach for mining frequent weighted patterns over data streams<p>A

```
H. Bui, T. -A. Nguyen-Hoang, B. Vo, H. Nguyen and T. Le, "A Sliding Window-Based Approach for Mining Frequent Weighted Patterns Over Data Streams," in IEEE Access, vol. 9, pp. 56318-56329, 2021, doi: 10.1109/ACCESS.2021.3070132. keywords: {Data mining;Data models;Databases;Urban areas;Itemsets;Mathematical model;Information technology;Pattern mining;data streams;frequent weighted patterns;sliding window model},
```

# Example usage

Using the existing window manager to add a transaction to the window and start the mining process

```py
from random import randint
from collections import OrderedDict
from fwpods_py.classes import *

FWPs = []
runtimes = []
item_weights = {}

window_size = 45000
min_ws = 0.8
panel_size = 1
twm = weights_manager()

transactions = OrderedDict()
count = 0
# This sample dataset can be found on the SPMF website at https://www.philippe-fournier-viger.com/spmf/index.php?link=datasets.php
ds_name = "retail"
with open(f"./datasets/{ds_name}.txt", "r") as f:
    t_id = "1"
    for line in f:
        if count == window_size + 50:
            break
        transactions[t_id] = line.strip().split()
        for item in line.strip().split():
            if item in item_weights:
                continue
            else:
                item_weights[item] = randint(1, 10)
        t_id = str(int(t_id) + 1)
        count += 1

win_man = window_manager(None, window_size, panel_size, min_ws)
win_man.new_weights(item_weights)

# Simulate a data stream
for t_id, t_items in transactions.items():
    win_man.add_transaction(t_id, t_items)

res_location = f"./results/{ds_name}/"
with open(f"{ds_name}_runtime_total.txt", "w") as f:
    for ttr in win_man.total_runtime:
        f.write(f"{ttr.total_seconds()}\n")

with open(f"{ds_name}_runtime_algo.txt", "w") as f:
    for art in win_man.algo_runtime:
        f.write(f"{art.total_seconds()}\n")

with open(f"{ds_name}_runtime_tree.txt", "w") as f:
    for tr in win_man.tree_build_time:
        f.write(f"{tr.total_seconds()}\n")
```
