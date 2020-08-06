import pandas as pd

df = pd.read_csv("data.csv", index_col=0)

print("Preview of dataframe")
print(df.head())

print("Describe first feature")
print(df['1'].describe())
