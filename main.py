import pandas as pd

myvarr = {
    "car":['BMW', 'Volvo', 'Tata'],

    "range":['s', 'd', 'f']
}

df = pd.DataFrame(myvarr)

print(df)
print("---------------")
print(df.loc[[0,1]])

