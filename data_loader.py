import pandas as pd

print(df.to_string()) 

class DataLoader:
    def __init__(self):
        pass

    def loadData(self, path: str) -> None:
        self.data = pd.read_csv(path)
    
    def getData(self):
        return self.data
