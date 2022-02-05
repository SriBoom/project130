import pandas as pd
import csv

df=pd.read_csv("merged_data.csv")

del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]

cleaned_data = df.dropna()
print(cleaned_data)

cleaned_data.to_csv("cleaned_data.csv")