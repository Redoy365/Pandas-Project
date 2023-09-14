import pandas as pd

df = pd.read_csv('data1.csv')

x = df["Roll"].mode()[0]

df["Name"].fillna(x, inplace=True)

print(df)