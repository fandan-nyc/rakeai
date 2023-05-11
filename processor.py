from padelpy import from_smiles
import time

import pandas as pd

class Processor:
    def __init__(self, data_input: pd.DataFrame):
        self.data = data_input

    def process(self):
        count = 0
        col_list = self.data["SMILES"].values.tolist()
        print(len(col_list))
        print("start")
        for i in range(len(col_list) // 10 ):
            curr = col_list[i*10 : (i+1)*10]
            start = time.time()
            descriptors = from_smiles(curr, True, True, timeout = 60, maxruntime  = -1, threads  = 10)
            end = time.time()
            print("{},{}".format(i, end - start))

   #     for row in range(len(self.data.index)):
   #         smile_str = self.data.loc[row]['SMILES']
   #         self.__calc_descriptor(smile_str)
   #         count += 1


    def calc_descriptor(self, row: int, smile_str: str) ->  pd.DataFrame:
        descriptors = from_smiles(smile_str)
        start = time.time()
        descriptors = from_smiles(curr, True, True, timeout = 60, maxruntime  = -1, threads  = 10)
        end = time.time()
        print("{},{}".format(row, end - start))
