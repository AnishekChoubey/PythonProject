import pandas as pd
data = [
    [3,213,243,534,5,35,34],
    [234,492,34,23,43,24,49],
    [324,432,594,62,84,234,923],
    [423,234,23,746,664,23,74],
    [4234,34,23,874,34,333,43]
]
df = pd.DataFrame(data)
print(df)
print("First 3 Rows:\n",df.head(3))
print("Last 3 Rows:\n",df.tail(3))
