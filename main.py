import pandas as pd

df = pd.read_csv('data1.csv')

df["Name"].fillna(130, inplace = True)

print(df)