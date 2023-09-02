
import tensorflow as tf
import pandas as pd
from tensorflow.keras.regularizers import l2
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam
import numpy as np
from collections import defaultdict
from keras.layers import BatchNormalization
from keras.layers import LayerNormalization
from tensorflow.keras.regularizers import l2
from keras.callbacks import EarlyStopping


print(tf.__version__)
# To make the results reproducible, set the random seed value.
tf.random.set_seed(22)
np.random.seed(42)


df = pd.read_csv("./dataset_07072023.csv")

# trim columns with NaN
nan_columns = df.columns[df.isna().any()].tolist()

# Delete empty columns
dataset = df.drop(nan_columns, axis=1)
training_dataset, temp_dataset = train_test_split(dataset, test_size=0.20, random_state=1)
validation_dataset, testing_dataset = train_test_split(temp_dataset, test_size=0.50, random_state=1)



x_train, y_train = training_dataset.iloc[:, 3:], training_dataset.iloc[:, 2]
cols = x_train.columns
# with open("./cols", "w") as f:
#   import json
#   f.write(json.dumps(list(cols)))
# exit()
x_validation, y_validation = validation_dataset.iloc[:, 3:], validation_dataset.iloc[:, 2]
x_test, y_test = testing_dataset.iloc[:, 3:], testing_dataset.iloc[:, 2]

print(x_train.loc[0, ].size)
exit()

x_dic = defaultdict(list)
y_dic = defaultdict(list)
all_doi = set()
for i in range(len(validation_dataset)):
  full_name = validation_dataset.iloc[i, 0]
  doi = full_name.split('*')[0]
  all_doi.add(doi)
  x = x_validation.iloc[i, :]
  y = y_validation.iloc[i]
  x_dic[doi].append(x)
  y_dic[doi].append(y)
print(len(validation_dataset), len(all_doi))
model = tf.keras.models.Sequential([
    BatchNormalization(),
    LayerNormalization(),
    tf.keras.layers.Dense(1024, activation='relu', input_shape=(1448,), kernel_regularizer=l2(0.03)), # L2
    tf.keras.layers.Dense(512, activation='relu', kernel_regularizer=l2(0.03)), # L2
    tf.keras.layers.Dense(256, activation='relu', kernel_regularizer=l2(0.03)), # L2
    tf.keras.layers.Dense(128, activation='relu', kernel_regularizer=l2(0.03)), # L2
    tf.keras.layers.Dense(1, activation='sigmoid',kernel_regularizer=l2(0.03))
])
# Compile the model with logistic loss
optimizer = Adam(learning_rate=0.0001)
model.compile(optimizer=optimizer,
              #loss=precision_loss,
              loss='binary_crossentropy',
              metrics=['accuracy', tf.keras.metrics.Precision()])


# Define early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
# Train the model
model.fit(x_train, y_train, epochs=400, batch_size=256, validation_data=(x_validation, y_validation), callbacks=[early_stopping])
# Evaluate the model
validation_loss, validation_acc, validation_precision = model.evaluate(x_validation, y_validation)
test_loss, test_acc, test_precision = model.evaluate(x_test, y_test)

model.save("./model", overwrite=True, save_format="tf")