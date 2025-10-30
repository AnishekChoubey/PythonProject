import pandas as pd
data = {
    "Name":["John","Michael","Merry","Jerry"],
    "Age":[69,67,90,88],
    "City":["London","Mumbai","Goa","Paris"]
}
df = pd.DataFrame(data)
print("Row labels:\n",df.index)
print("Column labels:\n",df.columns)
print("DataFrame dimensions:\n",df.shape)