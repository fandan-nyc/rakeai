import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy as np

public_data = pd.read_csv ('data/data_06242023.csv')
longchuan = pd.read_csv("data/longchuan1_processed.csv")
column_for_plot =["MW", "ALogP", "XLogP", "SpDiam_Dzp", "SpDiam_Dzi", "VR3_Dzi", "SpDiam_DzZ", "SssNH", "SsssN"]

effective = public_data.loc[public_data['Binary_efficiency'] == 1]
print(len(effective))

fig, axes = plt.subplots(3, 3, figsize=(12, 6))  # 3 rows, 3 columns for 3 plots

for i, ax in enumerate(axes.flat):
    bp = effective.boxplot(column=column_for_plot[i], ax=ax)
    value = longchuan.at[3, column_for_plot[i]]
    ax.plot(1, value, 'ro')
    # ax.set_title(column_for_plot[i])

plt.tight_layout()
plt.savefig('box_plots.jpg', dpi=300)
plt.show()

#plt.xticks(rotation=45, ha='right')  # Rotate the labels by 45 degrees and align them to the right
#plt.tight_layout()  # Adjust spacing between subplots



