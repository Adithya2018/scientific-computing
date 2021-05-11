# Display sum of column (0, 0, 0, 0)

import pandas as pd
import numpy as np
df = pd.read_csv("ScientificComputing.csv")
arr = df.to_numpy()
num_rows, num_cols = arr.shape
print("Sum of arr : ", (np.sum(arr, axis=1))[0])
