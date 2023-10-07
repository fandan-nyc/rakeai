from padelpy import from_smiles
import pandas as pd
import json
import tensorflow as tf
import numpy as np

def calc_descriptor(smile):
    bothSignal = from_smiles(smile, descriptors=True, fingerprints=True, timeout = 10)
    df: DataFrame = pd.DataFrame.from_dict([bothSignal])
    with open(f"util/columns", "r") as f:
        data_str = f.read()
        data = json.loads(data_str)
    data = df[data].fillna(0)
    return tf.constant(data.values.astype(np.float32))

if __name__ == "__main__":
    feature = calc_descriptor("CN(C)CCCN(CCC(OCCSSCCCCCCCCCC)=O)CCC(OCCSSCCCCCCCCCC)=O")
    # exit()
    from keras.models import load_model
    model = load_model("/home/yangfan/workspace/modelapi/model")
    res = model.predict(feature)
    print(res)
