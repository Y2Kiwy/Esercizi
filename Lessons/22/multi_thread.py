from typing import *

import json

from datetime import *
from time import *

import os

import threading, time

def find_resource_stat(file_path: str, stat_key: str) -> Any:
    time.sleep(1)
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)

    print(json_data[stat_key])

# ----------------------------------------------------------------------------

phase_ids: list[int] = ['0', '1', '2']

json_dirs_path: str = "Simco-Utils\\Tkinter\\P1\\build\\data\\api\\resources"
resource_stat_key: str = "producedAnHour"

# ----------------------------------------------------------------------------



# Data extraction without multi-threading ------------------------------------

print(f"Starting data extraction without multithreading at: {datetime.now()}")

start: float = time.time()

for id in phase_ids:

    json_path: str = os.path.join(json_dirs_path, id, "1.json")

    find_resource_stat(json_path, resource_stat_key)

end: float = time.time()

print(f"Finished data extraction without multithreading at: {datetime.now()} -> {end - start}s")

# ----------------------------------------------------------------------------

print("\n\n") # Formatting

# Data extraction with multi-threading ---------------------------------------

print(f"Starting data extraction with multithreading at: {datetime.now()}")

start: float = time.time()

threads: list = list()

for id in phase_ids:

    json_path: str = os.path.join(json_dirs_path, id, "1.json")

    x = threading.Thread(target=find_resource_stat, args=(json_path, resource_stat_key))

    threads.append(x)

    x.start()

for thread in threads:
    thread.join()

end: float = time.time()

print(f"Finished data extraction with multithreading at: {datetime.now()} -> {end - start}s")

# ----------------------------------------------------------------------------
