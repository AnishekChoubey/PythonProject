import pandas as pd
data = {
    "Name":["John","Michael","Merry","Jerry"],
    "Age":[69,67,90,88],
    "City":["London","Mumbai","Goa","Paris"]
}
df = pd.DataFrame(data)
del df['Age']
print(df)
