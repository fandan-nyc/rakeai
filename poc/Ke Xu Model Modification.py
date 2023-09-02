#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install -q seaborn')


# In[ ]:


# import all packages
import tensorflow as tf
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
import sklearn.metrics as sk_metrics
import tempfile
import os
from tensorflow.keras.regularizers import l2
from sklearn.model_selection import train_test_split
from tensorflow.keras.optimizers import Adam
import numpy as np


# In[ ]:


print(tf.__version__)
# To make the results reproducible, set the random seed value.
tf.random.set_seed(22)
np.random.seed(42)


# # Logistic regression with manually defined 0, 1 labels
# 

# In[ ]:


# upload dataset CSV file from local
from google.colab import files
uploaded = files.upload()


# In[ ]:


import io
# you can download the dataset file from shared drive
df = pd.read_csv(io.BytesIO(uploaded[next(iter(uploaded))]))


# In[ ]:


# trim columns with NaN
nan_columns = df.columns[df.isna().any()].tolist()

# Delete empty columns
dataset = df.drop(nan_columns, axis=1)


# In[ ]:


dataset


# #Random split

# In[ ]:


training_dataset, temp_dataset = train_test_split(dataset, test_size=0.20, random_state=1)


validation_dataset, testing_dataset = train_test_split(temp_dataset, test_size=0.50, random_state=1)


# In[ ]:


testing_dataset


# In[ ]:


x_train, y_train = training_dataset.iloc[:, 3:], training_dataset.iloc[:, 2]
x_validation, y_validation = validation_dataset.iloc[:, 3:], validation_dataset.iloc[:, 2]
x_test, y_test = testing_dataset.iloc[:, 3:], testing_dataset.iloc[:, 2]


# In[ ]:


from collections import defaultdict
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


# In[ ]:


# Define the model architecture
from keras.layers import BatchNormalization
from keras.layers import LayerNormalization
from tensorflow.keras.regularizers import l2

model = tf.keras.models.Sequential([
    BatchNormalization(),
    LayerNormalization(),
    tf.keras.layers.Dense(1024, activation='relu', input_shape=(1448,), kernel_regularizer=l2(0.03)), # L2
    tf.keras.layers.Dense(512, activation='relu', kernel_regularizer=l2(0.03)), # L2
    tf.keras.layers.Dense(256, activation='relu', kernel_regularizer=l2(0.03)), # L2
    tf.keras.layers.Dense(128, activation='relu', kernel_regularizer=l2(0.03)), # L2
    tf.keras.layers.Dense(1, activation='sigmoid',kernel_regularizer=l2(0.03))
])


# In[ ]:


# Compile the model with logistic loss
optimizer = Adam(learning_rate=0.0001)

model.compile(optimizer=optimizer,
              #loss=precision_loss,
              loss='binary_crossentropy',
              metrics=['accuracy', tf.keras.metrics.Precision()])


# In[ ]:


from keras.callbacks import EarlyStopping

# Define early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)


# In[ ]:


# Train the model
model.fit(x_train, y_train, epochs=400, batch_size=256, validation_data=(x_validation, y_validation), callbacks=[early_stopping])


# In[ ]:


# Evaluate the model
validation_loss, validation_acc, validation_precision = model.evaluate(x_validation, y_validation)


# In[ ]:


test_loss, test_acc, test_precision = model.evaluate(x_test, y_test)


# In[ ]:


y_validation


# In[ ]:


# check the precision in each paper
i = 1
result_dic = {}
for doi in all_doi:
  x = pd.DataFrame(x_dic[doi])
  y = pd.DataFrame(y_dic[doi])
  print(i, doi)
  validation_loss, validation_acc, validation_precision = model.evaluate(x, pd.DataFrame(y))
  y_pred = model.predict(x)
  true_positives = tf.math.count_nonzero(tf.logical_and(tf.equal(y, 1), tf.equal(tf.round(y_pred), 1)), axis=0)
  predicted_positives = tf.math.count_nonzero(tf.equal(tf.round(y_pred), 1), axis=0)
  total_positives = tf.math.count_nonzero(tf.equal(y, 1), axis=0)
  print(true_positives/predicted_positives)
  print("true_positive: ", true_positives)
  print("predicted_positive: ", predicted_positives)
  print("total_positives: ", total_positives)
  result_dic[doi] = (validation_precision, true_positives, predicted_positives, total_positives)
  i += 1


# In[ ]:


for doi in result_dic:
  print(doi)
  for x in result_dic[doi]:
   tf.print(x)


# In[ ]:


for x in result_dic['ja301621z']:
   tf.print(x)


# In[ ]:


y_pred = tf.squeeze(model.predict(x_validation))
true_positives = tf.math.count_nonzero(tf.logical_and(tf.equal(y_validation, 1), tf.equal(tf.round(y_pred), 1)), axis=0)
predicted_positives = tf.math.count_nonzero(tf.equal(tf.round(y_pred), 1), axis=0)
print(true_positives/predicted_positives)
print("true_positive: ", true_positives)
print("predicted_positive: ", predicted_positives)


# ## Predictions on LongChuan data

# In[ ]:


# upload dataset CSV file from local
from google.colab import files
uploaded = files.upload()


# In[ ]:


import io
# you can download the dataset file from shared drive
test_dataset = pd.read_csv(io.BytesIO(uploaded[next(iter(uploaded))]))


# In[ ]:


test_dataset


# In[ ]:


test_dataset_trim = test_dataset.drop(nan_columns[2:], axis=1)


# In[ ]:


test_dataset_trim


# In[ ]:


# Evaluate the model
predict = model.predict(test_dataset_trim.iloc[:, 2:])


# In[ ]:


tf.math.count_nonzero(tf.equal(tf.round(predict), 1))


# In[ ]:


predict[:]


# In[ ]:


import numpy as np

def save_array_to_csv(array, filename, download=False):
    array = np.array(array).reshape(-1, 1)
    df = pd.DataFrame(array, columns=['Values'])
    df.to_csv(filename, index=False)
    files.download(filename)


save_array_to_csv(predict[:], 'array.csv')

