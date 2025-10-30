import pandas as pd

data = {
    "Anish":pd.Series([61,32,63,84,25],index=['A','B','C','D','E']),
    "Piyush":pd.Series(data=[12,23,34,65],index=['A','B','D','E']),
    "Manas":pd.Series(data=[14,62,36,42,58],index=['A','B','C','D','E'])
}

df = pd.DataFrame(data)
print(df)

