import pandas as pd

class DataLoader:
    def __init__(self, path: str = ""):
        if path:
            load(data)

    def loadData(self, path: str) -> None:
        self.data = pd.read_csv(path)
    
    def getData(self) -> pd.DataFrame:
        return self.data
