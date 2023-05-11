from data_loader import DataLoader
from processor import Processor
from multiprocessing import Pool, Lock
from padelpy import from_smiles
import time
import multiprocessing as mp

import pandas as pd

def calc_descriptor(data):
    try:
        row = data[0]
        smile = data[1]
        print("start {}".format(row))
        start = time.time()
        bothSignal  =from_smiles(smile, descriptors = True, fingerprints =  True, timeout = 10)
        end = time.time()
        print("both {},{}".format(row, end - start))
        print("size:" + str(len(bothSignal)))
    except:
        print("{},{}".format(row, "faild !"))

if __name__ == "__main__":
    print(mp.cpu_count())
    print("1")
    x = DataLoader()
    # x.loadData('/Users/lisipu/src/github/aurigian/data/hard_data.csv')
    x.loadData('/content/aurigian/data/hard_data.csv')
    y = x.getData()
    print("2")
    processor = Processor(y)
    data_for_concurrency = []
    for row in range(len(y.index)):
        smile_str = y.loc[row]['SMILES']
        data_for_concurrency.append((row, smile_str))
    print("3")
    data_for_concurrency.reverse()
    with Pool(2) as p:
        p.map(calc_descriptor, data_for_concurrency)
    #calc_descriptor(data_for_concurrency[0])

