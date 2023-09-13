import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# =========================

b = [[1,3,5],[2,4,6]]

bvar = pd.Series(b)

print(bvar)
print(bvar[0][1])