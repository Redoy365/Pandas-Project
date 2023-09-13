import pandas as pd

myvarr = {
    'car':['BMW', 'Volvo', 'Tata'],

    'range':['110', '100', '105']
}

df = pd.DataFrame(myvarr)

print(df.loc[2])

