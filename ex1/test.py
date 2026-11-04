import pandas as pd
import numpy as np

x_data = np.arange(5)

df = pd.DataFrame({"Time": x_data})
df["Manipulated"] = df["Time"] + 50

print(df)