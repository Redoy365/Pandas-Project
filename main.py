import pandas as pd

df = pd.read_csv('data1.csv')

df.fillna("anonemus",inplace=True)

print(df.to_string())