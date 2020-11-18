import time
import os
import pandas

while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")
        print(data)
    else:
        print("ERROR! File not found.")
    time.sleep(10)